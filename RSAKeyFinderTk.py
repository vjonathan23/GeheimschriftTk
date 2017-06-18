from Primzahlfinder import findePrimzahlen, ggT
from random import choice, randint
from tkinter import *

def finder():
    global p,q,n,phi,e,d
    pl = choice(findePrimzahlen(1000,2000))
    ql = choice(findePrimzahlen(2000,3000))
    nl = pl * ql
    phil = (pl-1)*(ql-1)
    p.delete(1.0, END)
    q.delete(1.0, END)
    n.delete(1.0, END)
    phi.delete(1.0, END)
    p.insert(1.0,"p = "+str(pl))
    q.insert(1.0,"q = "+str(ql))
    n.insert(1.0,"n = "+str(nl))
    phi.insert(1.0,"phi = "+str(phil))
    #print("Suche Codier-Exponenten...")
    found = False
    while not found:
        el = randint(10000, 20000)
        if ggT(el, phil) == 1:
            for dl in range(phil):
                if ( el * dl ) % phil == 1:
                    found = True
                    break
    e.delete(1.0,END)
    d.delete(1.0,END)
    e.insert(1.0,"e = "+str(el))
    d.insert(1.0,"d = "+str(dl))

def start():
    global p,q,n,phi,e,d
    window = Tk()
    window.title("RSASchlüsselFinder")
    frame = Frame(master=window)

    buttonSchluessel = Button(master=frame,text="Schlüsselfinder", width=12,
                    font = ("Arial", 12), command=finder)
    p = Text(master=window, width=15, height=1, font=("Arial", 14), wrap=WORD)
    q = Text(master=window, width=15, height=1, font=("Arial", 14), wrap=WORD)
    n = Text(master=window, width=15, height=1, font=("Arial", 14), wrap=WORD)
    phi = Text(master=window, width=15, height=1, font=("Arial", 14), wrap=WORD)
    e = Text(master=window, width=15, height=1, font=("Arial", 14), wrap=WORD)
    d = Text(master=window, width=15, height=1, font=("Arial", 14), wrap=WORD)

    frame.pack()
    buttonSchluessel.pack()
    p.pack()
    q.pack()
    n.pack()
    phi.pack()
    e.pack()
    d.pack()

    window.mainloop()

p = ""
q = ""
n = ""
phi = ""
e = ""
d = ""
#start()
