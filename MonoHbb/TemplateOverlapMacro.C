{
#include <ctime>
#include <cstdlib>
#include "TStyle.h" 
 time_t now = time(0);
 tm *ltm = localtime(&now);
 TString dirpathname;

 TString DirPreName = "AnalysisHistograms_MergedSkimmedV12_Puppi_V1/zj";
 dirpathname = "05122016"; //.Form("%d%1.2d%d",ltm->tm_mday,1 + ltm->tm_mon,1900 + ltm->tm_year);
 system("mkdir -p  " + DirPreName+dirpathname +"/MonoHROOT");
 system("mkdir -p  " + DirPreName+dirpathname +"/MonoHPdf");
 system("mkdir -p  " + DirPreName+dirpathname +"/MonoHPng");
 
 
 ofstream mout;
 mout.open(DirPreName+dirpathname +"/HISTPATH"+dirpathname +"Integral.txt",std::ios::app);
 ofstream rout;
 rout.open(DirPreName+dirpathname +"/HISTPATH"+dirpathname +"Integral.html",std::ios::app);
 ofstream tableout;
 tableout.open(DirPreName+dirpathname +"/HISTPATH"+dirpathname +"IntegralWithError.txt",std::ios::app);                                                                  
 TString outputshapefilename = DirPreName+dirpathname +"/HISTPATH.root";
 TFile *fshape = new TFile(outputshapefilename,"RECREATE");

if(VARIABLEBINS){
ofstream metbinsout_1;
ofstream metbinsout_2;
ofstream metbinsout_3;

 system("mkdir -p  " + DirPreName+"METBIN_1");
 system("mkdir -p  " + DirPreName+"METBIN_2");
 system("mkdir -p  " + DirPreName+"METBIN_3");


 metbinsout_1.open(DirPreName+"METBIN_1/HISTPATH"+dirpathname +"Integral.txt",std::ios::app);
 metbinsout_2.open(DirPreName+"METBIN_2/HISTPATH"+dirpathname +"Integral.txt",std::ios::app);
 metbinsout_3.open(DirPreName+"METBIN_3/HISTPATH"+dirpathname +"Integral.txt",std::ios::app);
}

gROOT->ProcessLine(".L /afs/hep.wisc.edu/cms/khurana/Monika/CMSSW_7_4_5/src/RKGlobalAnalyzer/tdrstyle.C");                                     setTDRStyle();
gStyle->SetOptStat(0);
gStyle->SetOptTitle(0);
gStyle->SetFrameLineWidth(3);
//gStyle->SetErrorX(0);
gStyle->SetLineWidth(1);

//Provide luminosity of total data
float lumi = 12900.; // It will print on your plots too
//float lumi = 3200.; // It will print on your plots too
float luminosity = 12.9;

std::vector<TString> filenameString;
//Change here Directories of the file


// histogram declaration for shape analysis
TH1F*  monoHbbM600;
TH1F*  monoHbbM800; 
TH1F*  monoHbbM1000;
TH1F*  monoHbbM1200;
TH1F*  monoHbbM1400; 
TH1F*  monoHbbM1700;
TH1F*  monoHbbM2000;
TH1F*  monoHbbM2500;
TH1F*  DIBOSON;
TH1F*  ZH; 
TH1F*  TT;
TH1F*  TTJets;
TH1F*  WJets;
TH1F*  DYJets; 
TH1F*  STop;
TH1F*  data_obs;

TString filenamepath("AnalysisHistograms_MergedSkimmedV12_Puppi_V1/zj/"); 
// DYJets 0
filenameString.push_back(filenamepath + "Merged_WW_TuneCUETP8M1_13TeV-pythia8-SkimTree.root");
//WJets  1
filenameString.push_back(filenamepath + "Merged_WW_TuneCUETP8M1_13TeV-pythia8-SkimTree.root");

// Diboson WW WZ ZZ 2 3 4
filenameString.push_back(filenamepath + "Merged_WW_TuneCUETP8M1_13TeV-pythia8-SkimTree.root");
filenameString.push_back(filenamepath + "Merged_WZ_TuneCUETP8M1_13TeV-pythia8-SkimTree.root");
filenameString.push_back(filenamepath + "Merged_ZZ_TuneCUETP8M1_13TeV-pythia8-SkimTree.root");

// TTJets 5
filenameString.push_back(filenamepath + "Merged_TT_TuneCUETP8M1_13TeV-powheg-pythia8-SkimTree.root");

//Raman ZH background 6                                                                                                                       
filenameString.push_back(filenamepath + "Merged_ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8-SkimTree.root"); 

//Raman Signal Sample 7-11

filenameString.push_back(filenamepath + "Merged_ZprimeToA0hToA0chichihbb_2HDM_MZp-600_MA0-300_13TeV-madgraph-SkimTree.root");
filenameString.push_back(filenamepath + "Merged_ZprimeToA0hToA0chichihbb_2HDM_MZp-800_MA0-300_13TeV-madgraph-SkimTree.root");  
filenameString.push_back(filenamepath + "Merged_ZprimeToA0hToA0chichihbb_2HDM_MZp-1000_MA0-300_13TeV-madgraph-SkimTree.root");  
filenameString.push_back(filenamepath + "Merged_ZprimeToA0hToA0chichihbb_2HDM_MZp-1200_MA0-300_13TeV-madgraph-SkimTree.root");  
filenameString.push_back(filenamepath + "Merged_ZprimeToA0hToA0chichihbb_2HDM_MZp-1400_MA0-300_13TeV-madgraph-SkimTree.root");  
//comment out
//filenameString.push_back(filenamepath + "Merged_ZprimeToA0hToA0chichihbb_2HDM_MZp-1700_MA0-300_13TeV-madgraph-SkimTree.root");  
//filenameString.push_back(filenamepath + "Merged_ZprimeToA0hToA0chichihbb_2HDM_MZp-2000_MA0-300_13TeV-madgraph-SkimTree.root");  
//filenameString.push_back(filenamepath + "Merged_ZprimeToA0hToA0chichihbb_2HDM_MZp-2500_MA0-300_13TeV-madgraph-SkimTree.root");  


//DYJets High pt DYSample 12,13,14,15,16,17,18
filenameString.push_back(filenamepath + "Merged_ZJetsToNuNu_HT-100To200_13TeV-madgraph-SkimTree.root");
filenameString.push_back(filenamepath + "Merged_ZJetsToNuNu_HT-200To400_13TeV-madgraph-SkimTree.root");
filenameString.push_back(filenamepath + "Merged_ZJetsToNuNu_HT-400To600_13TeV-madgraph-SkimTree.root");
filenameString.push_back(filenamepath + "Merged_ZJetsToNuNu_HT-600To800_13TeV-madgraph-SkimTree.root");
filenameString.push_back(filenamepath + "Merged_ZJetsToNuNu_HT-800To1200_13TeV-madgraph-SkimTree.root");
filenameString.push_back(filenamepath + "Merged_ZJetsToNuNu_HT-1200To2500_13TeV-madgraph-SkimTree.root");
filenameString.push_back(filenamepath + "Merged_ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph-SkimTree.root");



// WJets in Bins  19,20,21,22,23,24,25
filenameString.push_back(filenamepath + "Merged_WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-SkimTree.root");
filenameString.push_back(filenamepath + "Merged_WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-SkimTree.root");
filenameString.push_back(filenamepath + "Merged_WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-SkimTree.root");
filenameString.push_back(filenamepath + "Merged_WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-SkimTree.root");
filenameString.push_back(filenamepath + "Merged_WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-SkimTree.root");
filenameString.push_back(filenamepath + "Merged_WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-SkimTree.root");
filenameString.push_back(filenamepath + "Merged_WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-SkimTree.root");

// Single Top 26,27,28,29,30
//fixme filenameString.push_back(filenamepath + "Merged_ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1-SkimTree.root");
filenameString.push_back(filenamepath + "Merged_ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1-SkimTree.root");
filenameString.push_back(filenamepath + "Merged_ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1-SkimTree.root");
filenameString.push_back(filenamepath + "Merged_ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1-SkimTree.root");
filenameString.push_back(filenamepath + "Merged_ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1-SkimTree.root");
filenameString.push_back(filenamepath + "Merged_ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1-SkimTree.root");

//                                                                   
//Data Filex

filenameString.push_back(filenamepath + "Merged_MET-SkimTree.root");

//histoname

//const int n_integral = (int)filenameString.size();

TString histnameString("HISTNAME");
TString old_name = histnameString;
TString new_name =  old_name.ReplaceAll("_0","_1");





TFile *fIn;
const int nfiles = (int) filenameString.size();

float Integral[nfiles] , Integral_Error[nfiles];

//check it once
float Xsec[nfiles];
Xsec[0] = 6104;
Xsec[1] = 61500;

Xsec[2] = 118.7; 
Xsec[3] = 66.1;
Xsec[4] = 15.4;

//float Stt = 0.95;
float Stt = 1.;
Xsec[5] = Stt * 831.76; // ttbar
Xsec[6] = (0.8696) * 0.577 * 0.2 ; //ZH checked from Michele

float scalexs = 0.577; 
//
//Xsec[7]  = scalexs ;//600
//Xsec[8]  = scalexs ;//800
//Xsec[9]  = scalexs ; //1000
//Xsec[10] = scalexs ; //1200
//Xsec[11] = scalexs ; //1400
//Xsec[12] = scalexs ; //1700
//Xsec[13] = scalexs ; //2000
//Xsec[14] = scalexs ; //2500


// CMS Cross-section NOT MULTIPLIED WITH BR:
// scalexs is BR
//Xsec[7]  = scalexs * 0.042386;//600
//Xsec[8]  = scalexs * 0.045097;//800
//Xsec[9] = scalexs *  0.035444; //1000
//Xsec[10] = scalexs * 0.02607; //1200
//Xsec[11] = scalexs * 0.018942; //1400
//Xsec[12] = scalexs * 0.011778; //1700
//Xsec[13] = scalexs * 0.0074456; //2000
//Xsec[14] = scalexs * 0.0036446; //2500

//600 0.024456722
//800 0.026020969
//1000 0.020451188
//1200 0.01504239
//1400 0.010929534
//1700 0.006795906
//2000 0.0042961112
//2500 0.0021029342



// ATLAS Cross-section NOT MULTIPLIED WITH BR:
// scalexs is BR
Xsec[7]  = scalexs * 0.3722;//600
Xsec[8]  = scalexs * 0.23067;//800
Xsec[9] = scalexs *  0.11934; //1000
Xsec[10] = scalexs * 0.063054; //1200
Xsec[11] = scalexs * 0.034536; //1400


//Xsec[12] = scalexs * 0.015007; //1700
//Xsec[13] = scalexs * 0.0069696; //2000
//Xsec[14] = scalexs * 0.0021672; //2500


// use cross-section as 1 pb
// scalexs is BR
//Xsec[7]  = scalexs ;//600
//Xsec[8]  = scalexs ;//800
//Xsec[9] = scalexs  ; //1000
//Xsec[10] = scalexs ; //1200
//Xsec[11] = scalexs ; //1400
//Xsec[12] = scalexs ; //1700
//Xsec[13] = scalexs ; //2000
//Xsec[14] = scalexs ; //2500


float Sznunu = 1.;
//float Sznunu = 0.77;
Xsec[12] = Sznunu * 1.626*280.47; // Znunu HT
Xsec[13] = Sznunu * 1.617*78.36; // Znunu HT
Xsec[14] = Sznunu * 1.459*10.94; // Znunu HT
Xsec[15] = Sznunu *  1.0* 3.221; // Znunu HT
Xsec[16] = Sznunu *  1.0* 1.474;// Znunu HT
Xsec[17] = Sznunu *  1.0* 0.3586;// Znunu HT
Xsec[18] = Sznunu *  1.0* 0.008203; // Znunu HT

//Xsec[15] = 1.23*280.47; // Znunu HT
//Xsec[16] = 1.23*78.36; // Znunu HT
//Xsec[17] = 1.23*10.94; // Znunu HT
//Xsec[18] = 1.23*4.203;  // Znunu HT


//float Sw = 0.95;
float Sw = 1.;

Xsec[19] = Sw  *  1.459*1347;  // WJets HT 100-200
Xsec[20] = Sw  *  1.434*360;   // WJets HT 200-400
Xsec[21] = Sw  *  1.532*48.9;  // WJets HT 400-600
Xsec[22] = Sw  *  1.004*12.8;  // WJets HT 600-800
Xsec[23] = Sw  *  1.004*5.26;  // WJets HT 800-1200
Xsec[24] = Sw  *  1.004*1.33;  // WJets HT 1200-2500
Xsec[25] = Sw  *  1.004*0.03089;  // WJets HT 2500-Inf

//Xsec[19] = Sw  *  1.21*1347;  // WJets HT 100-200
//Xsec[20] = Sw  *  1.21*360;   // WJets HT 200-400
//Xsec[21] = Sw  *  1.21*48.9;  // WJets HT 400-600
//Xsec[22] = Sw  *  1.21*12.8;  // WJets HT 600-800
//Xsec[23] = Sw  *  1.21*5.26;  // WJets HT 800-1200
//Xsec[24] = Sw  *  1.21*1.33;  // WJets HT 1200-2500
//Xsec[25] = Sw  *  1.21*0.03089;  // WJets HT 2500-Inf

Xsec[26] = Stt  *  44.51; // single top
Xsec[27] = Stt  *  26.49; // single top
Xsec[28] = Stt  *  3.38; // single top
Xsec[29] = Stt  *  35.85; // single top
Xsec[30] = Stt  *  35.85; // single top

//Xsec[15] = 1.23*139.4; // DY HT
//Xsec[16] = 1.23*42.75; // DY HT
//Xsec[17] = 1.23*5.497; // DY HT
//Xsec[18] = 1.23*2.21;  // DY HT
//

double metbins[4]={200,350,500,1000};
TH1F* h_mc[nfiles] ;
TH1F* h_mc_both[nfiles];
float normalization[nfiles];
TH1F *h_data;
TH1F * h_temp;

for(int i =0; i<(int)filenameString.size()-1; i++){
fIn = new TFile(filenameString[i],"READ");
if(VARIABLEBINS){
h_temp = (TH1F*) fIn->Get(histnameString);
h_temp->Sumw2();
h_temp->Rebin(3,"hnew",metbins);
h_mc[i]= (TH1F*)hnew->Clone();
}else{
h_mc[i] = (TH1F*) fIn->Get(histnameString);
//h_mc_both[i] = (TH1F*) fIn->Get(new_name);
//h_mc[i]->Add(h_mc_both[i]);
h_mc[i]->Rebin(REBIN); 
h_mc[i]->Sumw2();
}
// h_total      = (TH1F*) fIn->Get("nEvents_weight");
 h_total      = (TH1F*) fIn->Get("h_total_weight");
 
//std::cout<<" normalization for = "<<i<<"  "<<filenameString[i]<<"   "
//<<h_mc[i]->Integral()
//<<std::endl;

 if(h_total->Integral()>0)
   normalization[i]     = (lumi* Xsec[i])/(h_total->Integral());
 else normalization[i]      = 0;
 //cout<<"normalization :" << normalization[i] << std::endl;

 Integral[i] = h_mc[i]->Integral();
 if(Integral[i]<=0) Integral_Error[i] = 0.0;
 if(Integral[i]>0) Integral_Error[i] = TMath::Sqrt(Integral[i]) * normalization[i];
 h_mc[i]->Scale(normalization[i]);  

std::cout<<" file = "<<filenameString[i]<<"   "<<" integral = "<<h_mc[i]->Integral()<<std::endl;
//std::cout<<i <<"       integral = "<<Integral[i]
//      <<" Integral_Error[i]"<<Integral_Error[i]<<"  normalization[i] = "<<normalization[i]<<" mul = "<<TMath::Sqrt(Integral[i]) * normalization[i]<<std::endl;
// mout << filenameString[i] <<  "  &  " << Xsec[i] <<"  &  " << std::endl; 
//// cout << "Integral : " << h_total->Integral() << "  Entries :  " << h_total->GetEntries() << std::endl;                                         

 }

fIn = new TFile(filenameString[nfiles-1],"READ");
if(VARIABLEBINS){
h_temp =(TH1F*) fIn->Get(histnameString);
h_temp->Rebin(3,"hnew",metbins);
h_data= (TH1F*)hnew->Clone();
std::cout<<" Number of events in data histogram = "<<h_data->Integral()<<std::endl;
}else{
h_data = (TH1F*) fIn->Get(histnameString);
//TH1F *h_data_new = (TH1F*) fIn->Get(new_name);

//h_data->Add(h_data_new);
h_data->Rebin(REBIN);
std::cout<<" Number of events in data histogram = "<<h_data->Integral()<<" file name = "<<filenameString[i]<<std::endl;                                                                                                  

h_data->Sumw2();
}

data_obs = (TH1F*) fIn->Get(histnameString);
monoHbbM600  = (TH1F*)h_mc[7]->Clone();
monoHbbM800  = (TH1F*)h_mc[8]->Clone();
monoHbbM1000 = (TH1F*)h_mc[9]->Clone();
monoHbbM1200 = (TH1F*)h_mc[10]->Clone();
monoHbbM1400 = (TH1F*)h_mc[11]->Clone();
monoHbbM1700 = (TH1F*)h_mc[12]->Clone();
monoHbbM2000 = (TH1F*)h_mc[13]->Clone();
monoHbbM2500 = (TH1F*)h_mc[14]->Clone();

DIBOSON   = (TH1F*)h_mc[2]->Clone();
DIBOSON->Add(h_mc[3]);
DIBOSON->Add(h_mc[4]);

ZH        = (TH1F*)h_mc[6]->Clone();

TTJets        = (TH1F*)h_mc[5]->Clone();

STop=(TH1F*)h_mc[26]->Clone();
for(int ttjets = 27; ttjets < 31; ttjets++){
STop->Add(h_mc[ttjets]);}

TT = (TH1F*)TTJets->Clone();
TT->Add(STop);

WJets     = (TH1F*)h_mc[19]->Clone();
for(int wjets1 = 20; wjets1 < 26; wjets1++){
WJets->Add(h_mc[wjets1]);}

DYJets    = (TH1F*)h_mc[12]->Clone();
for(int DYjets = 13; DYjets < 19; DYjets++){
DYJets->Add(h_mc[DYjets]);}


 //Legend
 TLegend *legend;
 
 if(NORATIOPLOT){
 //legend = new TLegend(0.73, 0.62, 0.95,0.92,NULL,"brNDC");
legend = new TLegend(0.58, 0.69, 0.92,0.94,NULL,"brNDC");
 legend->SetTextSize(0.036);
 }else{

legend = new TLegend(0.57, 0.62, 0.94,0.90,NULL,"brNDC"); 
//legend = new TLegend(0.13, 0.85, 0.95,0.92,NULL,"brNDC");
// legend = new TLegend(0.7, 0.68, 0.95,0.92,NULL,"brNDC");
 legend->SetTextSize(0.046); }
 legend->SetBorderSize(0);
 legend->SetLineColor(1);
 legend->SetLineStyle(1);
 legend->SetLineWidth(1);
 legend->SetFillColor(0);
 legend->SetFillStyle(0);
 legend->SetTextFont(62);
 legend->SetNColumns(2);
 legend->AddEntry(h_data,"Data","p");                                                                                                         
// legend->AddEntry(h_mc[9],"M_{Z'}=1000", "l");

 legend->AddEntry(DYJets,"Zj","f");
// legend->AddEntry(h_mc[11],"M_{Z'}=1400", "l");

 legend->AddEntry(WJets,"Wj","f");
// legend->AddEntry(h_mc[13],"M_{Z'}=2000", "l");

 legend->AddEntry(TT,"Top","f");

  

 
//===========================Latex=================//
TString latexCMSname= "CMS #it{#bf{Preliminary}}";
TString latexPreCMSname= "Z'#rightarrow DM+H(b#bar{b})";
 
TString latexnamemiddle;
latexnamemiddle.Form("%1.1f fb^{-1}",luminosity); 
TString latexnamepost = " (13 TeV)";
//TString latexname = latexnamepre+latexnamemiddle+latexnamepost;  
TString latexname = latexnamemiddle+latexnamepost;
TString histolabel;
if("HISTPATH" == "Signal"){
histolabel = "SR(boosted)";}
if("HISTPATH" =="histfacFatJet_ZLight"){
histolabel = "Zj CR(boosted)";}
if("HISTPATH" =="histfacFatJet_WHeavy" ){
histolabel = "1-lepton CR(boosted)";}


TLatex *t2b;
TLatex *t2c;
TLatex *t2d;

if(NORATIOPLOT){
 t2b = new TLatex(0.15,0.85,latexCMSname);
 t2b->SetTextSize(0.036);

 t2a = new TLatex(0.65,0.95,latexname);
 t2a->SetTextSize(0.034);

// t2c = new TLatex(0.25,0.82,latexPreCMSname);
// t2c->SetTextSize(0.036);
// t2d = new TLatex(0.25,0.77,histolabel);
// t2d->SetTextSize(0.036);
 t2c = new TLatex(0.15,0.84,latexPreCMSname);
 t2c->SetTextSize(0.036);

 t2d = new TLatex(0.15,0.79,histolabel);
 t2d->SetTextSize(0.036);

 }else{
 t2b = new TLatex(0.180,0.88,latexCMSname);
 t2b->SetTextSize(0.05);

 t2a = new TLatex(0.660,0.975,latexname);
 t2a->SetTextSize(0.047); 

 t2c = new TLatex(0.180,0.835,latexPreCMSname);
 t2c->SetTextSize(0.047);

 t2d = new TLatex(0.180,0.785,histolabel);
 t2d->SetTextSize(0.05);

// t2c = new TLatex(0.270,0.79,latexPreCMSname);
// t2c->SetTextSize(0.047);

// t2d = new TLatex(0.270,0.74.5,histolabel);
// t2d->SetTextSize(0.05);


 }
//SetTextAlign(12);
//    latex->SetTextFont(62);
 t2a->SetTextAlign(12);
 t2a->SetNDC(kTRUE);
 t2a->SetTextFont(62);

 t2b->SetTextAlign(12);
 t2b->SetNDC(kTRUE);
 t2b->SetTextFont(62);

 t2c->SetTextAlign(12);
 t2c->SetNDC(kTRUE);
 t2c->SetTextFont(62);

 t2d->SetTextAlign(12);
 t2d->SetNDC(kTRUE);
 t2d->SetTextFont(62);

 


//============== CANVAS DECLARATION ===================
TCanvas *c12 = new TCanvas("Hist", "Hist", 0,0,550,550);
 
//==================Stack==========================                                                                  
THStack *hs = new THStack("hs"," ");

// For N-1 Plots only
bool nminus = 0;
TLatex *tt;
if(("HISTPATH" == "ElectronNMinus1E") || ("HISTPATH" == "ElectronNMinus1B") ){
nminus =1;
tt  = new TLatex(0.5,0.87,"N-1");
tt->SetTextSize(0.05);
tt->SetTextAlign(22);
tt->SetNDC(kTRUE);
tt->SetTextFont(22);
}                                                                                


                                                                                       
//Colors for Histos

h_mc[0]->SetFillColor(616);
h_mc[0]->SetLineColor(1);
//DYJets->SetFillColor(5);
DYJets->SetFillColor(kOrange-3);
DYJets->SetLineColor(1);
//DYJets->SetLineWidth(3);

ZH->SetFillColor(kRed-10);
ZH->SetLineColor(1);

//DIBOSON->SetFillColor(920);
DIBOSON->SetFillColor(kGray+2);
DIBOSON->SetLineColor(1);

//TT->SetFillColor(596);
TT->SetFillColor(kCyan+2);
TT->SetLineColor(1);

//WJets->SetFillColor(820);                                                                                                            
WJets->SetFillColor(kGreen+3);                                                                                                            
WJets->SetLineColor(1);



//h_mc[9]->SetLineColor(41);
//h_mc[9]->SetLineWidth(3);
//h_mc[11]->SetLineColor(43);
//h_mc[11]->SetLineWidth(3);
//h_mc[13]->SetLineColor(47);
//h_mc[13]->SetLineWidth(3);
//
h_mc[9]->SetLineColor(kBlue);
h_mc[9]->SetLineWidth(3);
h_mc[9]->SetLineStyle(8);
h_mc[11]->SetLineColor(kMagenta);
h_mc[11]->SetLineWidth(3);
h_mc[11]->SetLineStyle(8);
h_mc[10]->SetLineColor(kGreen);
h_mc[10]->SetLineWidth(3);
h_mc[10]->SetLineStyle(8);


//hadd all the histos acc to their contributions


float tt_i = TT->Integral();
float wj_i = WJets->Integral();
float zj_i = DYJets->Integral();

int order_ = 0;

if (tt_i > wj_i && tt_i > zj_i) order_ = 0;
if (wj_i > tt_i && wj_i > zj_i) order_ = 1;
if ( zj_i > tt_i && zj_i > wj_i) order_ = 2;

hs->Add(DIBOSON,"hist");
hs->Add(ZH,"hist"); 

if (order_==0) {
hs->Add(WJets,"hist");
hs->Add(DYJets,"hist");
hs->Add(TT,"hist");
}

if (order_==1) {
hs->Add(DYJets,"hist");
hs->Add(TT,"hist");
hs->Add(WJets,"hist");
}

if (order_==2) {
hs->Add(TT,"hist");
hs->Add(WJets,"hist");
hs->Add(DYJets,"hist");
}





h_data->SetMarkerColor(kBlack);
h_data->SetMarkerStyle(20);
float maxi = h_data->GetMaximum();

 TH1F *Stackhist = (TH1F*)hs->GetStack()->Last(); 
 TH1F* h_err;
 h_err = (TH1F*) h_data->Clone("h_err");
 h_err->Sumw2();
 h_err->Reset();



h_err->Add(DIBOSON);
h_err->Add(ZH); 
h_err->Add(WJets);
h_err->Add(DYJets);
h_err->Add(TT);



 
// h_err->Add(h_mc[2]);
 //h_err->Add(h_mc[3]);
 //h_err->Add(h_mc[4]);
 //h_err->Add(h_mc[5]);
 //h_err->Add(h_mc[6]);

 
 //h_err->Add(h_mc[12]);
 //h_err->Add(h_mc[13]);
 //h_err->Add(h_mc[14]);
 //h_err->Add(h_mc[15]);
 //h_err->Add(h_mc[16]);
 //h_err->Add(h_mc[17]);
 //h_err->Add(h_mc[18]);

 //h_err->Add(h_mc[19]);
 //h_err->Add(h_mc[20]);
 //h_err->Add(h_mc[21]);
 //h_err->Add(h_mc[22]);
 //h_err->Add(h_mc[23]);
 //h_err->Add(h_mc[24]);
 //h_err->Add(h_mc[25]);
 //h_err->Add(h_mc[26]);
 //h_err->Add(h_mc[27]);
 //h_err->Add(h_mc[28]);
 //h_err->Add(h_mc[29]);
 //h_err->Add(h_mc[30]);

Stackhist->SetLineWidth(2);                                                                                                                                                        

// for (int ibin=0; ibin<h_err->GetNbinsX();ibin++){
  // std::cout<<" stack err = "<<h_err->GetBinError(ibin)<<std::endl;
// }


//Setting canvas without log axis
c12->SetLogy(0);
  
  
  
  // Upper canvas declaration
 
  if(NORATIOPLOT){
  TPad *c1_2 = new TPad("c1_2","newpad",0,0.05,1,0.993);
  }else{
  TPad *c1_2 = new TPad("c1_2","newpad",0,0.3,1,1.0);
  c1_2->SetBottomMargin(0.03);
  c1_2->SetTopMargin(0.06);
  }

  c1_2->SetLogy(ISLOG);
  if(VARIABLEBINS){ c1_2->SetLogx(0);}
  c1_2->Draw();
  c1_2->cd();


hs->Draw();


std::cout<<" PREFITDIR "<<std::endl;
TH1F* h_prefit;
TFile* fprefit;
TString prefitfilename = "PREFITDIR/HISTPATH.root";
if(DRAWPREFIT){
fprefit = new TFile(prefitfilename,"READ");
h_prefit = (TH1F*) fprefit->Get("bkgSum");
std::cout<<" inside prefit loop "<<h_prefit->Integral()<<std::endl;
h_prefit->SetLineColor(kRed);
h_prefit->SetLineWidth(3);
h_prefit->SetFillColor(0);
//h_prefit->Draw("histsame");

//Stackhist->Draw("histsame");
//Stackhist->SetLineColor(kBlack);
//Stackhist->SetLineWidth(2);
//Stackhist->SetFillColor(0);

}

//dirnames=['MonoHFatJetSelection_JetAndLeptonVeto','histfacFatJet_ZLight','histfacFatJet_WHeavy']
if("HISTNAME"=="h_cutFlow0"){
   if("HISTPATH" == "MonoHFatJetSelection_JetAndLeptonVeto"){
    hs->GetXaxis()->SetBinLabel(1,"Preselection");
    hs->GetXaxis()->SetBinLabel(2,"AntiQCD");
    hs->GetXaxis()->SetBinLabel(3,"Mass");
    hs->GetXaxis()->SetBinLabel(4,"CSV1/2");
    hs->GetXaxis()->SetBinLabel(5,"l-veto");
    hs->GetXaxis()->SetBinLabel(6,"jet(b)-veto");
}

   if("HISTPATH" == "histfacFatJet_ZLight"){
    hs->GetXaxis()->SetBinLabel(1,"Preselection");
    hs->GetXaxis()->SetBinLabel(2,"AntiQCD");
    hs->GetXaxis()->SetBinLabel(3,"Mass");
    hs->GetXaxis()->SetBinLabel(4,"CSV1/2");
    hs->GetXaxis()->SetBinLabel(5,"l-veto");
    hs->GetXaxis()->SetBinLabel(6,"jet(b)-veto");
}


   if("HISTPATH" == "histfacFatJet_WHeavy"){
    hs->GetXaxis()->SetBinLabel(1,"Preselection");
    hs->GetXaxis()->SetBinLabel(2,"AntiQCD");
    hs->GetXaxis()->SetBinLabel(3,"Mass");
    hs->GetXaxis()->SetBinLabel(4,"CSV1/2");
    hs->GetXaxis()->SetBinLabel(5,"1-lepton");
}




}


  TH1F *Stackhist1 = (TH1F*)hs->GetStack()->Last(); 
  h_err->Draw("E2 SAME");
  h_err->Sumw2();
//  h_err->SetFillColor(kGray+3);
//  h_err->SetLineColor(kGray+3);

  h_err->SetFillColor(kRed+3);
  h_err->SetLineColor(kRed+3);
  h_err->SetMarkerSize(0);
  h_err->SetFillStyle(3013);

  h_data->SetLineColor(1);
  if(!NORATIOPLOT){
  h_data->Draw("same p e1");
  }
  if(!NORATIOPLOT){
  if(ISLOG)    hs->SetMinimum(0.1);
  if(!ISLOG)   hs->SetMinimum(1);
  if(!ISLOG)   hs->SetMaximum(maxi *1.8);
  if(ISLOG)    hs->SetMaximum(maxi *500);
  //if(!ISLOG) hs->SetMaximum(0.4);
  }else{
  if(ISLOG)    hs->SetMinimum(0.1);
  if(!ISLOG)   hs->SetMinimum(1);
  if(!ISLOG)   hs->SetMaximum(maxi *1.70);
  if(ISLOG)    hs->SetMaximum(maxi *100);
} 


//  cout <<"binofwidth = "<< binofwidth <<" binwidth_ = "<<binwidth_<<std::endl;

  double binofwidth = h_mc[0]->GetBinWidth(1);
  TString binwidth_;
  binwidth_.Form("%1.1f",binofwidth);
  
//hs->GetXaxis()->SetTickLength(0.07);
hs->GetXaxis()->SetNdivisions(508);                                                                                                                                             

  if(NORATIOPLOT){
  hs->GetXaxis()->SetTitleSize(0.05);
  hs->GetXaxis()->SetTitleOffset(0.97);
  hs->GetXaxis()->SetTitleFont(22);
  hs->GetXaxis()->SetLabelFont(22);
  hs->GetXaxis()->SetLabelSize(.05);
  hs->GetYaxis()->SetTitle("Events");
  if(!VARIABLEBINS){    hs->GetYaxis()->SetTitle("Events/"+binwidth_);}
  hs->GetYaxis()->SetTitleSize(0.05);
  hs->GetYaxis()->SetTitleOffset(0.88);
  hs->GetYaxis()->SetTitleFont(22);
  hs->GetYaxis()->SetLabelFont(22);
  hs->GetYaxis()->SetLabelSize(0.05);
  hs->GetXaxis()->SetTitle("XAXISLABEL");
  if(VARIABLEBINS){
   hs->GetXaxis()->SetMoreLogLabels();                                                                                                       
  hs->GetXaxis()->SetNoExponent();}
  }else{
  hs->GetXaxis()->SetLabelOffset(999);
  hs->GetXaxis()->SetLabelSize(0); 
  hs->GetYaxis()->SetTitle("Events");                                                                                                                                                 if(!VARIABLEBINS){   hs->GetYaxis()->SetTitle("Events/"+binwidth_);                                   }

  hs->GetYaxis()->SetTitleSize(0.07); 
  hs->GetYaxis()->SetTitleOffset(0.8);
  hs->GetYaxis()->SetTitleFont(22);
  hs->GetYaxis()->SetLabelFont(22);
  hs->GetYaxis()->SetLabelSize(.07);

  }  


  hs->GetXaxis()->SetRangeUser(XMIN,XMAX);  
  hs->GetXaxis()->SetNdivisions(508); 
 // if(VARIABLEBINS){ hs->GetXaxis()->SetNdivisions(310);}

  legend->AddEntry(h_prefit,"Pre-fit","l");
  legend->AddEntry(DIBOSON,"VV","f");
  legend->AddEntry(Stackhist,"Post-fit","l");
  legend->AddEntry(ZH,"VH","f");
  legend->AddEntry(h_err,"Stats. Unc.","f");

   legend->Draw("same"); 
  t2a->Draw("same");
  t2b->Draw("same");
  t2c->Draw("same");
  t2d->Draw("same");
  
  if(nminus = =1){tt->Draw("same");}
  
// Commenting out the signal for control region

//  h_mc[9]->Draw("hist same");
  //h_mc[11]->Draw("hist same");
//  h_mc[13]->Draw("hist same");

  h_data->Draw("same p e1");
// for lower band stat and sys band


TH1F * ratiostaterr = (TH1F *) h_err->Clone("ratiostaterr");
ratiostaterr->Sumw2();
ratiostaterr->SetStats(0);
ratiostaterr->SetMinimum(0);
ratiostaterr->SetMarkerSize(0);
ratiostaterr->SetFillColor(kBlack);
ratiostaterr->SetFillStyle(3013);
 
for(Int_t i = 0; i < h_err->GetNbinsX()+2; i++) {
   ratiostaterr->SetBinContent(i, 1.0);

   if(h_err->GetBinContent(i) >1e-6 ) {  //< not empty
     double binerror = h_err->GetBinError(i)/h_err->GetBinContent(i);
     ratiostaterr->SetBinError(i, binerror);
//     cout << "bin:" <<i << "binerror:" <<h_err->GetBinContent(i)<< "errorband:" << binerror <<std::endl;
   }else {
     ratiostaterr->SetBinError(i, 999.);

   }

 }

TH1F * ratiosysterr = (TH1F *) ratiostaterr->Clone("ratiosysterr");
ratiosysterr->Sumw2();
ratiosysterr->SetMarkerSize(0);
//ratiosysterr->SetFillColor(kYellow-4);
// final plot
ratiosysterr->SetFillColor(kGray);
//ratiosysterr->SetFillStyle(3002);
ratiosysterr->SetFillStyle(1001);

for(Int_t i = 0; i < h_err->GetNbinsX()+2; i++) {
   if (h_err->GetBinContent(i) > 1e-6) {  //< not empty
   double binerror2 = (pow(h_err->GetBinError(i), 2) +
   pow(0.30 * WJets->GetBinContent(i), 2) +
   pow(0.20 * WJets->GetBinContent(i), 2) +
   pow(0.30 * ZH->GetBinContent(i), 2) +
   pow(0.30 * DYJets->GetBinContent(i), 2) +
   pow(0.20 * TT->GetBinContent(i), 2) +
   pow(0.30 * STop->GetBinContent(i), 2) +
   pow(0.30 * DIBOSON->GetBinContent(i), 2));
   double binerror = sqrt(binerror2);
   ratiosysterr->SetBinError(i, binerror / h_err->GetBinContent(i));
   }
}

TLegend * ratioleg = new TLegend(0.35, 0.85, 0.94, 0.94);
ratioleg->SetFillColor(0);
ratioleg->SetLineColor(0);
ratioleg->SetShadowColor(0);
ratioleg->SetTextFont(62);
ratioleg->SetTextSize(0.09);
ratioleg->SetBorderSize(1);
ratioleg->SetNColumns(2);
//ratioleg->SetTextSize(0.07);
ratioleg->AddEntry(ratiosysterr, "MC uncert. (stat + syst)", "f");                                                                                    
ratioleg->AddEntry(ratiostaterr, "MC uncert. (stat)", "f");

  
 // Lower Tpad Decalaration
  if(! NORATIOPLOT){
  c12->cd();
  TH1F *DataMC    = (TH1F*) h_data->Clone();
  TH1F *DataMCPre = (TH1F*) h_data->Clone();
  DataMC->Divide(Stackhist);
  DataMCPre->Divide(h_prefit);
  DataMC->GetYaxis()->SetTitle("Data/MC");
  DataMC->GetYaxis()->SetTitleSize(0.14);
  DataMC->GetYaxis()->SetTitleOffset(0.38);
  DataMC->GetYaxis()->SetTitleFont(22);
  DataMC->GetYaxis()->SetLabelSize(0.15);
  DataMC->GetYaxis()->CenterTitle();
  DataMC->GetXaxis()->SetTitle("XAXISLABEL");
//DataMC->GetXaxis()->SetIndiceSize(0.1);
  DataMC->GetXaxis()->SetLabelSize(0.157);
  DataMC->GetXaxis()->SetTitleSize(0.16);
  DataMC->GetXaxis()->SetTitleOffset(1.02);
  DataMC->GetXaxis()->SetTitleFont(22);
  DataMC->GetXaxis()->SetTickLength(0.07);
  DataMC->GetXaxis()->SetLabelFont(22);
  DataMC->GetYaxis()->SetLabelFont(22);     
  
 if("HISTNAME"=="h_cutFlow0"){
   if("HISTPATH" == "MonoHFatJetSelection_JetAndLeptonVeto"){
    DataMC->GetXaxis()->SetBinLabel(1,"Preselection");
    DataMC->GetXaxis()->SetBinLabel(2,"AntiQCD");
    DataMC->GetXaxis()->SetBinLabel(3,"Mass");
    DataMC->GetXaxis()->SetBinLabel(4,"CSV1/2");
    DataMC->GetXaxis()->SetBinLabel(5,"l-veto");
    DataMC->GetXaxis()->SetBinLabel(6,"jet(b)-veto");
}

   if("HISTPATH" == "histfacFatJet_ZLight"){
    DataMC->GetXaxis()->SetBinLabel(1,"Preselection");
    DataMC->GetXaxis()->SetBinLabel(2,"AntiQCD");
    DataMC->GetXaxis()->SetBinLabel(3,"Mass");
    DataMC->GetXaxis()->SetBinLabel(4,"CSV1/2");
    DataMC->GetXaxis()->SetBinLabel(5,"l-veto");
    DataMC->GetXaxis()->SetBinLabel(6,"jet(b)-veto");
}


   if("HISTPATH" == "histfacFatJet_WHeavy"){
    DataMC->GetXaxis()->SetBinLabel(1,"Preselection");
    DataMC->GetXaxis()->SetBinLabel(2,"AntiQCD");
    DataMC->GetXaxis()->SetBinLabel(3,"Mass");
    DataMC->GetXaxis()->SetBinLabel(4,"CSV1/2");
    DataMC->GetXaxis()->SetBinLabel(5,"1-lepton");
}
}

 TPad *c1_1 = new TPad("c1_1", "newpad",0,0.00,1,0.3);
 c1_1->Draw();
 c1_1->cd();
 c1_1->Range(-7.862408,-629.6193,53.07125,486.5489);
 c1_1->SetFillColor(0);
 c1_1->SetTicky(1);
 c1_1->SetLeftMargin(0.1290323);
 c1_1->SetRightMargin(0.05040323);
 c1_1->SetTopMargin(0.0);//0.0
 c1_1->SetBottomMargin(0.366666678814);
 c1_1->SetFrameFillStyle(0);
 c1_1->SetFrameBorderMode(0);
 c1_1->SetFrameFillStyle(0);
 c1_1->SetFrameBorderMode(0);
 c1_1->SetLogy(0);
if(VARIABLEBINS){ c1_1->SetLogx(0);                                                                                                           
 DataMC->GetXaxis()->SetMoreLogLabels();                                                                                                       DataMC->GetXaxis()->SetNoExponent();
 DataMC->GetXaxis()->SetNdivisions(508);
 }     
 DataMC->GetXaxis()->SetRangeUser(XMIN,XMAX);
 DataMC->SetMarkerSize(0.7);
 DataMC->SetMarkerStyle(20);
 DataMC->SetMarkerColor(1);
 DataMCPre->SetMarkerSize(0.7);
 DataMCPre->SetMarkerStyle(20);
 DataMCPre->SetMarkerColor(kRed);
 DataMCPre->SetLineColor(kRed);


 DataMC->Draw("P e1");
 //DataMCPre->Draw("P e1 same");
ratiosysterr->Draw("e2 same");
ratiostaterr->Draw("e2 same");
 DataMC->Draw("P e1 same");
 //DataMCPre->Draw("P e1 same");

DataMC->Draw("P e1 same");
 DataMC->SetMinimum(-0.2);
 DataMC->SetMaximum(2.2);
 DataMC->GetXaxis()->SetNdivisions(508);
 DataMC->GetYaxis()->SetNdivisions(505);
 TLine* line0= new TLine(XMIN,1,XMAX,1);
 line0->SetLineStyle(2);
 line0->Draw("same");
 //c1_1->SetGridy();
ratioleg->Draw("same");
 }
  


if(TEXTINFILE){ 
   
//=======================================================================
  //Calculating the contribution of each background in particular range
 // As Data DY(ee) diboson TTjets WWJets
 TAxis *xaxis = h_mc[0]->GetXaxis();
 Int_t binxmin = xaxis->FindBin(XMIN);
 Int_t binxmax = xaxis->FindBin(XMAX);
      
float dyjets = h_mc[12]->Integral() + h_mc[13]->Integral() + h_mc[14]->Integral() + h_mc[15]->Integral()+h_mc[16]->Integral()+h_mc[17]->Integral()+h_mc[18]->Integral(); 
float dyjets_error = TMath::Sqrt(pow(Integral_Error[15],2) + pow(Integral_Error[16],2) + pow(Integral_Error[17],2) + pow(Integral_Error[18],2) );

float diboson_ = h_mc[2]->Integral() + h_mc[3]->Integral() + h_mc[4]->Integral();
float diboson_error = TMath::Sqrt(pow(Integral_Error[2],2) + pow(Integral_Error[3],2) + pow(Integral_Error[4],2));

float tt_ = h_mc[5]->Integral() + h_mc[26]->Integral()+h_mc[27]->Integral()+h_mc[28]->Integral()+h_mc[29]->Integral()+ h_mc[30]->Integral() ;
float tt_error = TMath::Sqrt(pow(Integral_Error[5],2) + pow(Integral_Error[26],2) + pow(Integral_Error[27],2) +pow(Integral_Error[28],2) +pow(Integral_Error[29],2) +pow(Integral_Error[30],2)) ;

float wjets = h_mc[19]->Integral() +h_mc[20]->Integral()+h_mc[21]->Integral()+h_mc[22]->Integral()+h_mc[23]->Integral()+h_mc[24]->Integral()+h_mc[25]->Integral() ;
float wjets_error = TMath::Sqrt(pow(Integral_Error[19],2) + pow(Integral_Error[20],2) +pow(Integral_Error[21],2) +pow(Integral_Error[22],2) +pow(Integral_Error[23],2) +pow(Integral_Error[24],2) +pow(Integral_Error[25],2)) ;

std::cout<<" wjets_error = "<<wjets_error<<std::endl;
float zh = h_mc[6]->Integral();
float zh_error = TMath::Sqrt(pow(Integral_Error[6],2));


  mout << "HISTPATH_HISTNAME"            <<  " a b"<<std::endl; 
  mout << " DATA "    << h_data->Integral()  <<" 0"<< std::endl; 
  mout << " DIBOSON " << diboson_                  <<" "<<diboson_error << std::endl;
  mout << " TT "      << tt_ <<" "<<tt_error <<  std::endl; 
  mout << " WJETS "   << wjets<< " "<<wjets_error<<std::endl;
  mout << " ZH "      << zh <<" "<<zh_error<< std::endl;
  mout << " DYJETS "  <<dyjets <<" "<<dyjets_error <<std::endl;  
  mout << " M600 "    << h_mc[7]->Integral() <<" "<<Integral_Error[7]<< std::endl;
  mout << " M800 "    << h_mc[8]->Integral() <<" "<<Integral_Error[8]<< std::endl;
  mout << " M1000 "    << h_mc[9]->Integral() <<" "<<Integral_Error[9]<< std::endl;
  mout << " M1200 "    << h_mc[10]->Integral() <<" "<<Integral_Error[10]<< std::endl;
  mout << " M1400 "   << h_mc[11]->Integral() <<" "<<Integral_Error[11]<< std::endl;
  mout << " M1700 "   << h_mc[12]->Integral() <<" "<<Integral_Error[12]<< std::endl;
  mout << " M2000 "   << h_mc[13]->Integral() <<" "<<Integral_Error[13]<< std::endl;
  mout << " M2500 "   << h_mc[14]->Integral() <<" "<<Integral_Error[14]<< std::endl;
//  mout << "Total Bkg " <<diboson_+tt_+wjets+zh+dyjets <<" "<< diboson_error+tt_error+wjets_error+zh_error+dyjets_error <<std::endl;
  mout << "========= ======================== =====================" <<std::endl;
//=========================================================================

if(VARIABLEBINS){
//  metbinsout_2.precision(3);
  metbinsout_2 << " DATA "    << h_data->GetBinContent(2)   <<" 0"<< std::endl; 
  metbinsout_2 << " DIBOSON " << DIBOSON->GetBinContent(2)  <<" "<<DIBOSON->GetBinError(2)<< std::endl;
  metbinsout_2 << " TT "      << TT->GetBinContent(2)       <<" "<<TT->GetBinError(2)     <<  std::endl; 
  metbinsout_2 << " WJETS "   << WJets->GetBinContent(2)    <<" "<<WJets->GetBinError(2)  <<std::endl;
  metbinsout_2 << " ZH "      << ZH->GetBinContent(2)       <<" "<<ZH->GetBinError(2)     << std::endl;
  metbinsout_2 << " DYJETS "  <<DYJets->GetBinContent(2)    <<" "<<DYJets->GetBinError(2) <<std::endl;  
  metbinsout_2 << " M600 "    << h_mc[7]->GetBinContent(2)  <<" "<<h_mc[7]->GetBinError(2)<< std::endl;
  metbinsout_2 << " M800 "    << h_mc[8]->GetBinContent(2)  <<" "<<h_mc[8]->GetBinError(2)<< std::endl;
  metbinsout_2 << " M1000 "   << h_mc[9]->GetBinContent(2)  <<" "<<h_mc[9]->GetBinError(2)<< std::endl;
  metbinsout_2 << " M1200 "   << h_mc[10]->GetBinContent(2) <<" "<<h_mc[10]->GetBinError(2)<< std::endl;
  metbinsout_2 << " M1400 "   << h_mc[11]->GetBinContent(2) <<" "<<h_mc[11]->GetBinError(2)<< std::endl;
  metbinsout_2 << " M1700 "   << h_mc[12]->GetBinContent(2) <<" "<<h_mc[12]->GetBinError(2)<< std::endl;
  metbinsout_2 << " M2000 "   << h_mc[13]->GetBinContent(2) <<" "<<h_mc[13]->GetBinError(2)<< std::endl;
  metbinsout_2 << " M2500 "   << h_mc[14]->GetBinContent(2) <<" "<<h_mc[14]->GetBinError(2)<< std::endl;
  mout << "========= ======================== =====================" <<std::endl;
}

if(VARIABLEBINS){
  //metbinsout_3.precision(3);
  metbinsout_3 << " DATA "    << h_data->GetBinContent(3)   <<" 0"<< std::endl; 
  metbinsout_3 << " DIBOSON " << DIBOSON->GetBinContent(3)  <<" "<<DIBOSON->GetBinError(3)<< std::endl;
  metbinsout_3 << " TT "      << TT->GetBinContent(3)       <<" "<<TT->GetBinError(3)     <<  std::endl; 
  metbinsout_3 << " WJETS "   << WJets->GetBinContent(3)    <<" "<<WJets->GetBinError(3)  <<std::endl;
  metbinsout_3 << " ZH "      << ZH->GetBinContent(3)       <<" "<<ZH->GetBinError(3)     << std::endl;
  metbinsout_3 << " DYJETS "  <<DYJets->GetBinContent(3)    <<" "<<DYJets->GetBinError(3) <<std::endl;  
  metbinsout_3 << " M600 "    << h_mc[7]->GetBinContent(3)  <<" "<<h_mc[7]->GetBinError(3)<< std::endl;
  metbinsout_3 << " M800 "    << h_mc[8]->GetBinContent(3)  <<" "<<h_mc[8]->GetBinError(3)<< std::endl;
  metbinsout_3 << " M1000 "   << h_mc[9]->GetBinContent(3)  <<" "<<h_mc[9]->GetBinError(3)<< std::endl;
  metbinsout_3 << " M1200 "   << h_mc[10]->GetBinContent(3) <<" "<<h_mc[10]->GetBinError(3)<< std::endl;
  metbinsout_3 << " M1400 "   << h_mc[11]->GetBinContent(3) <<" "<<h_mc[11]->GetBinError(3)<< std::endl;
  metbinsout_3 << " M1700 "   << h_mc[12]->GetBinContent(3) <<" "<<h_mc[12]->GetBinError(3)<< std::endl;
  metbinsout_3 << " M2000 "   << h_mc[13]->GetBinContent(3) <<" "<<h_mc[13]->GetBinError(3)<< std::endl;
  metbinsout_3 << " M2500 "   << h_mc[14]->GetBinContent(3) <<" "<<h_mc[14]->GetBinError(3)<< std::endl;
  mout << "========= ======================== =====================" <<std::endl;
}

if(VARIABLEBINS){
 // metbinsout_1.precision(3);
  metbinsout_1 << " DATA "    << h_data->GetBinContent(1)   <<" 0"<< std::endl; 
  metbinsout_1 << " DIBOSON " << DIBOSON->GetBinContent(1)  <<" "<<DIBOSON->GetBinError(1)<< std::endl;
  metbinsout_1 << " TT "      << TT->GetBinContent(1)       <<" "<<TT->GetBinError(1)     <<  std::endl; 
  metbinsout_1 << " WJETS "   << WJets->GetBinContent(1)    <<" "<<WJets->GetBinError(1)  <<std::endl;
  metbinsout_1 << " ZH "      << ZH->GetBinContent(1)       <<" "<<ZH->GetBinError(1)     << std::endl;
  metbinsout_1 << " DYJETS "  <<DYJets->GetBinContent(1)    <<" "<<DYJets->GetBinError(1) <<std::endl;  
  metbinsout_1 << " M600 "    << h_mc[7]->GetBinContent(1)  <<" "<<h_mc[7]->GetBinError(1)<< std::endl;
  metbinsout_1 << " M800 "    << h_mc[8]->GetBinContent(1)  <<" "<<h_mc[8]->GetBinError(1)<< std::endl;
  metbinsout_1 << " M1000 "   << h_mc[9]->GetBinContent(1)  <<" "<<h_mc[9]->GetBinError(1)<< std::endl;
  metbinsout_1 << " M1200 "   << h_mc[10]->GetBinContent(1) <<" "<<h_mc[10]->GetBinError(1)<< std::endl;
  metbinsout_1 << " M1400 "   << h_mc[11]->GetBinContent(1) <<" "<<h_mc[11]->GetBinError(1)<< std::endl;
  metbinsout_1 << " M1700 "   << h_mc[12]->GetBinContent(1) <<" "<<h_mc[12]->GetBinError(1)<< std::endl;
  metbinsout_1 << " M2000 "   << h_mc[13]->GetBinContent(1) <<" "<<h_mc[13]->GetBinError(1)<< std::endl;
  metbinsout_1 << " M2500 "   << h_mc[14]->GetBinContent(1) <<" "<<h_mc[14]->GetBinError(1)<< std::endl;
  mout << "========= ======================== =====================" <<std::endl;
}




// --------------------- table output --------------------
  tableout.precision(3);
  tableout << " Z \\rightarrow \\nu \\nu+Jets & "<< dyjets <<" \\pm "<<dyjets_error <<"\\\\"<<std::endl;  
  tableout << " t \\bar{t} & "<< tt_ <<" \\pm "<<tt_error <<"\\\\"<< std::endl; 
  tableout << " W+Jets & "  <<wjets <<" \\pm "<<wjets_error <<"\\\\"<< std::endl;
  tableout << " WW/WZ/ZZ & " << diboson_ <<" \\pm "<<diboson_error  <<"\\\\"<< std::endl;
  tableout << " ZH & "      << h_mc[6]->Integral() <<" \\pm "<<Integral_Error[6]<<"\\\\"<< std::endl;
  tableout << " M600  & "    << h_mc[7]->Integral() <<" \\pm "<<Integral_Error[7]<<"\\\\"<< std::endl;
  tableout << " M800  & "    << h_mc[8]->Integral() <<" \\pm "<<Integral_Error[8]<<"\\\\"<< std::endl;
  tableout << " M1000 &  "    << h_mc[9]->Integral() <<" \\pm "<<Integral_Error[9]<<"\\\\"<< std::endl;
  tableout << " M1200 &  "    << h_mc[10]->Integral() <<" \\pm "<<Integral_Error[10]<<"\\\\"<< std::endl;
  tableout << " M1400 &  "   << h_mc[11]->Integral() <<" \\pm "<<Integral_Error[11]<<"\\\\"<< std::endl;
  tableout << " M1700 &  "   << h_mc[12]->Integral() <<" \\pm "<<Integral_Error[12]<<"\\\\"<< std::endl;
  tableout << " M2000 &  "   << h_mc[13]->Integral() <<" \\pm "<<Integral_Error[13]<<"\\\\"<< std::endl;
  tableout << " M2500 &  "   << h_mc[14]->Integral() <<" \\pm "<<Integral_Error[14]<<"\\\\"<< std::endl;
  tableout << " DATA  & "    << h_data->Integral()  << std::endl; 

float a = wjets;
float b = tt_;
float c = h_data->Integral() - (diboson_ + zh + dyjets);

tableout << "a "<<a<<" "<<" b "<<b<<" "<<" c "<<c<<std::endl;
tableout << a <<"  "<< b <<"  " << diboson_ <<"  " << zh <<"  "<< dyjets<<std::endl;
tableout<<" total_bkg "<<a + b + diboson_ + zh + dyjets<<std::endl;
tableout<< " "<<std::endl;
}
 
 c12->Draw();
if(!ISLOG){
 c12->SaveAs(DirPreName+dirpathname +"/MonoHPdf/zj_HISTNAME.pdf");
 c12->SaveAs(DirPreName+dirpathname +"/MonoHPng/zj_HISTNAME.png");
 c12->SaveAs(DirPreName+dirpathname +"/MonoHROOT/zj_HISTNAME.root");                                                                         
 rout<<"<hr/>"<<std::endl;
 rout<<"<table class=\"\"> <tr><td><img src=\""<<"DYPng/HISTPATH_HISTNAME.png\" height=\"400\" width=\"400\"></td>   </tr> </table>"<<std::endl;

}
 
if(ISLOG){
 c12->SaveAs(DirPreName+dirpathname +"/MonoHPdf/HISTPATH_HISTNAME_log.pdf");
 c12->SaveAs(DirPreName+dirpathname +"/MonoHPng/HISTPATH_HISTNAME_log.png");
 c12->SaveAs(DirPreName+dirpathname +"/MonoHROOT/HISTPATH_HISTNAME_log.root");                                                                        
}


fshape->cd();
//Save root files for datacards
Stackhist->SetNameTitle("bkgSum","bkgSum");
Stackhist->Write();
monoHbbM600->SetNameTitle("monoHbbM600","monoHbbM600"); 
monoHbbM600->Write();
monoHbbM800->SetNameTitle("monoHbbM800","monoHbbM800");
monoHbbM800->Write();
monoHbbM1000->SetNameTitle("monoHbbM1000","monoHbbM1000");
monoHbbM1000->Write();
monoHbbM1200->SetNameTitle("monoHbbM1200","monoHbbM1200");
monoHbbM1200->Write();
monoHbbM1400->SetNameTitle("monoHbbM1400","monoHbbM1400");
monoHbbM1400->Write(); 
monoHbbM1700->SetNameTitle("monoHbbM1700","monoHbbM1700");
monoHbbM1700->Write();
monoHbbM2000->SetNameTitle("monoHbbM2000","monoHbbM2000");
monoHbbM2000->Write();
monoHbbM2500->SetNameTitle("monoHbbM2500","monoHbbM2500");
monoHbbM2500->Write();
DIBOSON->SetNameTitle("DIBOSON","DIBOSON");
DIBOSON->Write();
ZH->SetNameTitle("ZH","ZH");
ZH->Write();
TT->SetNameTitle("TT","TT");
TT->Write();
WJets->SetNameTitle("WJets","WJets");
WJets->Write();
DYJets->SetNameTitle("DYJets","DYJets");
DYJets->Write(); 
data_obs->SetNameTitle("data_obs","data_obs");
data_obs->Write();
fshape->Write();
fshape->Close();
if (VARIABLEBINS)
{
system("cp "+outputshapefilename+" "+DirPreName+"METBIN_1");
system("cp "+outputshapefilename+" "+DirPreName+"METBIN_2");
system("cp "+outputshapefilename+" "+DirPreName+"METBIN_3");
}



 }
