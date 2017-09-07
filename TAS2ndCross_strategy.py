#####################
######  NOTES  ######
#####################

#    TS['TAS_signal_prepa0'] = list(map(TAS_signal_prepa_STinfLT, TasST, TasLT))
#    TS['TAS_signal_STinfLT'] = TS['TAS_signal_prepa0'].shift(1)

#    TS['TAS_signal_prepa_sup'] = list(map(TAS_signal_prepa_STsupLT, TasST, TasLT))
#    TS['TAS_signal_STsupLT'] = TS['TAS_signal_prepa_sup'].shift(1)

#    TS['TasST_prev'] = TS['TasST'].shift(1)
#    TS['TasLT_prev'] = TS['TasLT'].shift(1)

#    TS['PriceRelEntry'] = (TS['Adj Close'] / TS['Price_entry'])




#from TAS2ndCross_data import TAS2ndCrossData
from subprocess import Popen
import TAS2ndCross_indicators as indics


class marco_strategy():
#class marco_strat(indics_launch_class.make_DF()):
    #import TAS2ndCross_indicators as indics

    def get_data_from_indicators(self):
        indics_launch_class = indics.indicateurs()
        indics_launch_run = indics_launch_class.run_all()
        indics_launch_df = indics_launch_class.make_DF()
        #indics_launch_makecsv = indics_launch_class.make_CSV()
        self.TS = indics_launch_run



    ### STOCHASTICS ###
    #def marco_TAS(self):
        #TasST_nbr_of_days = 14
        #TasLT_nbr_of_days = 3

        #Lowest_low = self.TS['Low'].rolling(window=TasST_nbr_of_days, min_periods=None).min()
        #Highest_high = self.TS['High'].rolling(window=TasST_nbr_of_days, min_periods=None).max()

        #TasST = ((self.TS['Close'] - Lowest_low) / (Highest_high - Lowest_low)) * 100
        #TasLT = TasST.rolling(window=TasLT_nbr_of_days, min_periods=None).mean()

        #self.TS['TasST'] = TasST
        #self.TS['TasLT'] = TasLT


    def TAS_signal_prepa_STinfLT(self, TasST, TasLT):
        if TasST < TasLT:
            return 1
        else:
            return 0


#    def TAS_signal_STinfLT(self):
#        TAS_signal_STinfLT = TAS_signal_prepa_STinfLT(TasST, TasLT).shift(1)
#        return TAS_signal_STinfLT

        #TS['TAS_signal_prepa_inf'] = list(map(self.TAS_signal_prepa_STinfLT, TasST, TasLT))
        #self.TS['TAS_signal_STinfLT'] = self.TS['TAS_signal_prepa_inf'].shift(1)


    def TAS_signal_prepa_STsupLT(self, TasST, TasLT):
        if TasST > TasLT:
            return 1
        else:
            return 0

        #self.TS['TAS_signal_prepa_sup'] = list(map(TAS_signal_prepa_STsupLT, TasST, TasLT))
        #self.TS['TAS_signal_STsupLT'] = self.TS['TAS_signal_prepa_sup'].shift(1)

        #self.TS['TasST_prev'] = self.TS['TasST'].shift(1)
        #self.TS['TasLT_prev'] = self.TS['TasLT'].shift(1)


    def TAS_cross_pos(self, TAS_signal_STinfLT, TasST, TasLT):
        if (TAS_signal_STinfLT == 1) and (TasST > TasLT):
            return 1
        else:
            return 0

            #self.TS['cross_pos'] = list(map(self.TAS_cross_pos, TAS_signal_STinfLT, TasST, TasLT))
            #self.TS['cross_pos'] = list(map(TAS_cross_pos, self.TS['TAS_signal_STinfLT'], self.TS['TasST'], self.TS['TasLT']))


    def TAS_cross_neg(self, TAS_signal_STsupLT, TasST, TasLT):
        if (TAS_signal_STsupLT == 1) and (TasST < TasLT):
            return 1
        else:
            return 0

        #self.TS['cross_neg'] = list(map(TAS_cross_neg, self.TS['TAS_signal_STsupLT'], self.TS['TasST'], self.TS['TasLT']))



    ### TAS_signal_0 ###
    def TAS_signal_0(self, TasST, TasLT, prepa,Level_TAS_signal_0):
        Level_TAS_signal_0 = 30
        if TasST < Level_TAS_signal_0 and TasST > TasLT and prepa == 1:
            return 1
        else:
            return 0

    ##############################################
        #self.TS['TAS_signal_0'] = list(map(TAS_signal_0, TasST, TasLT, self.TS['TAS_signal_STinfLT']))



    ### TAS_nbr_days_since_TAS_signal_0 ###
    NbrOfDays0 = 0

    def TAS_nbr_days_since_TAS_signal_0(self, trigger0, NbrOfDays0):
    #    global NbrOfDays0
        if trigger0 == 1:
            NbrOfDays0 = 0
            return NbrOfDays0
        else:
            NbrOfDays0 += 1
            return NbrOfDays0

#################### !!!!!!!  #################
        #TS['TAS_nbr_days_since_TAS_signal_0'] = list(map(TAS_nbr_days_since_TAS_signal_0, self.TS['TAS_signal_0'], 0))



    ### TAS_signal_1 ###
    def TAS_signal_1(self, TasST_signal1, TasST_prev, TasST, TasLT, prepa_signal1):
        TasST_signal1 = 50
        if (TasST_prev >= TasST_signal1) \
                and (TasST < TasLT) \
                and (prepa_signal1 == 1):
            return 1
        else:
            return 0

        #self.TS['TAS_signal_1'] = list(map(TAS_signal_1, self.TS['TasST_prev'], self.TS['TasST'], self.TS['TasLT'], self.TS['TAS_signal_STsupLT']))



    ### TAS_nbr_days_since_TAS_signal_1 ###
    def TAS_nbr_days_since_TAS_signal_1(self, NbrOfDays1, trigger1):
        NbrOfDays1 = 0
        if trigger1 == 1:
            NbrOfDays1 = 0
            return NbrOfDays1
        else:
            NbrOfDays1 += 1
            return NbrOfDays1

        #self.TS['TAS_nbr_days_since_TAS_signal_1'] = list(map(TAS_nbr_days_since_TAS_signal_1, self.TS['TAS_signal_1']))



    ### TAS_signal_cross ###
    def TAS_signal_cross(self, NbrOfDays_trigger0, NbrOfDays_trigger1, TAS_nbr_days_since_TAS_signal_0, TAS_nbr_days_since_TAS_signal_1, TasST, TasLT,
                         TAS_signal_STinfLT):
        NbrOfDays_trigger0 = 51
        NbrOfDays_trigger1 = 21

        if (TAS_nbr_days_since_TAS_signal_0 <= NbrOfDays_trigger0) \
                and (TAS_nbr_days_since_TAS_signal_1 <= NbrOfDays_trigger1) \
                and (TasST > TasLT) \
                and (TAS_signal_STinfLT == 1):
            return 1
        else:
            return 0


        #self.TS['TAS_signal_cross'] = list(map(TAS_signal_cross, self.TS['TAS_nbr_days_since_TAS_signal_0'], self.TS['TAS_nbr_days_since_TAS_signal_1'],
        #    self.TS['TasST'], self.TS['TasLT'], self.TS['TAS_signal_STinfLT']))



    ### TAS_nbr_days_since_TAS_signal_cross ###
    def TAS_nbr_days_since_TAS_signal_cross(self, NbrOfDaysCross, TriggerCross):
        NbrOfDaysCross = 0
        if TriggerCross == 1:
            NbrOfDaysCross = 0
            return NbrOfDaysCross
        else:
            NbrOfDaysCross += 1
            return NbrOfDaysCross

        #self.TS['TAS_nbr_days_since_TAS_signal_cross'] = list(map(TAS_nbr_days_since_TAS_signal_cross, self.TS['TAS_signal_cross']))



    ### TAS_signal_NbrOfPosCross ###
    def TAS_signal_NbrOfPosCross(self, CountCrossPos, cross_pos):
        CountCrossPos = 0
        if cross_pos == 1:
            CountCrossPos += 1
            return CountCrossPos
        else:
            return CountCrossPos

        #self.TS['TAS_signal_NbrOfPosCross'] = list(map(TAS_signal_NbrOfPosCross, self.TS['cross_pos']))



    ### TAS_signal_NbrOfNegCross ###
    def TAS_signal_NbrOfNegCross(self, CountCrossNeg, cross_neg, TAS_signal_0):
        CountCrossNeg = 0
        if cross_neg == 1:
            CountCrossNeg += 1
            return CountCrossNeg
        elif TAS_signal_0 == 1:
            CountCrossNeg = 0
            return CountCrossNeg
        else:
            return CountCrossNeg

        #self.TS['TAS_signal_NbrOfNegCross'] = list(map(TAS_signal_NbrOfNegCross, self.TS['cross_neg'], self.TS['TAS_signal_0']))



    def make_time_series(self):
        TasST_nbr_of_days = 14
        TasLT_nbr_of_days = 3


        Lowest_low = self.TS['Low'].rolling(window=TasST_nbr_of_days, min_periods=None).min()
        Highest_high = self.TS['High'].rolling(window=TasST_nbr_of_days, min_periods=None).max()
        TasST = ((self.TS['Close'] - Lowest_low) / (Highest_high - Lowest_low)) * 100
        TasLT = TasST.rolling(window=TasLT_nbr_of_days, min_periods=None).mean()

        self.TS['TasST'] = TasST
        self.TS['TasLT'] = TasLT

        self.TS['TAS_signal_prepa_inf'] = list(map(self.TAS_signal_prepa_STinfLT, TasST, TasLT))
        self.TS['TAS_signal_STinfLT'] = self.TS['TAS_signal_prepa_inf'].shift(1)

        self.TS['TAS_signal_prepa_sup'] = list(map(self.TAS_signal_prepa_STsupLT, TasST, TasLT))
        self.TS['TAS_signal_STsupLT'] = self.TS['TAS_signal_prepa_sup'].shift(1)

        self.TS['TasST_prev'] = self.TS['TasST'].shift(1)
        self.TS['TasLT_prev'] = self.TS['TasLT'].shift(1)

        self.TS['cross_pos'] = list(map(self.TAS_cross_pos, self.TS['TAS_signal_STinfLT'], self.TS['TasST'], self.TS['TasLT']))

        self.TS['cross_neg'] = list(map(self.TAS_cross_neg, self.TS['TAS_signal_STsupLT'], self.TS['TasST'], self.TS['TasLT']))

        self.TS['TAS_signal_0'] = list(map(self.TAS_signal_0, TasST, TasLT, self.TS['TAS_signal_STinfLT']))

        self.TS['TAS_nbr_days_since_TAS_signal_0'] = list(map(TAS_nbr_days_since_TAS_signal_0, self.TS['TAS_signal_0'], 0))

        self.TS['TAS_signal_1'] = list(map(TAS_signal_1, self.TS['TasST_prev'], self.TS['TasST'], self.TS['TasLT'], self.TS['TAS_signal_STsupLT']))

        self.TS['TAS_nbr_days_since_TAS_signal_1'] = list(map(TAS_nbr_days_since_TAS_signal_1, self.TS['TAS_signal_1']))

        self.TS['TAS_signal_cross'] = list(map(TAS_signal_cross, self.TS['TAS_nbr_days_since_TAS_signal_0'], self.TS['TAS_nbr_days_since_TAS_signal_1'],
        self.TS['TasST'], self.TS['TasLT'], self.TS['TAS_signal_STinfLT']))

        self.TS['TAS_nbr_days_since_TAS_signal_cross'] = list(map(TAS_nbr_days_since_TAS_signal_cross, self.TS['TAS_signal_cross']))

        self.TS['TAS_signal_NbrOfPosCross'] = list(map(TAS_signal_NbrOfPosCross, self.TS['cross_pos']))

        self.TS['TAS_signal_NbrOfNegCross'] = list(map(TAS_signal_NbrOfNegCross, self.TS['cross_neg'], self.TS['TAS_signal_0']))







### Data and CSV ###
    def strategy_data_handling(self):
        self.TS.to_csv('Strategy_in_CSV.csv')
        Popen('Strategy_in_CSV.csv', shell=True)



    def strat_run_all(self):
        self.get_data_from_indicators()
        #self.marco_TAS()
        self.TAS_signal_prepa_STinfLT(self.TS['TasST'], self.TS['TasLT'])
        self.TAS_signal_prepa_STsupLT(self.TS['TasST'], self.TS['TasLT'])
        self.TAS_cross_pos()
        self.TAS_cross_neg()
        self.TAS_signal_0()
        self.TAS_nbr_days_since_TAS_signal_0()
        self.TAS_signal_1()
        self.TAS_nbr_days_since_TAS_signal_1()
        self.TAS_signal_cross()
        self.TAS_nbr_days_since_TAS_signal_cross()
        self.TAS_signal_NbrOfPosCross()
        self.TAS_signal_NbrOfNegCross()
        self.strategy_data_handling()

aa = marco_strategy()
aa.strat_run_all()

