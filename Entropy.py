#!/usr/bin/python
import sys
import EntropyCalculator

"""Invoke as Entropy.py Document Output.csv
   Document may be plain text or XML
   Analysis will be performed with a block size of 1000 words
   May add options to customize analysis or output at a later date
   Columns of output are word, Entropy per instance of that word,
   proportion of document's entropy from instances of that word.
   Summary statistics will be printed to stdout"""
   

H=EntropyCalculator.EntropyCalculator(10)
data=open(sys.argv[1],'r')
H.SetText(data)
H.SetWordsPerPart(1000)
H.AnalyseText()
output=open(sys.argv[2],'w')
H.OutputWords(output)
data.close()
output.close()
print argv[1], "contains",H.Nwords
print "Analysed with", H.Parts, "blocks"
print "Total entropy", H.TotalEntropy,"bits"
print "Words with entropy >",float(H.Parts)/(H.Parts+1),"are likely to be particulary significant"
print "Detailed analysis written to ",sys.argv[2]
