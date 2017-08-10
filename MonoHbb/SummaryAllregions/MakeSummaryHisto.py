### 
###
# Created By : Raman Khurana
# Date       : 20:July:2017
# Time       : 22:20:30 
###
###
'''
- This macro take the mlfit.root as input
- The post-fit (background-only) histograms are used
- data histogram is taken from: 
- For each process one histogram is defined in which each bin will correspond
  to a given region. Last bin correspond to the signal region. 

'''

## import user defined modules
#from Utils import *
import Utils
import sys
#sys.argv.append( '-b-' )

## this imports basics
from array import array
from ROOT import gROOT, gSystem, gStyle, gRandom
from ROOT import TFile, TChain, TTree, TCut, TH1F, TH2F, THStack, TGraph, TGaxis, TH1, TH2, TObject
from ROOT import TStyle, TCanvas, TPad, TLegend, TLatex, TText
import ROOT
import os

ROOT.gROOT.SetBatch(True)

import sys, optparse


## import helpers files 
import sys
## this will search for files in the previous directory
sys.path.append('../')

## this will search for files in '../Helpers'
sys.path.append('../Helpers')
import fileutils


## Open input file
fin = fileutils.OpenRootFile('mlfit.root')

## set some paths and variables 
processes = ['qcd', 'vh', 'dibosons', 'stop', 'ttbar', 'zll', 'wjets', 'zvv']
region = ['ten', 'ten_fail', 'tmn', 'tmn_fail', 'wen', 'wen_fail', 'wmn', 'wmn_fail', 'zee', 'zee_fail', 'zmm', 'zmm_fail', 'sig']

## create one historam for one process
## and one bin for one region 
h_summary = []
for iprocess in range(len(processes)):
    h_summary.append(TH1F('h_summary_'+processes[iprocess], 'h_summary', 13, 0,13))
    


def ReadHistogram(fitdir, region, process):
    #hist_ = []
    ## construct histogram name 
    histname = fitdir + '/' + region + '/' + process
    TH1.AddDirectory(0)

    ## get histo from the rootfile 
    hist_ = fin.Get(histname)
    
    TH1.AddDirectory(0)
    
    ## This will take into account of underfow and overflow 
    ## "width" will multiply the bin-content with bin-width. This is to get the correct integral for bin-width normalised histogram. 
    integral_ = 0.0
    if type(hist_) is TObject:
        integral_ = 0.0
    elif type(hist_) is TH1F:
        integral_ =  hist_.Integral(0,-1, "width")
    print 'histname = ',histname, 'integral =', integral_

    return integral_

def DictToHist(YieldDict, RegionBin):
    
    for iprocess in range(len(processes)):
        binNumber  = region.index(RegionBin)+1
        binContent = YieldDict[processes[iprocess]]
        h_summary[iprocess].AddBinContent(binNumber, binContent)



if __name__ == "__main__":
    
    processYield = {'qcd':0.0}
    for iregion in region:
        for iprocess in processes:
            processYield[iprocess] = ReadHistogram('shapes_fit_b', iregion, iprocess)
        h = DictToHist(processYield, iregion)
        print iregion, processYield
    
    fout = fileutils.OpenRootFile('summaryHisto.root',"RECREATE")
    fout.cd()
    for ihist in h_summary:
        ihist.Write()
    fout.Close()
 
