#!/usr/bin/env python
from ROOT import TFile, TTree, TH1F, TH1D, TH1, TCanvas, TChain,TGraphAsymmErrors, TMath, TH2D, TLorentzVector, AddressOf, gROOT, TNamed
import ROOT as ROOT
import os
import sys, optparse
from array import array
import math
import numpy as numpy_

ROOT.gROOT.LoadMacro("Loader.h+")
outfilename= "Signal_train.root"

ntuple = TChain("tree/treeMaker")
ntuple.Add(sys.argv[1])


def AnalyzeDataSet():
    NEntries = ntuple.GetEntries()
    outfile = TFile(outfilename,'RECREATE')
    outTree = TTree( 'outTree', 'tree branches' )



    z_ratio                       = array( 'f', [ 0 ] )
    SubJet_csv                    = array( 'f', [ 0 ] )
    trackSipdSig_3                = array( 'f', [ 0 ] )
    trackSipdSig_2                = array( 'f', [ 0 ] )
    trackSipdSig_1                = array( 'f', [ 0 ] )
    trackSipdSig_0                = array( 'f', [ 0 ] )
    trackSipdSig_1_0              = array( 'f', [ 0 ] )
    trackSipdSig_0_0              = array( 'f', [ 0 ] )
    trackSipdSig_1_1              = array( 'f', [ 0 ] )
    trackSipdSig_0_1              = array( 'f', [ 0 ] )
    trackSip2dSigAboveCharm_0     = array( 'f', [ 0 ] )
    trackSip2dSigAboveBottom_0    = array( 'f', [ 0 ] )
    trackSip2dSigAboveBottom_1    = array( 'f', [ 0 ] )
    tau1_trackEtaRel_0            = array( 'f', [ 0 ] )
    tau1_trackEtaRel_1            = array( 'f', [ 0 ] )
    tau1_trackEtaRel_2            = array( 'f', [ 0 ] )
    tau0_trackEtaRel_0            = array( 'f', [ 0 ] )
    tau0_trackEtaRel_1            = array( 'f', [ 0 ] )
    tau0_trackEtaRel_2            = array( 'f', [ 0 ] )
    tau_vertexMass_0              = array( 'f', [ 0 ] )
    tau_vertexEnergyRatio_0       = array( 'f', [ 0 ] )
    tau_vertexDeltaR_0            = array( 'f', [ 0 ] )
    tau_flightDistance2dSig_0     = array( 'f', [ 0 ] )
    tau_vertexMass_1              = array( 'f', [ 0 ] )
    tau_vertexEnergyRatio_1       = array( 'f', [ 0 ] )
    tau_flightDistance2dSig_1     = array( 'f', [ 0 ] )
    jetNTracks                    = array( 'f', [ 0 ] )
    nSV                           = array( 'f', [ 0 ] )
    massPruned                    = array( 'f', [ 0 ] )
    flavour                       = array( 'f', [ 0 ] )
    nbHadrons                     = array( 'f', [ 0 ] )
    ptPruned                      = array( 'f', [ 0 ] )
    etaPruned                     = array( 'f', [ 0 ] )

    nEle                          = array( 'f', [ 0 ] )



    outTree.Branch( 'z_ratio', z_ratio , 'z_ratio/F')
    outTree.Branch( 'SubJet_csv',SubJet_csv,'SubJet_csv/F')
    outTree.Branch( 'trackSipdSig_3',trackSipdSig_3,'trackSipdSig_3/F')
    outTree.Branch( 'trackSipdSig_2',trackSipdSig_2,'trackSipdSig_2/F')
    outTree.Branch( 'trackSipdSig_1',trackSipdSig_1,'trackSipdSig_1/F')
    outTree.Branch( 'trackSipdSig_0',trackSipdSig_0,'trackSipdSig_0/F')
    outTree.Branch( 'trackSipdSig_1_0',trackSipdSig_1_0,'trackSipdSig_1_0/F')
    outTree.Branch( 'trackSipdSig_0_0',trackSipdSig_0_0,'trackSipdSig_0_0/F')
    outTree.Branch( 'trackSipdSig_1_1',trackSipdSig_1_1,'trackSipdSig_1_1/F')
    outTree.Branch( 'trackSipdSig_0_1',trackSipdSig_0_1,'trackSipdSig_0_1/F')
    outTree.Branch( 'trackSip2dSigAboveCharm_0',trackSip2dSigAboveCharm_0,'trackSip2dSigAboveCharm_0/F')
    outTree.Branch( 'trackSip2dSigAboveBottom_0',trackSip2dSigAboveBottom_0,'trackSip2dSigAboveBottom_0/F')
    outTree.Branch( 'trackSip2dSigAboveBottom_1',trackSip2dSigAboveBottom_1,'trackSip2dSigAboveBottom_1/F')
    outTree.Branch( 'tau1_trackEtaRel_0',tau1_trackEtaRel_0,'tau1_trackEtaRel_0/F')
    outTree.Branch( 'tau1_trackEtaRel_1',tau1_trackEtaRel_1,'tau1_trackEtaRel_1/F')
    outTree.Branch( 'tau1_trackEtaRel_2',tau1_trackEtaRel_2,'tau1_trackEtaRel_2/F')
    outTree.Branch( 'tau0_trackEtaRel_0',tau0_trackEtaRel_0,'tau0_trackEtaRel_0/F')
    outTree.Branch( 'tau0_trackEtaRel_1',tau0_trackEtaRel_1,'tau0_trackEtaRel_1/F')
    outTree.Branch( 'tau0_trackEtaRel_2',tau0_trackEtaRel_2,'tau0_trackEtaRel_2/F')
    outTree.Branch( 'tau_vertexMass_0',tau_vertexMass_0,'tau_vertexMass_0/F')
    outTree.Branch( 'tau_vertexEnergyRatio_0',tau_vertexEnergyRatio_0,'tau_vertexEnergyRatio_0/F')
    outTree.Branch( 'tau_vertexDeltaR_0',tau_vertexDeltaR_0,'tau_vertexDeltaR_0/F')
    outTree.Branch( 'tau_flightDistance2dSig_0',tau_flightDistance2dSig_0,'tau_flightDistance2dSig_0/F')
    outTree.Branch( 'tau_vertexMass_1',tau_vertexMass_1,'tau_vertexMass_1/F')
    outTree.Branch( 'tau_vertexEnergyRatio_1',tau_vertexEnergyRatio_1,'tau_vertexEnergyRatio_1/F')
    outTree.Branch( 'tau_flightDistance2dSig_1',tau_flightDistance2dSig_1,'tau_flightDistance2dSig_1/F')
    outTree.Branch( 'jetNTracks',jetNTracks,'jetNTracks/F')
    outTree.Branch( 'nSV',nSV,'nSV/F')
    outTree.Branch( 'massPruned',massPruned,'massPruned/F')
    outTree.Branch( 'flavour',flavour,'flavour/F')
    outTree.Branch( 'nbHadrons',nbHadrons,'nbHadrons/F')
    outTree.Branch( 'ptPruned',ptPruned,'ptPruned/F')
    outTree.Branch( 'etaPruned',etaPruned,'etaPruned/F')

    outTree.Branch( 'nEle',nEle,'nEle/F')

    if len(sys.argv)>2:
        NEntries=int(sys.argv[2])
        print "WARNING: Running in TEST MODE"




    for ievent in range(NEntries):
        if ievent%100==0: print "Processed %d of %d events..." %(ievent,NEntries)

        ntuple.GetEntry(ievent)
        #doublebtag   = ntuple.__getattr__('CA15Puppi_doublebtag')


        CA15Puppi_z_ratio                    = ntuple.__getattr__('CA15Puppi_z_ratio')
        CA15Puppi_SubJet_csv                 = ntuple.__getattr__('CA15Puppi_SubJet_csv')
        CA15Puppi_trackSipdSig_3             = ntuple.__getattr__('CA15Puppi_trackSipdSig_3')
        CA15Puppi_trackSipdSig_2             = ntuple.__getattr__('CA15Puppi_trackSipdSig_2')
        CA15Puppi_trackSipdSig_1             = ntuple.__getattr__('CA15Puppi_trackSipdSig_1')
        CA15Puppi_trackSipdSig_0             = ntuple.__getattr__('CA15Puppi_trackSipdSig_0')
        CA15Puppi_trackSipdSig_1_0           = ntuple.__getattr__('CA15Puppi_trackSipdSig_1_0')
        CA15Puppi_trackSipdSig_0_0           = ntuple.__getattr__('CA15Puppi_trackSipdSig_0_0')
        CA15Puppi_trackSipdSig_1_1           = ntuple.__getattr__('CA15Puppi_trackSipdSig_1_1')
        CA15Puppi_trackSipdSig_0_1           = ntuple.__getattr__('CA15Puppi_trackSipdSig_0_1')
        CA15Puppi_trackSip2dSigAboveCharm_0  = ntuple.__getattr__('CA15Puppi_trackSip2dSigAboveCharm_0')
        CA15Puppi_trackSip2dSigAboveBottom_0 = ntuple.__getattr__('CA15Puppi_trackSip2dSigAboveBottom_0')
        CA15Puppi_trackSip2dSigAboveBottom_1 = ntuple.__getattr__('CA15Puppi_trackSip2dSigAboveBottom_1')
        CA15Puppi_tau1_trackEtaRel_0         = ntuple.__getattr__('CA15Puppi_tau1_trackEtaRel_0')
        CA15Puppi_tau1_trackEtaRel_1         = ntuple.__getattr__('CA15Puppi_tau1_trackEtaRel_1')
        CA15Puppi_tau1_trackEtaRel_2         = ntuple.__getattr__('CA15Puppi_tau1_trackEtaRel_2')
        CA15Puppi_tau0_trackEtaRel_0         = ntuple.__getattr__('CA15Puppi_tau0_trackEtaRel_0')
        CA15Puppi_tau0_trackEtaRel_1         = ntuple.__getattr__('CA15Puppi_tau0_trackEtaRel_1')
        CA15Puppi_tau0_trackEtaRel_2         = ntuple.__getattr__('CA15Puppi_tau0_trackEtaRel_2')
        CA15Puppi_tau_vertexMass_0           = ntuple.__getattr__('CA15Puppi_tau_vertexMass_0')
        CA15Puppi_tau_vertexEnergyRatio_0    = ntuple.__getattr__('CA15Puppi_tau_vertexEnergyRatio_0')
        CA15Puppi_tau_vertexDeltaR_0         = ntuple.__getattr__('CA15Puppi_tau_vertexDeltaR_0')
        CA15Puppi_tau_flightDistance2dSig_0  = ntuple.__getattr__('CA15Puppi_tau_flightDistance2dSig_0')
        CA15Puppi_tau_vertexMass_1           = ntuple.__getattr__('CA15Puppi_tau_vertexMass_1')
        CA15Puppi_tau_vertexEnergyRatio_1    = ntuple.__getattr__('CA15Puppi_tau_vertexEnergyRatio_1')
        CA15Puppi_tau_flightDistance2dSig_1  = ntuple.__getattr__('CA15Puppi_tau_flightDistance2dSig_1')
        CA15Puppi_jetNTracks                 = ntuple.__getattr__('CA15Puppi_jetNTracks')
        CA15Puppi_nSV_                        = ntuple.__getattr__('CA15Puppi_nSV_')
        CA15Puppi_massPruned                 = ntuple.__getattr__('CA15Puppi_massPruned')
        CA15Puppi_flavour                    = ntuple.__getattr__('CA15Puppi_flavour')
        CA15Puppi_nbHadrons                  = ntuple.__getattr__('CA15Puppi_nbHadrons')
        CA15Puppi_ptPruned                   = ntuple.__getattr__('CA15Puppi_ptPruned')
        CA15Puppi_etaPruned                  = ntuple.__getattr__('CA15Puppi_etaPruned')


        #Other variables
        eleIsPassLoose             = ntuple.__getattr__('eleIsPassLoose')
        nElectron                  = ntuple.__getattr__('nEle')
        eleP4                      = ntuple.__getattr__('eleP4')

        myEles=[]
        for iele in range(nElectron):
            if (eleP4[iele].Pt() > 10. ) & (abs(eleP4[iele].Eta()) <2.5) & (bool(eleIsPassLoose[iele]) == True) :
                myEles.append(iele)


        if len(CA15Puppi_ptPruned) > 0:
            z_ratio[0]                = CA15Puppi_z_ratio[0]
            SubJet_csv[0]             = CA15Puppi_SubJet_csv[0]
            trackSipdSig_3[0]         = CA15Puppi_trackSipdSig_3[0]
            trackSipdSig_2[0]         = CA15Puppi_trackSipdSig_2[0]
            trackSipdSig_1[0]         = CA15Puppi_trackSipdSig_1[0]
            trackSipdSig_0[0]         = CA15Puppi_trackSipdSig_0[0]
            trackSipdSig_1_0[0]       = CA15Puppi_trackSipdSig_1_0[0]
            trackSipdSig_0_0[0]       = CA15Puppi_trackSipdSig_0_0[0]
            trackSipdSig_1_1[0]       = CA15Puppi_trackSipdSig_1_1[0]
            trackSipdSig_0_1[0]       = CA15Puppi_trackSipdSig_0_1[0]
            trackSip2dSigAboveCharm_0[0]  = CA15Puppi_trackSip2dSigAboveCharm_0[0]
            trackSip2dSigAboveBottom_0[0] = CA15Puppi_trackSip2dSigAboveBottom_0[0]
            trackSip2dSigAboveBottom_1[0] = CA15Puppi_trackSip2dSigAboveBottom_1[0]
            tau1_trackEtaRel_0[0]         = CA15Puppi_tau1_trackEtaRel_0[0]
            tau1_trackEtaRel_1[0]         = CA15Puppi_tau1_trackEtaRel_1[0]
            tau1_trackEtaRel_2[0]         = CA15Puppi_tau1_trackEtaRel_2[0]
            tau0_trackEtaRel_0[0]         = CA15Puppi_tau0_trackEtaRel_0[0]
            tau0_trackEtaRel_1[0]         = CA15Puppi_tau0_trackEtaRel_1[0]
            tau0_trackEtaRel_2[0]         = CA15Puppi_tau0_trackEtaRel_2[0]
            tau_vertexMass_0[0]           = CA15Puppi_tau_vertexMass_0[0]
            tau_vertexEnergyRatio_0[0]    = CA15Puppi_tau_vertexEnergyRatio_0[0]
            tau_vertexDeltaR_0[0]         = CA15Puppi_tau_vertexDeltaR_0[0]
            tau_flightDistance2dSig_0[0]  = CA15Puppi_tau_flightDistance2dSig_0[0]
            tau_vertexMass_1[0]           = CA15Puppi_tau_vertexMass_1[0]
            tau_vertexEnergyRatio_1[0]    = CA15Puppi_tau_vertexEnergyRatio_1[0]
            tau_flightDistance2dSig_1[0]  = CA15Puppi_tau_flightDistance2dSig_1[0]
            jetNTracks[0]                 = CA15Puppi_jetNTracks[0]
            nSV[0]                        = CA15Puppi_nSV_[0]
            massPruned[0]                 = CA15Puppi_massPruned[0]
            flavour[0]                    = CA15Puppi_flavour[0]
            nbHadrons[0]                  = CA15Puppi_nbHadrons[0]
            ptPruned[0]                   = CA15Puppi_ptPruned[0]
            etaPruned[0]                  = CA15Puppi_etaPruned[0]
            #other variables
            nEle[0] = len(myEles)


        outTree.Fill()

    outfile.Write()



if __name__ == "__main__":
    AnalyzeDataSet()


###################################
