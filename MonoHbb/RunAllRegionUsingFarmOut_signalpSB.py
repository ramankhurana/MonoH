#!/usr/bin/env python                                                                                                                                                                
#from MonoHBranchReader import AnalyzeDataSet, CheckFilter, MakeTable, DeltaR, Phi_mpi_pi
import os

mode='signalpSB'
#inputfilename='NCUGlobalTuples_1.root'
#inputfilename='input.txt'
#outfilename='out.root'

inputfilename = os.environ['INPUT']
outfilename   = os.environ['OUTPUT']

if mode == 'signal':
    os.system('./MonoHBranchReader.py  -m 100.0 -M 150.0 -i '+inputfilename+' -o '+outfilename+'  -a -j 0 -J 2 -l 0 -L 1  --MLow1 100.0 --MHigh1 150.0 -F ')

if mode == 'signalpSB':
    os.system('./MonoHBranchReader.py  -m 30.0 -M 250.0 -i '+inputfilename+' -o '+outfilename+'  -a -j 0 -J 2 -l 0 -L 1  --MLow1 30.0 --MHigh1 250.0  -F ')

## Mass Sidebands
## inverting the mass cut

if mode == 'zj':
    os.system('./MonoHBranchReader.py  -m 30.0 -M 100.0 -i '+inputfilename+' -o '+outfilename+'  -a -j 0 -J 2 -l 0 -L 1  --MLow1 150.0 --MHigh1 250.0  -F')

##WJets
## 1 additinal lepton
## remove the mass cut
if mode == 'wj':
    os.system('./MonoHBranchReader.py  -m 30.0 -M 250.0 -i '+inputfilename+' -o '+outfilename+'  -a -j 1 -J 2 -l 1 -L 2  --MLow1 30.0 --MHigh1 250.0  -F')


##TT
## 1 additional lepton 
## >1 additional jets
if mode == 'tt':
    os.system('./MonoHBranchReader.py  -m 30.0 -M 250.0 -i '+inputfilename+' -o '+outfilename+'  -a -j 2 -J 10 -l 1 -L 2  --MLow1 30.0 --MHigh1 250.0  -F')
    
## TT+WJ
if mode == 'wt':
    os.system('./MonoHBranchReader.py  -m 30.0 -M 250.0 -i '+inputfilename+' -o '+outfilename+'  -a -j 0 -J 10 -l 1 -L 2  --MLow1 30.0 --MHigh1 250.0  -F')

## WJAlphaBet
if mode == 'wjalphabet':
    os.system('./MonoHBranchReader.py  -m 30.0 -M 100.0 -i '+inputfilename+' -o '+outfilename+'  -a -j 1 -J 2 -l 1 -L 2  --MLow1 150.0 --MHigh1 250.0  -F')

## TTAlphabet
if mode == 'ttalphabet':
    os.system('./MonoHBranchReader.py  -m 30.0 -M 100.0 -i '+inputfilename+' -o '+outfilename+'  -a -j 2 -J 10 -l 1 -L 2  --MLow1 150.0 --MHigh1 250.0  -F')

##WTAlphabet
if mode == 'wtalphabet':
    os.system('./MonoHBranchReader.py  -m 30.0 -M 100.0 -i '+inputfilename+' -o '+outfilename+'  -a -j 0 -J 10 -l 1 -L 2  --MLow1 150.0 --MHigh1 250.0  -F')
