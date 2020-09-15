# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 15:22:20 2019

@author: Ajayi Raymond T
"""

from tkinter import *
from winsound import Beep
all_clear = False

root = Tk()
root.title('ATM GUI')
root.geometry('600x700')

username_verify = StringVar()
password_verify = StringVar()
def LoginVerify():
    pass
xlab= Label(root,width='30').pack(side='right',fill=Y)
ylab= Label(root,width='30').pack(side='left',fill=Y)
lab = Label(root,text = 'Shugar\nATM',bg = '#7e5b41',fg ='#ff342f', font =('courier',20, 'bold'),height='2')
lab.pack(side='top',fill=BOTH)
lab3 = Label(root,bg='red',height='1')
lab3.pack(side='top',fill=BOTH)
lab1 = Label(root,bg='red',height='18')
lab1.pack(side='bottom',fill=BOTH)
lab3 = Label(root,bg='red',width='6')
lab3.pack(side='left',fill=BOTH)
lab2 = Label(root,bg='red',width='20')
lab2.pack(side='left',fill=BOTH)
back = Label(root,bg='navy blue',text = 'Welcome To\nShugar e-Banking',fg ='#ff342f',height='15',width='65')
back.pack(side='left')

'''   
Label(back,text = 'Username  * ', font =('courier',11, 'bold')).pack()
username_entry1 = Entry(back, textvariable = username_verify)
username_entry1.pack()
Label(back, text = 'Password *', font =('courier',11, 'bold')).pack()
password_entry1 = Entry(back, textvariable = password_verify, show = '*')
password_entry1.pack()
Label(back, text = '').pack()
Button(back,text = 'Login',height = '1', fg='navy blue', bg='#00ffff', width = '30', command = LoginVerify, font =('courier',10, 'bold')).pack()
'''
#can = Entry(root,bg='#656565',width ='80',justify='center',font = ('serif 15',8, 'bold'),relief=RAISED)
#can.pack(side='left')
lab6 = Label(root,bg='red',width='3')
lab6.pack(side='right',fill=BOTH)
lab4 = Label(root,bg='red',width='40')
lab4.pack(side='right',fill=BOTH)
lab5 = Label(root,bg='red',width='3')
lab5.pack(side='right',fill=BOTH)
lab3 = Label(root,bg='red',width='20')
lab3.pack(side='right',fill=BOTH)

def btn_sound():
    Beep(800,70)
    
def on_screen(display):
    global can,all_clear
    btn_sound()
    if all_clear == True:
        can.delete(0,"end")
        all_clear = False
    if can.get() == "0" and display != ".":
        can.delete(0,'end')
        can.insert(0,display)
    else:
        s_length = len(can.get())
        can.insert(s_length,display)
        
        
#Right hand Label
labi = Label(lab3,height = 1,bg= 'red')#green
labi.grid(row =0,column=0)
labii = Label(lab3,width = 2,bg= 'red')#green
labii.grid(row =2,column=0)
labiii = Label(lab3,width = 2,bg= 'red')#green
labiii.grid(row =1,column=2)
btni = Button(lab3,height = 3,relief= 'sunken',padx=2,width='12',bg = 'powder blue',command = lambda: btn_sound())
btni.grid(row = 1, column = 1)
btnii = Button(lab3,height = 3,relief= 'sunken',padx=2,width='12',bg = 'powder blue',command = lambda: btn_sound())
btnii.grid(row = 3, column = 1)
labiv = Label(lab3,height = 1,bg= 'red')#green
labiv.grid(row =4,column=1)
btniii= Button(lab3,height = 3,relief= 'sunken',padx=2,width='12',bg = 'powder blue',command = lambda: btn_sound())
btniii.grid(row = 5, column = 1)
labv = Label(lab3,height = 1,bg= 'red')#green
labv.grid(row =6,column=1)

#Right hand Label-2
labi = Label(lab4,height = 1,bg= 'red',width='10')
labi.grid(row =0,column=0)
labi = Label(lab4,height = 1,bg= 'red',width='10')
labi.grid(row =1,column=0)
labw = Label(lab4,height = 1,bg= 'white',width='10')
labw.grid(row =2,column=0)
btng = Button(labw,relief= 'sunken',padx=3,width = '10',bg='black')
btng.grid(row =0,column=0)
labi = Label(lab4,font=('courier',8, 'bold'),height = 1,bg= 'powder blue',text='Receipt',width='10')
labi.grid(row =3,column=0)
labi = Label(lab4,height = 1,bg= 'red',width='10')
labi.grid(row =4,column=0)
labw1 = Label(lab4,height = 1,bg= 'white',width='10')
labw1.grid(row =5,column=0)
btng = Button(labw1,relief= 'sunken',padx=3,width = '10',bg='black')
btng.grid(row =0,column=0)
labi = Label(lab4,height = 1,font=('courier',8, 'bold'),text='Insert Card',bg= 'powder blue',width='10')
labi.grid(row =6,column=0)
labi = Label(lab4,height = 1,bg= 'red',width='10')
labi.grid(row =7,column=0)
labw2 = Label(lab4,height = 1,bg= 'white',width='10')
labw2.grid(row =8,column=0)
btng = Button(labw2,relief= 'sunken',padx=3,width = '10',bg='black')
btng.grid(row =0,column=0)
labi = Label(lab4,height = 1,bg= 'powder blue',font=('courier',8, 'bold'),text='Deposit',width='10')
labi.grid(row =9,column=0)

#Left hand Label
labi = Label(lab2,height = 1,bg= 'red')#green
labi.grid(row =0,column=0)
labii = Label(lab2,width = 2,bg= 'red')#green
labii.grid(row =2,column=0)
labiii = Label(lab2,width = 2,bg= 'red')#green
labiii.grid(row =1,column=2)
btni = Button(lab2,height = 3,relief= 'sunken',padx=2,width='12',bg = 'powder blue',command = lambda: btn_sound())
btni.grid(row = 1, column = 1)
btnii = Button(lab2,height = 3,relief= 'sunken',padx=2,width='12',bg = 'powder blue',command = lambda: btn_sound())
btnii.grid(row = 3, column = 1)
labiv = Label(lab2,height = 1,bg= 'red')#green
labiv.grid(row =4,column=1)
btniii= Button(lab2,height = 3,relief= 'sunken',padx=2,width='12',bg = 'powder blue',command = lambda: btn_sound())
btniii.grid(row = 5, column = 1)
labv = Label(lab2,height = 1,bg= 'red')#green
labv.grid(row =6,column=1)

#Bottom Label
labi = Label(lab1,bg='red',height='1',width='70')#blue
labi.grid(row =0,column=1)
labi = Label(lab1,bg='red',height='1',width='22')#yellow
labi.grid(row =0,column=0)
labblk = Label(lab1,bg='red',height='1',width='100')#black
labblk.grid(row =0,column=3)
labe = Label(lab1,width='40',bg='white',height='1')
labe.grid(row=4,column=2)
btng = Button(labe,relief= 'sunken',padx=3,width = '15',bg='black')
btng.grid(row =0,column=0)
labi = Label(lab1,bg='red',height='1',width='5')#green
labi.grid(row =1,column=1)
laba = Label(lab1,bg='red',height='1',width='8')
laba.grid(row =2,column=1)
btna= Button(laba,height = 3,relief= 'sunken',padx=1,width='12',bg = 'powder blue', font =('courier',9, 'bold'),text='9', command = lambda: on_screen('9'))
btna.grid(row = 0, column = 0)
btnb= Button(laba,height = 3,relief= 'sunken',padx=1,width='12',bg = 'powder blue', font =('courier',9, 'bold'),text='8', command = lambda: on_screen('8'))
btnb.grid(row = 0, column = 1)
btnc= Button(laba,height = 3,relief= 'sunken',padx=1,width='12',bg = 'powder blue', font =('courier',9, 'bold'),text='7', command = lambda: on_screen('7'))
btnc.grid(row = 0, column = 2)
labi = Label(lab1,bg='red',height='1')
labi.grid(row =3,column=1)
labb = Label(lab1,bg='red',height='2')
labb.grid(row =4,column=1)
btnc= Button(labb,height = 3,relief= 'sunken',padx=1,width='12',bg = 'powder blue', font =('courier',9, 'bold'),text='6', command = lambda: on_screen('6'))
btnc.grid(row = 0, column =0)
btna= Button(labb,height = 3,relief= 'sunken',padx=1,width='12',bg = 'powder blue', font =('courier',9, 'bold'),text='5', command = lambda: on_screen('5'))
btna.grid(row = 0, column = 1)
btnb= Button(labb,height = 3,relief= 'sunken',padx=1,width='12',bg = 'powder blue', font =('courier',9, 'bold'),text='4', command = lambda: on_screen('4'))
btnb.grid(row = 0, column = 2)
labi = Label(lab1,bg='red',height='1')
labi.grid(row =5,column=1)
labc = Label(lab1,bg='red',height='2')
labc.grid(row =6,column=1)
btnc= Button(labc,height = 3,relief= 'sunken',padx=1,width='12',bg = 'powder blue', font =('courier',9, 'bold'),text='3', command = lambda: on_screen('3'))
btnc.grid(row = 0, column = 0)
btnc= Button(labc,height = 3,relief= 'sunken',padx=1,width='12',bg = 'powder blue', font =('courier',9, 'bold'),text='2', command = lambda: on_screen('2'))
btnc.grid(row = 0, column = 1)
btnc= Button(labc,height = 3,relief= 'sunken',padx=1,width='12',bg = 'powder blue', font =('courier',9, 'bold'),text='1', command = lambda: on_screen('1'))
btnc.grid(row = 0, column = 2)
labi = Label(lab1,bg='red',height='1')
labi.grid(row =7,column=1)
labf = Label(lab1,bg='red',height='1')
labf.grid(row =8,column=1)
btnc= Button(labf,height = 3,relief= 'sunken',padx=1,width='12',bg = 'powder blue', font =('courier',9, 'bold'),text='0', command = lambda: on_screen('0'))
btnc.grid(row = 0, column = 0)
btnc= Button(labf,height = 3,relief= 'sunken',padx=1,width='12',bg = 'powder blue', font =('courier',9, 'bold'),text='*', command = lambda: on_screen('*'))
btnc.grid(row = 0, column = 1)
btnc= Button(labf,height = 3,relief= 'sunken',padx=1,width='12',bg = 'powder blue', font =('courier',9, 'bold'),text='#', command = lambda: on_screen('#'))
btnc.grid(row = 0, column = 2)
labi = Label(lab1,bg='red',height='1')
labi.grid(row =9,column=1)
root.mainloop()