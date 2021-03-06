from ROOT import TFile, TTree, TH1F, TH1D, TH1, TCanvas, TChain,TGraphAsymmErrors, TMath, TH2D, TH2F
import ROOT as ROOT
class MonoHbbQuantities:

    def __init__(self, rootfilename):
        self.rootfilename = rootfilename
        #self.allquantities = allquantities
        self.regime   =  True
        
        self.met      =  -999.0
        self.h_met         =  []
        #self.h_met_rebin         =  []
        
        self.mass     =  -999.0
        self.h_mass        =  []
        
        self.csv1     =  -999.0
        self.h_csv1        =  []
        
        self.csv2     =  -999.0
        self.h_csv2        =  []
        
        self.mt              = -999.
        self.dPhi            = -999.
        self.N_e             = -10
        self.N_mu            = -10
        self.N_tau           = -10
        self.N_Pho           = -10
        self.N_b             = -10
        self.N_j             = -10
        self.mass            = -999.
        self.HiggsPt         = -999.
        self.HiggsEta        = -999.
        self.HiggsPhi        = -999.


        self.h_mt              = []
        self.h_dPhi            = []
        self.h_N_e             = []
        self.h_N_mu            = []
        self.h_N_tau           = []
        self.h_N_Pho           = []
        self.h_N_b             = []
        self.h_N_j             = []
        self.h_mass            = []
        self.h_HiggsPt         = []
        self.h_HiggsEta        = []
        self.h_HiggsPhi        = []
        self.h_met_pdf         = []
        self.h_met_muR         = []
        self.h_met_muF         = []
        
        ## 2d histograms 
        self.h_met_vs_mass     = []
        
        self.weight   = 1.0 

        self.weight_pdf   = []
        self.weight_muR   = []
        self.weight_muF   = []

        self.h_total   = []
        self.h_total_weight   = []
        
    def defineHisto(self):
        self.h_total.append(TH1F('h_total','h_total',4,0,4))
        self.h_total_weight.append(TH1F('h_total_weight','h_total_weight',4,0,4))
        
        for iregime in range(2):
            postname = str(iregime)
            self.h_met.append(TH1F('h_met_'+postname,  'h_met_'+postname,  1000,0.,1000.))
            
            
            #metbins_ = [200,350,500,1000]
            #self.h_met_rebin.append(TH1F('h_met_rebin_'+postname,  'h_met_rebin'+postname,  3, array(('d'),metbins_)))
            
            self.h_mass.append(TH1F('h_mass_'+postname, 'h_mass_'+postname, 400,0.,400.))
            
            self.h_met_vs_mass.append(TH2F('h_met_vs_mass_'+postname, 'h_met_vs_mass_'+postname, 1000, 0., 1000., 250, 0, 250.))

            self.h_csv1.append(TH1F('h_csv1_'+postname, 'h_csv1_'+postname, 20,0.,1.))
            self.h_csv2.append(TH1F('h_csv2_'+postname, 'h_csv2_'+postname, 20,0.,1.))
            self.h_mt.append(TH1F('h_mt_'+postname,'h_mt_'+postname,100,400.,1400.))
            self.h_dPhi.append(TH1F('h_dPhi_'+postname,'h_dPhi_'+postname,70, -3.5, 3.5 ))
            self.h_N_e.append(TH1F('h_N_e_'+postname,'h_N_e_'+postname,3,0,3))
            self.h_N_mu.append(TH1F('h_N_mu_'+postname,'h_N_mu_'+postname,3,0,3))
            self.h_N_tau.append(TH1F('h_N_tau_'+postname,'h_N_tau_'+postname,3,0,3))
            self.h_N_Pho.append(TH1F('h_N_Pho_'+postname,'h_N_Pho_'+postname,3,0,3))
            self.h_N_b.append(TH1F('h_N_b_'+postname,'h_N_b_'+postname,3,0,3))
            self.h_N_j.append(TH1F('h_N_j_'+postname,'h_N_j_'+postname,5,0,5))
            self.h_HiggsPt.append(TH1F('h_HiggsPt_'+postname,'h_HiggsPt_'+postname,1000,0.,1000.))
            self.h_HiggsEta.append(TH1F('h_HiggsEta_'+postname,'h_HiggsEta_'+postname,70, -3.5, 3.5))
            self.h_HiggsPhi.append(TH1F('h_HiggsPhi_'+postname,'h_HiggsPhi_'+postname,70, -3.5, 3.5))
            h_met_pdf_tmp = []
            for ipdf in range(101):
                midname = str(ipdf)
                h_met_pdf_tmp.append(TH1F('h_met_pdf'+'_'+midname+'_'+postname,  'h_met_pdf'+postname,  1000,0.,1000.))
            self.h_met_pdf.append(h_met_pdf_tmp)
            h_met_muR_tmp = []
            for imuR in range(2):
                midname = str(imuR)
                h_met_muR_tmp.append(TH1F('h_met_muR'+'_'+midname+'_'+postname,  'h_met_muR'+postname,  1000,0.,1000.))
            self.h_met_muR.append(h_met_muR_tmp)
            h_met_muF_tmp = []
            for imuF in range(2):
                midname = str(imuF)
                h_met_muF_tmp.append(TH1F('h_met_muF'+'_'+midname+'_'+postname,  'h_met_muF'+postname,  1000,0.,1000.))
            self.h_met_muF.append(h_met_muF_tmp)
                
        print "histo defined"
        
    def FillHisto(self):
        type_ = -1
        if self.regime: type_ = 0
        if not self.regime: type_ = 1
        WF = self.weight
        #print "WF = ", WF
        self.h_met        [type_].Fill(self.met,       WF)
        
        
        for ipdf in range(101):
            self.h_met_pdf        [type_][ipdf].Fill(self.met,       1.0)

        for imuR in range(2):
            self.h_met_muR        [type_][imuR].Fill(self.met,       1.0)
            
        for imuF in range(2):
            self.h_met_muF        [type_][imuF].Fill(self.met,       1.0)
        

        self.h_met_vs_mass [type_].Fill(self.met, self.mass, WF)

        self.h_mass       [type_].Fill(self.mass,      WF)
        self.h_csv1       [type_].Fill(self.csv1,      WF)
        self.h_csv2       [type_].Fill(self.csv2,      WF)
        self.h_mt         [type_].Fill(self.mt,        WF)
        self.h_dPhi       [type_].Fill(self.dPhi,      WF)
        self.h_N_e        [type_].Fill(self.N_e,       WF)
        self.h_N_mu       [type_].Fill(self.N_mu,      WF)
        self.h_N_tau      [type_].Fill(self.N_tau,     WF)
        self.h_N_Pho      [type_].Fill(self.N_Pho,     WF)
        self.h_N_b        [type_].Fill(self.N_b,       WF)
        self.h_N_j        [type_].Fill(self.N_j,       WF)
        self.h_HiggsPt    [type_].Fill(self.HiggsPt,   WF)
        self.h_HiggsEta   [type_].Fill(self.HiggsEta,  WF)
        self.h_HiggsPhi   [type_].Fill(self.HiggsPhi,  WF)
        
    def WriteHisto(self, (nevts,nevts_weight)):
        f = TFile(self.rootfilename,'RECREATE')
        f.cd()
        self.h_total[0].SetBinContent(1,nevts)
        self.h_total[0].Write()
        
        self.h_total_weight[0].SetBinContent(1,nevts_weight)
        self.h_total_weight[0].Write()
        
        for iregime in range(2):
            self.h_met[iregime].Write()
            #self.h_met_rebin[iregime].Write()
            for ipdf in range(101):
                self.h_met_pdf[iregime][ipdf].Write()
            for imuR in range(2):
                self.h_met_muR[iregime][imuR].Write()
            for imuF in range(2):
                self.h_met_muF[iregime][imuF].Write()

            self.h_met_vs_mass[iregime].Write()

            self.h_mass[iregime].Write()
            self.h_csv1[iregime].Write()
            self.h_csv2[iregime].Write()
            self.h_mt[iregime].Write()
            self.h_dPhi[iregime].Write()
            self.h_N_e[iregime].Write()
            self.h_N_mu[iregime].Write()
            self.h_N_tau[iregime].Write()
            self.h_N_Pho[iregime].Write()
            self.h_N_b[iregime].Write()
            self.h_N_j[iregime].Write()
            self.h_mass[iregime].Write()
            self.h_HiggsPt[iregime].Write()
            self.h_HiggsEta[iregime].Write()
            self.h_HiggsPhi[iregime].Write()
