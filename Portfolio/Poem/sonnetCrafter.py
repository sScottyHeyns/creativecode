#sonnetCrafter.py
import syllables as SY
from random import *

def Bard(title, file, lineList):
    File= open(file, "a+")
    File.write(("\n%s\n" % title))
    for i in range(12):
        num= randrange(len(lineList))
        File.write(lineList[num])
        File.write("\n")
    File.close()

def FileOpener(filename, permission):
    if (permission == "r"):
        file= open(filename, permission)
        internal= file.read()
        file.close()
        return internal
    else:
        return

def Validate(lineList):
    valid= []
    for sentence in lineList:
        sylls= SY.estimate(sentence)
        if (sylls == 10):
            valid.append(sentence)

    return valid

def main():
    #Import books into variables
    books= []
    onShelf= input("Enter list of book files: ")
    onShelf= onShelf.split(", ")
    for i in onShelf:
        books.append(FileOpener(i, "r"))

    #Divide books into individual sentences
    lines= []
    for i in books:
        lines.append(i.split("\n"))

    #Keep only sentences with 10 syllables
    valid= []
    for i in lines:
        valid.append(Validate(i))

    #Print 12 Poems in each book's file
    for j in range(12):
        count= 0
        for i in valid:
            Bard(("%s" % onShelf[count][0:-4]), ("%s_Poems.txt" % onShelf[count][0:-4]), i)
            count += 1
  
main()
