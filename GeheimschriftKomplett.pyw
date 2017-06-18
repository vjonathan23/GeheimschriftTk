#!/usr/bin/python3
from tkinter import *
import os

def Bild():
    command = "python3 BildSteganographie.py"
    os.system(command)
def Ca():
    command = "python3 CaesarTk.py"
    os.system(command)
def En():
    command = "python3 RotorTest2.py"
    os.system(command)
def Vi():
    command = "python3 VigenereTk.py"
    os.system(command)
def RSA():
    command = "python3 RSATk.py"
    os.system(command)

window = Tk()
window.title("Geheimschriften")

Bildb = Button(master=window,text="Bild-Steganographie",
              width=15,font = ("Arial", 12), command=Bild)
Cab = Button(master=window,text="Caesarchiffre",
              width=15,font = ("Arial", 12), command=Ca)
Enb = Button(master=window,text="Enigma",
              width=15,font = ("Arial", 12), command=En)
Vib = Button(master=window,text="Vigenere",
              width=15,font = ("Arial", 12), command=Vi)
RSAb = Button(master=window,text="RSA",
              width=15,font = ("Arial", 12), command=RSA)

Bildb.grid(column=0,row=0)
Cab.grid(column=1,row=0)
Enb.grid(column=2,row=0)
Vib.grid(column=0,row=1)
RSAb.grid(column=1,row=1)

window.mainloop()
