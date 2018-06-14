#!/usr/bin/env python
from ROOT import TFile, TStyle,TTree,TLatex, TH1F, TH1D,TH2D, TH1, TCanvas, TChain,TGraphAsymmErrors, TMath, TH2D, TLorentzVector, AddressOf, gROOT, TNamed, gStyle, TLegend
import ROOT as ROOT
import os
import sys, optparse


gStyle.SetFrameLineWidth(3)
gStyle.SetHistFillStyle(0)
#gStyle->SetHistLineColor(kBlack);
gStyle.SetHistLineStyle(1)
gStyle.SetHistLineWidth(1)
gStyle.SetEndErrorSize(0)

gStyle.SetOptStat(0)
gStyle.SetOptTitle(0)
gStyle.SetLegendBorderSize(0)
#gStyle.SetFillColor(0)
#gStyle.SetPadColor(1)

cmsname=TLatex(0.15,0.95,'   ')
#cmsname=TLatex(0.15,1.85,"CMS #it{#bf{Preliminary}}")
cmsname.SetTextSize(0.036)
cmsname.SetTextAlign(12)
cmsname.SetNDC(1)
cmsname.SetTextFont(61)

canvas = ROOT.TCanvas()
canvas.SetLogy()

f2 = ROOT.TFile.Open('OUTPUT_signal_ZpBaryonic_MZp-1000_MChi-1_train.root', 'read')
f1 = ROOT.TFile.Open('OUTPUT_QCD500-700_train.root', 'read')

h1_z_ratio= f1.Get('h_z_ratio')
h1_SubJet_csv= f1.Get('h_SubJet_csv')
# h_trackSipdSig_3.Fill()
# h_trackSipdSig_2.Fill()
# h_trackSipdSig_1.Fill()
# h_trackSipdSig_0.Fill()
# h_trackSipdSig_1_0.Fill()
# h_trackSipdSig_1_1.Fill()
# h_trackSipdSig_0_1.Fill()
h1_trackSip2dSigAboveCharm_1= f1.Get('h_trackSip2dSigAboveCharm_0')
h1_trackSip2dSigAboveBottom_0= f1.Get('h_trackSip2dSigAboveBottom_0')
h1_trackSip2dSigAboveBottom_1= f1.Get('h_trackSip2dSigAboveBottom_1')
h1_tau1_trackEtaRel_0= f1.Get('h_tau1_trackEtaRel_0')
h1_tau1_trackEtaRel_1= f1.Get('h_tau1_trackEtaRel_1')

h1_tau1_trackEtaRel_2= f1.Get('h_tau1_trackEtaRel_2')
h1_tau0_trackEtaRel_0= f1.Get('h_tau0_trackEtaRel_0')
h1_tau0_trackEtaRel_1= f1.Get('h_tau0_trackEtaRel_1')
h1_tau0_trackEtaRel_2= f1.Get('h_tau0_trackEtaRel_2')
h1_tau_vertexMass_0= f1.Get('h_tau_vertexMass_0')
h1_tau_vertexEnergyRatio_0= f1.Get('h_tau_vertexEnergyRatio_0')
h1_tau_vertexDeltaR_0= f1.Get('h_tau_vertexDeltaR_0')
h1_tau_flightDistance2dSig_0= f1.Get('h_tau_flightDistance2dSig_0')
h1_tau_vertexMass_1= f1.Get('h_tau_vertexMass_1')
h1_tau_vertexEnergyRatio_1= f1.Get('h_tau_vertexEnergyRatio_1')
h1_tau_flightDistance2dSig_1= f1.Get('h_tau_flightDistance2dSig_1')
h1_jetNTracks= f1.Get('h_jetNTracks')
h1_nSV= f1.Get('h_nSV')


h2_z_ratio= f2.Get('h_z_ratio')
h2_SubJet_csv= f2.Get('h_SubJet_csv')
# h_trackSipdSig_3.Fill()
# h_trackSipdSig_2.Fill()
# h_trackSipdSig_1.Fill()
# h_trackSipdSig_0.Fill()
# h_trackSipdSig_1_0.Fill()
# h_trackSipdSig_1_1.Fill()
# h_trackSipdSig_0_1.Fill()
h2_trackSip2dSigAboveCharm_1= f2.Get('h_trackSip2dSigAboveCharm_0')
h2_trackSip2dSigAboveBottom_0= f2.Get('h_trackSip2dSigAboveBottom_0')
h2_trackSip2dSigAboveBottom_1= f2.Get('h_trackSip2dSigAboveBottom_1')
h2_tau1_trackEtaRel_0= f2.Get('h_tau1_trackEtaRel_0')
h2_tau1_trackEtaRel_1= f2.Get('h_tau1_trackEtaRel_1')

h2_tau1_trackEtaRel_2= f2.Get('h_tau1_trackEtaRel_2')
h2_tau0_trackEtaRel_0= f2.Get('h_tau0_trackEtaRel_0')
h2_tau0_trackEtaRel_1= f2.Get('h_tau0_trackEtaRel_1')
h2_tau0_trackEtaRel_2= f2.Get('h_tau0_trackEtaRel_2')
h2_tau_vertexMass_0= f2.Get('h_tau_vertexMass_0')
h2_tau_vertexEnergyRatio_0= f2.Get('h_tau_vertexEnergyRatio_0')
h2_tau_vertexDeltaR_0= f2.Get('h_tau_vertexDeltaR_0')
h2_tau_flightDistance2dSig_0= f2.Get('h_tau_flightDistance2dSig_0')
h2_tau_vertexMass_1= f2.Get('h_tau_vertexMass_1')
h2_tau_vertexEnergyRatio_1= f2.Get('h_tau_vertexEnergyRatio_1')
h2_tau_flightDistance2dSig_1= f2.Get('h_tau_flightDistance2dSig_1')
h2_jetNTracks= f2.Get('h_jetNTracks')
h2_nSV= f2.Get('h_nSV')

hists1=[h1_z_ratio,h1_SubJet_csv,h1_trackSip2dSigAboveCharm_1,h1_trackSip2dSigAboveBottom_0,h1_trackSip2dSigAboveBottom_1,h1_tau1_trackEtaRel_0,h1_tau1_trackEtaRel_1,h1_tau1_trackEtaRel_2,h1_tau0_trackEtaRel_0,h1_tau0_trackEtaRel_1,h1_tau0_trackEtaRel_2,h1_tau_vertexMass_0,h1_tau_vertexEnergyRatio_0,h1_tau_vertexDeltaR_0,h1_tau_flightDistance2dSig_0,h1_tau_vertexMass_1,h1_tau_vertexEnergyRatio_1,h1_tau_flightDistance2dSig_1,h1_jetNTracks,h1_nSV]
hists2=[h2_z_ratio,h2_SubJet_csv,h2_trackSip2dSigAboveCharm_1,h2_trackSip2dSigAboveBottom_0,h2_trackSip2dSigAboveBottom_1,h2_tau1_trackEtaRel_0,h2_tau1_trackEtaRel_1,h2_tau1_trackEtaRel_2,h2_tau0_trackEtaRel_0,h2_tau0_trackEtaRel_1,h2_tau0_trackEtaRel_2,h2_tau_vertexMass_0,h2_tau_vertexEnergyRatio_0,h2_tau_vertexDeltaR_0,h2_tau_flightDistance2dSig_0,h2_tau_vertexMass_1,h2_tau_vertexEnergyRatio_1,h2_tau_flightDistance2dSig_1,h2_jetNTracks,h2_nSV]
xaxis=['z_ratio','SubJet_csv','trackSip2dSigAboveCharm_1','trackSip2dSigAboveBottom_0','trackSip2dSigAboveBottom_1','tau1_trackEtaRel_0','tau1_trackEtaRel_1','tau1_trackEtaRel_2','tau0_trackEtaRel_0','tau0_trackEtaRel_1','tau0_trackEtaRel_2','tau_vertexMass_0','tau_vertexEnergyRatio_0','tau_vertexDeltaR_0','tau_flightDistance2dSig_0','tau_vertexMass_1','tau_vertexEnergyRatio_1','tau_flightDistance2dSig_1','jetNTracks','nSV']

for i in range(len(hists1)):
    legend=TLegend(.53,.79,.77,.89)
    legend.SetTextSize(0.035)
    # print (hists1[i].Integral())
    hists1[i].Draw('HIST')
    hists1[i].SetXTitle(xaxis[i])
    hists1[i].SetLineColor(4)
    hists1[i].SetLineWidth(3)
    hists1[i].Scale(1/hists1[i].Integral())
    legend.AddEntry(hists1[i],"QCD_pt500-700","L")
    hists2[i].SetLineColor(2)
    hists2[i].SetLineWidth(3)
    hists2[i].Scale(1/hists2[i].Integral())
    legend.AddEntry(hists2[i],"ZpBaryonic_MZp-1000_MChi-1","L")
    hists2[i].Draw('HIST same')
    legend.Draw()
    cmsname.Draw()
    canvas.SaveAs(xaxis[i]+'.pdf')
    canvas.SaveAs(xaxis[i]+'.png')
