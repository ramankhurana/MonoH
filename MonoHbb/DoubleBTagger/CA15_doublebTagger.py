# %matplotlib inline

''' original source for this tutorial
https://betatim.github.io/posts/sklearn-for-TMVA-users/
'''
print ("importing packages for python and ROOT")
import random

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier #AdaBoostClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import classification_report, roc_auc_score
from sklearn.metrics import classification_report, roc_auc_score
from sklearn.metrics import roc_curve, auc


from root_numpy import root2array, rec2array

print ("importing packages is done")

def get_numpy_array(sample,tree,branch_names,selection):
    branch_names = [c.strip() for c in branch_names]
    branch_names = (b.replace(" ", "_") for b in branch_names)
    branch_names = list(b.replace("-", "_") for b in branch_names)
    output_arr = root2array(sample,tree,branch_names, selection=selection)
    output_arr=rec2array(output_arr)
    return output_arr

def merge_addColoumn(signal,backgr):
    X=np.concatenate((signal,backgr))
    #add one more column, 1 is for signal and 0 is for background.
    y = np.concatenate((np.ones(signal.shape[0]),np.zeros(backgr.shape[0])))
    return X, y

def get_weight_coloumn(signal_sample,tree,weight_branch,selection):
    weight_arr = root2array(signal_sample,tree,weight_branch,selection=selection)
    weight_arr = rec2array(weight_arr)
    return weight_arr

def compare_train_test(clf, X_train, y_train, X_test, y_test, bins=30):
    decisions = []
    for X,y in ((X_train, y_train), (X_test, y_test)):
        d1 = clf.decision_function(X[y>0.5]).ravel()
        d2 = clf.decision_function(X[y<0.5]).ravel()
        decisions += [d1, d2]

    low = min(np.min(d) for d in decisions)
    high = max(np.max(d) for d in decisions)
    low_high = (low,high)

    plt.hist(decisions[0],
             color='r', alpha=0.5, range=low_high, bins=bins,
             histtype='stepfilled', normed=True,
             label='S (train)')
    plt.hist(decisions[1],
             color='b', alpha=0.5, range=low_high, bins=bins,
             histtype='stepfilled', normed=True,
             label='B (train)')

    hist, bins = np.histogram(decisions[2],
                              bins=bins, range=low_high, normed=True)
    scale = len(decisions[2]) / sum(hist)
    err = np.sqrt(hist * scale) / scale

    width = (bins[1] - bins[0])
    center = (bins[:-1] + bins[1:]) / 2
    plt.errorbar(center, hist, yerr=err, fmt='o', c='r', label='S (test)')

    hist, bins = np.histogram(decisions[3],
                              bins=bins, range=low_high, normed=True)
    scale = len(decisions[2]) / sum(hist)
    err = np.sqrt(hist * scale) / scale

    plt.errorbar(center, hist, yerr=err, fmt='o', c='b', label='B (test)')

    plt.xlabel("BDT output")
    plt.ylabel(" ")
    plt.legend(loc='best')
    plt.savefig("BDToutput_weight_sum.pdf")
    plt.savefig("BDToutput_weight_sum.png")



def test_roc_value(X_test,y_test):
    decisions = bdt.decision_function(X_test)
    print (decisions)
    fpr, tpr, thresholds = roc_curve(y_test, decisions)
    return fpr, tpr

def train(sample_signal,sample_bkg,tree,branch_names,selection):
    print (branch_names)
    signal=get_numpy_array(sample_signal,tree,branch_names,selection)
    backgr=get_numpy_array(sample_bkg,tree,branch_names,selection)
    print ("signal sample and bkg num py array done")

    X,y = merge_addColoumn(signal, backgr)
    print ("signal , bkg merging done ")
    sig_weight = get_weight_coloumn(sample_signal,tree,['weight'],selection)
    bkg_weght=np.ones((backgr.shape[0],1))
    sig_weight=np.concatenate(sig_weight, axis=0)
    bkg_weght=np.concatenate(bkg_weght,axis=0)
    weight= np.concatenate((sig_weight,bkg_weght),axis=0)
    print ("weight np array done")
    print ("splitting start")
    X_train,X_test,y_train,y_test,weight_train,weight_test = train_test_split (X, y, weight ,test_size=0.33, random_state=42)
    print ("splitting done")

    print ("start training")

    dt = DecisionTreeClassifier(max_depth=5)
    bdt = AdaBoostClassifier(dt,algorithm='SAMME',n_estimators=800,learning_rate=0.5)
    # bdt = GradientBoostingClassifier(dt,n_estimators=800,learning_rate=0.5)
    bdt.fit(X_train, y_train,sample_weight=weight_train)
    print ("bdt had done the fitting")
    print ("start testing")
    decisions = bdt.decision_function(X_test)
    print (decisions)
    fpr, tpr, thresholds = roc_curve(y_test, decisions)
    print ("training done")
    return fpr, tpr

def train_sum(sample_signal,sample_bkg,tree,branch_names,selection):


    csv1=['SubJet_csv_1']
    csv2=['SubJet_csv_2']
    sig_csv1=root2array(sample_signal,"outTree",csv1,selection=selection )
    sig_csv2=root2array(sample_signal,"outTree",csv2,selection=selection )
    bkg_csv1=root2array(sample_bkg,"outTree",csv1,selection=selection )
    bkg_csv2=root2array(sample_bkg,"outTree",csv2,selection=selection )
    sig_csv1=rec2array(sig_csv1)
    sig_csv2=rec2array(sig_csv2)
    bkg_csv1=rec2array(bkg_csv1)
    bkg_csv2=rec2array(bkg_csv2)

    sig_sum_csv=[[x[0]+y[0]] for x, y in zip(sig_csv1,sig_csv2) ]
    bkg_sum_csv=[[x[0]+y[0]] for x, y in zip(bkg_csv1,bkg_csv2) ]
    sig_sum_csv = np.array(sig_sum_csv)
    bkg_sum_csv = np.array(bkg_sum_csv)

    print (branch_names)
    signal=get_numpy_array(sample_signal,tree,branch_names,selection)
    backgr=get_numpy_array(sample_bkg,tree,branch_names,selection)

    signal=np.append(signal, sig_sum_csv, axis=1)
    backgr=np.append(backgr, bkg_sum_csv,axis=1)
    print ("signal sample and bkg num py array done")

    X,y = merge_addColoumn(signal, backgr)
    print ("signal , bkg merging done ")
    sig_weight = get_weight_coloumn(sample_signal,tree,['weight'],selection)
    bkg_weght=np.ones((backgr.shape[0],1))
    sig_weight=np.concatenate(sig_weight, axis=0)
    bkg_weght=np.concatenate(bkg_weght,axis=0)
    weight= np.concatenate((sig_weight,bkg_weght),axis=0)
    print ("weight np array done")
    print ("splitting start")
    X_train,X_test,y_train,y_test,weight_train,weight_test = train_test_split (X, y, weight ,test_size=0.33, random_state=42)
    print ("splitting done")

    print ("start training")

    dt = DecisionTreeClassifier(max_depth=5)
    bdt = AdaBoostClassifier(dt,algorithm='SAMME',n_estimators=800,learning_rate=0.5)
    # bdt = GradientBoostingClassifier(dt,n_estimators=800,learning_rate=0.5)
    bdt.fit(X_train, y_train,sample_weight=weight_train)
    print ("bdt had done the fitting")
    print ("start testing")
    decisions = bdt.decision_function(X_test)
    print (decisions)
    fpr, tpr, thresholds = roc_curve(y_test, decisions)
    print ("training done")
    return fpr, tpr


def roc_plot(fpr,tpr,name):
    print ("making ROC curve")
    plt.plot(tpr,fpr, color='blue', lw=1, label='double-b-tag+Subjet CSVv2')
    #plt.plot([0, 1], [0, 1], '--', color='navy')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.001, 1])
    plt.xticks([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1])
    plt.ylabel(r'Mistagging Efficiency')
    plt.xlabel(r'Tagging Efficiency(${H \rightarrow b\bar b}$)')
    # plt.title(r'Receiver operating characteristic')
    plt.legend(loc="upper left")
    plt.grid()
    plt.yscale('log')
    plt.text(.1, 0.25, r'CA15',color='r')
    plt.text(.1, 0.15, r'50<m<200GeV, $p_{T}$ > 170 ')
    # fig = plt.figure()
    # ax = fig.add_subplot(111)
    # ax.text(2, 6, r'an equation: $E=mc^2$', fontsize=15)
    # ticks=[pow(10,i) for i in range(-3,1)]
    # plt.yticks(ticks,ticks)
    # plt.yticks([0.001,0.01,0.1,1])
    # plt.yscale('log')
    plt.savefig('roc_weight'+name+'.pdf')
    plt.savefig('roc_weight'+name+'.png')
    plt.clf()
    plt.cla()
    plt.close('all')



sample_bkg='bkg_QCD_Train.root'
sample_signal='MZp-2000_MA0-300_train_ptreweight.root'
selection='ptPruned > 170.0 & massPruned > 50 & massPruned < 200 & SubJet_csv_min > 0 & SubJet_csv_1 > 0 & SubJet_csv_2 > 0'

branch_names_sum=['flavour','nbHadrons','z_ratio','trackSipdSig_3','trackSipdSig_2','trackSipdSig_1','trackSipdSig_0','trackSipdSig_1_0','trackSipdSig_0_0','trackSipdSig_1_1','trackSipdSig_0_1','trackSip2dSigAboveCharm_0','trackSip2dSigAboveBottom_0','trackSip2dSigAboveBottom_1','tau0_trackEtaRel_0','tau0_trackEtaRel_1','tau0_trackEtaRel_2','tau1_trackEtaRel_0','tau1_trackEtaRel_1','tau1_trackEtaRel_2','tau_vertexMass_0','tau_vertexEnergyRatio_0','tau_vertexDeltaR_0','tau_flightDistance2dSig_0','tau_vertexMass_1','tau_vertexEnergyRatio_1','tau_flightDistance2dSig_1','jetNTracks','nSV']


branch_names_fn=['fn_csv','flavour','nbHadrons','z_ratio','trackSipdSig_3','trackSipdSig_2','trackSipdSig_1','trackSipdSig_0','trackSipdSig_1_0','trackSipdSig_0_0','trackSipdSig_1_1','trackSipdSig_0_1','trackSip2dSigAboveCharm_0','trackSip2dSigAboveBottom_0','trackSip2dSigAboveBottom_1','tau0_trackEtaRel_0','tau0_trackEtaRel_1','tau0_trackEtaRel_2','tau1_trackEtaRel_0','tau1_trackEtaRel_1','tau1_trackEtaRel_2','tau_vertexMass_0','tau_vertexEnergyRatio_0','tau_vertexDeltaR_0','tau_flightDistance2dSig_0','tau_vertexMass_1','tau_vertexEnergyRatio_1','tau_flightDistance2dSig_1','jetNTracks','nSV']

branch_names_min=['SubJet_csv_min','flavour','nbHadrons','z_ratio','trackSipdSig_3','trackSipdSig_2','trackSipdSig_1','trackSipdSig_0','trackSipdSig_1_0','trackSipdSig_0_0','trackSipdSig_1_1','trackSipdSig_0_1','trackSip2dSigAboveCharm_0','trackSip2dSigAboveBottom_0','trackSip2dSigAboveBottom_1','tau0_trackEtaRel_0','tau0_trackEtaRel_1','tau0_trackEtaRel_2','tau1_trackEtaRel_0','tau1_trackEtaRel_1','tau1_trackEtaRel_2','tau_vertexMass_0','tau_vertexEnergyRatio_0','tau_vertexDeltaR_0','tau_flightDistance2dSig_0','tau_vertexMass_1','tau_vertexEnergyRatio_1','tau_flightDistance2dSig_1','jetNTracks','nSV']
#fn_csv

tree="outTree"
#######################################################################################################
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
# from sklearn.ensemble import GradientBoostingClassifier
eff=[]
mistag=[]
name=['csvSum','csvWithFn','min_csv']
col=['blue','red','green']
# print (get_numpy_array(sample_bkg,tree,branch_names,selection))
branch=[branch_names_sum,branch_names_fn,branch_names_min]
for i in range(len(branch)):
    if i==0:
        fpr,tpr = train_sum(sample_signal,sample_bkg,tree,branch[i],selection)
        eff.append(tpr)
        mistag.append(fpr)
        roc_plot(fpr,tpr,name[i])
    else:
        fpr, tpr = train(sample_signal,sample_bkg,tree,branch[i],selection)
        eff.append(tpr)
        mistag.append(fpr)
        roc_plot(fpr,tpr,name[i])


for i in range(len(eff)):
    print ("making Full ROC curve")
    plt.plot(eff[i],mistag[i], color=col[i], lw=1, label='double-b-tag+Subjet'+name[i])

plt.xlim([0.0, 1.0])
plt.ylim([0.001, 1])
plt.xticks([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1])
plt.ylabel(r'Mistagging Efficiency')
plt.xlabel(r'Tagging Efficiency(${H \rightarrow b\bar b}$)')
# plt.title(r'Receiver operating characteristic')
plt.legend(loc="upper left")
plt.grid()
plt.yscale('log')
plt.text(.1, 0.25, r'CA15',color='r')
plt.text(.1, 0.15, r'50<m<200GeV, $p_{T}$ > 170 ')
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.text(2, 6, r'an equation: $E=mc^2$', fontsize=15)
# ticks=[pow(10,i) for i in range(-3,1)]
# plt.yticks(ticks,ticks)
# plt.yticks([0.001,0.01,0.1,1])
# plt.yscale('log')
plt.savefig('roc_weight_combined.pdf')
plt.savefig('roc_weight_combined.png')
plt.clf()
plt.cla()
plt.close('all')
