 ##  BDT Training
 (All the ntuples can be found at this location: ```/dpm/indiacms.res.in/home/cms/store/user/dekumar/t3store2/2HDM_trainfile``` and ```/dpm/indiacms.res.in/home/cms/store/user/dekumar/t3store2/QCD_signan_train_v3```)
 
 To do training please follow these steps:
 ### pT dependent training
#### Step1
Run this command locally (lxplus) to get the training file:
```
python trainfilemaker.py /path/of/ntuple/file
 ```
(Edit the output file name inside the file ```trainfilemaker.py```)
 
 (For condor job submition please see the instructions below)
 
#### Step2
To do training open the terminal and run the command:
```
jupyter notebook
```
 Now run this file ```CA15DoubleBJetTagger.ipynb```. Before running change the inputfile name and selection and replace ```bdt.fit(X_train, y_train,sample_weight=nw_train)``` with ```bdt.fit(X_train, y_train)``` and do not use branch```weight_branch=['weight']```
 
### pT independent training
To do pT independent training follow these steps(Only for signal):

#### Step1
Run this command locally (lxplus) to get the training file:
```
python trainfilemaker.py /path/of/ntuple/file
 ```
Edit the output file name inside the file ```trainfilemaker.py``` and use this outputfile as input for this command:

```
python pt_reweight.py inputfilename(which is output of step1)
```
After step1 we get new file ```pt_weight.root``` . This file we will use in the next step.
#### Step2
Run this command to get training file (In this file we can see one more branch ```weight``` this branch we will use in the training) :
```
python signal_TrainfileMaker_weight.py /path/of/ntupe/file
```
 Note: We need to provide same signal input file which we provided in step1.
 
 #### Step3
 
 To do training open the terminal and run the command:
```
jupyter notebook
```
  Now run this file ```CA15DoubleBJetTagger.ipynb```. Before running change the inputfile name and selection and replace  ```bdt.fit(X_train, y_train)``` with ```bdt.fit(X_train, y_train,sample_weight=nw_train)```  and use branch```weight_branch=['weight']```. Please check correct branch name in the root file.
 
 ### Condor job submition for QCD samples
  
 If you want to do training over all the QCD samples then its good to submit condor job to get the training files for all the QCD samples.
 ```
 ssh username@login.uscms.org
 mkdir <workdir>
 cd <workdir>
 git clone https://github.com/deepakcern/MonoH.git
 cd MonoH/bbDM/bbMET/Train_Condor/
 . submitjobs.sh
 ```
 Once jobs are done then do
 ```
 python HADD_multi_v2.py
 ```
 Now login into lxplus and set tree weight in all the QCD samples using the command:
 ```
 python Scale_tree.py
 ```
 Please provide the input and output dir path inside the file ```Scale_tree.py```
 
 ### Training for all the QCD samples
 (Not done yet)
 
  #  Deep Jet ( training and evaluation of deep neural networks for Jet identification)
  
  ## Setup python packages (CERN)
  
It is essential to perform all these steps on lxplus7. Simple ssh to 'lxplus7' instead of 'lxplus'

Pre-Installtion: Anaconda setup (only once) Download miniconda3

```
mkdir condasetup
cd condasetup
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```

Please follow the installation process. If you don't know what an option does, please answer 'yes'. After installation, you have to log out and log in again for changes to take effect. If you don't use bash, you might have to add the conda path to your .rc file

```
export PATH="<your miniconda directory>/miniconda3/bin:$PATH"
```

This has to be only done once.

 ## Installation:
 
 ```
 source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc7_amd64_gcc700
cmsrel CMSSW_10_1_7
cd CMSSW_9_3_7/src
```

```
https://github.com/jmduarte/DeepJetCore.git 
https://github.com/jmduarte/DeepJet.git
cd DeepJetCore/environment
./setupEnv.sh deepjetLinux3.conda
```

For enabling gpu support add 'gpu' as an additional option to the last command. This will take a while. Please log out and in again once the installation is finised.

## Compiling DeepJetCore
When the installation was successful, the DeepJetCore tools need to be compiled.

```
cd DeepJetCore
source lxplus_env.sh / gpu_env.sh
cd compiled
make -j4
```

## Usage

After logging in, please source the right environment (please cd to the directory first!):
```
cd <your working dir>/DeepJet
source lxplus_env.sh / gpu_env.sh
```
I used ```source lxplus_env.sh```

(Used the root files from the locations: 
```
our ntuples (LPC):
/eos/uscms/store/group/lpchbb/20180401_ak8/

mixed+merged ntuples (LPC)
/eos/uscms/store/group/lpcjj/doubleb_merged_h_q_lessQCD/

data collection numpy arrays (LPC):
/eos/uscms/store/group/lpcjj/convert_20180401_ak8_deepDoubleB_db_cpf_sv_reduced_lessQCD_dl4jets_train_val
/eos/uscms/store/group/lpcjj/convert_20180401_ak8_deepDoubleB_db_cpf_sv_reduced_lessQCD_dl4jets_test
```

## The preparation for the training consists of the following steps

- define the data structure for the training (example in modules/TrainData_template.py)
  for simplicity, copy the file to TrainData_template.py and adjust it. 
  Define a new class name (e.g. TrainData_template), leave the inheritance untouched
  
- register this class in DeepJet_DBB/convertFromRoot/convertFromRoot.py by 
  a) importing it (the line in the code is indiacted by a comment)
  b) adding it to the class list below'

- Make a list of training and testing samples
  ```
  python list_writer.py --train <path/to/train/files> --test <path/to/test/files>
  ```
- So far, the data structure used are:
  ```
  TrainData_deepDoubleC_db_cpf_sv_reduced   for Hcc vs QCD discrimination
  TrainData_deepDoubleCvB_db_cpf_sv_reduced   for Hcc vs Hbb discrimination 	
  ```  

- convert the root file to the data strucure for training:
  ```
  # Prepare train data
  cd DeepJet_DBB/convertFromRoot
  ./convertFromRoot.py -i /path/to/the/root/ntuple/list_of_root_files.txt -o /output/path/that/needs/some/disk/space -c TrainData_myclass
  #example
  python convertFromRoot.py -i train_list.txt -o Jan23_train_full_BB -c TrainData_deepDoubleB_db_pf_cpf_sv

  # Prepare test data
  python convertFromRoot.py --testdatafor Jan23_train_full_BB/trainsamples.dc -i test_files.txt -o Jan23_test_full_BB
  ```
  
  This step can take a while.
  
## Training
  
the training is launched in the following way:
```
cd DeepJet/Train
python deepDoubleB_reference.py /path/to/the/output/of/convert/dataCollection.dc <output dir of your choice>
```
(Check this location to get datacollection.dc file: ```/eos/uscms/store/group/lpcjj/convert_20180401_ak8_deepDoubleB_db_cpf_sv_reduced_lessQCD_dl4jets_train_val```

## Evaluation

After the training has finished, the performance can be evaluated.
The evaluation consists of a few steps:

1) converting the test data
```
cd DeepJet/convertFromRoot
./convertFromRoot.py --testdatafor <output dir of training>/trainsamples.dc -i /path/to/the/root/ntuple/list_of_test_root_files.txt -o /output/path/for/test/data
```

2) applying the trained model to the test data
```
predict.py <output dir of training>/KERAS_model.py  /output/path/for/test/data/dataCollection.dc <output directory>
```
This creates output trees. and a tree_association.txt file that is input to the plotting tools

There is a set of plotting tools with examples in 
DeepJet/Train/Plotting









