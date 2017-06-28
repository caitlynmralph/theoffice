import re
import sys
import csv
from urllib2 import urlopen
from bs4 import BeautifulSoup
import numpy as np
import os

os.chdir('/Applications/MAMP/htdocs/theoffice/spreadsheets')

reload(sys)
sys.setdefaultencoding("utf-8")

with open('/Applications/MAMP/htdocs/theoffice/spreadsheets/character_appearances.csv', 'a') as csvfile:

    writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

    counts = np.zeros([1,2], dtype=object)

    url = "http://www.imdb.com/title/tt0386676/fullcredits?ref_=tt_cl_sm#cast"

    html = urlopen(url).read()
    soup = BeautifulSoup(html, "lxml")

    content = soup.find_all("td", {"class": "character"})

    for i in range(0,len(content)):
        if content[i].find('a') == None:
            pass
        else:
            character = content[i].find('a').contents[0]
            number = re.search(r'\((.*?\))', str(content[i]))
            count = str(number.group(1))
            row = np.reshape([character,count],[1,2])
            counts = np.append(counts,row, axis=0)

    for row in counts:
        name = row[0]
        count = row[1]
        writer.writerow([name,count])