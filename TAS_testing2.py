from subprocess import Popen
import TAS2ndCross_indicators as inds

class marco_strat():
    def problem_Df_1(self):
        callmarco = inds.indicateurs()
        runmarco = callmarco.run_all()
        self.TS_marco = callmarco.make_DF()
        self.TS_marco['test extra column1'] = self.TS_marco['Close'] * self.TS_marco['Close']
        #self.TS_marco.to_csv('testing_testing_1.csv')

    def add_to_DF(self):
        self.TS_marco['test extra column2'] = self.TS_marco['test extra column1'] * self.TS_marco ['Close']
        self.TS_marco['test extra column3'] = self.TS_marco['test extra column1'] * self.TS_marco['test extra column2']

    def random_fct(self, column_2, column_1):
        if column_2 > column_1:
            random_fct_output = 1
            #return random_fct
        else:
            random_fct_output = 0
            #return random_fct
        self.TS_marco['random_TS'] = list(map(self.random_fct, self.TS_marco['test extra column2'], self.TS_marco['test extra column1']))
        self.TS_marco.to_csv('testing_testing_2.csv')
        Popen('testing_testing_2.csv', shell=True)

    def run_function(self):
        self.problem_Df_1()
        self.add_to_DF()
        self.random_fct(self.TS_marco['test extra column2'], self.TS_marco['test extra column1'])

aa = marco_strat()
ab = aa.run_function()



