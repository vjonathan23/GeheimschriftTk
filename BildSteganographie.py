from tkinter import *
from tkinter import filedialog

def getPos(blocknr):
    global image
    x = ((blocknr - 1) * 8 ) %  image.width()
    y = ((blocknr - 1) * 8 ) // image.width()
    return x,y

def nextPos(x,y):
    global image
    #print(str(x)+ " " +str(y))
    x += 1
    if x >= image.width():
        x = 0
        y += 1
    #print("=> "+str(x)+ " " +str(y)+ " " + str(image.width()))
    return x,y 

def writeBlock(zR, zG, zB, blocknr):
    global image
    x, y = getPos(blocknr)
    #print(str(zR)+ " " +str(zG) + " " +str(zB))
    for i in range(8):
        # lade pixel
        #print("Block "+str(blocknr)+" "+str(i))
        c = list(image.get(x,y))
        #print(c)
        # setze 1. Bit zurück auf 0
        for k in range(3):
            if c[k] % 2 == 1:
                c[k] -= 1
        #print(c)
        # setze 1. Bit mit i-tem Bit aus Zahl
        if zR & 2**i != 0:
            c[0] += 1
        if zG & 2**i != 0:
            c[1] += 1
        if zB & 2**i != 0:
            c[2] += 1
        #print(c)
        # Farbe in Hex
        h = []
        for k in range(3):
            farbcode = hex(c[k])[2:]
            if len(farbcode) == 1:
                farbcode = "0"+farbcode
            h.append(farbcode)
        hexFarbe = "#"+"".join(h)
        # schreibe neuen Pixel
        image.put(hexFarbe, (x,y))
        # nächster Pixel
        x,y = nextPos(x,y)

def readBlock(blocknr):
    global image
    x, y = getPos(blocknr)
    zR = 0
    zG = 0
    zB = 0
    for i in range(8):
        # lade pixel
        c = list(image.get(x,y))
        #print("Block "+str(blocknr)+" "+str(i))
        #print(c)
        # lese 1. Bit aus Farbcode
        if c[0] % 2 == 1:
            zR += 2**i 
        if c[1] % 2 == 1:
            zG += 2**i 
        if c[2] % 2 == 1:
            zB += 2**i 
        x,y = nextPos(x,y)
    return zR, zG, zB

        
def encode():
    global text
    nachricht = text.get(1.0,END)[:-1]
    while len(nachricht)%3 != 0:
        nachricht += " "
    zR = len(nachricht) & 255
    zG = ( len(nachricht) >> 8 ) & 255
    zB = ( len(nachricht) >> 16 ) & 255
    #print(str(zR)+" "+str(zG)+ " " +str(zB))
    writeBlock(zR,zG,zB,1)
    i = 0
    block = 2
    while i < len(nachricht):
        zR = ord(nachricht[i])
        i += 1
        zG = ord(nachricht[i])
        i += 1
        zB = ord(nachricht[i])
        i += 1
        writeBlock(zR,zG,zB,block)
        block += 1

def decode():
    global text
    nachricht = ""
    zR, zG, zB = readBlock(1)
    #print(str(zR)+" "+str(zG)+ " " +str(zB))
    nLen = zR + (zG << 8) + (zB << 16)
    #print(nLen)
    i = 0
    block = 2
    #print("Length: "+str(nLen))
    while i < nLen:
        zR, zG, zB = readBlock(block)
        nachricht = nachricht + chr(zR) + chr(zG) + chr(zB)
        block += 1
        i += 3
    text.delete(1.0, END)
    text.insert(1.0, nachricht)
    

def loadImage():
    global image, label, path
    p = filedialog.askopenfilename()
    if p:
        try:
            image = PhotoImage(file=p)
            label.config(image=image)
            path = p
        except:
            messagebox.showerror("", "Foto unleserlich")

def saveImage():
    p = filedialog.asksaveasfilename()
    if p:
        image.write(p)


def start():
    global label, text
    window = Tk()
    window.title("Bild-Steganographie")
    frame = Frame(master=window)
    label = Label(master=window, font = ("Arial", 14), text="Bitte ein Bild laden")
    
    buttonEncode = Button(master=frame,text="Bild verschlüsseln", width=12,
                    font = ("Arial", 12), command=encode)
    buttonDecode = Button(master=frame,text="Bild entschlüsseln", width=12,
                    font = ("Arial", 12), command=decode)
    buttonLoad = Button(master=frame,text="Laden", width=12,
                    font = ("Arial", 12), command=loadImage)  
    buttonSave = Button(master=frame,text="Speichern", width=12,
                    font = ("Arial", 12), command=saveImage)
    
    text = Text(master=window, width=60, height=4, font=("Arial", 14), wrap=WORD)
    
    
    frame.pack()
    buttonEncode.pack(side=LEFT, padx=2, pady=2)
    buttonDecode.pack(side=LEFT, padx=2, pady=2)
    buttonLoad.pack(side=LEFT, padx=2, pady=2)
    buttonSave.pack(side=LEFT, padx=2, pady=2)
    text.pack()
    label.pack()
    
    
    window.mainloop()           

text = ""
label = ""
start()

