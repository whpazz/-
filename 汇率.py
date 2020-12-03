class Account(object):
    def __init__(self,rate):
        self.__amt=0
        self.rate=rate
     
     @property
     def amount(self):
         return self.__amt
      
     @property
     def inr(self):
     return self._amt *self.rate

     @amount.setter
     def amount(self,value):
         if value<0:
             print("Sorry,no negative amount in the account.")
             return
         self.__amt=value
if __name__=='__main__':
    acc=Account(rate=61)
    acc.amount=20
    print("Dollar amount:",acc.amount)
    print("In INR:",acc.inr)
    acc.amount=-100
    print("dollar amount:",acc.amount)

