import pandas as pd

class TAS2ndCrossData:
    #starttime = dt.datetime(2000, 1, 1)
    #endtime = dt.datetime(2017, 12, 31)
    #dataTS = web.DataReader('JPM', 'yahoo', starttime, endtime)
    #dataTS.to_csv('YHOO.csv')

    def __init__(self, Stock):
        #TS = pd.DataFrame()

        self.Stock = Stock

    def makeDf(self):
        text_for_CSV = self.Stock + '.csv'
        return pd.read_csv(text_for_CSV, parse_dates=True, index_col=0)



#TS = TAS2ndCrossData(my_dataframe)

        #self.TS_df = TS.copy()

        #TS.reset_index(inplace=True)
        #TS.to_csv('YHOO_backup.csv')
        #CloseP = TS['Adj Close']
        #TS[['Open', 'High', 'Low', 'Adj Close']].plot()
        #TS['Adj Close'].plot()
