from tkinter import *
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def Encode():
    global schluessel, eingabe, ausgabe
    geheimsatz = []  # leere Ergebnismenge

    #Eingabe
    satz = eingabe.get(1.0,END)[:-1]
    chiffre = schluessel.get(1.0,END)[:-1]

    satz = satz.upper()
    
    for i in range(len(satz)):
        buchstabe = satz[i]
        if buchstabe in alphabet:
            position = alphabet.index(buchstabe) + int(chiffre) # verschieben!
            while position >= len(alphabet):
                position = position - len(alphabet)
            while position < 0:
                position = position + len(alphabet)
            geheimsatz.append(alphabet[position])
        else:
            geheimsatz.append(buchstabe)
    #Ausgabe
    ausgabel = "".join(geheimsatz)
    ausgabe.delete(1.0, END)
    ausgabe.insert(1.0,ausgabel)

def start():
    global schluessel, eingabe, ausgabe
    window = Tk()
    window.title("Caesar-Chiffre")

    buttonEncode = Button(master=window,text="Verschlüsseln", width=12,
                    font = ("Arial", 12), command=Encode)
    schluessel = Text(master=window, width=10, height=1, font=("Arial", 14), wrap=WORD)
    eingabe = Text(master=window, width=30, height=6, font=("Arial", 14), wrap=WORD)
    ausgabe = Text(master=window, width=30, height=6, font=("Arial", 14), wrap=WORD)
    slabel = Label(master=window,font=("Arial",12),text="Chiffre:")
    elabel = Label(master=window,font=("Arial",12),text="Eingabe:")
    alabel = Label(master=window,font=("Arial",12),text="Ausgabe:")
    buttonEncode.grid(column=0,row=0)
    schluessel.grid(column=0,row=3)
    slabel.grid(column=0,row=2)
    elabel.grid(column=1,row=1)
    alabel.grid(column=3,row=1)
    eingabe.grid(column=1,row=2,columnspan=2,rowspan=4)
    ausgabe.grid(column=3,row=2,columnspan=2,rowspan=4)

    window.mainloop()

schluessel = ""
eingabe = ""
ausgabe = ""
start()
