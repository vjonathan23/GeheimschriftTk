from tkinter import *
import RSAKeyFinderTk

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "

def Potenz(x, h, n):
    # x = Zahl
    # h = Exponent (Hochzahl)
    # n = modulo-Zahl
    # Mod[ x ^ h, n ]

    b = bin(h)
    b = str(b)[2:]
    #print(b)
    l = list(b)
    l.reverse()
    #print(l)
    e = 1
    f = x
    for i in l:
        if i == "1":
            e = (e * f) % n
        f = (f * f) % n
    return e

def Encode():
    global ed, n, eingabe, ausgabe
    e = ed.get(1.0,END)[:-1]
    nl = n.get(1.0,END)[:-1]
    msg = eingabe.get(1.0,END)[:-1]
    msg = msg.upper()
    if len(msg) % 2 == 1:
        msg = msg + " "
    msgL = []
    msgE = []
    for i in range(0,len(msg),2):
        msgL.append(msg[i:i+2])
    #print(msgL)
    for block in msgL:
        zahl = (alphabet.index(block[0])+1) * 100 + alphabet.index(block[1])+1
        ergebnis = str(Potenz(zahl, int(e), int(nl)))
        lenabschnitte = len(str(int(nl)-1))
        while len(ergebnis) < lenabschnitte:
            ergebnis = "0" + ergebnis
        msgE.append(ergebnis)
    msgGeheim = "".join(msgE)
    ausgabe.delete(1.0, END)
    ausgabe.insert(1.0,msgGeheim)

def Decode():
    global ed, n, eingabe, ausgabe
    d = ed.get(1.0,END)[:-1]
    nl = n.get(1.0,END)[:-1]
    msg = eingabe.get(1.0,END)[:-1]
    ni = int(nl)
    blockSize = len(str(ni-1))
    msgE=[]
    for i in range(0,len(msg),blockSize):
        block = int(msg[i:i+blockSize])
        ergebnis = Potenz(block, int(d), ni)
        #print(ergebnis)
        buchstabe1 = alphabet[ergebnis // 100-1]
        buchstabe2 = alphabet[ergebnis % 100-1]
        msgE.append(buchstabe1 + buchstabe2)
    msgKlar = "".join(msgE)
    ausgabe.delete(1.0, END)
    ausgabe.insert(1.0,msgKlar)

def startFinder():
    RSAKeyFinderTk.start()

def start():
    global ed, n, eingabe, ausgabe
    window = Tk()
    window.title("RSA")

    buttonEncode = Button(master=window,text="Verschlüsseln", width=12,
                    font = ("Arial", 12), command=Encode)
    buttonDecode = Button(master=window,text="Entschlüsseln", width=12,
                    font = ("Arial", 12), command=Decode)
    buttonFinder = Button(master=window,text="RSAKeyFinder",width=12,
                    font = ("Arial", 12), command=startFinder)
    ed = Text(master=window, width=10, height=1, font=("Arial", 14), wrap=WORD)
    n = Text(master=window, width=10, height=1, font=("Arial", 14), wrap=WORD)
    eingabe = Text(master=window, width=30, height=6, font=("Arial", 14), wrap=WORD)
    ausgabe = Text(master=window, width=30, height=6, font=("Arial", 14), wrap=WORD)
    edlabel = Label(master=window,font=("Arial",12),text="E/D:")
    nlabel = Label(master=window,font=("Arial",12),text="N:")
    elabel = Label(master=window,font=("Arial",12),text="Eingabe:")
    alabel = Label(master=window,font=("Arial",12),text="Ausgabe:")
    buttonEncode.grid(column=0,row=0)
    buttonDecode.grid(column=1,row=0)
    buttonFinder.grid(column=2,row=0)
    ed.grid(column=0,row=3)
    n.grid(column=0,row=5)
    edlabel.grid(column=0,row=2)
    nlabel.grid(column=0,row=4)
    elabel.grid(column=1,row=1)
    alabel.grid(column=3,row=1)
    eingabe.grid(column=1,row=2,columnspan=2,rowspan=4)
    ausgabe.grid(column=3,row=2,columnspan=2,rowspan=4)


    window.mainloop()

ed = ""
n = ""
eingabe = ""
ausgabe = ""
start()
