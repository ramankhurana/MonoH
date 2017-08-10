#include <Riostream.h>
#include <string>
#include <vector>
#include <math.h>
#include <algorithm>
#include <cstdlib>
#include "TTree.h"
#include "TH1D.h"
#include "TFile.h"
#include "TROOT.h"
#include "TGraphAsymmErrors.h"
#include "TCanvas.h"
#include "TLine.h"
#include "TLatex.h"
#include "TLegend.h"
#include "TStyle.h"
#include "TPaveText.h"
#define nXm 7

const float intLumi = 36.6;
const string dirXSect = "./";

void plot_Asymptotic_Limit_zpb();
void setFPStyle();
void scaleGraph(TGraphAsymmErrors* g, double factor)
{
  int npoints = g->GetN();
  for(int i=0; i!=npoints; ++i) {
    double x = g->GetX()[i];
    double y = g->GetY()[i];
    double eyh = g->GetEYhigh()[i];
    double eyl = g->GetEYlow()[i];
    y = (y*factor);
    eyh = (eyh*factor);
    eyl = (eyl*factor);
    g->SetPoint(i,x,y);
    g->SetPointEYhigh(i, eyh);
    g->SetPointEYlow(i, eyl);
  }

}

double expo_interp(double s2, double s1,  double newM, double m2, double m1)
{
  if (m1 > m2) {
    double tmps = s1;
    double tmpm = m1;
    s1 = s2;
    m1 = m2;
    s2 = tmps;
    m2 = tmpm;
  }
  double deltaM = m2 - m1;
  double alpha = (log(s2) - log(s1)) / deltaM;
  double newS = s1 * pow(exp(newM - m1), alpha);
  return newS;
}



double linear_interp(double s2, double s1, double mass, double m2, double m1)
{
  if (m1 > m2) {
    double tmps = s1;
    double tmpm = m1;
    s1 = s2;
    m1 = m2;
    s2 = tmps;
    m2 = tmpm;
  }
  return (s1 + (s2 - s1) * (mass - m1) / (m2 - m1));
}



void plot_Asymptotic_Limit_zpb(string outputdir, string mode, string postfix_)
{
  
  bool drawth = true;
  TString outfilename = TString(outputdir.c_str())+"/SPlusBFit.root";
  TFile *fout = new TFile(outfilename,"RECREATE");
  bool useNewStyle = true;
  if (useNewStyle)  setFPStyle();
//  gROOT->LoadMacro("CMS_lumi.C");
 
  TFile *fFREQ[nXm];
  TTree *t[nXm];
  int Xmass[nXm]={20, 50, 200, 300, 500, 1000, 2000} ; //600,800,1000,1200,1400,1700,2000,2500};  
  vector<double> v_mh, v_median, v_68l, v_68h, v_95l, v_95h, v_obs;
 
 
  for(int n=0;n<nXm;n++)
  {
    char limitfilename[100];
    sprintf(limitfilename,"higgsCombineTest_Asymptotic_signalMZp_%d_Mdm_1GeV_MonoHbb_13TeV.root",Xmass[n]);
    TString limitfile = outputdir+"/"+limitfilename;
    fFREQ[n] = new TFile(limitfile, "READ");
    cout<<" Read limit file: "<<limitfile<<endl;
    t[n] = (TTree*)fFREQ[n]->Get("limit");
  
    double mh, limit;
    float quant;
    t[n]->SetBranchAddress("mh", &mh);
    t[n]->SetBranchAddress("limit", &limit);
    t[n]->SetBranchAddress("quantileExpected", &quant);
  
    
    
    //int iMH = 0;
    //while (iMH < n) {
 
      for (int i = 0; i < t[n]->GetEntries(); i++) {

        t[n]->GetEntry(i);

        if(false) cout<<" quant : "<<quant<<" limit : " <<limit<<endl;
        /// Map: mh --> observed, 95low, 68low, expected, 68hi, 95hi, xsec
        if (quant > -1.01 && quant < -0.99) {
        v_obs.push_back(limit);
        } 
        else if (quant > 0.02 && quant < 0.03) {
	v_95l.push_back(limit);
        }
        else if (quant > 0.15 && quant < 0.17) {
	v_68l.push_back(limit);
        }
        else if (quant > 0.49 && quant < 0.51) {
	v_median.push_back(limit);
        v_mh.push_back(mh);
        }
        else if (quant > 0.83 && quant < 0.85) {
	v_68h.push_back(limit);
        }
        else if (quant > 0.965 && quant < 0.98) {
	v_95h.push_back(limit);
        }
        else {
        cout << "Error! Quantile =  " << quant << endl;
        }
     }
      //iMH++;
	//     }//end while loop

  }//file loop
  
  string xsect_file_th;
  string xsect_file_th_atlas;

  if(mode == "cms")  xsect_file_th = dirXSect + "xsec_MonoHzpbTheoryCMS.txt";
  if(mode == "atlas")  xsect_file_th = dirXSect + "xsec_MonoHTheoryATLAS.txt";
  if(mode == "one") xsect_file_th = dirXSect + "xsecUnity_MonoHTheory.txt";
  if(mode=="comb") xsect_file_th = dirXSect + "xsec_MonoHTheoryATLAS.txt";
  
  xsect_file_th_atlas = dirXSect + "xsec_MonoHTheoryCMS.txt";  
  
  std::cout<<" xsect_file_th_atlas = "<<xsect_file_th_atlas<<std::endl;
  
  ifstream xsect_file(xsect_file_th.c_str(), ios::in);
  if (! xsect_file.is_open()) {
    cout << "Failed to open file with xsections: " << xsect_file_th << endl;
  }
  
  ifstream xsect_file_atlas(xsect_file_th_atlas.c_str(), ios::in);
  if (! xsect_file_atlas.is_open()) {
    cout << "Failed to open file with xsections: " << xsect_file_th_atlas << endl;
  }
  
  
  float mH, CS;
  vector<float> v_mhxs, v_xs, v_toterrh, v_toterrl;
  while (xsect_file.good()) {
    xsect_file >> mH >> CS;
  
    v_mhxs.push_back(mH);
    v_xs.push_back(CS);//*BRZZ2l2q (multyply by BRZZ2l2q only if exp rates in cards are for process X->ZZ->2l2q !)
    
    //unavailable theory errors for graviton

    float tot_err_p = 0.0;
    float tot_err_m = 0.0;

    v_toterrh.push_back(1.0 + (tot_err_p));
    v_toterrl.push_back(1.0 - (tot_err_m));
  }
  


  // 
  //  read atlass x-section text file
  float mH_atlas, CS_atlas;
  vector<float> v_mhxs_atlas, v_xs_atlas;
  while (xsect_file_atlas.good()) {
    xsect_file_atlas >> mH_atlas >> CS_atlas;
  
    v_mhxs_atlas.push_back(mH_atlas);
    v_xs_atlas.push_back(CS_atlas);
  }
  
  ///////////////////////////
  // END THEORY INPUT PART //
  ///////////////////////////


  /// Here we multiply the limits in terms of signal strength by the cross-section.
  /// There are also some hooks to exclude sick mass points.
  
  double mass[nXm], obs_lim_cls[nXm];
  double medianD[nXm];
  double up68err[nXm], down68err[nXm], up95err[nXm], down95err[nXm];
  double xs[nXm], xs_uperr[nXm], xs_downerr[nXm], xs_atlas[nXm];
  double xs10[nXm], xs10_uperr[nXm], xs10_downerr[nXm];
  int nMassEff = 0;
  
  for (int im = 0; im < nXm; im++) {


    double fl_xs = double(v_xs.at(im)); 
    double fl_xs10 = double(v_xs_atlas.at(im)); 
    fl_xs = (fl_xs);
    fl_xs10 = (fl_xs10);

      mass[nMassEff] = Xmass[im];

    /// This is the part where we multiply the limits in terms of signal strength
    /// by the cross-section, in order to have limits in picobarns.
    //std::cerr << mass[nMassEff] << ":" << v_obs.at(im) << std::endl;
      obs_lim_cls[nMassEff] = v_obs.at(im);
      medianD[nMassEff] = v_median.at(im) ;
      up68err[nMassEff] = (v_68h.at(im) - v_median.at(im)) ;
      down68err[nMassEff] = (v_median.at(im) - v_68l.at(im));

      //obs_lim_cls[nMassEff] = v_obs.at(im) * fl_xs;
      //medianD[nMassEff] = v_median.at(im) * fl_xs;
      //up68err[nMassEff] = (v_68h.at(im) - v_median.at(im)) * fl_xs;
      //down68err[nMassEff] = (v_median.at(im) - v_68l.at(im)) * fl_xs;

      //scale factor 100 for making the xsect visible
      xs[nMassEff] = fl_xs; //*100.0;
      xs_atlas[nMassEff] = fl_xs10;
      
      xs_uperr[nMassEff] = double(v_toterrh.at(im))  - xs[nMassEff];
      xs_downerr[nMassEff] =  xs[nMassEff] - double(v_toterrl.at(im)) ;
      //xs_uperr[nMassEff] = double(v_toterrh.at(im)) * xs[nMassEff] - xs[nMassEff];
      //xs_downerr[nMassEff] =  xs[nMassEff] - double(v_toterrl.at(im)) * xs[nMassEff];

      xs10[nMassEff] = fl_xs10; //*100.0;
      
      xs10_uperr[nMassEff] = double(v_toterrh.at(im)) - xs10[nMassEff];
      xs10_downerr[nMassEff] =  xs10[nMassEff] - double(v_toterrl.at(im));

      //xs10_uperr[nMassEff] = double(v_toterrh.at(im)) * xs10[nMassEff] - xs10[nMassEff];
      //xs10_downerr[nMassEff] =  xs10[nMassEff] - double(v_toterrl.at(im)) * xs10[nMassEff];

      up95err[nMassEff] = (v_95h.at(im) - v_median.at(im)) ;
      down95err[nMassEff] = (v_median.at(im) - v_95l.at(im));
      //up95err[nMassEff] = (v_95h.at(im) - v_median.at(im)) * fl_xs;
      //down95err[nMassEff] = (v_median.at(im) - v_95l.at(im)) * fl_xs;
    
      cout<<"fl_xs:"<<fl_xs<<" v_obs: "<<v_obs.at(im)<<" obs_lim_cls: "<<obs_lim_cls[nMassEff]  <<medianD[nMassEff] <<" mass: "<<mass[nMassEff]
	  <<" exp: "<<v_median.at(im)<<" exp x th: "<<medianD[nMassEff]<<endl;
 
      nMassEff++;
    
    
  }//end loop over im (mass points)



  /// The TGraphs themselves.

  //cout<<"Working on TGraph"<<endl;
  TGraphAsymmErrors *grobslim_cls = new TGraphAsymmErrors(nMassEff, mass, obs_lim_cls);
  grobslim_cls->SetName("LimitObservedCLs");
  TGraphAsymmErrors *grmedian_cls = new TGraphAsymmErrors(nMassEff, mass, medianD);
  grmedian_cls->SetName("LimitExpectedCLs");
  TGraphAsymmErrors *gr68_cls = new TGraphAsymmErrors(nMassEff, mass, medianD, 0, 0, down68err, up68err);
  gr68_cls->SetName("Limit68CLs");
  TGraphAsymmErrors *gr95_cls = new TGraphAsymmErrors(nMassEff, mass, medianD, 0, 0, down95err, up95err);
  gr95_cls->SetName("Limit95CLs");

  //   TGraphAsymmErrors *grthSM=new TGraphAsymmErrors(nMassEff1,mass1,xs,0,0,0,0);//xs_downerr,xs_uperr);
  TGraph *grthSM=new TGraph(nMassEff,mass,xs);//xs_downerr,xs_uperr);
  grthSM->SetName("SMXSection");


  // TGraphAsymmErrors *grthSM10=new TGraphAsymmErrors(nMassEff1,mass1,xs10,0,0,0,0);
  TGraph *grthSM10=new TGraph(nMassEff,mass,xs_atlas);
  grthSM10->SetName("SMXSection_2nd");

  // double fr_left = 590.0, fr_down = 1E-5, fr_right = 2000.0, fr_up = 0.5; 
   double fr_left = 10.0, fr_down = 5E-5, fr_right = 2010.0, fr_up = 5;

  TCanvas *cMCMC = new TCanvas("c_lim_Asymptotic", "canvas with limits for Asymptotic CLs", 630, 600);
  cMCMC->cd();
  cMCMC->SetGridx(1);
  cMCMC->SetGridy(1);
  // draw a frame to define the range

  TH1F *hr = cMCMC->DrawFrame(fr_left, fr_down, fr_right, fr_up, "");
  TString VV = "ZH";
  
  //std::cout<<" working upto this point "<<std::endl;
  hr->SetXTitle("m_{Z'} [GeV]");
  hr->GetXaxis()->SetNdivisions(508);
  //hr->SetYTitle("#sigma_{95% CL}(Z`#rightarrow#chi#bar{#chi}H)[pb]"); // #rightarrow 2l2q
  hr->SetYTitle("#sigma_{95% CL}[pb]"); // #rightarrow 2l2q
  //hr->SetYTitle("95% CLs on #sigma(Z`#rightarrow#chi#bar{#chi}H)[pb]"); // #rightarrow 2l2q

  hr->SetMinimum(0.001);
  hr->SetMaximum(1000);
  if(mode == "one") hr->SetMinimum(0.1);


  gr95_cls->SetFillColor(kYellow);
  gr95_cls->SetFillStyle(1001);//solid
  gr95_cls->SetLineStyle(kDashed);
  gr95_cls->SetLineWidth(3);
  gr95_cls->GetYaxis()->SetTitleSize(0.45);
  gr95_cls->GetXaxis()->SetTitleSize(0.45);
  gr95_cls->GetXaxis()->SetTitle("m_{Z'} [GeV]");
  gr95_cls->GetYaxis()->SetTitle("#sigma_{95% CL}(Z`#rightarrow#chi#bar{#chi}H)[pb] "); // #rightarrow 2l2q
  //gr95_cls->GetYaxis()->SetTitle("95% CLs on #sigma(Z`#rightarrow#chi#bar{#chi}H)[pb] "); // #rightarrow 2l2q
  gr95_cls->GetXaxis()->SetRangeUser(fr_left, fr_right);

  gr95_cls->Draw("3");
  //gr95_cls->SetMinimum(0.1);
  //xgr95_cls->SetMaximum(1000.0);
  
  //grmedian_cls->SetMinimum(0.00001);
  //grmedian_cls->SetMaximum(1000.0);
  
  gr68_cls->SetFillColor(kGreen);
  gr68_cls->SetFillStyle(1001);//solid
  gr68_cls->SetLineStyle(kDashed);
  gr68_cls->SetLineWidth(3);
  gr68_cls->Draw("3same");
  grmedian_cls->GetXaxis()->SetTitle("m_{Z'} [GeV]");
  grmedian_cls->GetYaxis()->SetTitle("#sigma_{95% CL}(Z`#rightarrow#chi#bar{#chi}H)[pb]"); // #rightarrow 2l2q
  grmedian_cls->SetMarkerStyle(24);//25=hollow squre
  grmedian_cls->SetMarkerColor(kBlack);
  grmedian_cls->SetLineStyle(2);
  grmedian_cls->SetLineWidth(3);
  
  std::cout<<" working upto this point 2"<<std::endl;

  grobslim_cls->SetMarkerColor(kBlack);
  grobslim_cls->SetMarkerStyle(21);//24=hollow circle
  grobslim_cls->SetMarkerSize(1.0);
  grobslim_cls->SetLineStyle(1);
  grobslim_cls->SetLineWidth(3);

  grthSM->SetLineColor(kBlue);
  grthSM->SetLineWidth(3);
  //grthSM->SetLineStyle(1);
  grthSM->SetLineStyle(kDashed);
  grthSM->SetFillColor(kBlue);
  grthSM->SetFillStyle(3344);

  grthSM10->SetLineColor(kRed);
  grthSM10->SetLineWidth(3);
  //grthSM10->SetLineStyle(1);
  grthSM10->SetLineStyle(kDashed);
  grthSM10->SetFillColor(kRed);
  grthSM10->SetFillStyle(3344);
  
  // open 
  // draw
  
  /*
  TFile* lineA=TFile::Open("lineA.root");
  TFile* lineC=TFile::Open("lineC.root");
  TGraph* tgA=(TGraph*)lineA->FindObjectAny("Graph");
  TGraph* tgC=(TGraph*)lineC->FindObjectAny("Graph");
  
  
  tgA->SetLineColor(kBlue);
  tgA->SetLineWidth(3);
  //grthSM->SetLineStyle(1);
  tgA->SetLineStyle(kDashed);
  tgA->SetFillColor(kBlue);
  tgA->SetFillStyle(3344);

  tgC->SetLineColor(kRed);
  tgC->SetLineWidth(3);
  //grthSM10->SetLineStyle(1);
  tgC->SetLineStyle(kDashed);
  tgC->SetFillColor(kRed);
  tgC->SetFillStyle(3344);
  
  tgA->Draw("L3");
  tgC->Draw("L3");
  */
  std::cout<<" working upto this point 3"<<std::endl;
  if(drawth)   grthSM->Draw("L3");
  grmedian_cls->Draw("L");
  //if(mode=="comb") grthSM10->Draw("L3");

  // observed limit
  grobslim_cls->Draw("L");
  
  
  
  /*
  TGraph *interPoint = new TGraph();
  Int_t i = 0;
  unsigned int a_up = tgA->GetN()-1;
  unsigned int b_up = grobslim_cls->GetN()-1;
 
  // Loop over all points in this TGraph                                                                            
  for(size_t a_i = 0; a_i < a_up; ++a_i)
    {
      // Loop over all points in the other TGraph
      for(size_t b_i = 0; b_i < b_up; ++b_i)
        {

          // Get the current point, and the next point for each of the objects  
          Double_t x1, y1, x2, y2 = 0;
          Double_t ax1, ay1, ax2, ay2 = 0;
          tgA->GetPoint(a_i, x1, y1);
          tgA->GetPoint(a_i+1, x2, y2);
          grobslim_cls->GetPoint(b_i, ax1, ay1);
          grobslim_cls->GetPoint(b_i+1, ax2, ay2);

          // Calculate the intersection between two straight lines, x axis
          Double_t x = (ax1 *(ay2 *(x1-x2)+x2 * y1 - x1 * y2 )+ ax2 * (ay1 * (-x1+x2)- x2 * y1+x1 * y2))
            / (-(ay1-ay2) * (x1-x2)+(ax1-ax2)* (y1-y2));

          // Calculate the intersection between two straight lines, y axis 
          Double_t y = (ax1 * ay2 * (y1-y2)+ax2 * ay1 * (-y1+y2)+(ay1-ay2) * (x2 * y1-x1 * y2))/(-(ay1-ay2) * (x1-x2)+(ax1-ax2) * (y1-y2));

          // Find the tightest interval along the x-axis defined by the four points
          Double_t xrange_min = max(min(x1, x2), min(ax1, ax2));
          Double_t xrange_max = min(max(x1, x2), max(ax1, ax2));

          // If points from the two lines overlap, they are trivially intersecting 
          if ((x1 == ax1 and y1 == ay1) or (x2 == ax2 and y2 == ay2)){
            interPoint->SetPoint(i, (x1 == ax1 and y1 == ay1) ? x1 : x2, (x1 == ax1 and y1 == ay1) ? y1 : y2);
            i++;
          }

	  // If the intersection between the two lines is within the tight range, add it to the list of intersections.  
          else if(x > xrange_min && x < xrange_max)
            {
              interPoint->SetPoint(i,x, y);
              i++;
            }
        }
    }
  */
 
  /* unsigned int i_up = interPoint->GetN();

  for(size_t i = 0; i < i_up; ++i)
    {
      Double_t x, y = 0;
      interPoint->GetPoint(i, x, y);
      printf("x=%f, y=%f\n", x, y);

      //ll.DrawLatex(x - 2, y - 0.003, TString::Format("(%0.2f,%0.2f)", x, y));

    }
  */
  /*
  TFile *fUnMPlus=new TFile("AsymptoticCLs_UnmatchedPlus_TGraph.root","READ");
  TGraph *grobs_ump=(TGraph*)fUnMPlus->Get("LimitObservedCLs");
  TGraph *grmedian_ump=(TGraph*)fUnMPlus->Get("LimitExpectedCLs");
  grobs_ump->SetName("LimitObs_UnmatchedPlus");
  grmedian_ump->SetName("LimitExp_UnmatchedPlus");
  grobs_ump->SetMarkerColor(kBlue);
  grobs_ump->SetLineColor(kBlue);
  grobs_ump->SetMarkerStyle(25);
  grmedian_ump->SetMarkerColor(kBlue);
  grmedian_ump->SetLineColor(kBlue);
  grmedian_ump->SetMarkerStyle(25);
  grobs_ump->Draw("P");
  grmedian_ump->Draw("L");
  */

  //draw grid on top of limits
  gStyle->SetOptStat(0);
  TH1D* postGrid = new TH1D("postGrid", "", 1, fr_left, fr_right);
  postGrid->GetYaxis()->SetRangeUser(fr_down, fr_up);
  postGrid->Draw("AXIGSAME");

  //more graphics
  std::cout<<" working upto this point 4"<<std::endl;
  TLegend *leg;
  
  if( mode!="comb") leg = new TLegend(.60, .73, .95, .95);
  if( mode=="comb") leg = new TLegend(.25, .58, .95, .78);
  leg->SetBorderSize(1);
  //leg->SetLineColor(0);                                                                                                                     
  leg->SetLineStyle(1);
  leg->SetLineWidth(1);
  leg->SetFillColor(0);
  leg->SetFillStyle(1001);


  leg->SetFillColor(0);
  leg->SetLineColor(0);
 
  leg->SetShadowColor(0);
  leg->SetTextFont(42);
  leg->SetTextSize(0.03);
  //   leg->SetBorderMode(0);
  leg->AddEntry(grmedian_cls,"Expected","L");
  leg->AddEntry(grobslim_cls, "Observed Asimov", "L");
  leg->AddEntry(gr68_cls, "Expected #pm 1#sigma", "LF");
  leg->AddEntry(gr95_cls, "Expected #pm 2#sigma", "LF");
  if(mode!= "comb") leg->AddEntry(grthSM, "#sigma_{TH} ", "L");
  
  if(mode=="comb"){
    //leg->AddEntry(grthSM10, "#sigma_{TH}, g_{Z'}<= 0.03#times#frac{g_{W}}{cos#theta_{W}#timessin^{2}#beta}#times #frac{#sqrt{m_{Z'}^{2}-m_{Z}^{2}}}{m_{Z}}", "L");
    leg->AddEntry(grthSM10, "#sigma_{TH}, g_{Z'}= 0.8", "L");
    leg->AddEntry(grthSM, "#sigma_{TH}, g_{Z'} = 0.8", "L");
  }
//    leg->AddEntry(grthSM, "#sigma_{TH} x BR(Z' #rightarrow " + VV + "), #tilde{k}=0.50", "L"); // #rightarrow 2l2q
//    leg->AddEntry(grthSM10, "#sigma_{TH} x BR(Z' #rightarrow " + VV + "), #tilde{k}=0.20", "L"); // #rightarrow 2l2q
  leg->Draw();
  
  std::cout<<" working upto this point 5"<<std::endl;
    TLatex * latex = new TLatex();
    latex->SetNDC();
    latex->SetTextSize(0.032);
    latex->SetTextAlign(12); // align left
    latex->SetNDC(kTRUE);                                                                                                                         latex->SetTextFont(62);
    latex->DrawLatex(0.18, 0.91, "CMS #it{#bf{Preliminary}}");
    latex->DrawLatex(0.68, 0.965, Form("%.1f fb^{-1} (13 TeV)", intLumi));
        
    latex->DrawLatex(0.18,0.88, "Z' Baryonic");
    latex->DrawLatex(0.18,0.84, "g_{q} = 0.25, g_{DM} = 1");
    if(mode == "atlas")latex->DrawLatex(0.18,0.765, "g_{Z'} = 0.8, tan#beta = 1");
    //if(mode == "cms") latex->DrawLatex(0.18,0.755, "g_{Z'}<= 0.03#times#frac{g_{W}}{cos#theta_{W}#timessin^{2}#beta}#times #frac{#sqrt{m_{Z'}^{2}-m_{Z}^{2}}}{m_{Z}}");
    if(mode == "cms") latex->DrawLatex(0.18,0.80, "m_{#chi} = 1 GeV");

    if(mode == "one") latex->DrawLatex(0.18,0.765, "tan#beta = 1");
  // cMCMC->RedrawAxis("");
  gPad->RedrawAxis("");
  // hr->GetYaxis()->DrawClone();
  cMCMC->Update();
  char fnam[50];
  //string outputname="shape2d";
  //string outputname="shape1d";
  //string outputname="counting";
  
  std::cout<<" working upto this point 6"<<std::endl;
  std::string postname = "MonoHToDMbb_Asymptotic_"+mode+".png";
  std::string name = outputdir+postname;
  
  
  cMCMC->SaveAs(name.c_str());
  
  gPad->SetLogy(1);
  postname = "MonoHToDMbb_Asymptotic_Log_"+mode+"_"+postfix_+".png";
  name = outputdir+postname;
  cMCMC->SaveAs(name.c_str());
  
  postname = "MonoHToDMbb_Asymptotic_Log_"+mode+"_"+postfix_+".pdf";
  name = outputdir+postname;
  cMCMC->SaveAs(name.c_str());
  
  std::cout<<" working upto this point 7"<<name <<std::endl;
  
  //postname = "MonoHToDMbb_Asymptotic.root";
  //name = outputdir+postname;
  //TFile* fout = TFile(name,"RECREATE");
  //fout->cd();
    
  /*
    sprintf(fnam, "XZHllbb_%s_Asymptotic.root",outputdir.data() );
    cMCMC->SaveAs(fnam);
    sprintf(fnam, "XZHllbb_%s_Asymptotic.eps", outputdir.data());
    cMCMC->SaveAs(fnam);
    
    sprintf(fnam, "XZHllbb_%s_Asymptotic.pdf", outputdir.data());
    cMCMC->SaveAs(fnam);
    gPad->SetLogy();
    sprintf(fnam, "XZHllbb_%s_Asymptotic_log.eps", outputdir.data());
    cMCMC->SaveAs(fnam);
    sprintf(fnam, "XZHllbb_%s_Asymptotic_log.pdf", outputdir.data());
    cMCMC->SaveAs(fnam);
  */

  cMCMC->Draw();

  fout->cd();
  grthSM->Write();
  grobslim_cls->Write();
  grmedian_cls->Write();
  fout->Close();

}//end main

void setFPStyle()
{
  gStyle->SetPadBorderMode(0);
  gStyle->SetFrameBorderMode(0);
  gStyle->SetPadBottomMargin(0.12);
  gStyle->SetPadLeftMargin(0.12);
  gStyle->SetCanvasColor(kWhite);
  gStyle->SetCanvasDefH(600); //Height of canvas
  gStyle->SetCanvasDefW(600); //Width of canvas
  gStyle->SetCanvasDefX(0);   //Position on screen
  gStyle->SetCanvasDefY(0);

  gStyle->SetPadTopMargin(0.05);
  gStyle->SetPadBottomMargin(0.15);//0.13);
  gStyle->SetPadLeftMargin(0.15);//0.16);
  gStyle->SetPadRightMargin(0.05);//0.02);

  // For the Pad:
  gStyle->SetPadBorderMode(0);
  // gStyle->SetPadBorderSize(Width_t size = 1);
  gStyle->SetPadColor(kWhite);
  gStyle->SetPadGridX(false);
  gStyle->SetPadGridY(false);
  gStyle->SetGridColor(0);
  gStyle->SetGridStyle(3);
  gStyle->SetGridWidth(1);

  // For the Frame:
  gStyle->SetFrameBorderMode(0);
  gStyle->SetFrameBorderSize(1);
  gStyle->SetFrameFillColor(0);
  gStyle->SetFrameFillStyle(0);
  gStyle->SetFrameLineColor(1);
  gStyle->SetFrameLineStyle(1);
  gStyle->SetFrameLineWidth(1);

  gStyle->SetAxisColor(1, "XYZ");
  gStyle->SetStripDecimals(kTRUE);
  gStyle->SetTickLength(0.03, "XYZ");
  gStyle->SetNdivisions(605, "XYZ");
  gStyle->SetPadTickX(1);  // To get tick marks on the opposite side of the frame
  gStyle->SetPadTickY(1);
  gStyle->SetGridColor(0);
  gStyle->SetGridStyle(3);
  gStyle->SetGridWidth(1);


  gStyle->SetTitleColor(1, "XYZ");
  gStyle->SetTitleFont(42, "XYZ");
  gStyle->SetTitleSize(0.05, "XYZ");
  // gStyle->SetTitleXSize(Float_t size = 0.02); // Another way to set the size?
  // gStyle->SetTitleYSize(Float_t size = 0.02);
  gStyle->SetTitleXOffset(1.15);//0.9);
  gStyle->SetTitleYOffset(1.3); // => 1.15 if exponents
  gStyle->SetLabelColor(1, "XYZ");
  gStyle->SetLabelFont(42, "XYZ");
  gStyle->SetLabelOffset(0.007, "XYZ");
  gStyle->SetLabelSize(0.045, "XYZ");

  gStyle->SetPadBorderMode(0);
  gStyle->SetFrameBorderMode(0);
  gStyle->SetTitleTextColor(1);
  gStyle->SetTitleFillColor(10);
  gStyle->SetTitleFontSize(0.05);
}


