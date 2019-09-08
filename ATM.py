# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 08:17:25 2019

@author: Ajayi Raymond T
"""
import random
class Account:
    #construct an accoun object
    def __init__(self,id,balance =0,annualinterestRate =3.4):
        self.id = id
        self.balance = balance
        self.annualinterestRate = annualinterestRate
        
    def getid(self):
        return self.id
    def getbalance(self):
        return self.balance
    def getannualinterestRate(self):
        return self.annualinterestRate
    def getmonthlyinterestRate(self):
        return self.monthlyinterestRate/12
    def withdraw(self,amount):
        self.balance -= amount
    def deposite(self,amount):
       self.balance += amount
    def getmonthlyinterest(self):
        return self.balance * self.getmonthlyinterestRate()
def main():
    #creating accounts
    accounts =[]
    for i in range (1000,9999):
        account = Account(i,0)
        accounts.append(account)
#ATM process
        while True:
            #reading id from user
            id = int(input('\n Enter account pin:'))
            #loop till id is valid
            while id <1000 or id >9999:
                id = int (input('\n invalid id...Re enter:'))
            #iterating over account session    
            while True:
                #print menu
                print('\n1-View Balance\t 2- Withdraw \t 3- Deposite\t 4-Exit')
                #reading selection
                selection = int(input('\n Enter your selection:'))
                #getting account obj
                
                for acc in accounts:
                    #comparing account id
                    if acc.getid()==id:
                        accountObj = acc
                        break
                    #view balance
                    if selection == 1:
                        #print balance
                        print(accountObj.getbalance())
                    #withdrawal
                    elif selection == 2:
                        amt = float(input('\nEnter amount to withdraw:'))
                        ver_withdraw = input('is this the correct amount,yes or no?'+ str(amt) + '')
                        if ver_withdraw == 'yes':
                            print('verify withdraw')
                        else:
                            break
                        if amt < accountObj.getbalance():
                            #calling withdraw method
                            accountObj.withdraw(amt)
                            #printing updated balance
                            print('\nUpdated balance:'+str(accountObj.getbalance()+'n'))
                            print('\nPlease make a deposite.');
                    elif selection == 3:
                        #reading amount
                        amt = float(input('\nEnter amount to deposit:'))
                        ver_deposite = input('is this the correct amount,yes or no?'+ str(amt) + '')
                        if ver_deposite == 'yes':
                            #calling deposite method
                            accountObj.deposite(amt)
                            #printing updated balance
                            print('\nUpdated balance:'+str(accountObj.getbalance()+'n'))
                        else:
                            break
                    elif selection == 4:
                        print('nTransaction is now complete.')
                        print('Transaction number:',random.randint(10000,1000000))
                        print('Current interest Rate:',accountObj.annualinterestRate)
                        print('Monthly Interest Rate:',accountObj.annualinterestRate/12)
                        print('Thanks for banking with us.')
                        exit()
                        #any other choice
                    else:
                        print('nThats an invalid choice')
                        #main function
main()
                             
                             
                         
            
            
    
    
    