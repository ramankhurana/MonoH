### 
###
# Created By : Raman Khurana
# Date       : 03:March:2016
# Time       : 22:20:30 
###
###

## import user defined modules
#from Utils import *
import Utils
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


#########################################
#
# Set Weights for each sample
#
#########################################

debug_=False


ROOT.gROOT.ProcessLine('.L BinUnroller.C+')

####################################################################################################################
## weighted and summed over all samples histograms for a given physics process. 
####################################################################################################################
def MakeRooDataHist(phys_process, histname, fullrange_=False):
    print "--------- inside MakeRooDataHist ------------"
    #filedata = TFile('Histograms_CMSSW76X_BaseLine_METSys_V12/AnalysisHistograms_V0/'+Utils.samples['TT']['files'][0], 'READ')
    filedata = TFile(Utils.prefix+'/'+Utils.samples['TT']['files'][0], 'READ')
    hist_met_ = filedata.Get(histname)
    hist_met_.Sumw2()
    #print (phys_process, hist_met_.Integral())
    hist_met_.SetDirectory(0)
    TH1.AddDirectory(0)
    TH2.AddDirectory(0)

    hist_met_.Scale(0.0)
    iweight = 0
    for irootfile in Utils.samples[phys_process]['files']:
        file01 = TFile(Utils.prefix+'/'+irootfile, 'READ')
        hist_ = file01.Get(histname)
        #print hist_.Integral()
        #hist_.SetDirectory(0)
        TH1.AddDirectory(0)
        TH2.AddDirectory(0)
        
        if phys_process != 'data_obs': hist_.Scale(Utils.samples[phys_process]['weight'][iweight])
        if phys_process == 'data_obs': hist_.Scale(1)
        
        #print (Utils.prefix+'/'+irootfile, hist_.Integral(1,-1))
        hist_met_.Add(hist_)
        iweight = iweight + 1
        
        if debug_ :
            print "before ",hist_.Integral()
    h = hist_met_
    
    ## put overflow in the last bin 
    nbins  = h.GetNbinsX()
    #print "Integral  = ", (h.Integral(), h.Integral(1,-1), h.GetBinContent(nbins+1), Utils.prefix+'/'+irootfile)
    overflow = h.GetBinContent(nbins+1)
    h.AddBinContent(nbins, overflow) 
    return h

############################################################
## background RooDataHist taken from input Rootfiles. 
## to fix the normalisation and pdf of TT and VV and ZH
############################################################

def WriteHistograms(nominalname, postfix, rootfilename, rebininfo,  filemode='UPDATE'):
    print "--------- inside MakeRooDataHist ------------"
    weights=[]
    if debug_ : print "Top"
    h_tt    = MakeRooDataHist('TT', nominalname, True) 
    h_st    = MakeRooDataHist('ST', nominalname, True) 
    #print " h_tt = ",h_tt.Integral(1,-1)
    #print "h_st = ",h_st.Integral(1,-1)
    
    weight_  = Utils.samples['TT']['weight'][0]         ;  weights.append(weight_)
    weight_  = Utils.samples['VV']['weight'][0]         ;  weights.append(weight_)
    weight_  = Utils.samples['znunujets']['weight'][0]  ;  weights.append(weight_)
    weight_  = Utils.samples['wjets']['weight'][0]      ;  weights.append(weight_)
    weight_  = Utils.samples['ZH']['weight'][0]         ;  weights.append(weight_)

    h_tt.Add(h_st)
    h_tt.SetNameTitle('TT'+postfix,'TT')
    
    
    if debug_ : print "VV"
    h_VV    = MakeRooDataHist('VV', nominalname, True) 
    h_VV.SetNameTitle('DIBOSON'+postfix,'DIBOSON')
    
    if debug_ : print "ZNN"
    h_znn    = MakeRooDataHist('znunujets', nominalname, True) 
    h_znn.SetNameTitle('DYJETS'+postfix,'DYJETS')
    
    if debug_ : print "WJ"
    h_wj    = MakeRooDataHist('wjets', nominalname, True) 
    h_wj.SetNameTitle('WJETS'+postfix,'WJETS')
    
    if debug_ : print "ZH"
    h_zh    = MakeRooDataHist('ZH', nominalname, True) 
    h_zh.SetNameTitle('ZH'+postfix,'ZH')
    
    if debug_ : print "signals start"
    
    ## make a stack of the backgrounds
    if nominalname == 'h_met_0':
        c1 = TCanvas()
        bkgStack = THStack ("bkgStack","bkgStack")
        h_zh.SetFillColor(1)
        h_VV.SetFillColor(2)
        h_tt.SetFillColor(3)
        h_znn.SetFillColor(4)
        h_wj.SetFillColor(5)
        
        if type(h_zh) is TH1F:
            rebin_ = 1
            h_zh.Rebin(rebin_)
            h_VV.Rebin(rebin_)
            h_tt.Rebin(rebin_)
            h_znn.Rebin(rebin_)
            h_wj.Rebin(rebin_)

        bkgStack.Add(h_zh,'hist')
        bkgStack.Add(h_VV,'hist')
        bkgStack.Add(h_tt,'hist')
        bkgStack.Add(h_znn,'hist')
        bkgStack.Add(h_wj,'hist')
            
        bkgStack.Draw()
        
        h_data = []#TH1F()
        #if filemode =='RECREATE':
        if debug_ : print "data"
        h_data = MakeRooDataHist('data_obs', nominalname, True)
        h_data.SetNameTitle('data_obs', 'data_obs')
        #print "data integral = ",h_data.Integral()
        #bins=[200., 350., 500., 3000.]
        #h_data.Rebin(3,"data_obs", bins)
        h_data.Draw('same')
        if type(h_data) is TH1F:
            h_data.Rebin(rebin_)
        c1.SaveAs('METstack.pdf')
    
    ## Stack macro ends here
   
    ## 2HDM mass points.
    Zp2HDM_namelist = Utils.Zp2HDM_names
    h_Zp2HDM = []
    for iZp2HDM_name in Zp2HDM_namelist:
        weights.append(Utils.samples[iZp2HDM_name]['weight'][0])
        h_tmp = MakeRooDataHist(iZp2HDM_name, nominalname, True)
        iZp2HDM_name = iZp2HDM_name.replace('signal','monoHbbM')
        h_tmp.SetNameTitle(iZp2HDM_name+postfix,iZp2HDM_name)
        h_Zp2HDM.append(h_tmp)
    

    
    ZpB_NameList = Utils.ZpB_Names
    
    
    weightZpB = []
    h_ZpB = []
    for samplename in ZpB_NameList:
        weightZpB_  = Utils.samples[samplename]['weight'][0]  
        
        weightZpB.append(weightZpB_)
        weights.append(weightZpB_)
        h_tmp = MakeRooDataHist(samplename, nominalname, True)
        h_tmp.SetNameTitle(samplename+postfix,samplename)
        h_ZpB.append(h_tmp)
        
    #print h_ZpB
        
    if debug_ : print "signal end"
    
    h_data = []#TH1F()
    #if filemode == 'RECREATE':
    if debug_ : print "data"
        #newname = nominalname.replace("_Nominal","")
        #if debug_ : print "-- newname = ", newname
    h_data = MakeRooDataHist('data_obs', nominalname, True)
    h_data.SetNameTitle('data_obs', 'data_obs')
        #print "data integral = ",h_data.Integral()
        #bins=[200., 350., 500., 3000.]
        #h_data.Rebin(3,"data_obs", bins)
        
        
    fshape = TFile(rootfilename+'.root',filemode)
    fshape.cd()
    
    h_all=[]
    h_all.append(h_tt)
    h_all.append(h_VV)
    h_all.append(h_znn)
    h_all.append(h_wj)
    h_all.append(h_zh)
    
    for ihistogram in h_Zp2HDM:
        h_all.append(ihistogram)
    ## add all the ZpB histograms
    
    for ihistogram in h_ZpB:
        h_all.append(ihistogram)
    
    ## add data histogram at last
    weights.append(1.0)
    h_all.append(h_data)
    
    
    if postfix =='':
        yieldfile = open(rootfilename+'.txt','w')
    ihist = 0
    
    
    for ih in h_all:
        name = ih.GetName()
        title = ih.GetTitle()
        h_new = []#TH1F()

        if rebininfo['rebin']: 
            ## for fixed bin-width
            if len(rebininfo['bins'])==1:
                h_tmp = ih.Clone(name)
                if type(h_tmp) is TH1F:
                    h_new = TH1F (h_tmp.Rebin(rebininfo['bins'][0]))
                if type(h_tmp) is TH2F:
                    h_new = h_tmp
            
            ## for variable bin-width
            if len(rebininfo['bins'])>1:
                metbins_ = rebininfo['bins'] #[200.,350.,500.,1000.]
                metbins = array('d', metbins_)
                h_tmp = ih.Clone(name)
                if type(h_tmp) is TH1F:
                    h_new = TH1F (h_tmp.Rebin(len(metbins_)-1,name , metbins))
                if type(h_tmp) is TH2F:
                    h_new = h_tmp

        
        h_new.Write()
        h_new_unrolled=[]
        if type (h_new) is TH2F:
            print "This is 2D histogram"
            h_new_unrolled  = ROOT.BinUnroller(h_new)
            print (" type of h_new_unrolled = ", type(h_new_unrolled)) 
            name_ = h_new.GetName()
            #name_ = name_.replace('_2d','_unroll')
            name_ = name_.replace('_2d','')
            h_new_unrolled.SetName(name_)
            h_new_unrolled.Write()
        
        if type (h_new) is TH1F:
            h_new_unrolled = h_new
            
        error_ = 0.0
        #if postfix =='_2d': error_ = weights[ihist] * TMath.Sqrt(ih.Integral())
        #if postfix =='_2d': yieldfile.write(ih.GetName()+' '+str(ih.Integral())+' '+str(error_)+'\n')
        #if postfix =='_2d': yieldfile.close()
        print "ihist = ", (ihist, len(h_all))
        if postfix =='': error_ = weights[ihist] * TMath.Sqrt(h_new_unrolled.Integral())
        if postfix =='': 
            line_ = h_new_unrolled.GetName()+' '+str(h_new_unrolled.Integral())+' '+str(error_)+'\n'
            line_ = line_.replace('data_obs','DATA')
            yieldfile.write(line_)
        ihist = ihist+1



def HistogramsOneDir(WhichRegion):
    print "--------For h_MET0_Nominal--------- "

    METReBinInfo = {'rebin':True,
                    'range':[200.0,1000.],
                    #'bins':[200.0,350.0,500.0,1001.0]
                    #'bins':[200.0,250.0,350.0,500.0, 650.0, 750.0, 850.0, 1000.0] # 7 bins
                    'bins':[200.0,250.0,350.0,450.0, 500.0, 550.0, 600., 700.0, 800, 900, 1000.0] # 10 bins
                    
                    }
    #WriteHistograms(nominalname, postfix, rootfilename, rebininfo,  filemode='UPDATE'):
    WriteHistograms('h_met_0','',WhichRegion, METReBinInfo,'RECREATE')
    
    MassReBinInfo = {'rebin':True,
                     'range':[30.0,250.],
                     'bins':[1] ## is only one number is provided then it serve as rebin factor
                     }
    #WriteHistograms('h_mass_0','_mass',WhichRegion,MassReBinInfo)
    
    MassReBinInfo = {'rebin':True,
                     'range':[-99999., 99999.],
                     'bins':[1] ## is only one number is provided then it serve as rebin factor
                     }
    #WriteHistograms('h_met_vs_mass_0','_2d',WhichRegion,MassReBinInfo)
    
    '''WriteHistograms(WhichRegion+'/h_MET0_muRUp','_CMS_monoHbb_scaleRUp',WhichRegion)
    WriteHistograms(WhichRegion+'/h_MET0_muRDown','_CMS_monoHbb_scaleRDown',WhichRegion)
    WriteHistograms(WhichRegion+'/h_MET0_muFUp','_CMS_monoHbb_scaleFUp',WhichRegion)
    WriteHistograms(WhichRegion+'/h_MET0_muFDown','_CMS_monoHbb_scaleFDown',WhichRegion)
    WriteHistograms(WhichRegion+'/h_MET0_EWKUp','_CMS_monoHbb_ewkUp',WhichRegion)
    WriteHistograms(WhichRegion+'/h_MET0_EWKDown','_CMS_monoHbb_ewkDown',WhichRegion)
    '''
    ''' for PDF
    for ipdf in range(101):
        hname = 'h_MET0_'+str(ipdf)
        WriteHistograms(WhichRegion+'/'+hname, '_PDF'+str(ipdf),WhichRegion)
    ''' 
    return 0



if __name__ == "__main__":
    
    print ("running the models of MakeShapesAndStack.py directly to test it ")
    
    
    
    #inputdir = 'AnalysisHistograms_MergedSkimmedV12_Puppi_V7/'
    inputdir = 'AnalysisHistograms_MergedSkimmedV12_Puppi_V8/'
    #inputdir = 'AnalysisHistograms_MergedSkimmedV12_PuppiCA15_V2/'
    mainoutdir = inputdir+ '/AllRegions' 
    datacardsdir = inputdir+ '/DataCards_AllRegions'

    os.system('mkdir '+mainoutdir)
    os.system('mkdir '+datacardsdir)

    regionstorun = ['wt', 'signalpSB']
    regionstorunstr = 'wt signalpSB'

    #regionstorun = ['signal', 'zj', 'wt', 'signalpSB']
    #regionstorunstr = 'signal zj wt signalpSB'


    print options.saveshapes
    print regionstorun
    
    if options.saveshapes:
        for iregion in regionstorun:
            printstr = "------------For "+iregion+"  Region--------------"
            print printstr
            Utils.prefix = inputdir+'/'+iregion+'/'
            Utils.setweights() ## weight should be set after writing the prefix value otherwise it will take the default value and it would not be correct. 
            HistogramsOneDir(iregion)
            os.system('mv '+iregion+'.txt '+mainoutdir)
            os.system('mv '+iregion+'.root '+mainoutdir)
            
    ####
    ####

    if options.makecards:
        os.system('python SelectTextFiles.py '+mainoutdir+' '+regionstorunstr)
        
    if options.combinecards: 
        print "combining cards"
        os.system('python CombineDataCardsZpB.py '+datacardsdir+' '+regionstorunstr)
        os.system('python CombineDataCards.py '+datacardsdir+' '+regionstorunstr)
        
    if options.bbb:
        os.system('source binbybin.sh')
        
    if options.runlimit:
        os.system('python CombineDataCardsZpB.py '+datacardsdir+' runlimit')
        os.system('python CombineDataCards.py '+datacardsdir+' runlimit')
        
    if bool(options.runlimit) & bool(options.obs):
        os.system('python CombineDataCardsZpB.py '+datacardsdir+' runlimit obs')
        os.system('python CombineDataCards.py '+datacardsdir+' runlimit obs')

        
    
else :
    print ("MakeShapesAndStack.py is being imported as a module......")

