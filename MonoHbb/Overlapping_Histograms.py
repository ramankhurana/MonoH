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

import os
colors=[1,2,4,3,32,20,6,8,20,11,41,46,30,12,28,20,32]
markerStyle=[23,21,22,20,24,25,26,27,28,29,20,21,22,23]            
linestyle=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

def DrawOverlap(fileVec, histVec, titleVec,legendtext,pngname,logstatus=[0,0],xRange=[-99999,99999,1]):

    gStyle.SetOptTitle(0)
    gStyle.SetOptStat(0)
    gStyle.SetTitleOffset(1.1,"Y");
    gStyle.SetTitleOffset(0.9,"X");
    gStyle.SetLineWidth(3)
    gStyle.SetFrameLineWidth(3); 

    i=0

    histList_=[]
    histList=[]
    histList1=[]
    maximum=[]
    
    ## Legend    
    leg = TLegend(0.1, 0.70, 0.89, 0.89)#,NULL,"brNDC");
    leg.SetBorderSize(0)
    leg.SetNColumns(2)
    leg.SetLineColor(1)
    leg.SetLineStyle(1)
    leg.SetLineWidth(1)
    leg.SetFillColor(0)
    leg.SetFillStyle(0)
    leg.SetTextFont(22)
    leg.SetTextSize(0.045)
     
    c = TCanvas("c1", "c1",0,0,500,500)
    #c.SetBottomMargin(0.15)
    #c.SetLeftMargin(0.15)
    #c.SetLogy(0)
    #c.SetLogx(0)
    c1_2 = TPad("c1_2","newpad",0.04,0.13,1,0.994)
    c1_2.Draw()

    
    print ("you have provided "+str(len(fileVec))+" files and "+str(len(histVec))+" histograms to make a overlapping plot" )
    print "opening rootfiles"
    c.cd()
    c1_2.SetBottomMargin(0.13)
    c1_2.SetLogy(logstatus[1])
    c1_2.SetLogx(logstatus[0])
    
    
    c1_2.cd()
    ii=0    
    inputfile={}
    print str(fileVec[(len(fileVec)-1)])

    for ifile_ in range(len(fileVec)):
        print ("opening file  "+fileVec[ifile_])
        inputfile[ifile_] = TFile( fileVec[ifile_] )
        print "fetching histograms"
        for ihisto_ in range(len(histVec)):
            print ("printing histo "+str(histVec[ihisto_]))
            histo = inputfile[ifile_].Get(histVec[ihisto_])
            #status_ = type(histo) is TGraphAsymmErrors
            histList.append(histo)
            # for ratio plot as they should nt be normalize 
            histList1.append(histo)
            print histList[ii].Integral()
            #histList[ii].Rebin(xRange[2])
            type_obj = type(histList[ii])
            if (type_obj is TH1D) or (type_obj is TH1F) or (type_obj is TH1) or (type_obj is TH1I) :
                histList[ii].Rebin(5)
            histList[ii].Scale(1.0/histList[ii].Integral())
            maximum.append(histList[ii].GetMaximum())
            maximum.sort()
            ii=ii+1

    print histList
    for ih in range(len(histList)):
        tt = type(histList[ih])
        if logstatus[1] is 1 :
            histList[ih].SetMaximum(maximum[(len(maximum)-1)]*25) #1.4 for log
            histList[ih].SetMinimum(1) #1.4 for log
        if logstatus[1] is 0 :
            histList[ih].SetMaximum(maximum[(len(maximum)-1)]*1.2) #1.4 for log
            histList[ih].SetMinimum(0) #1.4 for log
#        print "graph_status =" ,(tt is TGraphAsymmErrors)
#        print "hist status =", (tt is TH1D) or (tt is TH1F)
        if ih == 0 :      
            if (tt is TGraphAsymmErrors) | (tt is TGraph) : 
                histList[ih].Draw("AL3")
            if (tt is TH1D) or (tt is TH1F) or (tt is TH1) or (tt is TH1I) :
                histList[ih].Draw("CHIST")   
        if ih > 0 :
            #histList[ih].SetLineWidth(2)
            if (tt is TGraphAsymmErrors) | (tt is TGraph) : 
                histList[ih].Draw("L3 same")
            if (tt is TH1D) or (tt is TH1F) or (tt is TH1) or (tt is TH1I) :
                histList[ih].Draw("CHISTsame")   

        if (tt is TGraphAsymmErrors) | (tt is TGraph) :
            histList[ih].SetMaximum(10000.0) 
            histList[ih].SetMinimum(0.0001) 
            histList[ih].SetMarkerColor(colors[ih])
            histList[ih].SetLineColor(colors[ih])
            histList[ih].SetLineWidth(3)
            histList[ih].SetLineStyle(linestyle[ih])
            
            #histList[ih].SetMarkerStyle(markerStyle[ih])
            #histList[ih].SetMarkerSize(1)
            leg.AddEntry(histList[ih],legendtext[ih],"PL")
        if (tt is TH1D) or (tt is TH1F) or (tt is TH1) or (tt is TH1I) :
            histList[ih].SetLineStyle(linestyle[ih])
            histList[ih].SetLineColor(colors[ih])
            histList[ih].SetLineWidth(3)
            leg.AddEntry(histList[ih],legendtext[ih],"L")
        histList[ih].GetYaxis().SetTitle(titleVec[1])
        histList[ih].GetYaxis().SetTitleSize(0.052)
        histList[ih].GetYaxis().SetTitleOffset(0.88)
        histList[ih].GetYaxis().SetTitleFont(22)
        histList[ih].GetYaxis().SetLabelFont(22)
        histList[ih].GetYaxis().SetLabelSize(.052)
        histList[ih].GetXaxis().SetRangeUser(xRange[0],xRange[1])
        histList[ih].GetXaxis().SetLabelSize(0.0000);
        histList[ih].GetXaxis().SetTitle(titleVec[0])
        histList[ih].GetXaxis().SetLabelSize(0.052)
        histList[ih].GetXaxis().SetTitleSize(0.052)
        histList[ih].GetXaxis().SetTitleOffset(1.04)
        histList[ih].GetXaxis().SetTitleFont(22)
        histList[ih].GetXaxis().SetTickLength(0.07)
        histList[ih].GetXaxis().SetLabelFont(22)
        histList[ih].GetYaxis().SetLabelFont(22) 
# histList[ih].GetXaxis().SetNdivisions(508)
#

        i=i+1
    pt = TPaveText(0.0877181,0.9,0.9580537,0.96,"brNDC")
    pt.SetBorderSize(0)
    pt.SetTextAlign(12)
    pt.SetFillStyle(0)
    pt.SetTextFont(22)
    pt.SetTextSize(0.046)
    text = pt.AddText(0.05,0.5,"CMS Work in Progress")
    #text = pt.AddText(0.5,0.5,"12.9 fb^{-1} (13 TeV)")
    text = pt.AddText(0.8,0.5," (13 TeV)")
    text = pt.AddText(0.65,0.5," AK8")
    pt.Draw()
   
    

#    t2a = TPaveText(0.0877181,0.81,0.9580537,0.89,"brNDC")
#    t2a.SetBorderSize(0)
#    t2a.SetFillStyle(0)
#    t2a.SetTextSize(0.040) 
#    t2a.SetTextAlign(12)
#    t2a.SetTextFont(62)
#    histolabel1= str(fileVec[(len(fileVec)-1)])
#    text1 = t2a.AddText(0.06,0.5,"CMS Internal") 
#    t2a.Draw()
    leg.Draw()
#
#    c.cd()
    outputdirname = 'MonoHPlots/'
    histname=outputdirname+pngname 
    c.SaveAs(histname+'.png')
    c.SaveAs(histname+'.pdf')
    outputname = 'cp  -r '+ outputdirname +' /afs/hep.wisc.edu/home/khurana/public_html/'
    os.system(outputname) 


'''
print "calling the plotter"

files=['AnalysisHistograms_MergedSkimmedV12_Puppi_V1/DataCards_AllRegions/SPlusBFit.root',
       'AnalysisHistograms_MergedSkimmedV12_Puppi_V2/DataCards_AllRegions/SPlusBFit.root',
       'AnalysisHistograms_MergedSkimmedV12_Puppi_V3/DataCards_AllRegions/SPlusBFit.root',
       'AnalysisHistograms_MergedSkimmedV12_Puppi_V4/DataCards_AllRegions/SPlusBFit.root',
       'AnalysisHistograms_MergedSkimmedV12_Puppi_V5/DataCards_AllRegions/SPlusBFit.root',
       'AnalysisHistograms_MergedSkimmedV12_PuppiCA15_V1/DataCards_AllRegions/SPlusBFit.root'
       ]

legend=['subjet', 
        'DBT:M',
        'DBT:T',
        'DBT:L', 
        'subjet+TheaC' ,
        'CA15-subjet'
        ]

histodir=''
histodirMET=''


namelist=['LimitExpectedCLs']


for iname in namelist:
    histoname = histodir+iname 
    ytitle='#sigma_{95% CL}/#sigma_{th}'
    DrawOverlap(files,[histoname],["M_{Z'}",ytitle],legend,'limit_Comparison',[0,1],)
    


files=['AnalysisHistograms_MergedSkimmedV12_Puppi_V1/DataCards_AllRegions/SPlusBFit.root',
       'AnalysisHistograms_MergedSkimmedV12_PuppiCA15_V1/DataCards_AllRegions/SPlusBFit.root',
       #'AnalysisHistograms_MergedSkimmedV12_PuppiCA15_V2/DataCards_AllRegions/SPlusBFit.root'
       'MITGraphs/AK8.root',
       'MITGraphs/CA15.root'
       ]

legend=['AK8-BL', 
        'CA15-BL',
        #'CA15-SJ-TheaC',
        'AK8-New',
        'CA15-New'
        ]

histodir=''
histodirMET=''


namelist=['LimitExpectedCLs']


for iname in namelist:
    histoname = histodir+iname 
    ytitle='#sigma_{95% CL}/#sigma_{th}'
    DrawOverlap(files,[histoname],["M_{Z'}",ytitle],legend,'limit_Comparison_AK8_CA15',[0,1],)
    
'''
