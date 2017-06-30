# -*- coding: utf-8 -*-

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

url = "http://www.officequotes.net/no9-23.php"

html = urlopen(url).read()
soup = BeautifulSoup(html, "lxml")

episode = soup.find_all("b")
seasonEpisodeNumber = str(episode[11]).replace("<b>", "").replace("</b>", "").replace(" ", "").replace(
"<br/>", "").replace("\r", "").replace("\t", "").replace('"', "").replace("\n", "")

with open('/Applications/MAMP/htdocs/theoffice/spreadsheets/Season9/%s.csv' % (seasonEpisodeNumber),
      'a') as csvfile:

    writer = csv.writer(csvfile, delimiter='|',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)

    script = soup.find_all("div", {"class": "quote"})

    numberOfLines = 0

    for item in script:
        for element in item:
            quote = str(element)
            quote = re.split(r".*?\<b>(.*)</br>.*", quote)
            for part in quote:
                if part == "<br/>":
                    pass
                elif part == "\n":
                    pass
                else:
                    numberOfLines += 1

    transcript = np.empty([numberOfLines / 2, 2], dtype=object)

    i = 0

    for item in script:
        if "Deleted Scene" in str(item):
            break
        else:
            for element in item:
                quote = str(element)
                print quote
                if "Deleted Scene" in quote:
                    break
                elif "<i>" in quote:
                    break
                elif "[on computer]\n" in quote or "[video" in quote or "fake crying" in quote or "" or "After Dwight and Angela" in quote:
                    break
                else:
                    quote = re.split(r".*?\<b>(.*)</br>.*", quote)
                    for part in quote:
                        part = re.sub(r'\[.*?\]', '', part)
                        if part == "<br/>":
                            break
                        elif part == "\n" or part == "\r\n\t\t\t\t":
                            break
                        elif part[0] == "[":
                            break
                        else:
                            i += 1
                            part = part.replace("<b>", "").replace("</b>", "").replace("'", "").replace(":","").replace("â€¦","").replace("<i>","").replace("</i>","").replace("â€™","").replace("\n","")
                            print str(i) + part
                            if i % 2 == 0:
                                transcript[(i - 1) / 2:((i - 1) / 2) + 1, 1:2] = part
                            else:
                                transcript[(i - 1) / 2:((i - 1) / 2) + 1, 0:1] = part

    for row in transcript:
        if row[0] != None:
            name = row[0]
            print name
            line = row[1]
            print line
            writer.writerow([name, line])