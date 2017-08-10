# For bb+DM 

# Step 0: DelPanj
  - Following instructions assume that you already have the output files from DelPanj analyzer to test the following steps. 
  

# Step 1: Skimmer 
  - The first step is to skim the DelPanj samples into flat trees. 
  - This can be done using SkimTree.py
  - change the content of "MZp1700Ma0300.txt" or make a new text file which will have the path to the rootfiles which you want to skim. 
  - change the outfilename=  as per your need, 
  - You can run the code using "python SkimTree.py"
  - Once you have the code running locally, you can submit the batch jobs on lxplus or TIFR. 

# Step 2: Signal Regions Selection 

# Step 3: Signal efficiency extraction 

# Step 4: Signal selection optimisation

# Step 5: Control Region Selection 

# Step 6: Stack plots for signal and control regions 

# Step 7: Limit extraction using Higgs combination tool 


#-------

#Instructions below may be wrong/outdates. So refer to them at your own risk. 


# MonoH

#for combine
cd /afs/hep.wisc.edu/cms/khurana/MonoH2016MCProduction/MonoHEfficiency/CMSSW_7_4_7/src; cmsenv; cd -
-- MonoHBranchReader.py can be used to run on one rootfile and it gives back one rootfile with signal region histograms and text file with efficiency. 

-- This efficiency info will be in rootfile in future. 

python MonoHBranchReader.py -a -i rootfilename

# Run on all samples

-- MonoHbbAllSamplesReader.py will loop over all the filrs listed in in text file: allfiles.txt and run the MonoHBranchReader.py script on all these files one by one. 

-- Run it using 

python MonoHbbAllSamplesReader.py


-- For signal region use: 

## for commandline 
python MonoHBranchReader.py  -m 100.0 -M 150.0 -i NCUGlobalTuples_1.root  -a -j 0 -J 2 -l 0 -L 1 --MLow1 100.0 --MHigh1 150.0

#python MonoHBranchReader.py  -m 100 -M 150 -i NCUGlobalTuples_1.root  -a -j 0 -J 2 -l 0 -L 1 

## for Znunu Jets CR 
python MonoHBranchReader.py  -m 100 -M 150 -i NCUGlobalTuples_1.root  -a -j 0 -J 2 -l 0 -L 1 


## for faromout 
python MonoHBranchReader.py  -m 100 -M 150 -i NCUGlobalTuples_1.root  -a -j 0 -J 2 -l 0 -L 1 -F 


## for DiMu CR: 
python DiMuonControlRegion.py  -m 100 -M 150 -i NCUGlobalTuples_223.root -a -j 0 -J 2 -l 0 -L 1



## Version number of the dorectory
AnalysisHistograms_MergedSkimmedV12_Puppi_V1: AK8 Puppi jets with subjets
AnalysisHistograms_MergedSkimmedV12_Puppi_V2: AK8 Puppi jets with double b-tagger Medium WP
AnalysisHistograms_MergedSkimmedV12_Puppi_V3: AK8 Puppi jets with double b-tagger Tight WP
AnalysisHistograms_MergedSkimmedV12_Puppi_V4: AK8 Puppi jets with double b-tagger Loose WP
AnalysisHistograms_MergedSkimmedV12_Puppi_V5: AK8 Puppi jets with subjets/double b-tagger L/M/T WP with Thea correction on Uncorrected SD mass. 
AnalysisHistograms_MergedSkimmedV12_Puppi_V6: AK8 Puppi jets with double b-tagger Medium WP with b-tagging SF = 1
AnalysisHistograms_MergedSkimmedV12_Puppi_V7: same as V1 AK8 Puppi jets with subjets with ZpBaryonic Model and full dataset. 
AnalysisHistograms_MergedSkimmedV12_Puppi_V8: same as V7 and added 2D MET vs Mass histogram with 1 GeV binning for bin-unrolling at later step. 


AnalysisHistograms_MergedSkimmedV12_PuppiCA15_V1: CA15 Puppi jets with subjet b-tagger 
AnalysisHistograms_MergedSkimmedV12_PuppiCA15_V1: CA15 Puppi jets with subjet b-tagger  and Thea correction on the mass. 


## Version number of the directory of Skimmer 
V12_PuppiCA15_V1: First version with CA15 jets. 
