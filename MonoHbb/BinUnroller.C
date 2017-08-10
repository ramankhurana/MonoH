#include "TH2F.h"
#include "TH1F.h"
#include "TCanvas.h"


TH1F* BinUnroller(TH2F* met_vs_mass){
  
  // Configurables
  
  // Rootfile name
  //TString rootfilename = "AnalysisHistograms_MergedSkimmedV12_Puppi_V8/signalpSB/Merged_ZprimeToA0hToA0chichihbb_2HDM_MZp-1000_MA0-300_13TeV-madgraph-SkimTree.root";
						\
  // histogram name
  //TString histname = "h_met_vs_mass_0";

  // binning of unrolled histo
  Double_t metbins[]={200,230,270,310,350,400,450,600,1000, 
		      1030, 1070, 1110, 1150, 1200, 1250, 1400, 1800,
		      1830, 1870, 1910, 1950, 2000, 2050, 2200, 2600,
		      2630, 2670, 2710, 2750, 2800, 2850, 3000, 3400,
		      3430, 3470, 3510, 3550, 3600, 3650, 3800, 4200};
  
  // Unrolled histogram
  TH1F* met_unrolled = new TH1F("met_unrolled","met_unrolled", 40,metbins);
  
  // original binning
  Double_t metbins_single[]={200,230,270,310,350,400,450,600,1000};
  
  //TCanvas *cMCMC = new TCanvas("c_lim_Asymptotic", "canvas with limits for Asymptotic CLs", 630, 600);
  //cMCMC->cd();
  //cMCMC->SetGridx(1);
  //cMCMC->SetGridy(1);
  
  TH1F* met_ = new TH1F("met_","met_", 8, metbins_single);
  
  met_ = (TH1F*) met_vs_mass->ProjectionX("h_met",50,80);
  TH1F* met_new = (TH1F*) met_->Rebin(8, "met_",metbins_single);
  met_new->AddBinContent(8,met_new->GetBinContent(9)); // add overflow
  
  met_ = (TH1F*) met_vs_mass->ProjectionX("h_met",81,110);
  TH1F* met_new_1 = (TH1F*) met_->Rebin(8, "met_",metbins_single);
  met_new_1->AddBinContent(8,met_new_1->GetBinContent(9)); // add overflow
  
  met_ = (TH1F*) met_vs_mass->ProjectionX("h_met",111,140);
  TH1F* met_new_2 = (TH1F*) met_->Rebin(8, "met_",metbins_single);
  met_new_2->AddBinContent(8,met_new_2->GetBinContent(9)); // add overflow
  
  met_ = (TH1F*) met_vs_mass->ProjectionX("h_met",141,170);
  TH1F* met_new_3 = (TH1F*) met_->Rebin(8, "met_",metbins_single);
  met_new_3->AddBinContent(8,met_new_3->GetBinContent(9)); // add overflow
  
  met_ = (TH1F*) met_vs_mass->ProjectionX("h_met",171,200);
  TH1F* met_new_4 = (TH1F*) met_->Rebin(8, "met_",metbins_single);
  met_new_4->AddBinContent(8,met_new_4->GetBinContent(9)); // add overflow
  
  int iunrollbin = 1;
  for (int ibin=1; ibin<=met_new->GetNbinsX(); ibin++){
    met_unrolled->SetBinContent(iunrollbin, met_new->GetBinContent(ibin));
    iunrollbin++;
  }

  for (int ibin=1; ibin<=met_new->GetNbinsX(); ibin++){
    met_unrolled->SetBinContent(iunrollbin, met_new_1->GetBinContent(ibin));
    iunrollbin++;
  }

    for (int ibin=1; ibin<=met_new->GetNbinsX(); ibin++){
    met_unrolled->SetBinContent(iunrollbin, met_new_2->GetBinContent(ibin));
    iunrollbin++;
  }
    
    for (int ibin=1; ibin<=met_new->GetNbinsX(); ibin++){
    met_unrolled->SetBinContent(iunrollbin, met_new_3->GetBinContent(ibin));
    iunrollbin++;
  }

    for (int ibin=1; ibin<=met_new->GetNbinsX(); ibin++){
    met_unrolled->SetBinContent(iunrollbin, met_new_4->GetBinContent(ibin));
    iunrollbin++;
  }


    //met_unrolled->Draw();
    //cMCMC->SaveAs("met_unrolled.pdf");

  return ((TH1F*)met_unrolled);
}
