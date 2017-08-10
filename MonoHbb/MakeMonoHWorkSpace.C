#include <vector>
#include <utility>

bool connectWZ = false;

void addTemplate(string procname, RooArgList& varlist, RooWorkspace& ws, TH1F* hist) {
  RooDataHist rhist(procname.c_str(), "", varlist, hist);
  ws.import(rhist);
}

void makeBinList(string procname, RooRealVar& var, RooWorkspace& ws, TH1F* hist, RooArgList& binlist, bool setConst = false) {
  for (int i = 1; i <= hist->GetNbinsX(); i++) {
    stringstream binss;
    binss << procname << "_bin" << i;
    RooRealVar* binvar;
    if (!setConst) binvar = new RooRealVar(binss.str().c_str(), "", hist->GetBinContent(i), 0., hist->GetBinContent(i)*2.0);
    else           binvar = new RooRealVar(binss.str().c_str(), "", hist->GetBinContent(i));
    binlist.add(*binvar);
  }

  stringstream normss;
  normss << procname << "_norm";

  RooParametricHist phist(procname.c_str(), "", var, binlist, *hist);
  RooAddition norm(normss.str().c_str(), "", binlist);

  ws.import(phist,RooFit::RecycleConflictNodes());
  ws.import(norm, RooFit::RecycleConflictNodes());

}

void makeConnectedBinList(string procname, RooRealVar& var, RooWorkspace& ws, TH1F* rhist, vector<pair<RooRealVar*, TH1*> > syst, const RooArgList& srbinlist, RooArgList* crbinlist=NULL) {
  if (crbinlist == NULL) crbinlist = new RooArgList();

  for (int i = 1; i <= rhist->GetNbinsX(); i++) {
    stringstream rbinss;
    rbinss << "r_" << procname << "_bin" << i;
    RooRealVar* rbinvar = new RooRealVar(rbinss.str().c_str(), "", rhist->GetBinContent(i));

    stringstream rerrbinss;
    rerrbinss << procname << "_bin" << i << "_Runc";
    RooRealVar* rerrbinvar = new RooRealVar(rerrbinss.str().c_str(), "", 0., -5., 5.);

    stringstream binss;
    binss << procname << "_bin" << i;

    RooArgList fobinlist;
    fobinlist.add(srbinlist[i-1]);
    fobinlist.add(*rbinvar);
    fobinlist.add(*rerrbinvar);

    stringstream formss;
    formss << "@0/";
    formss << "(";
    formss << "@1";
    formss << "*(1+" << rhist->GetBinError(i)/rhist->GetBinContent(i) << "*@2)";
    for (int j = 0; j < syst.size(); j++) {
      stringstream systbinss;
      if (syst[j].first == NULL) {
	systbinss << procname << "_bin" << i << "_" << syst[j].second->GetName();
	RooRealVar* systbinvar = new RooRealVar(systbinss.str().c_str(), "", 0., -5., 5.);
	fobinlist.add(*systbinvar);
      }
      else {
	fobinlist.add(*syst[j].first);
      }
      formss << "*(1+" << syst[j].second->GetBinContent(i) << "*@" << j+3 << ")";
    }
    formss << ")";

    RooFormulaVar* binvar = new RooFormulaVar(binss.str().c_str(), "", formss.str().c_str(), RooArgList(fobinlist));
    crbinlist->add(*binvar);
  }

  stringstream normss;
  normss << procname << "_norm";

  RooParametricHist phist(procname.c_str(), "", var, *crbinlist, *rhist);
  RooAddition norm(normss.str().c_str(),"", *crbinlist);

  ws.import(phist,RooFit::RecycleConflictNodes());
  ws.import(norm, RooFit::RecycleConflictNodes());
}


void MakeMonoHWorkSpace(){
  gSystem->Load("libHiggsAnalysisCombinedLimit.so");
    
  TFile *outfile = new TFile("workspace.root","RECREATE");
  RooWorkspace monoHWS("w","w");

  RooRealVar MET("MET","E_{T}",200, 1000.);
  RooArgList vars(MET);

  // Read rootfiles with input templates. 
  TFile* SRfile      = new TFile ("AnalysisHistograms_MergedSkimmedV12_Puppi_V8/AllRegions/signal.root");
  TFile* WTfile      = new TFile ("AnalysisHistograms_MergedSkimmedV12_Puppi_V8/AllRegions/wt.root");
  TFile* ZJfile      = new TFile ("AnalysisHistograms_MergedSkimmedV12_Puppi_V8/AllRegions/zj.root");
  
  /*
  TFile* signalfile = new TFile("ZnnG_histos.root");
  TFile* signalddri = new TFile("Monophoton_13TeV_bkg.root");
  
  TFile* WenuGfile = new TFile("WenG_histos.root");
  TFile* WenuGdatafile = new TFile("WenG_data_all.root");
  TFile* WenuGqcdfile = new TFile("WenG_qcd_all.root");


  TFile* WmunuGfile = new TFile("WmnG_histos.root");
  TFile* WmunuGdatafile = new TFile("WmnG_data_all.root");
  TFile* WmunuGqcdfile = new TFile("WmnG_qcd_all.root");


  TFile* ZeeGfile = new TFile("ZeeG_histos.root");
  TFile* ZeeGdatafile = new TFile("ZeeG_data_all.root");


  TFile* ZmuGfile = new TFile("ZmmG_histos.root");
  TFile* ZmuGdatafile = new TFile("ZmmG_data_all.root");
  */
  
  //--------------------------------------------------------------------------------------------------------------//
  // ---------------------------- SIGNAL REGION ------------------------------------------------------------------//
  //--------------------------------------------------------------------------------------------------------------//
  
  // Data
  addTemplate("data_obs_SR", vars, monoHWS, (TH1F*)SRfile->Get("data_obs"));
  
  // Signal shape
  addTemplate("signal_SR", vars, monoHWS, (TH1F*)SRfile->Get("monoHbbM600_300"));
    
  // Znunu backgroun
  TH1F* h_znn_SR = (TH1F*) SRfile->Get("DYJETS");
  RooArgList bins_znn_SR;
  makeBinList("Znunu_SR", MET, monoHWS, h_znn_SR, bins_znn_SR);
  
  // WJets background
  TH1F* h_wln_SR = (TH1F*)SRfile->Get("WJETS");
  RooArgList bins_wln_SR;
  
    vector<pair<RooRealVar*, TH1*> > syst_wln_SR;
    syst_wln_SR.clear();
    RooRealVar* re1_wln_SR = new RooRealVar("WJets_SR_RenScale1" , "", 0., -5., 5.);
    RooRealVar* fa1_wln_SR = new RooRealVar("WJets_SR_FactScale1", "", 0., -5., 5.);
    RooRealVar* re2_wln_SR = new RooRealVar("WJets_SR_RenScale2" , "", 0., -5., 5.);
    RooRealVar* fa2_wln_SR = new RooRealVar("WJets_SR_FactScale2", "", 0., -5., 5.);
    RooRealVar* pdf_wln_SR = new RooRealVar("WJets_SR_PDF"       , "", 0., -5., 5.);
    
    /*
    wln_SR_syst.push_back(pair<RooRealVar*, TH1*>(NULL      , (TH1F*)templatesfile->Get("ZW_EWK")));
    wln_SR_syst.push_back(pair<RooRealVar*, TH1*>(wln_SR_re1, (TH1F*)templatesfile->Get("ZW_RenScale1")));
    wln_SR_syst.push_back(pair<RooRealVar*, TH1*>(wln_SR_fa1, (TH1F*)templatesfile->Get("ZW_FactScale1")));
    wln_SR_syst.push_back(pair<RooRealVar*, TH1*>(wln_SR_re2, (TH1F*)templatesfile->Get("ZW_RenScale2")));
    wln_SR_syst.push_back(pair<RooRealVar*, TH1*>(wln_SR_fa2, (TH1F*)templatesfile->Get("ZW_FactScale2")));
    wln_SR_syst.push_back(pair<RooRealVar*, TH1*>(wln_SR_pdf, (TH1F*)templatesfile->Get("ZW_PDF")));
    */
    
    if (!connectWZ) makeBinList("WJets_SR", MET, monoHWS, h_wln_SR, bins_wln_SR);
    else   makeConnectedBinList("WJets_SR", MET, monoHWS, (TH1F*)templatesfile->Get("zwjcorewkhist"), wln_SR_syst, znn_SR_bins, &wln_SR_bins);

    // Other MC backgrounds
    addTemplate("Others_SR"     , vars, monoHWS, (TH1F*)signalddri->Get("hstack1"));
    
    
    addTemplate("QCD_SR"       , vars, monoHWS, (TH1F*)signalddri->Get("qcd"));
    addTemplate("Elefa_SR"       , vars, monoHWS, (TH1F*)signalddri->Get("h_elefake"));
    addTemplate("BH_SR"       , vars, monoHWS, (TH1F*)signalddri->Get("h_beamhalo"));
    addTemplate("Spikes_SR"       , vars, monoHWS, (TH1F*)signalddri->Get("h_spike"));
    
    addTemplate("Diboson_SR"  , vars, monoHWS, (TH1F*)signalddri->Get("hstack2"));
    

    // ---------------------------- CONTROL REGION (Dimuon) -----------------------------------------------------------------//
  addTemplate("data_obs_ZM", vars, monoHWS, (TH1F*)ZmuGdatafile->Get("Photon_Et_range_4"));
  vector<pair<RooRealVar*, TH1*> >   znn_ZM_syst;

  TH1F* znn_ZMr_hist = (TH1F*)signalfile->Get("ZNuNuG");
  TH1F* znn_ZM_hist = (TH1F*)ZmuGfile->Get("ZllG");

  znn_ZMr_hist->Divide(znn_ZM_hist);

  makeConnectedBinList("Znunu_ZM", MET, monoHWS, znn_ZMr_hist, znn_ZM_syst, znn_SR_bins);


  TH1F* diboson = (TH1F*)ZmuGfile->Get("WWG");
  TH1F* WZm = (TH1F*)ZmuGfile->Get("WZ");
  TH1F* ZZm = (TH1F*)ZmuGfile->Get("ZZ");
  TH1F* Zllm = (TH1F*)ZmuGfile->Get("Zll");
  
  diboson->Add(WZm);
  diboson->Add(ZZm);
  diboson->Add(Zllm);
  


  // Other MC backgrounds in dimuon control region

  addTemplate("Top_ZM"       , vars, monoHWS, (TH1F*)ZmuGfile->Get("TTG"));
  addTemplate("Dibosons_ZM"  , vars, monoHWS, diboson);

  // ---------------------------- CONTROL REGION (Dielectron) -----------------------------------------------------------------//
  addTemplate("data_obs_ZE"  , vars, monoHWS, (TH1F*)ZeeGdatafile->Get("Photon_Et_range_4"));
  vector<pair<RooRealVar*, TH1*> > znn_ZE_syst;

  znn_ZMr_hist->Multiply(znn_ZM_hist);

  //  TH1F* znn_ZEr_hist = (TH1F*)signalfile->Get("ZNuNuG");
  TH1F* znn_ZE_hist = (TH1F*)ZeeGfile->Get("ZllG");

  znn_ZMr_hist->Divide(znn_ZE_hist);

    std::cout<<"den:"<<znn_ZMr_hist->GetBinContent(1)<<"and second; "<<znn_ZMr_hist->GetBinContent(2)<<std::endl;
  //std::cout<<"znn_ZE_hist Ratio "<<znn_ZEr_hist->GetBinContent(1)<<"and second; "<<znn_ZEr_hist->GetBinContent(2)<<std::endl;
  makeConnectedBinList("Znunu_ZE", MET, monoHWS, znn_ZMr_hist, znn_ZE_syst, znn_SR_bins);

  TH1F* diboson1 = (TH1F*)ZeeGfile->Get("WWG");
  TH1F* WZ1 = (TH1F*)ZeeGfile->Get("WZ");
  TH1F* ZZ1 = (TH1F*)ZeeGfile->Get("ZZ");
  TH1F* Zll1 = (TH1F*)ZeeGfile->Get("Zll");
  
  diboson1->Add(WZ1);
  diboson1->Add(ZZ1);
  diboson1->Add(Zll1);


  // Other MC backgrounds in dielectron control region
  addTemplate("Top_ZE"       , vars, monoHWS, (TH1F*)ZeeGfile->Get("TTG"));
  addTemplate("Dibosons_ZE"  , vars, monoHWS, diboson1);
 
  // ---------------------------- CONTROL REGION (Single muon) -----------------------------------------------------------------//
  addTemplate("data_obs_WM"  , vars, monoHWS, (TH1F*)WmunuGdatafile->Get("Photon_Et_range_4"));

  TH1F* wln_WMr_hist = (TH1F*)signalfile->Get("WG");
  TH1F* wln_WM_hist =  (TH1F*)WmunuGfile->Get("WG");


  wln_WMr_hist->Divide(wln_WM_hist);


  
  vector<pair<RooRealVar*, TH1*> > wln_WM_syst;
  makeConnectedBinList("WGamma_WM", MET, monoHWS, wln_WMr_hist, wln_WM_syst, wln_SR_bins);



  TH1F* dibosonwmu = (TH1F*)WmunuGfile->Get("WWG");
  TH1F* WZ2 = (TH1F*)WmunuGfile->Get("WZ");
  TH1F* ZZ2 = (TH1F*)WmunuGfile->Get("ZZ");

  
  dibosonwmu->Add(WZ2);
  dibosonwmu->Add(ZZ2);


  // Other MC backgrounds in single muon control region

  addTemplate("Top_WM"       , vars, monoHWS, (TH1F*)WmunuGfile->Get("TTG"));
  addTemplate("ZllG_WM"       , vars, monoHWS, (TH1F*)WmunuGfile->Get("ZllG"));
  addTemplate("Diphoton_WM"       , vars, monoHWS, (TH1F*)WmunuGfile->Get("diphoton"));

  addTemplate("QCD_WM"       , vars, monoHWS, (TH1F*)WmunuGqcdfile->Get("Photon_Et_range_4"));
  addTemplate("Dibosons_WM"  , vars, monoHWS, dibosonwmu);

  // ---------------------------- CONTROL REGION (Single electron) -----------------------------------------------------------------//
  addTemplate("data_obs_WE"  , vars, monoHWS, (TH1F*)WenuGdatafile->Get("Photon_Et_range_5"));

  wln_WMr_hist->Multiply(wln_WM_hist);


  TH1F* wln_WE_hist =  (TH1F*)WenuGfile->Get("WG");
  wln_WMr_hist->Divide(wln_WE_hist);
  vector<pair<RooRealVar*, TH1*> > wln_WE_syst;
  makeConnectedBinList("WGamma_WE", MET, monoHWS, wln_WMr_hist, wln_WE_syst, wln_SR_bins);

  TH1F* dibosonwe = (TH1F*)WenuGfile->Get("WWG");
  TH1F* WZ3 = (TH1F*)WenuGfile->Get("WZ");
  TH1F* ZZ3 = (TH1F*)WenuGfile->Get("ZZ");

  
  dibosonwe->Add(WZ3);
  dibosonwe->Add(ZZ3);




  addTemplate("Top_WE"       , vars, monoHWS, (TH1F*)WenuGfile->Get("TTG"));
  addTemplate("ZllG_WE"       , vars, monoHWS, (TH1F*)WenuGfile->Get("ZllG"));
  addTemplate("Diphoton_WE"       , vars, monoHWS, (TH1F*)WenuGfile->Get("diphoton"));

  addTemplate("QCD_WE"       , vars, monoHWS, (TH1F*)WenuGqcdfile->Get("Photon_Et_range_5"));
  addTemplate("Dibosons_WE"  , vars, monoHWS, dibosonwe);



  // ---------------------------- Write out the workspace -----------------------------------------------------------------//
  outfile->cd();
  monoHWS.Write();
  outfile->Close();

}
 

