class farmer:
    def __init__(self,fname,floan,fperiod,frate):
        self.name=fname
        self.loan=floan
        self.period=fperiod
        self.rate=frate
    def interest(self):
        final=(self.loan*self.period*self.rate)/100
        return final
        
f1=farmer("rumaan",120000,3,2)
print(f1.name)
res=f1.interest()
print(res)
f2=farmer("asgu",300000,5,3.0)
res2=f2.interest()
print(res2)