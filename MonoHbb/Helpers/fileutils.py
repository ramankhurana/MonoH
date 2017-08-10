from ROOT import TFile 

## open a rootfile with given mode
def OpenRootFile(filename, mode='READ'): 
    f = TFile(filename, mode)
    return f



## open a text file with given mode 

