def Primfaktoren(z,start=2):
    pf = []
    #print("PF "+str(z) + " "+ str(start) )    
    if z==1:
        return pf
    for t in range(start,z+1):
        if z % t == 0:
            g = z//t
            pf = Primfaktoren(g,t)
            pf.append(t)
            return pf

def istPrimzahl(z):
    if z != 2 and z % 2 == 0:
        return False
    pf = Primfaktoren(z)
    if len(pf) == 1:
        return True
    else:
        return False

def findePrimzahlen(von,bis):
    pz = []
    for i in range(von,bis+1):
        if istPrimzahl(i) == True:
            pz.append(i)
    return pz

def ggT(a,b):
    pfA = Primfaktoren(a)
    pfC = list(pfA)
    pfB = Primfaktoren(b)
    pfG = []    
    for f in pfC:
        if f in pfB:
            pfA.remove(f)
            pfB.remove(f)
            pfG.append(f)
    ggT = 1
    for f in pfG:
        ggT *= f
    return ggT
            
#print(ggT(100,25))        
#print(findePrimzahlen(1000, 2000))
