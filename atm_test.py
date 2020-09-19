# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 10:34:29 2019
#lol
@author: Ajayi Raymond T

"""
import mysql.connector
import sys

balance=[0.0]
amount = []
mycon = mysql.connector.connect(host='localhost',user= 'root',password='',database='atm_db')
mycursor= mycon.cursor()
#==================================================================================================================
#create table
#mycursor.execute('CREATE TABLE accounts (reg_id INT(4), Deposit INT(60), withdraw INT(60), Balance INT(60))')
#mycursor.execute('CREATE TABLE account (reg_id INT(4), Amount INT(60), Deposit INT(60))')
#mycon.commit()
#mycursor.execute('CREATE TABLE registration (reg_id INT(4), username VARCHAR(60), password VARCHAR(60))')
#mycon.commit()
#drop table
#mycursor.execute('DROP TABLE account')
#mycon.commit()
#creating database
#mycon = mysql.connector.connect(host='localhost',user= 'root',password='')
#mycursor= mycon.cursor()
#mycursor.execute('CREATE DATABASE atm_db')
#mycursor.execute('ALTER TABLE registration ADD Deposit INT(60)')
#mycon.commit()
#====================================================================================================
print('CREATE ACCOUNT')
acc_name = input('Enter your preferred accountName:')
pin = input('Enter your preferred 4-digit pin:')

sql = 'INSERT INTO registration(username,password) VALUES(%s,%s)'
val = (acc_name,pin)
mycursor.execute(sql,val)
mycon.commit()
print(mycursor.rowcount,'Record Inserted successfully')

#------------------------------------------------------------------------------
def viewbalance():
   print('NGN'+str(balance[0]))
   endprocess()
def withdraw():
    global balance
    print('\n1- 500\t 2- 1000 \t 3- 10000\t 4- 20000')
    choice = (input('\n Enter your choice:'))
    if int(choice ) >= balance[0]:
        print('Insufficient Balance')
    else:
        Withdraw = balance[0] - int(choice)
        balance.insert(0,Withdraw)
        print ('Your balance is:',balance[0])
        print('Transaction successful')
    
    endprocess()
        
def deposit():
    global balance
    amount = (input('Enter amount to deposit:'))
    deposit = balance[0] + int(amount)
    balance.insert(0,deposit)
    print('your balance is:',balance[0])
    print('Transaction successful')
    endprocess()
    
def Quick_Teller():
     print('\n1-Airtime Recharge\t 2- Cable Subscription \t 3-PHCN')
     option = int(input('\n Enter your choice:'))
     if option == 1:
        print(Airtime())
     elif option == 2:
        print(Cable_Subscription())
     else:
        print(PHCN())
     endprocess()
#-----------------------------------------------------------------------------------------------------------
def Airtime():
    print('Choose Service Provider:')
    print('\n1-MTN\t 2-GLO \t 3-AIRTEL\t 4-ETISALAT')
    user_choice=int(input('\n Enter your choice:'))
    if user_choice == 1:
        print('Thank you for choosing MTN')
    elif user_choice == 2:
        print('Thank you for choosing GLO')
    elif user_choice == 3:
        print('Thank you for choosing AIRTEL')
    else:
        print('Thank you for choosing ETISALAT')
    endprocess()
def Cable_Subscription():
     print('Choose Cable Subscription:')
     print('\n1-DSTV\t 2-Go-TV \t 3-STARTIMES\t 4-My TV')
     user_choice=int(input('\n Enter your choice:'))
     if user_choice == 1:
         print('Thank you for choosing DSTV')
     elif user_choice == 2:
         print('Thank you for choosing Go-TV')
     elif user_choice == 3:
         print('Thank you for choosing STARTIMES')
     else:
         print('Thank you for choosing My TV')
     endprocess()
def PHCN():
    input_ref = input('\n Enter reference Identification:')
    print('Loading...')
    endprocess()
#----------------------------------------------------------------------------------------------------
def acc_login():
    global acc_name
    print('LOGIN')
    pinVerify = input('Enter pin:')
    
    sql = 'SELECT * FROM registration WHERE password = %s'
    adr = (pinVerify,)
    mycursor.execute(sql,adr)
   
    result = mycursor.fetchone()
    
    #if len(result) > 0:
    
    if pinVerify == result[2]:#['password']:
            print('check confirmed')
            print('WELCOME ',acc_name,'TO SHUGAR E-BANKING SYSTEM')
            main_program()
            
    else:
              print('Incorrect Pin')
            
    #else:
        #print(' UserNotFound')
    '''
    if pinVerify == pin:
        #print('check confirmed')
        print('WELCOME ',acc_name,'TO SHUGAR E-BANKING SYSTEM')
        main_program()
    else:
        print('Incorrect Pin')
     '''   
def main_program():
    print('\n1-View Balance\t 2- Withdraw \t 3- Deposit\t 4-Pay Bills')
    select_options ={
	  '1':viewbalance,
	  '2':withdraw,
	  '3':deposit,
	  '4':Quick_Teller}
	selection = int(input('\n Enter your selection:'))
	if select_options.get(selection):
	   select_options[selection]()
	else:
		sys.exit()
def endprocess():
    print ('Do you want to continue process? \n1-Yes \t 2-No ')
    process = int(input('Enter:'))
    if process == 1:
        print(acc_login())
    else:
        print('Thank You for Banking with Us.')
 #-----------------------------------------------------------------------------------------------------------------               
acc_login()
endprocess()
