#Horror_Novel_Generator.py
import markovify as mk
import random as rng
from fpdf import FPDF

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

def generate(model, file, sent_num):
    counter= 0
    par_length= 0
    file.write("\t")
    for i in range(sent_num):
        if(counter==0):
            par_length= rng.randrange(4,8)
        file.write(str(model.make_sentence()+" "))
        if(counter==par_length):
            file.write("\n\t")
            counter= -1
        counter+= 1

def main():
    #Create Models
    dracBook= open("Dracula.txt","r")
    dracula= mk.Text(dracBook.read())
    dracBook.close()

    frankBook= open("Frankenstein.txt","r")
    frankenstein= mk.Text(frankBook.read())
    frankBook.close()

    cthuluBook= open("AtMoM.txt","r")
    mountains= mk.Text(cthuluBook.read())
    cthuluBook.close()

    #Create Samples From Individual Book Models
    output1= open("Abominations\\DifferentDracula.txt","w+")
    output1.close()
    output1= open("Abominations\\DifferentDracula.txt","a")
    output1.write("Different Dracula\n\n")
    generate(dracula, output1, 200)
    output1.close()
    makePDF("Abominations\\DifferentDracula.txt")
    
    output2= open("Abominations\\NewFrankenstein.txt","w+")
    output2.close()
    output2= open("Abominations\\NewFrankenstein.txt","a")
    output2.write("New Frankenstein\n\n")
    generate(frankenstein, output2, 200)
    output2.close()
    makePDF("Abominations\\NewFrankenstein.txt")
    
    output3= open("Abominations\\OriginalCthulhu.txt","w+")
    output3.close()
    output3= open("Abominations\\OriginalCthulhu.txt","a")
    output3.write("Original Cthulhu\n\n")
    generate(mountains, output3, 200)
    output3.close()

    #Combine Models and output combined story
    model= mk.combine([frankenstein, dracula])
    
    output4= open("Abominations\\Pure_Horror.txt","w+")
    output4.close()
    output4= open("Abominations\\Pure_Horror.txt","a")
    output4.write("Pure Horror\n\n")
    generate(model, output4, 55000)
    output4.close()
    makePDF("Abominations\\Pure_Horror.txt")

main()
