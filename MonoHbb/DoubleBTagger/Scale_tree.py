import sys
import os #, commands
import shutil
from ROOT import *
import ROOT
from optparse import OptionParser

#from glob import glob

#path=''

#files=sorted(glog.glob(path))


inDirName = '/afs/cern.ch/work/d/dekumar/public/monoH/ca15_trainfiles/QCD_v2/all_qcd'
outDirName = '/afs/cern.ch/work/d/dekumar/public/monoH/ca15_trainfiles/QCD_v2/all_qcd_scaled'

inTreeName = 'outTree'
ntuple = TChain("outTree")
#histName = "ptPruned"

n = 0
xSec = 1
genEv = 1
for inFileName in os.listdir(inDirName):
  if inFileName.endswith(".root"):
    n += 1
    print ("copying file %i" %n)

    if inFileName.find("HT200to300") != -1:
        xSec = 1712000.
        # genEv = 2001453. #events in DAS
        shutil.copy2("%s/%s" %(inDirName, inFileName), "%s/%s"%(outDirName, inFileName))
        inFile = TFile.Open( "%s/%s" %(outDirName, inFileName), "update" )
        print ("processing", inFileName)
    elif inFileName.find("HT300to500") != -1:
        xSec = 347700.
        genEv = 2001169. #events in DAS
        shutil.copy2("%s/%s" %(inDirName, inFileName), "%s/%s"%(outDirName, inFileName))
        inFile = TFile.Open( "%s/%s" %(outDirName, inFileName), "update" )
        print ("processing", inFileName)
    elif inFileName.find("HT500to700") != -1:
        xSec = 32100.
        #genEv = 1986177. #events in DAS
        shutil.copy2("%s/%s" %(inDirName, inFileName), "%s/%s"%(outDirName, inFileName))
        inFile = TFile.Open( "%s/%s" %(outDirName, inFileName), "update" )
        print ("processing", inFileName)


    elif inFileName.find("HT700to1000") != -1:
        xSec = 6831.
        #genEv = 2001453. #events in DAS
        shutil.copy2("%s/%s" %(inDirName, inFileName), "%s/%s"%(outDirName, inFileName))
        inFile = TFile.Open( "%s/%s" %(outDirName, inFileName), "update" )
        print ("processing", inFileName)
    elif inFileName.find("HT1000to1500") != -1:
        xSec = 12030.
        genEv = 2001169. #events in DAS
        shutil.copy2("%s/%s" %(inDirName, inFileName), "%s/%s"%(outDirName, inFileName))
        inFile = TFile.Open( "%s/%s" %(outDirName, inFileName), "update" )
        print ("processing", inFileName)
    elif inFileName.find("HT1500to2000") != -1:
        xSec = 119.9
        #genEv = 1986177. #events in DAS
        shutil.copy2("%s/%s" %(inDirName, inFileName), "%s/%s"%(outDirName, inFileName))
        inFile = TFile.Open( "%s/%s" %(outDirName, inFileName), "update" )
        print ("processing", inFileName)

    elif inFileName.find("HT2000toInf") != -1:
        xSec = 25.24
        #genEv = 1986177. #events in DAS
        shutil.copy2("%s/%s" %(inDirName, inFileName), "%s/%s"%(outDirName, inFileName))
        inFile = TFile.Open( "%s/%s" %(outDirName, inFileName), "update" )
        print ("processing", inFileName)

    else:
          print (" Cross section not defined! Exiting...")
          continue
    #print ("integral:")
    #print (inFile.Get(histName).Integral())
    ntuple.Add(inDirName+'/'+inFileName)
    genEv = ntuple.GetEntries()
    print ('Not using gen events from DAS! Using %i events stored in %s' %(genEv,inFileName))
    weight = xSec/genEv

    myTree = inFile.Get( inTreeName )
    myTree.SetWeight(weight)
    myTree.AutoSave()

inFile.Close()
del myTree
