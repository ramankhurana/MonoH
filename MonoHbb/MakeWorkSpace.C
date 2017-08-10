#include "RooWorkspace.h"
#include "../../HiggsAnalysis/CombinedLimit/interface/RooParametricHist.h"
#include "RooDataHist.h"
void MakeWorkSpace(){
  
  gSystem->Load("libHiggsAnalysisCombinedLimit.so");
  // As usual, load the combine library to get access to the RooParametricHist
  gSystem->Load("libHiggsAnalysisCombinedLimit.so");
    
  // Output file and workspace 
  TFile *fOut = new TFile("workspace.root","RECREATE");
  RooWorkspace wspace("wspace","wspace");

  // A search in a MET tail, define MET as our variable
  RooRealVar met("met","E_{T}^{miss}",200,1000);
  RooArgList vars(met);

  // ---------------------------- SIGNAL REGION -------------------------------------------------------------------//
  // Make a dataset, this will be just four bins in MET. 
  // its easiest to make this from a histogram. Set the contents to "somehting"
  TH1F data_th1("data_obs_SR","Data observed in signal region",4,200,1000);
  data_th1.SetBinContent(1,100);
  data_th1.SetBinContent(2,50);
  data_th1.SetBinContent(3,25);
  data_th1.SetBinContent(4,10);
  RooDataHist data_hist("data_obs_SR","Data observed",vars,&data_th1);
  wspace.import(data_hist);
 
  // In the signal region, our background process will be freely floating, 
  // Create one parameter per bin representing the yield. (note of course we can have multiple processes like this)
  // For each bin: the parameters for each background process is freely floating and hence the background in this bin. This will be constrained by the fit from the control regions.
  // with a naive initial value and meaningful range for each bin
  // this example consider that there is only one background. 
  RooRealVar bin1("bkg_SR_bin1","Background yield in signal region, bin 1",100,0,500); 
  RooRealVar bin2("bkg_SR_bin2","Background yield in signal region, bin 2",50,0,500);
  RooRealVar bin3("bkg_SR_bin3","Background yield in signal region, bin 3",25,0,500);
  RooRealVar bin4("bkg_SR_bin4","Background yield in signal region, bin 4",10,0,500);
  RooArgList bkg_SR_bins;
  bkg_SR_bins.add(bin1);
  bkg_SR_bins.add(bin2);
  bkg_SR_bins.add(bin3);
  bkg_SR_bins.add(bin4);

  
  // Create a RooParametericHist which contains those yields, last argument is just for the binning,
  // can use the data TH1 for that
  // To amke a RooParametericHist you will need: 
  //    - name of the parametric histogram
  //    - title 
  //    - roorealvar, MET in this case 
  //    - List of the RooRealVar which are denoting the parameters for each of the bin. 
  //    - histogram which has the defined binning. In this case this is data histogram
  RooParametricHist p_bkg("bkg_SR", "Background PDF in signal region",met,bkg_SR_bins,data_th1);
  
  // Always include a _norm term which should be the sum of the yields (thats how combine likes to play with pdfs)
  RooAddition p_bkg_norm("bkg_SR_norm","Total Number of events from background in signal region",bkg_SR_bins);

  // Every signal region needs a signal 
  TH1F signal_th1("signal_SR","Signal expected in signal region",4,200,1000);
  signal_th1.SetBinContent(1,1);
  signal_th1.SetBinContent(2,2);
  signal_th1.SetBinContent(3,3);
  signal_th1.SetBinContent(4,8);
  RooDataHist signal_hist("signal","Data observed",vars,&signal_th1);
  wspace.import(signal_hist);

  
  RooDataHist data_CRhist("data_obs_CR","Data observed",vars,&data_th1);
  wspace.import(data_CRhist);
    
  // This time, the background process will be dependent on the yields of the background in the signal region. 
  // The transfer factor TF must account for acceptance/efficiency etc differences in the signal to control 
  // In this example lets assume the control region is populated by the same process decaying to clean daughters with 2xBR 
  // compared to the signal region

  // NB// This example is a trivial one, these transfer factors and FormulaVars can be ANYTHING and allow for any level of 
  // complexity desired (ie a different function per bin, different TF per bin, functionally derived TF etc...
  // One can also add systematics to the transfer factors by including nuisance parameter modifiers in the formula and declaring those 
  // nuisances as "param" in the usual way in the datacard for combine!!!

  RooRealVar TF("TF","Trasnfer factor",2); TF.setConstant(); 
  RooFormulaVar CRbin1("bkg_CR_bin1","Background yield in control region, bin 1","@0*@1",RooArgList(TF,bin1));
  RooFormulaVar CRbin2("bkg_CR_bin2","Background yield in control region, bin 2","@0*@1",RooArgList(TF,bin2));
  RooFormulaVar CRbin3("bkg_CR_bin3","Background yield in control region, bin 3","@0*@1",RooArgList(TF,bin3));
  RooFormulaVar CRbin4("bkg_CR_bin4","Background yield in control region, bin 4","@0*@1",RooArgList(TF,bin4));

  RooArgList bkg_CR_bins;
  bkg_CR_bins.add(CRbin1);
  bkg_CR_bins.add(CRbin2);
  bkg_CR_bins.add(CRbin3);
  bkg_CR_bins.add(CRbin4);
  RooParametricHist p_CRbkg("bkg_CR", "Background PDF in control region",met,bkg_CR_bins,data_th1);
  RooAddition p_CRbkg_norm("bkg_CR_norm","Total Number of events from background in control region",bkg_CR_bins);
  // -------------------------------------------------------------------------------------------------------------//
   
  // import the pdfs
  wspace.import(p_bkg);
  wspace.import(p_bkg_norm,RooFit::RecycleConflictNodes());
  wspace.import(p_CRbkg);
  wspace.import(p_CRbkg_norm,RooFit::RecycleConflictNodes());
  fOut->cd();
  wspace.Write();

}
