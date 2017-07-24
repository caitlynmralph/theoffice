#import packages
import markovify
import csv
import numpy as np
import os

#change working directory
os.chdir('/Applications/MAMP/htdocs/theoffice/spreadsheets')

#create CSV file to write to and open it
with open('/Applications/MAMP/htdocs/theoffice/spreadsheets/dwight_markov_tweets.tsv', 'a') as csvfile:

    #csv writer
    writer = csv.writer(csvfile, delimiter='\t',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

    #upload corpus of text
    with open("dwight_lines.txt") as f:
        text = f.read()

    #build the markovify model
    text_model = markovify.NewlineText(text)

    #generate the sentences and write to CSV file
    for i in range(1000):
        print(text_model.make_short_sentence(140))
        writer.writerow(text_model.make_short_sentence(140))
