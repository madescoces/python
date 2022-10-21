import re 

class Regulares():
    txt= reg= ""
    def __init__(self, reg_, txt_):
        self.txt= txt_
        self.reg= reg_

    def printAllReg(self):
        return print(re.findall(self.reg,self.txt))

    def printReg(self):
        return print(re.match(self.reg,self.txt))


texto = """ 98.140.180.244 - harber4797 [21/Jun/2019:16:01:53 -0700] "POST /seize/b2b/synergistic HTTP/2.0" 203 9396
229.231.201.185 - - [21/Jun/2019:16:01:35 -0700] "HEAD /supply-chains/brand/strategic HTTP/1.1" 405 28109
197.150.196.204 - thiel4558 [21/Jun/2019:16:01:05 -0700] "PATCH /compelling HTTP/2.0" 500 14180 """
exp = r'[A-Z]{1,}\s\/*.*\d\.\d'

regex = Regulares(exp,texto)
regex.printAllReg()