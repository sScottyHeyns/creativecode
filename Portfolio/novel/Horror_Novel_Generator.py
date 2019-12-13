#Horror_Novel_Generator.py
import markovify as mk
import random as rng
from fpdf import FPDF
from Objectivity_Distribution import ObjDist

def makePDF(filename):
    #Get text, separating title and paragraphs
    #Assumes first line is title
    file= open(filename, "r")
    title= file.readline()
    pars= []
    for line in file:
        pars.append(line)
    file.close()

    #Format PDF
    pdf= FPDF(unit='pt')
    pdf.add_page()

    pdf.set_font("Helvetica", "U", 16)
    pdf.cell(595, 16, txt=title, ln=1, align="C")

    pdf.set_font("Helvetica", size=12)
    for par in pars:
        pdf.multi_cell(0, 12, txt=par)

    fileTitle= ("Abominations\\%s.pdf" % title[0:-1])
    pdf.output(fileTitle)

def generate(model, filename, sent_num):
    counter= 0
    counter2= 0
    par_length= 0
    chap_len= rng.randrange(15,31)
    chapter_num= 2
    file= open(filename, "a")
    file.write(("\n\nChapter %d\n\n" % (chapter_num - 1)))
    file.write("     ")
    file.close()
    for i in range(sent_num):
        if(counter==0):
            par_length= rng.randrange(4,8)
        file= open(filename, "a")
        file.write(str(model.make_sentence()+" "))
        file.close()
        if(counter==par_length):
            file= open(filename, "a")
            file.write("\n     ")
            file.close()
            counter2+= 1
            counter= -1
            if(counter2 == chap_len):
                file= open(filename, "a")
                file.write(("\n\nChapter %s\n\n" % chapter_num))
                file.close()
                chapter_num+= 1
                chap_len= rng.randrange(15,31)
                counter2= 0
        counter+= 1

def main():
    #Create Models
    print("Creating Models...")
    dracBook= open("Dracula.txt","r")
    dracula= mk.Text(dracBook.read())
    dracBook.close()

    frankBook= open("Frankenstein.txt","r")
    frankenstein= mk.Text(frankBook.read())
    frankBook.close()

    cthuluBook= open("AtMoM.txt","r", errors="surrogateescape")
    mountains= mk.Text(cthuluBook.read())
    cthuluBook.close()

    #Create Samples From Individual Book Models
    print("Writing Examples...")
    output1= open("Abominations\\DifferentDracula.txt","w+")
    output1.close()
    output1= open("Abominations\\DifferentDracula.txt","a")
    output1.write("Different Dracula\n\n")
    output1.close()
    generate(dracula, "Abominations\\DifferentDracula.txt", 200)
    makePDF("Abominations\\DifferentDracula.txt")
    
    output2= open("Abominations\\NewFrankenstein.txt","w+")
    output2.close()
    output2= open("Abominations\\NewFrankenstein.txt","a")
    output2.write("New Frankenstein\n\n")
    output2.close()
    generate(frankenstein, "Abominations\\NewFrankenstein.txt", 200)
    makePDF("Abominations\\NewFrankenstein.txt")
    
    output3= open("Abominations\\OriginalCthulhu.txt","w+")
    output3.close()
    output3= open("Abominations\\OriginalCthulhu.txt","a")
    output3.write("Original Cthulhu\n\n")
    output3.close()
    generate(mountains, "Abominations\\OriginalCthulhu.txt", 200)
    makePDF("Abominations\\OriginalCthulhu.txt")

    #Combine Models and output combined story
    print("Writing Pure Horror...")
    model= mk.combine([frankenstein, dracula, mountains])
    
    output4= open("Abominations\\Pure_Horror.txt","w+")
    output4.close()
    output4= open("Abominations\\Pure_Horror.txt","a")
    output4.write("Pure Horror\n\n")
    output4.close()
    generate(model, "Abominations\\Pure_Horror.txt", 55000)
    makePDF("Abominations\\Pure_Horror.txt")

    #Objectivity Model of Final Book
    print("Generating Objectivity Distribution...")
    ObjDist(["Abominations\\Pure_Horror.txt"])

main()
