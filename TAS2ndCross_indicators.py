from TAS2ndCross_data import TAS2ndCrossData
from subprocess import Popen

class indicateurs():

    df = TAS2ndCrossData('YHOO')
    
    TS = df.makeDf()


    def marco_MA(self):
        ### MOVING AVERAGES ###
        self.TS['MA10'] = self.TS['Adj Close'].rolling(window=10, min_periods=None).mean()
        self.TS['MA100'] = self.TS['Adj Close'].rolling(window=100, min_periods=None).mean()
        self.TS['MA200'] = self.TS['Adj Close'].rolling(window=200, min_periods=None).mean()

        self.TS['MAVolume10'] = self.TS['Volume'].rolling(window=10, min_periods=None).mean()
        self.TS['MAVolume100'] = self.TS['Volume'].rolling(window=100, min_periods=None).mean()
    
    
    
    def marco_RSI(self):
        ### RSI ###
        RSI_period = 14
    
        RSI_price_chg = self.TS['Adj Close'] - self.TS['Adj Close'].shift(1)
        self.TS['RSI_price_chg'] = RSI_price_chg
        #self.TS_df['RSI_price_chg'] = RSI_price_chg
    
    
        def RSI_Gain(RSI_price_chg):
            if RSI_price_chg > 0:
                return RSI_price_chg
            else:
                return 0
    
    
        def RSI_Loss(RSI_price_chg):
            if RSI_price_chg < 0:
                return RSI_price_chg * -1
            else:
                return 0
    

        self.TS['RSI_Gain'] = list(map(RSI_Gain(RSI_price_chg), self.TS['RSI_price_chg']))
        self.TS['RSI_Loss'] = list(map(RSI_Loss(RSI_price_chg), self.TS['RSI_price_chg']))
        self.TS['Avg_RSI_Gain'] = self.TS['RSI_Gain'].rolling(window=RSI_period, min_periods=None).mean()
        self.TS['Avg_RSI_Loss'] = self.TS['RSI_Loss'].rolling(window=RSI_period, min_periods=None).mean()
        self.TS['RS'] = self.TS['Avg_RSI_Gain'] / self.TS['Avg_RSI_Loss']
        self.TS['RSI'] = 100 - (100 / (1 + self.TS['RS']))
    
    

    def marco_MACD(self):
        ### MACD ###
        self.TS['MACD_ST'] = self.TS['Adj Close'].ewm(com=12, min_periods=0, adjust=True, ignore_na=False).mean()
        self.TS['MACD_LT'] = self.TS['Adj Close'].ewm(com=26, min_periods=0, adjust=True, ignore_na=False).mean()
        self.TS['MACD'] = self.TS['MACD_ST'] - self.TS['MACD_LT']
        self.TS['MACD_signal'] = self.TS['MACD'].rolling(window=9, min_periods=None).mean()
    
    
        def MACD_trigger(MACD, MACD_signal):
            if MACD > MACD_signal:
                return 1
            else:
                return 0
    
        def MACD_triggger(self):
            self.TS['MACD_trigger'] = list(map(self.MACD_trigger, self.TS['MACD'], self.TS['MACD_signal']))
            #return self.TS
    
    
    
    def marco_TAS_LT(self):
    
        ### STOCHASTICS ###
        TasST_nbr_of_days = 28
        TasLT_nbr_of_days = 6

    
        Lowest_low = self.TS['Low'].rolling(window=TasST_nbr_of_days, min_periods=None).min()
        Highest_high = self.TS['High'].rolling(window=TasST_nbr_of_days, min_periods=None).max()
    
        TasST_LT = ((self.TS['Close'] - Lowest_low) / (Highest_high - Lowest_low)) * 100
        TasLT_LT = TasST_LT.rolling(window=TasLT_nbr_of_days, min_periods=None).mean()
    
        # TasST = np.float64(TasST)
        # TasLT = np.float64(TasLT)
    
        self.TS['TasST_LT'] = TasST_LT
        self.TS['TasLT_LT'] = TasLT_LT




    def run_all(self):
        #self.marco_RSI()
        self.marco_MA()
        self.marco_MACD()
        self.marco_TAS_LT()
        return self.TS


    def make_DF(self):
        TS_df = self.TS.copy()
        return TS_df


    def make_CSV(self):
        Marco_df_indic = self.TS.copy()
        Marco_df_indic.to_csv('Marco_df_indic.csv')
        Popen('Marco_df_indic.csv', shell=True)
        return Marco_df_indic


#indic_call_class = indicateurs()
#indic_call_class.run_all()
#indic_call_class.make_DF()
#indic_call_class.make_CSV()

