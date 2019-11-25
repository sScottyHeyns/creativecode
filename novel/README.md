# Crafting Horror Novels

This program writes a unique horror novel based on some of the timeless classics. Here we use text files of Dracula by Bram Stoker and Frankenstein by Mary Shell with the Markovify library to generate a novel that mixes the two authors' unique styles. This generates a novel that sounds like it should be suspenseful and horrific, but mostly results in hysterical nonsense. After generation we used the FPDF library to make the novel into an easy-to-read PDF.

## Output

In a folder labeled "Abominations", this program will generate four different text files: DifferentDracula.txt, NewFrankenstein.txt,  OriginalCthulhu.txt, and Pure_Horror.txt. The first three are 200 sentence samples of the individual novels, to give you a feel of what Markovify will do to individual novels before mixing styles. The "Pure_Horror" file is the manuscript for the combined story, which our "makePDF" function will turn into a PDF directly.

## Need to Fix

Originally we were going to include In the Mountains of Madness by H.P. Lovecraft, and we include a 200 page text sample from that novel. However, there is a certain character in that book that the FPDF library can't encode. In a later project we will hunt down that character and eliminate it from the manuscript so that we may include this horror classic with our other examples.

## Objectivity Distribtion

Also included in this project is a failed experiment in story structure. The "Objectivity Distribution" was made to plot the objectivity, as defined by the TextBlob library, of the sentences in a story on a graph, using the MatPlotLib library. The idea was to see if there was a predictable ebb and flow to the objectivity of sentences in a novel, which could be used to give the generated story a more authentic feel to it. Unfortunately, there appears to be no correlation of objectivity with the structure of any of the three novels we have samples of.

## Modules Needed

Modules needed to run this code: Markovify('pip install markovify'), FPDF ('pip install fpdf')
