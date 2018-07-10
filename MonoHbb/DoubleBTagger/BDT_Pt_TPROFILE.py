import numpy
from scipy import optimize

from ROOT import TFile,TGraph,gStyle,TProfile, TTree, TH1F,TH2F,TH2D, TH1D, TH1, TCanvas, TChain,TGraphAsymmErrors, TMath, TH2D, TLorentzVector, AddressOf, gROOT, TNamed
import ROOT as ROOT
import os
import sys, optparse
from array import array
import math
import numpy as np

ROOT.gROOT.LoadMacro("Loader.h+")
ntuple = TChain("outTree")
ntuple.Add(sys.argv[1])

NEntries = ntuple.GetEntries()

if len(sys.argv)>2:
    #if sys.argv[2]=="test":
    NEntries=int(sys.argv[2])
    print ("WARNING: Running in TEST MODE")

print ('NEntries = '+str(NEntries))

x=[]
y=[]
hprof2d  = TProfile("hprof2d", " ",100,0,1000,-1.,1.)
c=TCanvas()
for ievent in range(NEntries):
    if ievent%100==0: print ("Processed %d of %d events..." %(ievent,NEntries))

    ntuple.GetEntry(ievent)

    n_weight   = ntuple.__getattr__('weight')
    n_ptPruned = ntuple.__getattr__('ptPruned')
    if (170 < n_ptPruned < 1000):
        x.append(n_ptPruned)
        y.append(n_weight)
        print (n_weight)
        hprof2d.Fill(n_ptPruned,n_weight)

# hprof2d.LabelsOption("h","pT")
hprof2d.SetMinimum(-0.2)
hprof2d.SetMaximum(0.3)
hprof2d.Draw()

c.SaveAs("old2dhist.png")


# # H = verification
# nbins = 100
# # xedges = 101
# # yedges =4
# H, xedges, yedges = np.histogram2d(x,y,bins=nbins)
#
# # print (xedges)
# print (yedges)
# # H= H.T
# # print (H)
# # verification = H
# # print (verification)
# H = np.rot90(H)
# H = np.flipud(H)
# # Hmasked = np.ma.masked_where(H==0,H)
# # denominator, xedges, yedges = np.histogram2d(x,y,bins=[1,100])
# # nominator, _, _ = np.histogram2d(x,y,bins=[xedges, yedges], weights=verification)
# # result = nominator / denominator
# #
# # print (result)
