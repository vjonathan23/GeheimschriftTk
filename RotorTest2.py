from tkinter import *

alphabet  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

reflektor = [ "ABCDEFGDIJKGMKMIEBFTCVVJAT",
              "ABCDEFGDIJKGMKMIEBFTCVVJAT",
              "", # brauchen wir bei Reflektor nicht
              " ", # Strom hin
              " "] # Strom zurück

rotor1  = [ str(alphabet),
            "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
            "Q", #shift
            " ", # Strom hin
            " "] # Strom zurück

rotor2  = [ str(alphabet),
            "AJDKSIRUXBLHWTMCQGZNPYFVOE",  
            "E",   #shift
            " ", # Strom hin
            " "] # Strom zurück

rotor3  = [ str(alphabet),
            "BDFHJLCPRTXVZNYEIWGAKMUSQO",  
            "V" ,   #shift
            " ", # Strom hin
            " "] # Strom zurück

inputOutput = [ str(alphabet),
                str(alphabet),
                "", # brauchen wir bei Reflektor nicht
                " ", # Strom hin
                " "] # Strom zurück

rotoren = [reflektor,rotor1, rotor2, rotor3, inputOutput]

class Rotor():
    def __init__(self,master,rotorNr,isRotor=True,nextRotor=None,autoShift=False):
        self.canvas = Canvas(master=master, bg='black',width=70,height=400)
        self.isRotor = isRotor
        self.autoShift = autoShift
        if self.isRotor: #nicht für Reflektor [0]
            self.canvas.bind("<B1-Motion>",self.dragRotor)
            self.canvas.bind("<ButtonRelease-1>",self.endDragRotor)
            self.dragStart = -1 #Anfangsposition beim Maus-Ziehen
        self.rNr = rotorNr 
        self.r = rotoren[self.rNr]
        self.rNext = nextRotor
        self.startPos = self.r[0][0] #Startposition Rotor
        self.rLen = len(self.r[0]) #26 Buchstaben
        self.dist = 14    # Abstand zwischen Buchstaben (Y-Differenz)
        #Rotorstreifen-Box
        self.box = self.canvas.create_rectangle(10,
                                                10,
                                                60,
                                                390,
                                                fill='white')
        #Erzeuge Textzellen für Links+Rechts und Shift-Feld
        self.tZ = []
        for i in range(self.rLen):
            #leere Textzellen für links+rechts+shiftSign
            tzL = self.canvas.create_text(20,
                                          25+i*self.dist,
                                          text="")
            tzR = self.canvas.create_text(40,
                                          25+i*self.dist,
                                          text="")
            tzS = self.canvas.create_text(55,
                                          25+i*self.dist,
                                          text="")
            tzG = self.canvas.create_text(30,
                                          25+i*self.dist,
                                          text="")
            self.tZ.append([tzL,tzR,tzS,tzG])
        #bewege ohne Vorrücken um Texte zu befüllen
        self.move(direction=" ")

    def dragRotor(self,event):
        diffY = 0
        if self.dragStart>=0:  
            diffY = event.y - self.dragStart
        else:
            self.dragStart = event.y
        if diffY>=self.dist:
            self.move(direction="Down",drag=True)
            self.dragStart = event.y
        elif diffY<=(-self.dist):
            self.move(direction="Up",drag=True)
            self.dragStart = event.y
        
    def endDragRotor(self,event):
        self.dragStart = -1
        
    #moveRotor wird von Tasten-Event aufgerufen
    def moveRotor(self,event):
        self.move(direction=event.keysym)

    #Bewege Rotor
    def move(self,direction,drag=False):
        #Rotation
        if direction=="Up": #Vor
            if self.r[1][0]==self.r[2] and self.rNext:
                self.rNext.move("Up") #nächster Rotor vor
            self.r[0]=self.r[0][1:]+self.r[0][0]
            self.r[1]=self.r[1][1:]+self.r[1][0]
        elif direction=="Down": #Zurück
            if self.r[1][self.rLen-1]==self.r[2] and self.rNext:
                self.rNext.move("Down") #nächster Rotor zurück
            self.r[0]=self.r[0][-1]+self.r[0][:-1]
            self.r[1]=self.r[1][-1]+self.r[1][:-1]
        if drag:  #merke neue Startposition
            self.startPos = self.r[0][0]
        #Fülle Textzellen
        for i in range(self.rLen):
            if self.isRotor and self.r[1][i] == self.r[2]:
                shiftSign = '#'
            else:
                shiftSign = ' '
            colorLeft = 'black'
            colorRight = 'black'
            underlineLeft = -1
            if self.r[1][i] == self.r[3] or self.r[1][i] == self.r[4]:
                colorRight = 'darkorange'
            if self.r[0][i] == self.r[3] or self.r[0][i] == self.r[4]:
                colorLeft = 'darkorange'
            if self.isRotor and self.r[0][i] == self.startPos:
                colorLeft = 'red'
                underlineLeft = 0 #erstes Zeichen unterstrichen
            self.canvas.itemconfig(self.tZ[i][0],text = self.r[0][i],fill=colorLeft,underline=underlineLeft)
            #textStrom = ""
            #if i == self.r[3] or i==self.r[4]:
            #    textStrom = "--"
            #if i == self.r[4] and i == self.r[3]:
            #    textStrom = "="
            #self.canvas.itemconfig(self.tZ[i][3],text = textStrom, fill="darkorange")
            if self.isRotor:
                self.canvas.itemconfig(self.tZ[i][1],text = self.r[1][i],fill=colorRight)
                self.canvas.itemconfig(self.tZ[i][2],text = shiftSign)
            #print(self.canvas.itemconfig(self.tZ[i][2]))
    def setSignal(self,LSignal,RSignal):
        self.LSignal = LSignal
        self.RSignal = RSignal
    def sendeStrom(self,index,richtung):
        if richtung == 'L':  # Hinstrom
            if self.autoShift:
                self.move("Up")
            self.r[3] = self.r[1][index]
            indexNeu = self.r[0].index(self.r[3])
            if self.LSignal:
                self.LSignal.sendeStrom(indexNeu,richtung)
            else:  # Reflektor
                if indexNeu == index:  #suche 2. Buchstaben im Relektor
                    indexNeu+=1
                    indexNeu = indexNeu + self.r[0][indexNeu:].index(self.r[3])
                self.RSignal.sendeStrom(indexNeu,"R") #drehe richtung               
        else:                # Rückstrom
            self.r[4] = self.r[0][index]
            indexNeu = self.r[1].index(self.r[4])
            self.RSignal.sendeStrom(indexNeu,richtung)
        self.move("") #aktualisieren

    def clear(self):
        for i in range(self.rLen):
            if self.isRotor and self.r[1][i] == self.r[2]:
                shiftSign = '#'
            else:
                shiftSign = ' '
            colorLeft = 'black'
            colorRight = 'black'
            underlineLeft = -1
            if self.isRotor and self.r[0][i] == self.startPos:
                colorLeft = 'red'
                underlineLeft = 0 #erstes Zeichen unterstrichen
            self.canvas.itemconfig(self.tZ[i][0],text = self.r[0][i],fill=colorLeft,underline=underlineLeft)
            if self.isRotor:
                self.canvas.itemconfig(self.tZ[i][1],text = self.r[1][i],fill=colorRight)
                self.canvas.itemconfig(self.tZ[i][2],text = shiftSign)

class TextFeld:
    def __init__(self,master):
        self.canvas = Canvas(master=master, bg='black',width=200,height=200)
        #Rotorstreifen-Box
        self.box = self.canvas.create_rectangle(10,
                                                10,
                                                190,
                                                190,
                                                fill='white')
        #Erzeuge Textzelle
        self.buchstabenProZeile = 17
        self.zeilen = 12
        self.tZ=[]
        self.LSignal=None
        self.RSignal=None
        self.nextLSignal=None
        self.nnextLSignal=None
        self.nnnextLSignal=None
        self.nnnnextLSignal=None
        self.ausgabe=None
        for i in range(self.zeilen):
            for j in range(self.buchstabenProZeile):
                tz = self.canvas.create_text(20+10*j,20+i*14,text="")
                self.tZ.append(tz)
        self.text = ""

    def taste(self,event):
        global rotoren
        eingabe = event.keysym.upper()
        if eingabe in alphabet:
            self.text = self.text + eingabe
            self.LSignal.sendeStrom(alphabet.index(eingabe),"L")
        elif eingabe == "BACKSPACE" and len(self.text) > 0:
            self.text = self.text[:-1]
            if self.LSignal:
                self.nextLSignal.move("Down")
                self.LSignal.clear()
                self.nextLSignal.clear()
                self.nnextLSignal.clear()
                self.nnnextLSignal.clear()
                self.nnnnextLSignal.clear()
                for i in range(4):
                    rotoren[i][3] = " "
                    rotoren[i][4] = " "
            if self.ausgabe:
                self.ausgabe.taste(event)
        self.updateText()

    def updateText(self):
        text = self.text
        #alle Zellen zurücksetzen
        for zelle in self.tZ:
            self.canvas.itemconfig(zelle,text = "",fill="darkblue")
        if len(text) > self.zeilen * self.buchstabenProZeile:
            text = text[-self.zeilen*self.buchstabenProZeile:]
        for i in range(len(text)//self.buchstabenProZeile+1):
            for j in range(self.buchstabenProZeile):
                index = i*self.buchstabenProZeile+j
                if index<len(text):
                    self.canvas.itemconfig(self.tZ[index],text = text[index],fill="darkblue")
    def setSignal(self,LSignal,RSignal,nextLSignal=None,nnextLSignal=None,nnnextLSignal=None,nnnnextLSignal=None):
        self.LSignal = LSignal
        self.RSignal = RSignal
        self.nextLSignal = nextLSignal
        self.nnextLSignal = nnextLSignal
        self.nnnextLSignal = nnnextLSignal
        self.nnnnextLSignal = nnnnextLSignal
    def setAusgabe(self,ausgabe):
        self.ausgabe = ausgabe
    def sendeStrom(self,index,richtung):
        self.text = self.text + alphabet[index]
        self.updateText()
        
                    
class MainWindow:
    def __init__(self):
        #Initialisiere Hauptfenster
        self.window = Tk()
        self.window.title("Enigma")
        #self.canvas = Canvas(master=self.window, bg='black',width=800,height=450)
        #self.canvas.pack()
        #Reflektor [0] & 3 Rotoren [1-3]
        self.r0 = Rotor(self.window,0,isRotor=False)        
        self.r1 = Rotor(self.window,1)
        self.r2 = Rotor(self.window,2,nextRotor=self.r1)
        self.r3 = Rotor(self.window,3,nextRotor=self.r2,autoShift=True)
        self.r4 = Rotor(self.window,4,isRotor=False)        
        self.eingabe = TextFeld(self.window)
        self.ausgabe = TextFeld(self.window)
        self.eingabe.setSignal(self.r4,None,self.r3,self.r2,self.r1,self.r0)
        self.eingabe.setAusgabe(self.ausgabe)
        self.r4.setSignal(self.r3,self.ausgabe)        
        self.r3.setSignal(self.r2,self.r4)
        self.r2.setSignal(self.r1,self.r3)
        self.r1.setSignal(self.r0,self.r2)
        self.r0.setSignal(None,self.r1)
        self.r0.canvas.grid(column=0,row=0,rowspan=2)
        self.r1.canvas.grid(column=1,row=0,rowspan=2)
        self.r2.canvas.grid(column=2,row=0,rowspan=2)
        self.r3.canvas.grid(column=3,row=0,rowspan=2)
        self.r4.canvas.grid(column=4,row=0,rowspan=2)
        self.eingabe.canvas.grid(column=5,row=0)
        self.ausgabe.canvas.grid(column=5,row=1)
        #Rotor 3 lauscht auf Tasteneingabe
        self.window.bind("<KeyPress-Up>", self.r3.moveRotor)
        self.window.bind("<KeyPress-Down>", self.r3.moveRotor)
        self.window.bind("<KeyPress>", self.eingabe.taste)
        #Start
        self.window.mainloop()

#Öffne Fenster        
MainWindow()

