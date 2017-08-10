# In this at the end of filevector I am putting the dirname
# so loop over n-1 files and n will give the name of the output dir.

# In legend also the n element will give the name for the ratio plot y axis label.
#edited by Monika Mittal 
#Script for ratio plot 
#import sys
#sys.argv.append( '-b-' )
import ROOT
ROOT.gROOT.SetBatch(True)

#import ROOT
from ROOT import TFile, TH1F, gDirectory, TCanvas, TPad, TProfile,TGraph, TGraphAsymmErrors
from ROOT import TH1D, TH1, TH1I
from ROOT import gStyle
from ROOT import gROOT
from ROOT import TStyle
from ROOT import TLegend
from ROOT import TMath
from ROOT import TPaveText
from ROOT import TLatex

from Overlapping_Histograms import *
import os


linestyle=[1,1,1,1,1,3,3,3,3,3]
files=['AnalysisHistograms_MergedSkimmedV12_Puppi_V1/signalpSB/Merged_ZprimeToA0hToA0chichihbb_2HDM_MZp-1000_MA0-300_13TeV-madgraph-SkimTree.root',
       #'AnalysisHistograms_MergedSkimmedV12_Puppi_V1/signalpSB/Merged_ZprimeToA0hToA0chichihbb_2HDM_MZp-1200_MA0-300_13TeV-madgraph-SkimTree.root',
       'AnalysisHistograms_MergedSkimmedV12_Puppi_V1/signalpSB/Merged_ZprimeToA0hToA0chichihbb_2HDM_MZp-1400_MA0-300_13TeV-madgraph-SkimTree.root',
       #'AnalysisHistograms_MergedSkimmedV12_Puppi_V1/signalpSB/Merged_ZprimeToA0hToA0chichihbb_2HDM_MZp-1700_MA0-300_13TeV-madgraph-SkimTree.root',
       'AnalysisHistograms_MergedSkimmedV12_Puppi_V1/signalpSB/Merged_ZprimeToA0hToA0chichihbb_2HDM_MZp-2000_MA0-300_13TeV-madgraph-SkimTree.root',
       'AnalysisHistograms_MergedSkimmedV12_Puppi_V5/signalpSB/Merged_ZprimeToA0hToA0chichihbb_2HDM_MZp-1000_MA0-300_13TeV-madgraph-SkimTree.root',
       #'AnalysisHistograms_MergedSkimmedV12_Puppi_V5/signalpSB/Merged_ZprimeToA0hToA0chichihbb_2HDM_MZp-1200_MA0-300_13TeV-madgraph-SkimTree.root',
       'AnalysisHistograms_MergedSkimmedV12_Puppi_V5/signalpSB/Merged_ZprimeToA0hToA0chichihbb_2HDM_MZp-1400_MA0-300_13TeV-madgraph-SkimTree.root',
       #'AnalysisHistograms_MergedSkimmedV12_Puppi_V5/signalpSB/Merged_ZprimeToA0hToA0chichihbb_2HDM_MZp-1700_MA0-300_13TeV-madgraph-SkimTree.root',
       'AnalysisHistograms_MergedSkimmedV12_Puppi_V5/signalpSB/Merged_ZprimeToA0hToA0chichihbb_2HDM_MZp-2000_MA0-300_13TeV-madgraph-SkimTree.root',
       ]

legend=['1000', 
        #'1200',
        '1400',
        #'1700', 
        '2000', 
        '1000-TheaC', 
        #'1200-TheaC',
        '1400-TheaC',
        #'1700-TheaC', 
        '2000-TheaC', 
]

histodir=''
histodirMET=''


namelist=['h_mass_0']


for iname in namelist:
    histoname = histodir+iname 
    ytitle=''
    DrawOverlap(files,[histoname],["m_{bb}[GeV]",ytitle],legend,'Puppi_vs_Thea_Mass',[0,0],[30.0,180.0])
    


