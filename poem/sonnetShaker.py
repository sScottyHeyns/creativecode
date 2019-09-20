# frankenpoem.py

##  A python program designed to take a word file and create poetry out
## it

from random import *

def main():
    origSon= open("Sonnet.txt", "r")
    sonLines= []

    newCouplet= randrange(1,7)

    for i in range(0, 14):
        line= origSon.readline()
        sonLines.append(line)

    origSon.close()

    couplet= [sonLines[12],sonLines[13]]
    if newCouplet==1 or newCouplet==2:
        oldLine= [sonLines[newCouplet-1],sonLines[newCouplet+1]]
        sonLines[newCouplet-1]= couplet[0]
        sonLines[newCouplet+1]= couplet[1]
        sonLines[12]= oldLine[0]
        sonLines[13]= oldLine[1]
    elif newCouplet==3 or newCouplet==4:
        oldLine= [sonLines[newCouplet+1],sonLines[newCouplet+3]]
        sonLines[newCouplet-1]= couplet[0]
        sonLines[newCouplet+1]= couplet[1]
        sonLines[12]= oldLine[0]
        sonLines[13]= oldLine[1]
    elif newCouplet==5 or newCouplet==6:
        oldLine= [sonLines[newCouplet+3],sonLines[newCouplet+5]]
        sonLines[newCouplet-1]= couplet[0]
        sonLines[newCouplet+1]= couplet[1]
        sonLines[12]= oldLine[0]
        sonLines[13]= oldLine[1]

    newSon= open("ShakenSonnet.txt","a+")
    for i in sonLines:
        newSon.write(i)

main()
