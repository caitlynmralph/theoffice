import markovify
import sys
import csv
import numpy as np
import os

os.chdir('/Applications/MAMP/htdocs/theoffice/spreadsheets')

with open('/Applications/MAMP/htdocs/theoffice/spreadsheets/dwight_markov_tweets.tsv', 'a') as csvfile:

    writer = csv.writer(csvfile, delimiter='\t',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

    lines = np.zeros([0,0], dtype=object)

    # Get raw text as string.
    with open("dwight_lines.txt") as f:
        text = f.read()

    # Build the model.
    text_model = markovify.NewlineText(text)

    # # Print five randomly-generated sentences
    # for i in range(5):
    #     print(text_model.make_sentence())
    #     text_model.make_sentence()

    # Print three randomly-generated sentences of no more than 140 characters
    for i in range(1000):
        print(text_model.make_short_sentence(140))
        lines = np.append(lines,text_model.make_short_sentence(140))

    for row in lines:
        writer.writerow([row])