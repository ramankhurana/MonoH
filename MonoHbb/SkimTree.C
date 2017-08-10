
void SkimTree(){
  TFile* inputfile = new TFile("NCUGlobalTuples_1.root","READ");
  //inputfile->cd("tree");
  tree_ = inputfile->Get("tree/treeMaker");
  TTree* newtree = (TTree*) (tree_->CopyTree("pfMetCorrPt>170 && FATjetP4[0].Pt()>200.0 && (FATjetP4[0].Eta())<2.4 && FATjetPassIDTight[0] == 1","",1000000000,0));
  TFile* outputfile = new TFile("skimmedMET.root","RECREATE");
  outputfile->cd();
  newtree->Write();
  outputfile->Write();

}
