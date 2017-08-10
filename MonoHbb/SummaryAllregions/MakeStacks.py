### 
###
# Created By : Raman Khurana
# Date       : 03:March:2016
# Time       : 22:20:30 
###
###

## import user defined modules
#from Utils import *
#import Utils
import sys
#sys.argv.append( '-b-' )

## this imports basics
from array import array
from ROOT import gROOT, gSystem, gStyle, gRandom
from ROOT import TFile, TChain, TTree, TCut, TH1F, TH2F, THStack, TGraph, TGaxis
from ROOT import TStyle, TCanvas, TPad, TLegend, TLatex, TText
import ROOT
import os

ROOT.gROOT.SetBatch(True)

import sys, optparse

###################################
## set up running mode of the code. 
###################################
usage = "usage: %prog [options] arg1 arg2"
parser = optparse.OptionParser(usage)
## data will be true if -d is passed and will be false if -m is passed
parser.add_option("-s", "--saveshapes", action="store_true",  dest="saveshapes")
parser.add_option("-m", "--makecards", action="store_true",  dest="makecards")
parser.add_option("-c", "--combinecards", action="store_true",  dest="combinecards")
parser.add_option("-b", "--bbb", action="store_true",  dest="bbb")
parser.add_option("-r", "--runlimit", action="store_true",  dest="runlimit")
parser.add_option("-o", "--obs", action="store_true",  dest="obs")

(options, args) = parser.parse_args()





from ROOT import *


## import helpers files                                                                                                                                                              
import sys
## this will search for files in the previous directory 
sys.path.append('../')

## this will search for files in '../Helpers'
sys.path.append('../Helpers')
import fileutils

#########################################
#
# Set Weights for each sample
#
#########################################
gStyle.SetOptStat(0)
gStyle.SetOptTitle(0)
gStyle.SetFrameLineWidth(3)
gStyle.SetLineWidth(1)

debug_=False

processes = ['qcd', 'vh', 'dibosons', 'stop', 'ttbar', 'zll', 'wjets', 'zvv']
processesLegend = ['QCD', 'SM H', 'VV', 'ST', 'TT', 'Zll', 'WJ', 'Z#nu#nu']
region = ['tt(e)', 'tt(e) fail', 'tt(#mu)', 'tt(#mu) fail', 'W(e)', 'W(e) fail', 'W(#mu)', 'W(#mu) fail', 'Zee', 'Zee fail', 'Z#mu#mu', 'Z#mu#mu fail', 'Sig']

fin = fileutils.OpenRootFile('summaryHisto.root')

bkgStack = THStack ("bkgStack","bkgStack")


qcd_color       = ROOT.TColor.GetColor(0.270, 0.2, 0.301)
vh_color        = 632
diboson_color   = ROOT.TColor.GetColor(0.709, 0.686, 0.721)
singletop_color = ROOT.TColor.GetColor(0.560, 0.662, 0.596)
ttbar_color     = ROOT.TColor.GetColor(0.886, 0.956, 0.803)
zll_color       = ROOT.TColor.GetColor(0.537, 0.494, 0.580)
wjets_color     = ROOT.TColor.GetColor(0.717, 0.815, 0.749)
zvv_color       = (kAzure+3)
syst_color      = ROOT.TColor.GetColor(0.960, 0.925, 0.6)

color=[qcd_color, vh_color, diboson_color, singletop_color, ttbar_color, zll_color, wjets_color, zvv_color]

print color


legend =  TLegend(0.65, 0.7, 0.92,0.89)
legend.SetTextSize(0.046)
legend.SetBorderSize(0)
legend.SetLineColor(1)
legend.SetLineStyle(1)
legend.SetLineWidth(1)
legend.SetFillColor(0)
legend.SetFillStyle(0)
legend.SetTextFont(42)
legend.SetNColumns(2)
i=0
for iprocess in processes:
    hist_met_ = fin.Get('h_summary_'+iprocess)
    hist_met_.Sumw2()
    hist_met_.SetDirectory(0)
    TH1.AddDirectory(0)
#    gStyle.SetPalette(53)
    hist_met_.SetFillColor(color[i])
    #hist_met_.SetLineColor(color[i])
    bkgStack.Add(hist_met_,'hist')
    legend.AddEntry(hist_met_,processesLegend[i],"f")
    i=i+1

c = TCanvas()

c.SetLogy(1)

bkgStack.Draw()
j=0
for iregion in region:
    bkgStack.GetXaxis().SetBinLabel(j+1,iregion)
    j=j+1
legend.Draw()


latex = TLatex(0.15,0.85,'CMS')
latex.SetTextSize(0.036)
latex.SetTextAlign(12)
latex.SetNDC(kTRUE)
latex.SetTextFont(61)
latex.Draw()


latex1 = TLatex(0.13,0.82,'Preliminary')
latex1.SetTextSize(0.036)
latex1.SetTextAlign(12)
latex1.SetNDC(kTRUE)
latex1.SetTextFont(61)
latex1.Draw()

latex2 = TLatex(0.65,0.93,"35.8 fb^{-1} (13 TeV)")
latex2.SetTextSize(0.036)
latex2.SetTextAlign(12)
latex2.SetNDC(kTRUE)
#latex2.SetTextFont(61)
latex2.Draw()


c.SaveAs('summary.pdf')


if __name__ == "__main__":
    
    print "done"
