#!/usr/bin/env python
from ROOT import TFile, TTree, TH1F, TH1D, TH1, TCanvas, TChain,TGraphAsymmErrors, TMath, TH2D, TLorentzVector, AddressOf, gROOT, TNamed
import ROOT as ROOT
import os
import sys, optparse
from array import array
import math
import numpy as numpy_

ROOT.gROOT.LoadMacro("Loader.h+")
outfilename= "ntupleHistos.root"

ntuple = TChain("outTree")
ntuple.Add(sys.argv[1])

NEntries = ntuple.GetEntries()

if len(sys.argv)>2:
    #if sys.argv[2]=="test":
    NEntries=int(sys.argv[2])
    print "WARNING: Running in TEST MODE"

print 'NEntries = '+str(NEntries)

h_z_ratio                     =TH1F('h_z_ratio','h_z_ratio',100,0,40)
h_SubJet_csv                  =TH1F('h_SubJet_csv',  'h_SubJet_csv',  100,0.,1.)
# h_trackSipdSig_3              =TH1F('h_trackSipdSig_3',  'h_trackSipdSig_3',  20,-10.,10.)
# h_trackSipdSig_2              =TH1F('h_trackSipdSig_2',  'h_trackSipdSig_2',  6,0.,6.)
# h_trackSipdSig_1              =TH1F('h_trackSipdSig_1',  'h_trackSipdSig_1',  80,0.,800.)
# h_trackSipdSig_0              =TH1F('h_trackSipdSig_0',  'h_trackSipdSig_0',  80,0.,400.)
# h_trackSipdSig_1_0            =TH1F('h_trackSipdSig_1_0',  'h_trackSipdSig_1_0',  80,0.,400.)
# h_trackSipdSig_1_1            =TH1F('h_trackSipdSig_1_1',  'h_trackSipdSig_1_1',  20,0.,1.)
# h_trackSipdSig_0_1            =TH1F('h_trackSipdSig_0_1',  'h_trackSipdSig_0_1',  20,0.,1.)
h_trackSip2dSigAboveCharm_0   =TH1F('h_trackSip2dSigAboveCharm_0',  'h_trackSip2dSigAboveCharm_0',  80,0.,40)
h_trackSip2dSigAboveBottom_0  =TH1F('h_trackSip2dSigAboveBottom_0',  'h_trackSip2dSigAboveBottom_0',  80,0,40)
h_trackSip2dSigAboveBottom_1  =TH1F('h_trackSip2dSigAboveBottom_1',  'h_trackSip2dSigAboveBottom_1',  80,0,40)
h_tau1_trackEtaRel_0          =TH1F('h_tau1_trackEtaRel_0',  'h_tau1_trackEtaRel_0',  60,0.,6.)
h_tau1_trackEtaRel_1          =TH1F('h_tau1_trackEtaRel_1',  'h_tau1_trackEtaRel_1',  60,0.,6.)

h_tau1_trackEtaRel_2         =TH1F('h_tau1_trackEtaRel_2','h_tau1_trackEtaRel_2',60,0,6)
h_tau0_trackEtaRel_0         =TH1F('h_tau0_trackEtaRel_0',  'h_tau0_trackEtaRel_0',  60,0.,6.)
h_tau0_trackEtaRel_1         =TH1F('h_tau0_trackEtaRel_1',  'h_tau0_trackEtaRel_1',  60,0.,6.)
h_tau0_trackEtaRel_2         =TH1F('h_tau0_trackEtaRel_2',  'h_tau0_trackEtaRel_2',  60,0.,6.)
h_tau_vertexMass_0           =TH1F('h_tau_vertexMass_0',  'h_tau_vertexMass_0',  80,0.,40.)
h_tau_vertexEnergyRatio_0    =TH1F('h_tau_vertexEnergyRatio_0',  'h_tau_vertexEnergyRatio_0',  80,0.,40.)
h_tau_vertexDeltaR_0         =TH1F('h_tau_vertexDeltaR_0',  'h_tau_vertexDeltaR_0',  20, 0., 1.5 )
h_tau_flightDistance2dSig_0  =TH1F('h_tau_flightDistance2dSig_0',  'h_tau_flightDistance2dSig_0',  200,0.,120.)
h_tau_vertexMass_1           =TH1F('h_tau_vertexMass_1',  'h_tau_vertexMass_1',  80,0.,40.)
h_tau_vertexEnergyRatio_1    =TH1F('h_tau_vertexEnergyRatio_1',  'h_tau_vertexEnergyRatio_1',  80,0.,40.)
h_tau_flightDistance2dSig_1  =TH1F('h_tau_flightDistance2dSig_1',  'h_tau_flightDistance2dSig_1',  200,0,120)
h_jetNTracks                 =TH1F('h_jetNTracks',  'h_jetNTracks',  40,0.,40.)
h_nSV                        =TH1F('h_nSV',  'h_nSV',  10,0.,10.)


h_massPruned                 =TH1F('h_massPruned',  'h_massPruned',  800,0.,400.)
h_nbHadrons                  =TH1F('h_nbHadrons',  'h_nbHadrons',  5,0.,5.)
h_ptPruned                   =TH1F('h_ptPruned',  'h_ptPruned',  100,0.,1000.)
h_etaPruned                  =TH1F('h_etaPruned',  'h_etaPruned',  20,-4.,4.)


for ievent in range(NEntries):
    if ievent%100==0: print "Processed %d of %d events..." %(ievent,NEntries)

    ntuple.GetEntry(ievent)
    #doublebtag   = ntuple.__getattr__('CA15Puppi_doublebtag')


    n_z_ratio                    = ntuple.__getattr__('z_ratio')
    n_SubJet_csv                 = ntuple.__getattr__('SubJet_csv')
    n_trackSipdSig_3             = ntuple.__getattr__('trackSipdSig_3')
    n_trackSipdSig_2             = ntuple.__getattr__('trackSipdSig_2')
    n_trackSipdSig_1             = ntuple.__getattr__('trackSipdSig_1')
    n_trackSipdSig_0             = ntuple.__getattr__('trackSipdSig_0')
    n_trackSipdSig_1_0           = ntuple.__getattr__('trackSipdSig_1_0')
    n_trackSipdSig_0_0           = ntuple.__getattr__('trackSipdSig_0_0')
    n_trackSipdSig_1_1           = ntuple.__getattr__('trackSipdSig_1_1')
    n_trackSipdSig_0_1           = ntuple.__getattr__('trackSipdSig_0_1')
    n_trackSip2dSigAboveCharm_0  = ntuple.__getattr__('trackSip2dSigAboveCharm_0')
    n_trackSip2dSigAboveBottom_0 = ntuple.__getattr__('trackSip2dSigAboveBottom_0')
    n_trackSip2dSigAboveBottom_1 = ntuple.__getattr__('trackSip2dSigAboveBottom_1')
    n_tau1_trackEtaRel_0         = ntuple.__getattr__('tau1_trackEtaRel_0')
    n_tau1_trackEtaRel_1         = ntuple.__getattr__('tau1_trackEtaRel_1')
    n_tau1_trackEtaRel_2         = ntuple.__getattr__('tau1_trackEtaRel_2')
    n_tau0_trackEtaRel_0         = ntuple.__getattr__('tau0_trackEtaRel_0')
    n_tau0_trackEtaRel_1         = ntuple.__getattr__('tau0_trackEtaRel_1')
    n_tau0_trackEtaRel_2         = ntuple.__getattr__('tau0_trackEtaRel_2')
    n_tau_vertexMass_0           = ntuple.__getattr__('tau_vertexMass_0')
    n_tau_vertexEnergyRatio_0    = ntuple.__getattr__('tau_vertexEnergyRatio_0')
    n_tau_vertexDeltaR_0         = ntuple.__getattr__('tau_vertexDeltaR_0')
    n_tau_flightDistance2dSig_0  = ntuple.__getattr__('tau_flightDistance2dSig_0')
    n_tau_vertexMass_1           = ntuple.__getattr__('tau_vertexMass_1')
    n_tau_vertexEnergyRatio_1    = ntuple.__getattr__('tau_vertexEnergyRatio_1')
    n_tau_flightDistance2dSig_1  = ntuple.__getattr__('tau_flightDistance2dSig_1')
    n_jetNTracks                 = ntuple.__getattr__('jetNTracks')
    n_nSV                        = ntuple.__getattr__('nSV')
    n_massPruned                 = ntuple.__getattr__('massPruned')
    n_flavour                    = ntuple.__getattr__('flavour')
    n_nbHadrons                  = ntuple.__getattr__('nbHadrons')
    n_ptPruned                   = ntuple.__getattr__('ptPruned')
    n_etaPruned                  = ntuple.__getattr__('etaPruned')

    nElectron                    = ntuple.__getattr__('nEle')


    h_z_ratio.Fill(n_z_ratio)
    h_SubJet_csv.Fill(n_SubJet_csv)
    # h_trackSipdSig_3.Fill()
    # h_trackSipdSig_2.Fill()
    # h_trackSipdSig_1.Fill()
    # h_trackSipdSig_0.Fill()
    # h_trackSipdSig_1_0.Fill()
    # h_trackSipdSig_1_1.Fill()
    # h_trackSipdSig_0_1.Fill()
    h_trackSip2dSigAboveCharm_0.Fill(n_trackSip2dSigAboveCharm_0)
    h_trackSip2dSigAboveBottom_0.Fill(n_trackSip2dSigAboveBottom_0)
    h_trackSip2dSigAboveBottom_1.Fill(n_trackSip2dSigAboveBottom_1)
    h_tau1_trackEtaRel_0.Fill(n_tau1_trackEtaRel_0)
    h_tau1_trackEtaRel_1.Fill(n_tau1_trackEtaRel_1)

    h_tau1_trackEtaRel_2.Fill(n_tau1_trackEtaRel_2)
    h_tau0_trackEtaRel_0.Fill(n_tau0_trackEtaRel_0)
    h_tau0_trackEtaRel_1.Fill(n_tau0_trackEtaRel_1)
    h_tau0_trackEtaRel_2.Fill(n_tau1_trackEtaRel_2)
    h_tau_vertexMass_0.Fill(n_tau_vertexMass_0)
    h_tau_vertexEnergyRatio_0.Fill(n_tau_vertexEnergyRatio_0)
    h_tau_vertexDeltaR_0.Fill(n_tau_vertexDeltaR_0)
    h_tau_flightDistance2dSig_0.Fill(n_tau_flightDistance2dSig_0)
    h_tau_vertexMass_1.Fill(n_tau_vertexMass_1)
    h_tau_vertexEnergyRatio_1.Fill(n_tau_vertexEnergyRatio_1)
    h_tau_flightDistance2dSig_1.Fill(n_tau_flightDistance2dSig_1)
    h_jetNTracks.Fill(n_jetNTracks)
    h_nSV.Fill(n_nSV)


    h_massPruned.Fill(n_massPruned)
    h_nbHadrons.Fill(n_nbHadrons)
    h_ptPruned.Fill(n_ptPruned)
    h_etaPruned.Fill(n_etaPruned)

f = TFile(outfilename,'RECREATE')
f.cd()
h_z_ratio.Write()
h_SubJet_csv.Write()
# h_trackSipdSig_3.Fill()
# h_trackSipdSig_2.Fill()
# h_trackSipdSig_1.Fill()
# h_trackSipdSig_0.Fill()
# h_trackSipdSig_1_0.Fill()
# h_trackSipdSig_1_1.Fill()
# h_trackSipdSig_0_1.Fill()
h_trackSip2dSigAboveCharm_0.Write()
h_trackSip2dSigAboveBottom_0.Write()
h_trackSip2dSigAboveBottom_1.Write()
h_tau1_trackEtaRel_0.Write()
h_tau1_trackEtaRel_1.Write()

h_tau1_trackEtaRel_2.Write()
h_tau0_trackEtaRel_0.Write()
h_tau0_trackEtaRel_1.Write()
h_tau0_trackEtaRel_2.Write()
h_tau_vertexMass_0.Write()
h_tau_vertexEnergyRatio_0.Write()
h_tau_vertexDeltaR_0.Write()
h_tau_flightDistance2dSig_0.Write()
h_tau_vertexMass_1.Write()
h_tau_vertexEnergyRatio_1.Write()
h_tau_flightDistance2dSig_1.Write()
h_jetNTracks.Write()
h_nSV.Write()

print "Histograms written to %s." %outfilename
