void PreparePUWeights(){
  TFile* f = new TFile("PileUpWeightedFile_new2016.root","READ");
  //  TFile* f = new TFile("/afs/hep.wisc.edu/cms/khurana/Monika/CMSSW_7_4_5/src/RKGlobalAnalyzer/PileUP/PileUpWeightedFile.root","READ");
  f->cd();
  
  TH1F* h = (TH1F*) f->Get("PileUpweighted");
  int nbins = h->GetNbinsX();
  
  std::cout<<"#include <iostream> "<<std::endl;
  std::cout<<"#include <fstream> "<<std::endl;
  ofstream f1;
  f1.open("PileUpWeights.h");
  
  f1<<"#ifndef PileUpWeights_h_"<<std::endl;
  f1<<"#define PileUpWeights_h_ "<<std::endl;
  f1<<"using namespace std; "<<std::endl;
  f1<<"class PileUpWeights{ "<<std::endl;
  f1<<" public: "<<std::endl;
  f1<<"   PileUpWeights(){};"<<std::endl;
  f1<<"   ~PileUpWeights(){};"<<std::endl;
  f1<<"   static Float_t PUWEIGHT(Int_t nvtx){"<<std::endl;
  f1<<"   Float_t  puweight[200]= {1.};"<<std::endl;
  f1<< "   puweight[0]  =  "<<1.<<";"<<std::endl;
  for (int i=0; i<=nbins; i++){
    f1<< "   puweight["<<i<<"]  =  "<<h->GetBinContent(i)<<";"<<std::endl;
  }
  f1<<"   if(nvtx >= 50) puweight[nvtx] =0;" <<std::endl;
  f1<<"   return puweight[nvtx];"<<std::endl;
  f1<<"  }"<<std::endl;
  f1<<"};"<<std::endl;
  f1<<"#endif"<<std::endl;
}
