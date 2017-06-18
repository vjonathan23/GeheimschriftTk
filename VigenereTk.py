from tkinter import *

#alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nummer = {"A":"0","B":"1","C":"2","D":"3","E":"4","F":"5","G":"6","H":"7","I":"8","J":"9","K":"10","L":"11","M":"12","N":"13","O":"14","P":"15","Q":"16","R":"17","S":"18","T":"19","U":"20","V":"21","W":"22","X":"23","Y":"24","Z":"25"}
#nummer2 = {"a":"0","b":"1","c":"2","d":"3","e":"4","f":"5","g":"6","h":"7","i":"8","j":"9","k":"10","l":"11","m":"12","n":"13","o":"14","p":"15","q":"16","r":"17","s":"18","t":"19","u":"20","v":"21","w":"22","X":"23","y":"24","z":"25"}
nummer3 = {"0":"A","1":"B","2":"C","3":"D","4":"E","5":"F","6":"G","7":"H","8":"I","9":"J","10":"K","11":"L","12":"M","13":"N","14":"O","15":"P","16":"Q","17":"R","18":"S","19":"T","20":"U","21":"V","22":"W","23":"X","24":"Y","25":"Z"}


def Encode():
    global schluessel,eingabe,ausgabe
    satz = eingabe.get(1.0,END)[:-1]
    schluessell = schluessel.get(1.0,END)[:-1]
    lens = len(schluessell)
    s = 0
    l = 0
    geheimsatz = []
    for i in range(len(satz)):
        buchstabe = satz[i]
        buchstabe = buchstabe.upper()
        nb = nummer[buchstabe]
        sbuchstabe = schluessell[s]
        sbuchstabe = sbuchstabe.upper()
        ns = nummer[sbuchstabe]
        gnBuchstabe = (int(nb) + int(ns)) % 26
        gBuchstabe = nummer3[str(gnBuchstabe)]
        geheimsatz.append(gBuchstabe)
        s += 1
        l += 1
        if s == lens:
            s = 0
        if l == 5:
            geheimsatz.append(" ")
            l = 0
    ausgabel = "".join(geheimsatz)
    ausgabe.delete(1.0, END)
    ausgabe.insert(1.0,ausgabel)

def Decode():
    global schluessel,eingabe,ausgabe
    satz = eingabe.get(1.0,END)[:-1]
    schluessell = schluessel.get(1.0,END)[:-1]
    lens = len(schluessell)
    s = 0
    l = 0
    geheimsatz = []
    for i in range(len(satz)):
        buchstabe = satz[i]
        buchstabe = buchstabe.upper()
        nb = nummer[buchstabe]
        sbuchstabe = schluessell[s]
        sbuchstabe = sbuchstabe.upper()
        ns = nummer[sbuchstabe]
        gnBuchstabe = (int(nb) - int(ns) + 26) % 26
        gBuchstabe = nummer3[str(gnBuchstabe)]
        geheimsatz.append(gBuchstabe)
        s += 1
        l += 1
        if s == lens:
            s = 0
        if l == 5:
            geheimsatz.append(" ")
            l = 0
    ausgabel = "".join(geheimsatz)
    ausgabe.delete(1.0, END)
    ausgabe.insert(1.0,ausgabel)

def start():
    global schluessel,eingabe,ausgabe
    window = Tk()
    window.title("Vigenere")

    buttonEncode = Button(master=window,text="Verschlüsseln", width=12,
                    font = ("Arial", 12), command=Encode)
    buttonDecode = Button(master=window,text="Entschlüsseln", width=12,
                    font = ("Arial", 12), command=Decode)
    schluessel = Text(master=window, width=10, height=1, font=("Arial", 14), wrap=WORD)
    eingabe = Text(master=window, width=30, height=6, font=("Arial", 14), wrap=WORD)
    ausgabe = Text(master=window, width=30, height=6, font=("Arial", 14), wrap=WORD)
    slabel = Label(master=window,font=("Arial",12),text="Schlüssel:")
    elabel = Label(master=window,font=("Arial",12),text="Eingabe:")
    alabel = Label(master=window,font=("Arial",12),text="Ausgabe:")
    buttonEncode.grid(column=0,row=0)
    buttonDecode.grid(column=1,row=0)
    schluessel.grid(column=0,row=3)
    slabel.grid(column=0,row=2)
    elabel.grid(column=1,row=1)
    alabel.grid(column=3,row=1)
    eingabe.grid(column=1,row=2,columnspan=2,rowspan=4)
    ausgabe.grid(column=3,row=2,columnspan=2,rowspan=4)


    window.mainloop()

eingabe = ""
ausgabe = ""
scluessel = ""
start()
