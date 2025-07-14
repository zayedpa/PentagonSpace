class farmer:
    def __init__(self,fname,floan,fperiod,frate):
        self.name=fname
        self.loan=floan
        self.period=fperiod
        self.rate=frate
    def interest(self):
        final=(self.loan*self.period*self.rate)/100
        print(final)
        
f1=farmer("rumaan",120000,3,2)
print(f1.name)
f1.interest()
f2=farmer("asgu",300000,5,3.0)
print(f2.name)
f2.interest()