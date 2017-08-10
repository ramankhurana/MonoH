//created by Monika mitta Khuaran
//It will a root file containing the nvtx or npileup histrogram 
// Please give input file name and output directory name 

#include <vector>
#include <string>
#include <iostream>
#include <TH1D.h>
#include <TMath.h>
#include <TFile.h>
#include <TClonesArray.h>
//x#include <TLorentzVector.h>
#include <TSystemDirectory.h>
void PileUpCode(){
  Int_t mcw =1;
 
  Float_t         mcWeight; 
  Float_t         pu_nTrueInt;
  TH1D * pileup   = new TH1D( "pileup", "pileup", 52, 0., 52.);
  
  TString PreoutFile("Pileup_"); 
  TString PostoutFile("MET.root");

  TString outputfilename = PreoutFile+PostoutFile;
  TFile efile(outputfilename,"recreate");
  TString InputDirectory("/hdfs/store/user/khurana//MonoH2016/V1/");
  TString InputFileName("ZprimeToA0hToA0chichihbb_2HDM_MZp-2500_MA0-600_13TeV-madgraph/crab_ZprimeToA0hToA0chichihbb_2HDM_MZp-2500_MA0-600_13TeV-madgraph/160819_093738/0000/");

  TString FullFileNme = InputDirectory+InputFileName;
  gSystem->Exec("find "+FullFileNme+" -name \\*.root >& inputroottextfile_MET.txt");
  std::ifstream inputFile("inputroottextfile_MET.txt");


  //std::cout <<  "inputfile :" << inputFile <<std::endl;
  std::vector<TString> infiles;
  std::string str;
  while (std::getline(inputFile, str))
    {
      infiles.push_back(str);
        
    }

    const int numfiles = infiles.size();
    //    cout << numfiles << infiles[0]<<std::endl;
    TFile *fileList[numfiles];
    
    for (int i=0; i < numfiles; i++){
      //  if(!(i%10 == 0)) continue; 
      fileList[i] = new TFile(infiles[i],"READ"); 
      TTree *tree= (TTree*)fileList[i]->Get("tree/treeMaker");
      tree->SetBranchAddress("mcWeight", &mcWeight);
      tree->SetBranchAddress("pu_nTrueInt", &pu_nTrueInt);
      int entry = tree->GetEntries();
      std::cout  << infiles[i] << "entries in tree: "<< entry <<std::endl; 
      for (Int_t im = 0; im < entry ; im++) {
	tree->GetEntry(im);
        if(mcWeight < 0) {mcw =-1;}
        if(mcWeight > 0) {mcw =1;}
	//    	  pileup->Fill(pu_nTrueInt,mcw);
	pileup->Fill(pu_nTrueInt);

      }
    }  
    efile.cd();
    pileup->Write();
}
