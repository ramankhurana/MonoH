#!/usr/bin/env python
from ROOT import TFile, TTree, TH1F, TH1D, TH1, TCanvas, TChain,TGraphAsymmErrors, TMath, TH2D, TLorentzVector, AddressOf, gROOT, TNamed
import ROOT as ROOT
import os
import sys, optparse
from array import array
import math
import numpy as numpy_

ROOT.gROOT.LoadMacro("Loader.h+")
outfilename= "bkg_QCD_Train.root"
#outfilename= "signal_ZpBaryonic_MZp-1000_MChi-1_train.root"


ntuple = TChain("tree/treeMaker")
ntuple.Add(sys.argv[1])


def AnalyzeDataSet():
    NEntries = ntuple.GetEntries()
    outfile = TFile(outfilename,'RECREATE')
    outTree = TTree( 'outTree', 'tree branches' )



    z_ratio                       = array( 'f', [ 0 ] )
    SubJet_csv_min                = array( 'f', [ 0 ] )
    SubJet_csv_1                  = array( 'f', [ 0 ] )
    SubJet_csv_2                  = array( 'f', [ 0 ] )
    fn_csv                        = array( 'f', [ 0 ] )
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

    nEle                          = array( 'L', [ 0 ] )
    nMu                           = array( 'L', [ 0 ] )
    nTau                          = array( 'L', [ 0 ] )
    nPho                          = array( 'L', [ 0 ] )



    outTree.Branch( 'z_ratio', z_ratio , 'z_ratio/F')
    outTree.Branch( 'SubJet_csv_min',SubJet_csv_min,'SubJet_csv_min/F')
    outTree.Branch( 'SubJet_csv_1',SubJet_csv_1,'SubJet_csv_1/F')
    outTree.Branch( 'SubJet_csv_2',SubJet_csv_2,'SubJet_csv_2/F')
    outTree.Branch( 'fn_csv',fn_csv,'fn_csv/F')
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

    outTree.Branch( 'nEle',nEle,'nEle/L')
    outTree.Branch( 'nMu',nMu,'nMu/L')
    outTree.Branch( 'nTau',nTau,'nTau/L')
    outTree.Branch( 'nPho',nPho,'nPho/L')


    if len(sys.argv)>2:
        NEntries=int(sys.argv[2])
        print "WARNING: Running in TEST MODE"




    for ievent in range(NEntries):
        if ievent%100==0: print "Processed %d of %d events..." %(ievent,NEntries)

        ntuple.GetEntry(ievent)
        #doublebtag   = ntuple.__getattr__('CA15Puppi_doublebtag')


        CA15Puppi_z_ratio                    = ntuple.__getattr__('CA15Puppi_z_ratio')
        CA15PuppisubjetCSV                   = ntuple.__getattr__('CA15PuppisubjetSDCSV')
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

        nPho_                       = ntuple.__getattr__('nPho')
        phoP4                      = ntuple.__getattr__('phoP4')
        phoIsPassLoose             = ntuple.__getattr__('phoIsPassLoose')

        nTau_                       = ntuple.__getattr__('HPSTau_n')
        tauP4                      = ntuple.__getattr__('HPSTau_4Momentum')
        isDecayModeFinding         = ntuple.__getattr__('disc_decayModeFinding')
        passLooseTauIso            = ntuple.__getattr__('disc_byLooseIsolationMVA3oldDMwLT')

        nMu_                        = ntuple.__getattr__('nMu')
        muP4                       = ntuple.__getattr__('muP4')
        isLooseMuon                = ntuple.__getattr__('isLooseMuon')
        muChHadIso                 = ntuple.__getattr__('muChHadIso')
        muNeHadIso                 = ntuple.__getattr__('muNeHadIso')
        muGamIso                   = ntuple.__getattr__('muGamIso')
        muPUPt                     = ntuple.__getattr__('muPUPt')
        muCharge                   = ntuple.__getattr__('muCharge')

        CA15jetcond = False

        # if len(CA15Puppi_ptPruned) > 0 & (170 < CA15Puppi_ptPruned < 1000) & (50 < CA15Puppi_massPruned < 200):
        #     Subjets_0 = CA15PuppisubjetCSV[0]
        #     if len(Subjets_0)==2: CA15jetcond = True
        #     else:CA15jetcond = False


        if len(CA15Puppi_ptPruned) > 0 & (170 < CA15Puppi_ptPruned < 3000) & (50 < CA15Puppi_massPruned < 200) :
            Subjets_0 = CA15PuppisubjetCSV[0]
            try:

                if len(Subjets_0)==2:# & (Subjets_0[0] > 0) & (Subjets_0[1] > 0):
                    print "subjets", len(Subjets_0)
                    print ("csv: ",Subjets_0[0],"and",Subjets_0[1])
                    new_csv=math.tanh(math.atanh(Subjets_0[0])+math.atanh(Subjets_0[1]))
                    print ("new csv: ",new_csv)

                    z_ratio[0]                = CA15Puppi_z_ratio[0]
                    SubJet_csv_min[0]         = CA15Puppi_SubJet_csv[0]
                    SubJet_csv_1[0]           = Subjets_0[0]
                    SubJet_csv_2[0]           = Subjets_0[1]
                    fn_csv[0]                 = new_csv
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

                    myEles=[]
                    for iele in range(nElectron):
                        if (eleP4[iele].Pt() > 10. ) & (abs(eleP4[iele].Eta()) <2.5) & (bool(eleIsPassLoose[iele]) == True) :
                            myEles.append(iele)
                    # print len(myEles)
                    myMuos = []
                    for imu in range(nMu_):
                        if (muP4[imu].Pt()>10.) & (abs(muP4[imu].Eta()) < 2.4) & (bool(isLooseMuon[imu]) == True):
                            relPFIso = (muChHadIso[imu]+ max(0., muNeHadIso[imu] + muGamIso[imu] - 0.5*muPUPt[imu]))/muP4[imu].Pt()
                            if relPFIso<0.25 :
                                myMuos.append(imu)
                    #print len(myMuos)
                    myTaus =[]
                    for itau in range(nTau_):
                        if (tauP4[itau].Pt()>18.) & (abs(tauP4[itau].Eta())<2.3) & (bool(isDecayModeFinding[itau]) == True) & (bool(passLooseTauIso[itau]) == True):
                            myTaus.append(itau)

                    #print len(myTaus)
                    myPhos=[]
                    for ipho in range(nPho_):
                        if (phoP4[ipho].Pt() > 15.) & (abs(phoP4[ipho].Eta()) <2.5) & (bool(phoIsPassLoose[ipho]) == True):
                            myPhos.append(ipho)
                    # print len(myPhos)
                    #other variables
                    nEle[0] = len(myEles)
                    nMu[0]  = len(myMuos)
                    nTau[0] = len(myTaus)
                    nPho[0] =  len(myPhos)

            except:
                print "There is problem in csv value , skipping event"


        outTree.Fill()

    outfile.Write()



if __name__ == "__main__":
    AnalyzeDataSet()


###################################
