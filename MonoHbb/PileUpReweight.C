void PileUpReweight(){

  TFile *f1 = new TFile("Pileup_MET.root","READ");
  TFile *f2 = new TFile("MyDataPileupHistogram_true.root","READ");
 
 TH1D *h1;
 TH1D *h2;
 TH1F *h3;  
 
 h1 = (TH1D*) f1->Get("pileup");
 h2 = (TH1D*) f2->Get("pileup");

 h1->Scale(1./h1->Integral());
 h2->Scale(1./h2->Integral()); 


 int nbins = h2->GetNbinsX();
 int xmin = h2->GetXaxis()->GetXmin();
 int xmax = h2->GetXaxis()->GetXmax();


 h3 = new TH1F("PileUpweighted","PileUpweighted",nbins,xmin,xmax);
 cout <<"Nbins:  " << nbins << "  xmin : " << xmin << "  xmax : " << xmax <<std::endl;


 for(int i = xmin; i < xmax; i++){
   Float_t num = Float_t(h2->GetBinContent(i+1));
   Float_t den = Float_t(h1->GetBinContent(i+1));
   Float_t rationd = (num)/(den);

   if(h1->GetBinContent(i+1) > 0.0){h3->SetBinContent(i+1,rationd);}
   else{ h3->SetBinContent(i+1,1.);}

   //h3->SetBinContent(i+1,rationd);
   Float_t h3bincontent = Float_t (h3->GetBinContent(i+1));
   
   cout  <<i <<  " : " <<num  <<"  "<< den <<"  "<< rationd <<"  "<< h3bincontent <<std::endl;




   //   cout << i  <<  " : "   << h2->GetBinContent(i+1) <<"     " <<h1->GetBinContent(i+1) << " "  <<float(h2->GetBinContent(i+1))/float(h1->GetBinContent(i+1)) << "  "<<h3->GetBinContent(i+1) <<std::endl;
   //   cout  << i << "   " <<h2->GetBinContent(h2->FindBin(i)) <<  "   " <<h1->GetBinContent(h1->FindBin(i))  << " " <<h3->GetBinContent(h2->FindBin(i)) <<std::endl;
   
 }
 


 h1->SetName("MC");
 h2->SetName("Data");
 h3->SetName("PileUpweighted");

 

 
 TFile *f3 = new TFile("PileUpWeightedFile_new2016.root","RECREATE");
 f3->cd();
 h1->Write();
 h2->Write();
 h3->Write();
 
 f3->Close();


}
