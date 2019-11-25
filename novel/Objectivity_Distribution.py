#Objectivity_Distribution.py
from textblob import TextBlob
from matplotlib import pyplot

def main():
    book= open("AtMoM.txt","r")
    text= TextBlob(book.read())
    book.close()

    y= []
    sent_tot= 0
    for sentence in text.sentences:
        y.append(sentence.sentiment.subjectivity)
        sent_tot+= 1

    pyplot.xlabel("Sentence Progression")
    pyplot.ylabel("Subjectivity")
    pyplot.plot(range(sent_tot),y,"bo")
    pyplot.show()

main()
