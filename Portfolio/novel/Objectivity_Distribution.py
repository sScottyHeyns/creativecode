#Objectivity_Distribution.py
from textblob import TextBlob
from matplotlib import pyplot

def ObjDist(fileList):
    text= []
    for i in fileList:
        book= open(i,"r")
        text.append(TextBlob(book.read()))
        book.close()
        
    for i in text:
        y= []
        sent_tot= 0
        for sentence in i.sentences:
            y.append(sentence.sentiment.subjectivity)
            sent_tot+= 1

        pyplot.xlabel("Sentence Progression")
        pyplot.ylabel("Subjectivity")
        pyplot.plot(range(sent_tot),y,"bo")
        pyplot.show()
