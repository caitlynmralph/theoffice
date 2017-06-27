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

# for season in range(1,10):
    # if season == 1:
    #     print "Season 1"
    #     for episode in range(01,07):
    #         url = "http://www.officequotes.net/no1-0%d.php" % (episode)
    #
    #         html = urlopen(url).read()
    #         soup = BeautifulSoup(html, "lxml")
    #
    #         episode = soup.find_all("b")
    #         seasonEpisodeNumber = str(episode[11]).replace("<b>", "").replace("</b>", "").replace(" ", "").replace(
    #             "<br/>", "").replace("\r", "").replace("\t", "").replace('"', "").replace("\n", "")
    #
    #         with open('/Applications/MAMP/htdocs/theoffice/spreadsheets/Season1/%s.csv' % (seasonEpisodeNumber),
    #                   'a') as csvfile:
    #
    #             writer = csv.writer(csvfile, delimiter='|',
    #                                 quotechar='|', quoting=csv.QUOTE_MINIMAL)
    #
    #             script = soup.find_all("div", {"class": "quote"})
    #
    #             numberOfLines = 0
    #
    #             for item in script:
    #                 for element in item:
    #                     quote = str(element)
    #                     quote = re.split(r".*?\<b>(.*)</br>.*", quote)
    #                     for part in quote:
    #                         if part == "<br/>":
    #                             pass
    #                         elif part == "\n":
    #                             pass
    #                         else:
    #                             numberOfLines += 1
    #
    #             transcript = np.empty([numberOfLines / 2, 2], dtype=object)
    #
    #             i = 0
    #
    #             for item in script:
    #                 if "Deleted Scene" in str(item):
    #                     break
    #                 else:
    #                     for element in item:
    #                         quote = str(element)
    #                         if "Deleted Scene" in quote:
    #                             break
    #                         else:
    #                             quote = re.split(r".*?\<b>(.*)</br>.*", quote)
    #                             for part in quote:
    #                                 part = re.sub(r'\[.*?\]', '', part)
    #                                 if part == "<br/>":
    #                                     break
    #                                 elif part == "\n" or part == "\r\n\t\t\t\t":
    #                                     break
    #                                 elif part[0] == "[":
    #                                     break
    #                                 else:
    #                                     i += 1
    #                                     part = part.replace("<b>", "").replace("</b>", "").replace("'", "").replace(":","").replace("â€¦","").replace("<i>","").replace("</i>","").replace("â€™","").replace("\n","")
    #                                     print str(i) + part
    #                                     if i % 2 == 0:
    #                                         transcript[(i - 1) / 2:((i - 1) / 2) + 1, 1:2] = part
    #                                     else:
    #                                         transcript[(i - 1) / 2:((i - 1) / 2) + 1, 0:1] = part
    #
    #             for row in transcript:
    #                 if row[0] != None:
    #                     name = row[0]
    #                     print name
    #                     line = row[1]
    #                     print line
    #                     writer.writerow([name, line])
    # elif season == 2:
    #     print "Season 2"
    #     for episode in range(1,23):
    #         if episode in range(0,10):
    #             url = "http://www.officequotes.net/no2-0%d.php" % (episode)
    #
    #             html = urlopen(url).read()
    #             soup = BeautifulSoup(html, "lxml")
    #
    #             episode = soup.find_all("b")
    #             seasonEpisodeNumber = str(episode[11]).replace("<b>", "").replace("</b>", "").replace(" ", "").replace(
    #                 "<br/>", "").replace("\r", "").replace("\t", "").replace('"', "").replace("\n", "")
    #
    #             with open('/Applications/MAMP/htdocs/theoffice/spreadsheets/Season2/%s.csv' % (seasonEpisodeNumber),
    #                       'a') as csvfile:
    #
    #                 writer = csv.writer(csvfile, delimiter='|',
    #                                     quotechar='|', quoting=csv.QUOTE_MINIMAL)
    #
    #                 script = soup.find_all("div", {"class": "quote"})
    #
    #                 numberOfLines = 0
    #
    #                 for item in script:
    #                     for element in item:
    #                         quote = str(element)
    #                         quote = re.split(r".*?\<b>(.*)</br>.*", quote)
    #                         for part in quote:
    #                             if part == "<br/>":
    #                                 pass
    #                             elif part == "\n":
    #                                 pass
    #                             else:
    #                                 numberOfLines += 1
    #
    #                 transcript = np.empty([numberOfLines / 2, 2], dtype=object)
    #
    #                 i = 0
    #
    #                 for item in script:
    #                     if "Deleted Scene" in str(item):
    #                         break
    #                     else:
    #                         for element in item:
    #                             quote = str(element)
    #                             if "Deleted Scene" in quote:
    #                                 break
    #                             else:
    #                                 quote = re.split(r'\<b>.*?\</br>', quote)
    #                                 for part in quote:
    #                                     part = re.sub(r'\[.*?\]', '', part)
    #                                     if part == "<br/>":
    #                                         break
    #                                     elif part == "\n" or part == "\r\n\t\t\t\t\t" or part == "\r\n\t\t\t\t" :
    #                                         break
    #                                     else:
    #                                         i += 1
    #                                         part = part.replace("<b>", "").replace("</b>", "").replace("'", "").replace(":","").replace("â€¦","").replace("<i>","").replace("</i>","").replace("â€™","")
    #                                         print str(i) + part
    #                                         if i % 2 == 0:
    #                                             transcript[(i - 1) / 2:((i - 1) / 2) + 1, 1:2] = part
    #                                         else:
    #                                             transcript[(i - 1) / 2:((i - 1) / 2) + 1, 0:1] = part
    #
    #                 for row in transcript:
    #                     if row[0] != None:
    #                         name = row[0]
    #                         print name
    #                         line = row[1]
    #                         print line
    #                         writer.writerow([name, line])
    #         else:
    #             url = "http://www.officequotes.net/no2-%d.php" % (episode)
    #
    #             html = urlopen(url).read()
    #             soup = BeautifulSoup(html, "lxml")
    #
    #             episode = soup.find_all("b")
    #             seasonEpisodeNumber = str(episode[11]).replace("<b>", "").replace("</b>", "").replace(" ", "").replace(
    #                 "<br/>", "").replace("\r", "").replace("\t", "").replace('"', "").replace("\n", "")
    #
    #             with open('/Applications/MAMP/htdocs/theoffice/spreadsheets/Season2/%s.csv' % (seasonEpisodeNumber),
    #                       'a') as csvfile:
    #
    #                 writer = csv.writer(csvfile, delimiter='|',
    #                                     quotechar='|', quoting=csv.QUOTE_MINIMAL)
    #
    #                 script = soup.find_all("div", {"class": "quote"})
    #
    #                 numberOfLines = 0
    #
    #                 for item in script:
    #                     for element in item:
    #                         quote = str(element)
    #                         quote = re.split(r".*?\<b>(.*)</br>.*", quote)
    #                         for part in quote:
    #                             if part == "<br/>":
    #                                 pass
    #                             elif part == "\n":
    #                                 pass
    #                             else:
    #                                 numberOfLines += 1
    #
    #                 transcript = np.empty([numberOfLines / 2, 2], dtype=object)
    #
    #                 i = 0
    #
    #                 for item in script:
    #                     if "Deleted Scene" in str(item):
    #                         break
    #                     else:
    #                         for element in item:
    #                             quote = str(element)
    #                             if "Deleted Scene" in quote:
    #                                 break
    #                             else:
    #                                 quote = re.split(r".*?\<b>(.*)</br>.*", quote)
    #                                 for part in quote:
    #                                     part = re.sub(r'\[.*?\]', '', part)
    #                                     if part == "<br/>":
    #                                         break
    #                                     elif part == "\n" or part == "\r\n\t\t\t\t":
    #                                         break
    #                                     else:
    #                                         i += 1
    #                                         part = part.replace("<b>", "").replace("</b>", "").replace("'", "").replace(":","").replace("â€¦","").replace("<i>","").replace("</i>","").replace("â€™","")
    #                                         print str(i) + part
    #                                         if i % 2 == 0:
    #                                             transcript[(i - 1) / 2:((i - 1) / 2) + 1, 1:2] = part
    #                                         else:
    #                                             transcript[(i - 1) / 2:((i - 1) / 2) + 1, 0:1] = part
    #
    #                 for row in transcript:
    #                     if row[0] != None:
    #                         name = row[0]
    #                         print name
    #                         line = row[1]
    #                         print line
    #                         writer.writerow([name, line])
    # if season == 3:
    #     print "Season 3"
    #     for episode in range(1,24):
    #         if episode in range(0, 10):
    #             url = "http://www.officequotes.net/no3-0%d.php" % (episode)
    #
    #             html = urlopen(url).read()
    #             soup = BeautifulSoup(html, "lxml")
    #
    #             episode = soup.find_all("b")
    #             seasonEpisodeNumber = str(episode[11]).replace("<b>", "").replace("</b>", "").replace(" ", "").replace(
    #                 "<br/>", "").replace("\r", "").replace("\t", "").replace('"', "").replace("\n", "")
    #
    #             with open('/Applications/MAMP/htdocs/theoffice/spreadsheets/Season3/%s.csv' % (seasonEpisodeNumber),
    #                       'a') as csvfile:
    #
    #                 writer = csv.writer(csvfile, delimiter='|',
    #                                     quotechar='|', quoting=csv.QUOTE_MINIMAL)
    #
    #                 script = soup.find_all("div", {"class": "quote"})
    #
    #                 numberOfLines = 0
    #
    #                 for item in script:
    #                     for element in item:
    #                         quote = str(element)
    #                         quote = re.split(r".*?\<b>(.*)</br>.*", quote)
    #                         for part in quote:
    #                             if part == "<br/>":
    #                                 pass
    #                             elif part == "\n":
    #                                 pass
    #                             else:
    #                                 numberOfLines += 1
    #
    #                 transcript = np.empty([numberOfLines / 2, 2], dtype=object)
    #
    #                 i = 0
    #
    #                 for item in script:
    #                     if "Deleted Scene" in str(item):
    #                         print "broke"
    #                         break
    #                     else:
    #                         for element in item:
    #                             quote = str(element)
    #                             if "Deleted Scene" in quote:
    #                                 break
    #                                 print "broke"
    #                             else:
    #                                 print quote
    #                                 quote = re.split(r".*?\<b>(.*)</br>.*", quote)
    #                                 for part in quote:
    #                                     part = re.sub(r'\[.*?\]', '', part)
    #                                     if part == "<br/>":
    #                                         break
    #                                     elif part == "\n" or part == "\r\n\t\t\t\t\t" or part == "\r\n\t\t\t\t":
    #                                         break
    #                                     else:
    #                                         i += 1
    #                                         part = part.replace("<b>", "").replace("</b>", "").replace("'", "").replace(":","").replace("â€¦","").replace("<i>","").replace("</i>","").replace("â€™","")
    #                                         print str(i) + part
    #                                         if i % 2 == 0:
    #                                             transcript[(i - 1) / 2:((i - 1) / 2) + 1, 1:2] = part
    #                                         else:
    #                                             transcript[(i - 1) / 2:((i - 1) / 2) + 1, 0:1] = part
    #
    #                 for row in transcript:
    #                     if row[0] != None:
    #                         name = row[0]
    #                         print name
    #                         line = row[1]
    #                         print line
    #                         writer.writerow([name, line])
    #         else:
    #             url = "http://www.officequotes.net/no3-23.php" # % (episode)
    #
    #             html = urlopen(url).read()
    #             soup = BeautifulSoup(html, "lxml")
    #
    #             episode = soup.find_all("b")
    #             seasonEpisodeNumber = str(episode[11]).replace("<b>", "").replace("</b>", "").replace(" ", "").replace(
    #                 "<br/>", "").replace("\r", "").replace("\t", "").replace('"', "").replace("\n", "")
    #
    #             with open('/Applications/MAMP/htdocs/theoffice/spreadsheets/Season3/%s.csv' % (seasonEpisodeNumber),
    #                       'a') as csvfile:
    #
    #                 writer = csv.writer(csvfile, delimiter='|',
    #                                     quotechar='|', quoting=csv.QUOTE_MINIMAL)
    #
    #                 script = soup.find_all("div", {"class": "quote"})
    #
    #                 numberOfLines = 0
    #
    #                 for item in script:
    #                     for element in item:
    #                         quote = str(element)
    #                         quote = re.split(r".*?\<b>(.*)</br>.*", quote)
    #                         for part in quote:
    #                             if part == "<br/>":
    #                                 pass
    #                             elif part == "\n":
    #                                 pass
    #                             else:
    #                                 numberOfLines += 1
    #
    #                 transcript = np.empty([numberOfLines / 2, 2], dtype=object)
    #
    #                 i = 0
    #
    #                 for item in script:
    #                     if "Deleted Scene" in str(item):
    #                         break
    #                     else:
    #                         for element in item:
    #                             quote = str(element)
    #                             if "Deleted Scene" in quote:
    #                                 break
    #                             else:
    #                                 print quote
    #                                 quote = re.split(r".*?\<b>(.*)</br>.*", quote)
    #                                 for part in quote:
    #                                     part = re.sub(r'\[.*?\]', '', part)
    #                                     if part == "<br/>":
    #                                         break
    #                                     elif part == "\n" or part == "\r\n\t\t\t\t\t" or part == "\r\n\t\t\t\t":
    #                                         break
    #                                     else:
    #                                         if part == "<i>Huge!</i>":
    #                                             continue
    #                                         i += 1
    #                                         part = part.replace("<b>", "").replace("</b>", "").replace("'", "").replace(":","").replace("â€¦","").replace("<i>","").replace("</i>","").replace("â€™","")
    #                                         print str(i) + part
    #                                         if i % 2 == 0:
    #                                             transcript[(i - 1) / 2:((i - 1) / 2) + 1, 1:2] = part
    #                                         else:
    #                                             transcript[(i - 1) / 2:((i - 1) / 2) + 1, 0:1] = part
    #
    #                 for row in transcript:
    #                     if row[0] != None:
    #                         name = row[0]
    #                         print name
    #                         line = row[1]
    #                         print line
    #                         writer.writerow([name, line])
    # elif season == 4:
    #     print "Season 4"
    #     for episode in range(1,15):
    #         if episode in range(0, 10):
    #             url = "http://www.officequotes.net/no4-0%d.php" % (episode)
    #
    #             html = urlopen(url).read()
    #             soup = BeautifulSoup(html, "lxml")
    #
    #             episode = soup.find_all("b")
    #             seasonEpisodeNumber = str(episode[11]).replace("<b>", "").replace("</b>", "").replace(" ", "").replace(
    #                 "<br/>", "").replace("\r", "").replace("\t", "").replace('"', "").replace("\n", "")
    #
    #             with open('/Applications/MAMP/htdocs/theoffice/spreadsheets/Season4/%s.csv' % (seasonEpisodeNumber),
    #                       'a') as csvfile:
    #
    #                 writer = csv.writer(csvfile, delimiter='|',
    #                                     quotechar='|', quoting=csv.QUOTE_MINIMAL)
    #
    #                 script = soup.find_all("div", {"class": "quote"})
    #
    #                 numberOfLines = 0
    #
    #                 for item in script:
    #                     for element in item:
    #                         quote = str(element)
    #                         quote = re.split(r".*?\<b>(.*)</br>.*", quote)
    #                         for part in quote:
    #                             if part == "<br/>":
    #                                 pass
    #                             elif part == "\n":
    #                                 pass
    #                             else:
    #                                 numberOfLines += 1
    #
    #                 transcript = np.empty([numberOfLines / 2, 2], dtype=object)
    #
    #                 i = 0
    #
    #                 for item in script:
    #                     if "Deleted Scene" in str(item):
    #                         break
    #                     else:
    #                         for element in item:
    #                             quote = str(element)
    #                             if "Deleted Scene" in quote:
    #                                 break
    #                             else:
    #                                 quote = re.split(r".*?\<b>(.*)</br>.*", quote)
    #                                 for part in quote:
    #                                     part = re.sub(r'\[.*?\]', '', part)
    #                                     if part == "<br/>":
    #                                         break
    #                                     elif part == "\n" or part == "\r\n\t\t\t\t\t" or part == "\r\n\t\t\t\t":
    #                                         break
    #                                     else:
    #                                         i += 1
    #                                         part = part.replace("<b>", "").replace("</b>", "").replace("'", "").replace(":","").replace("â€¦","").replace("<i>","").replace("</i>","").replace("â€™","")
    #                                         print str(i) + part
    #                                         if i % 2 == 0:
    #                                             transcript[(i - 1) / 2:((i - 1) / 2) + 1, 1:2] = part
    #                                         else:
    #                                             transcript[(i - 1) / 2:((i - 1) / 2) + 1, 0:1] = part
    #
    #                 for row in transcript:
    #                     if row[0] != None:
    #                         name = row[0]
    #                         print name
    #                         line = row[1]
    #                         print line
    #                         writer.writerow([name, line])
    #         else:
    #             url = "http://www.officequotes.net/no4-%d.php" % (episode)
    #
    #             html = urlopen(url).read()
    #             soup = BeautifulSoup(html, "lxml")
    #
    #             episode = soup.find_all("b")
    #             seasonEpisodeNumber = str(episode[11]).replace("<b>", "").replace("</b>", "").replace(" ", "").replace(
    #                 "<br/>", "").replace("\r", "").replace("\t", "").replace('"', "").replace("\n", "")
    #
    #             with open('/Applications/MAMP/htdocs/theoffice/spreadsheets/Season4/%s.csv' % (seasonEpisodeNumber),
    #                       'a') as csvfile:
    #
    #                 writer = csv.writer(csvfile, delimiter='|',
    #                                     quotechar='|', quoting=csv.QUOTE_MINIMAL)
    #
    #                 script = soup.find_all("div", {"class": "quote"})
    #
    #                 numberOfLines = 0
    #
    #                 for item in script:
    #                     for element in item:
    #                         quote = str(element)
    #                         quote = re.split(r".*?\<b>(.*)</br>.*", quote)
    #                         for part in quote:
    #                             if part == "<br/>":
    #                                 pass
    #                             elif part == "\n":
    #                                 pass
    #                             else:
    #                                 numberOfLines += 1
    #
    #                 transcript = np.empty([numberOfLines / 2, 2], dtype=object)
    #
    #                 i = 0
    #
    #                 for item in script:
    #                     if "Deleted Scene" in str(item):
    #                         break
    #                     else:
    #                         for element in item:
    #                             quote = str(element)
    #                             if "Deleted Scene" in quote:
    #                                 break
    #                             else:
    #                                 quote = re.split(r".*?\<b>(.*)</br>.*", quote)
    #                                 for part in quote:
    #                                     part = re.sub(r'\[.*?\]', '', part)
    #                                     if part == "<br/>":
    #                                         break
    #                                     elif part == "\n" or part == "\r\n\t\t\t\t\t" or part == "\r\n\t\t\t\t":
    #                                         break
    #                                     else:
    #                                         i += 1
    #                                         part = part.replace("<b>", "").replace("</b>", "").replace("'", "").replace(":","").replace("â€¦","").replace("<i>","").replace("</i>","").replace("â€™","")
    #                                         print str(i) + part
    #                                         if i % 2 == 0:
    #                                             transcript[(i - 1) / 2:((i - 1) / 2) + 1, 1:2] = part
    #                                         else:
    #                                             transcript[(i - 1) / 2:((i - 1) / 2) + 1, 0:1] = part
    #
    #                 for row in transcript:
    #                     if row[0] != None:
    #                         name = row[0]
    #                         print name
    #                         line = row[1]
    #                         print line
    #                         writer.writerow([name, line])
    # elif season == 5:
    #     print "Season 5"
    #     for episode in range(1,27):
    #         if episode in range(0, 10):
    #             url = "http://www.officequotes.net/no5-0%d.php" % (episode)
    #
    #             html = urlopen(url).read()
    #             soup = BeautifulSoup(html, "lxml")
    #
    #             episode = soup.find_all("b")
    #             seasonEpisodeNumber = str(episode[11]).replace("<b>", "").replace("</b>", "").replace(" ", "").replace(
    #                 "<br/>", "").replace("\r", "").replace("\t", "").replace('"', "").replace("\n", "")
    #
    #             with open('/Applications/MAMP/htdocs/theoffice/spreadsheets/Season5/%s.csv' % (seasonEpisodeNumber),
    #                       'a') as csvfile:
    #
    #                 writer = csv.writer(csvfile, delimiter='|',
    #                                     quotechar='|', quoting=csv.QUOTE_MINIMAL)
    #
    #                 script = soup.find_all("div", {"class": "quote"})
    #
    #                 numberOfLines = 0
    #
    #                 for item in script:
    #                     for element in item:
    #                         quote = str(element)
    #                         quote = re.split(r".*?\<b>(.*)</br>.*", quote)
    #                         for part in quote:
    #                             if part == "<br/>":
    #                                 pass
    #                             elif part == "\n":
    #                                 pass
    #                             else:
    #                                 numberOfLines += 1
    #
    #                 transcript = np.empty([numberOfLines / 2, 2], dtype=object)
    #
    #                 i = 0
    #
    #                 for item in script:
    #                     if "Deleted Scene" in str(item):
    #                         break
    #                     else:
    #                         for element in item:
    #                             quote = str(element)
    #                             if "Deleted Scene" in quote:
    #                                 break
    #                             else:
    #                                 quote = re.split(r".*?\<b>(.*)</br>.*", quote)
    #                                 for part in quote:
    #                                     part = re.sub(r'\[.*?\]', '', part)
    #                                     if part == "<br/>":
    #                                         break
    #                                     elif part == "\n" or part == "\r\n\t\t\t\t\t" or part == "\r\n\t\t\t\t":
    #                                         break
    #                                     else:
    #                                         i += 1
    #                                         part = part.replace("<b>", "").replace("</b>", "").replace("'", "").replace(":","").replace("â€¦","").replace("<i>","").replace("</i>","").replace("â€™","")
    #                                         print str(i) + part
    #                                         if i % 2 == 0:
    #                                             transcript[(i - 1) / 2:((i - 1) / 2) + 1, 1:2] = part
    #                                         else:
    #                                             transcript[(i - 1) / 2:((i - 1) / 2) + 1, 0:1] = part
    #
    #                 for row in transcript:
    #                     if row[0] != None:
    #                         name = row[0]
    #                         print name
    #                         line = row[1]
    #                         print line
    #                         writer.writerow([name, line])
    #         else:
    #             url = "http://www.officequotes.net/no5-%d.php" % (episode)
    #
    #             html = urlopen(url).read()
    #             soup = BeautifulSoup(html, "lxml")
    #
    #             episode = soup.find_all("b")
    #             seasonEpisodeNumber = str(episode[11]).replace("<b>", "").replace("</b>", "").replace(" ", "").replace(
    #                 "<br/>", "").replace("\r", "").replace("\t", "").replace('"', "").replace("\n", "")
    #
    #             with open('/Applications/MAMP/htdocs/theoffice/spreadsheets/Season5/%s.csv' % (seasonEpisodeNumber),
    #                       'a') as csvfile:
    #
    #                 writer = csv.writer(csvfile, delimiter='|',
    #                                     quotechar='|', quoting=csv.QUOTE_MINIMAL)
    #
    #                 script = soup.find_all("div", {"class": "quote"})
    #
    #                 numberOfLines = 0
    #
    #                 for item in script:
    #                     for element in item:
    #                         quote = str(element)
    #                         quote = re.split(r".*?\<b>(.*)</br>.*", quote)
    #                         for part in quote:
    #                             if part == "<br/>":
    #                                 pass
    #                             elif part == "\n" or part == "\r\n\t\t\t\t\t" or part == "\r\n\t\t\t\t":
    #                                 pass
    #                             else:
    #                                 numberOfLines += 1
    #
    #                 transcript = np.empty([numberOfLines / 2, 2], dtype=object)
    #
    #                 i = 0
    #
    #                 for item in script:
    #                     if "Deleted Scene" in str(item):
    #                         break
    #                     else:
    #                         for element in item:
    #                             quote = str(element)
    #                             if "Deleted Scene" in quote:
    #                                 break
    #                             else:
    #                                 if "[previously on The Office...]" in quote:
    #                                     break
    #                                 if "[Jim yawns at desk" in quote:
    #                                     break
    #                                 print quote
    #                                 quote = re.split(r".*?\<b>(.*)</br>.*", quote)
    #                                 for part in quote:
    #                                     part = re.sub(r'\[.*?\]', '', part)
    #                                     if part == "<br/>":
    #                                         break
    #                                     elif part == "\n" or part == "\r\n\t\t\t\t\t" or part == "\r\n\t\t\t\t":
    #                                         break
    #                                     else:
    #                                         i += 1
    #                                         part = part.replace("<b>", "").replace("</b>", "").replace("'", "").replace(":","").replace("â€¦","").replace("<i>","").replace("</i>","").replace("â€™","")
    #                                         print str(i) + part
    #                                         if i % 2 == 0:
    #                                             transcript[(i - 1) / 2:((i - 1) / 2) + 1, 1:2] = part
    #                                         else:
    #                                             transcript[(i - 1) / 2:((i - 1) / 2) + 1, 0:1] = part
    #
    #                 for row in transcript:
    #                     if row[0] != None:
    #                         name = row[0]
    #                         print name
    #                         line = row[1]
    #                         print line
    #                         writer.writerow([name, line])
    # if season == 6:
        # print "Season 6"
        # for episode in range(1,25):
        #     if episode in range(0, 10):
        #         url = "http://www.officequotes.net/no6-0%d.php" % (episode)
        #
        #         html = urlopen(url).read()
        #         soup = BeautifulSoup(html, "lxml")
        #
        #         episode = soup.find_all("b")
        #         seasonEpisodeNumber = str(episode[11]).replace("<b>", "").replace("</b>", "").replace(" ", "").replace(
        #             "<br/>", "").replace("\r", "").replace("\t", "").replace('"', "").replace("\n", "")
        #
        #         with open('/Applications/MAMP/htdocs/theoffice/spreadsheets/Season6/%s.csv' % (seasonEpisodeNumber),
        #                   'a') as csvfile:
        #
        #             writer = csv.writer(csvfile, delimiter='|',
        #                                 quotechar='|', quoting=csv.QUOTE_MINIMAL)
        #
        #             script = soup.find_all("div", {"class": "quote"})
        #
        #             numberOfLines = 0
        #
        #             for item in script:
        #                 for element in item:
        #                     quote = str(element)
        #                     quote = re.split(r".*?\<b>(.*)</br>.*", quote)
        #                     for part in quote:
        #                         if part == "<br/>":
        #                             pass
        #                         elif part == "\n":
        #                             pass
        #                         else:
        #                             numberOfLines += 1
        #
        #             transcript = np.empty([numberOfLines / 2, 2], dtype=object)
        #
        #             i = 0
        #
        #             for item in script:
        #                 if "Deleted Scene" in str(item):
        #                     break
        #                 else:
        #                     for element in item:
        #                         quote = str(element)
        #                         if "Deleted Scene" in quote:
        #                             break
        #                         else:
        #                             quote = re.split(r".*?\<b>(.*)</br>.*", quote)
        #                             for part in quote:
        #                                 part = re.sub(r'\[.*?\]', '', part)
        #                                 if part == "<br/>":
        #                                     break
        #                                 elif part == "\n" or part == "\r\n\t\t\t\t\t" or part == "\r\n\t\t\t\t":
        #                                     break
        #                                 else:
        #                                     i += 1
        #                                     part = part.replace("<b>", "").replace("</b>", "").replace("'", "").replace(":","").replace("â€¦","").replace("<i>","").replace("</i>","").replace("â€™","")
        #                                     print str(i) + part
        #                                     if i % 2 == 0:
        #                                         transcript[(i - 1) / 2:((i - 1) / 2) + 1, 1:2] = part
        #                                     else:
        #                                         transcript[(i - 1) / 2:((i - 1) / 2) + 1, 0:1] = part
        #
        #             for row in transcript:
        #                 if row[0] != None:
        #                     name = row[0]
        #                     print name
        #                     line = row[1]
        #                     print line
        #                     writer.writerow([name, line])
        #     else:
        #         url = "http://www.officequotes.net/no6-20.php" # % (episode)
        #
        #         html = urlopen(url).read()
        #         soup = BeautifulSoup(html, "lxml")
        #
        #         episode = soup.find_all("b")
        #         seasonEpisodeNumber = str(episode[11]).replace("<b>", "").replace("</b>", "").replace(" ", "").replace(
        #             "<br/>", "").replace("\r", "").replace("\t", "").replace('"', "").replace("\n", "")
        #
        #         with open('/Applications/MAMP/htdocs/theoffice/spreadsheets/Season6/%s.csv' % (seasonEpisodeNumber),
        #                   'a') as csvfile:
        #
        #             writer = csv.writer(csvfile, delimiter='|',
        #                                 quotechar='|', quoting=csv.QUOTE_MINIMAL)
        #
        #             script = soup.find_all("div", {"class": "quote"})
        #
        #             numberOfLines = 0
        #
        #             for item in script:
        #                 for element in item:
        #                     quote = str(element)
        #                     quote = re.split(r".*?\<b>(.*)</br>.*", quote)
        #                     for part in quote:
        #                         if part == "<br/>":
        #                             pass
        #                         elif part == "\n":
        #                             pass
        #                         else:
        #                             numberOfLines += 1
        #
        #             transcript = np.empty([numberOfLines / 2, 2], dtype=object)
        #
        #             i = 0
        #
        #             for item in script:
        #                 if "Deleted Scene" in str(item):
        #                     break
        #                 else:
        #                     for element in item:
        #                         quote = str(element)
        #                         if "Deleted Scene" in quote:
        #                             break
        #                         else:
        #                             if "[Andy, Angela, Phyllis" in quote:
        #                                 break
        #                             quote = re.split(r".*?\<b>(.*)</br>.*", quote)
        #                             for part in quote:
        #                                 part = re.sub(r'\[.*?\]', '', part)
        #                                 if part == "<br/>":
        #                                     break
        #                                 elif part == "\n" or part == "\r\n\t\t\t\t\t" or part == "\r\n\t\t\t\t":
        #                                     break
        #                                 else:
        #                                     i += 1
        #                                     part = part.replace("<b>", "").replace("</b>", "").replace("'", "").replace(":","").replace("â€¦","").replace("<i>","").replace("</i>","").replace("â€™","")
        #                                     print str(i) + part
        #                                     if i % 2 == 0:
        #                                         transcript[(i - 1) / 2:((i - 1) / 2) + 1, 1:2] = part
        #                                     else:
        #                                         transcript[(i - 1) / 2:((i - 1) / 2) + 1, 0:1] = part
        #
        #             for row in transcript:
        #                 if row[0] != None:
        #                     name = row[0]
        #                     print name
        #                     line = row[1]
        #                     print line
        #                     writer.writerow([name, line])
    # if season == 7:
    #     print "Season 7"
        # for episode in range(1,25):
        #     if episode in range(0, 10):
        #         url = "http://www.officequotes.net/no7-0%d.php" % (episode)
        #
        #         html = urlopen(url).read()
        #         soup = BeautifulSoup(html, "lxml")
        #
        #         episode = soup.find_all("b")
        #         seasonEpisodeNumber = str(episode[11]).replace("<b>", "").replace("</b>", "").replace(" ", "").replace(
        #             "<br/>", "").replace("\r", "").replace("\t", "").replace('"', "").replace("\n", "")
        #
        #         with open('/Applications/MAMP/htdocs/theoffice/spreadsheets/Season7/%s.csv' % (seasonEpisodeNumber),
        #                   'a') as csvfile:
        #
        #             writer = csv.writer(csvfile, delimiter='|',
        #                                 quotechar='|', quoting=csv.QUOTE_MINIMAL)
        #
        #             script = soup.find_all("div", {"class": "quote"})
        #
        #             numberOfLines = 0
        #
        #             for item in script:
        #                 for element in item:
        #                     quote = str(element)
        #                     quote = re.split(r".*?\<b>(.*)</br>.*", quote)
        #                     for part in quote:
        #                         if part == "<br/>":
        #                             pass
        #                         elif part == "\n":
        #                             pass
        #                         else:
        #                             numberOfLines += 1
        #
        #             transcript = np.empty([numberOfLines / 2, 2], dtype=object)
        #
        #             i = 0
        #
        #             for item in script:
        #                 if "Deleted Scene" in str(item):
        #                     break
        #                 else:
        #                     for element in item:
        #                         quote = str(element)
        #                         if "Deleted Scene" in quote:
        #                             break
        #                         else:
        #                             quote = re.split(r".*?\<b>(.*)</br>.*", quote)
        #                             for part in quote:
        #                                 part = re.sub(r'\[.*?\]', '', part)
        #                                 if part == "<br/>":
        #                                     break
        #                                 elif part == "\n" or part == "\r\n\t\t\t\t\t" or part == "\r\n\t\t\t\t":
        #                                     break
        #                                 else:
        #                                     i += 1
        #                                     part = part.replace("<b>", "").replace("</b>", "").replace("'", "").replace(":","").replace("â€¦","").replace("<i>","").replace("</i>","").replace("â€™","")
        #                                     print str(i) + part
        #                                     if i % 2 == 0:
        #                                         transcript[(i - 1) / 2:((i - 1) / 2) + 1, 1:2] = part
        #                                     else:
        #                                         transcript[(i - 1) / 2:((i - 1) / 2) + 1, 0:1] = part
        #
        #             for row in transcript:
        #                 if row[0] != None:
        #                     name = row[0]
        #                     print name
        #                     line = row[1]
        #                     print line
        #                     writer.writerow([name, line])
        #     else:
                # url = "http://www.officequotes.net/no7-16.php" # % (episode)
                #
                # html = urlopen(url).read()
                # soup = BeautifulSoup(html, "lxml")
                #
                # episode = soup.find_all("b")
                # seasonEpisodeNumber = str(episode[11]).replace("<b>", "").replace("</b>", "").replace(" ", "").replace(
                #     "<br/>", "").replace("\r", "").replace("\t", "").replace('"', "").replace("\n", "")
                #
                # with open('/Applications/MAMP/htdocs/theoffice/spreadsheets/Season7/%s.csv' % (seasonEpisodeNumber),
                #           'a') as csvfile:
                #
                #     writer = csv.writer(csvfile, delimiter='|',
                #                         quotechar='|', quoting=csv.QUOTE_MINIMAL)
                #
                #     script = soup.find_all("div", {"class": "quote"})
                #
                #     numberOfLines = 0
                #
                #     for item in script:
                #         for element in item:
                #             quote = str(element)
                #             quote = re.split(r".*?\<b>(.*)</br>.*", quote)
                #             for part in quote:
                #                 if part == "<br/>":
                #                     pass
                #                 elif part == "\n":
                #                     pass
                #                 else:
                #                     numberOfLines += 1
                #
                #     transcript = np.empty([numberOfLines / 2, 2], dtype=object)
                #
                #     i = 0
                #
                #     for item in script:
                #         if "Deleted Scene" in str(item):
                #             break
                #         else:
                #             for element in item:
                #                 quote = str(element)
                #                 if "[Elevator opens on Andy" in quote:
                #                     break
                #                 elif "Delivery Guy" in quote:
                #                     break
                #                 elif "Samuel" in quote:
                #                     break
                #                 elif "sitting at a desk in the Oval Office]" in quote:
                #                     break
                #                 elif "Narrator" in quote:
                #                     break
                #                 elif "It's your old enemy" in quote:
                #                     break
                #                 elif "with his face painted with" in quote:
                #                     break
                #                 elif "Cherokee Jack" in quote:
                #                     break
                #                 elif "begins to cry as Goldenface laughs" in quote:
                #                     break
                #                 elif "you came in second" in quote:
                #                     break
                #                 elif "acting as a jazz singer" in quote:
                #                     break
                #                 elif "walking into the Funky Cat" in quote:
                #                     break
                #                 elif "singing gibberish while laying" in quote:
                #                     break
                #                 elif "You have to let us go Goldenface" in quote:
                #                     break
                #                 elif "gun and shoots at Michael" in quote:
                #                     break
                #                 elif "More Tylenol" in quote:
                #                     break
                #                 elif "Where had I gone wrong" in quote:
                #                     break
                #                 elif "Beer me Billy" in quote:
                #                     break
                #                 elif "I'm too depressed to save the big game Billy" in quote:
                #                     break
                #                 elif "Why is your face gold" in quote:
                #                     break
                #                 elif "Please Goldenface" in quote:
                #                     break
                #                 elif "Ha ha ha" in quote:
                #                     break
                #                 elif "Some breakfast for me" in quote:
                #                     break
                #                 elif "I need you for another mission" in quote:
                #                     break
                #                 elif "Makes all the girlies feel alright" in quote:
                #                     break
                #                 elif "Deleted Scene" in quote:
                #                     break
                #                 else:
                #                     quote = re.split(r".*?\<b>(.*)</br>.*", quote)
                #                     for part in quote:
                #                         part = re.sub(r'\[.*?\]', '', part)
                #                         if part == "<br/>":
                #                             break
                #                         elif part == "\n" or part == "\r\n\t\t\t\t\t" or part == "\r\n\t\t\t\t":
                #                             break
                #                         else:
                #                             i += 1
                #                             part = part.replace("<b>", "").replace("</b>", "").replace("'", "").replace(":","").replace("â€¦","").replace("<i>","").replace("</i>","").replace("â€™","")
                #                             print str(i) + part
                #                             if i % 2 == 0:
                #                                 transcript[(i - 1) / 2:((i - 1) / 2) + 1, 1:2] = part
                #                             else:
                #                                 transcript[(i - 1) / 2:((i - 1) / 2) + 1, 0:1] = part
                #
                #     for row in transcript:
                #         if row[0] != None:
                #             name = row[0]
                #             print name
                #             line = row[1]
                #             print line
                #             writer.writerow([name, line])
    # elif season == 8:
    #     print "Season 8"
    #     for episode in range(1,25):
    #         if episode in range(0, 10):
    #             url = "http://www.officequotes.net/no8-0%d.php" % (episode)
    #
    #             html = urlopen(url).read()
    #             soup = BeautifulSoup(html, "lxml")
    #
    #             episode = soup.find_all("b")
    #             seasonEpisodeNumber = str(episode[11]).replace("<b>", "").replace("</b>", "").replace(" ", "").replace(
    #                 "<br/>", "").replace("\r", "").replace("\t", "").replace('"', "").replace("\n", "")
    #
    #             with open('/Applications/MAMP/htdocs/theoffice/spreadsheets/Season8/%s.csv' % (seasonEpisodeNumber),
    #                       'a') as csvfile:
    #
    #                 writer = csv.writer(csvfile, delimiter='|',
    #                                     quotechar='|', quoting=csv.QUOTE_MINIMAL)
    #
    #                 script = soup.find_all("div", {"class": "quote"})
    #
    #                 numberOfLines = 0
    #
    #                 for item in script:
    #                     for element in item:
    #                         quote = str(element)
    #                         quote = re.split(r".*?\<b>(.*)</br>.*", quote)
    #                         for part in quote:
    #                             if part == "<br/>":
    #                                 pass
    #                             elif part == "\n":
    #                                 pass
    #                             else:
    #                                 numberOfLines += 1
    #
    #                 transcript = np.empty([numberOfLines / 2, 2], dtype=object)
    #
    #                 i = 0
    #
    #                 for item in script:
    #                     if "Deleted Scene" in str(item):
    #                         break
    #                     else:
    #                         for element in item:
    #                             quote = str(element)
    #                             if "Deleted Scene" in quote:
    #                                 break
    #                             else:
    #                                 quote = re.split(r".*?\<b>(.*)</br>.*", quote)
    #                                 for part in quote:
    #                                     part = re.sub(r'\[.*?\]', '', part)
    #                                     if part == "<br/>":
    #                                         break
    #                                     elif part == "\n" or part == "\r\n\t\t\t\t\t" or part == "\r\n\t\t\t\t":
    #                                         break
    #                                     else:
    #                                         # print part
    #                                         i += 1
    #                                         part = part.replace("<b>", "").replace("</b>", "").replace("'", "").replace(":","").replace("â€¦","").replace("<i>","").replace("</i>","").replace("â€™","").replace("\n","")
    #                                         part = re.sub(r'\[.*?\]', '', part)
    #                                         print str(i) + part
    #                                         if i % 2 == 0:
    #                                             transcript[(i - 1) / 2:((i - 1) / 2) + 1, 1:2] = part
    #                                         else:
    #                                             transcript[(i - 1) / 2:((i - 1) / 2) + 1, 0:1] = part
    #
    #                 for row in transcript:
    #                     if row[0] != None:
    #                         name = row[0]
    #                         print name
    #                         line = row[1]
    #                         print line
    #                         writer.writerow([name, line])
    #         else:
    #             url = "http://www.officequotes.net/no8-%d.php" % (episode)
    #
    #             html = urlopen(url).read()
    #             soup = BeautifulSoup(html, "lxml")
    #
    #             episode = soup.find_all("b")
    #             seasonEpisodeNumber = str(episode[11]).replace("<b>", "").replace("</b>", "").replace(" ", "").replace(
    #                 "<br/>", "").replace("\r", "").replace("\t", "").replace('"', "").replace("\n", "")
    #
    #             with open('/Applications/MAMP/htdocs/theoffice/spreadsheets/Season8/%s.csv' % (seasonEpisodeNumber),
    #                       'a') as csvfile:
    #
    #                 writer = csv.writer(csvfile, delimiter='|',
    #                                     quotechar='|', quoting=csv.QUOTE_MINIMAL)
    #
    #                 script = soup.find_all("div", {"class": "quote"})
    #
    #                 numberOfLines = 0
    #
    #                 for item in script:
    #                     for element in item:
    #                         quote = str(element)
    #                         quote = re.split(r".*?\<b>(.*)</br>.*", quote)
    #                         for part in quote:
    #                             if part == "<br/>":
    #                                 pass
    #                             elif part == "\n":
    #                                 pass
    #                             else:
    #                                 numberOfLines += 1
    #
    #                 transcript = np.empty([numberOfLines / 2, 2], dtype=object)
    #
    #                 i = 0
    #
    #                 for item in script:
    #                     if "Deleted Scene" in str(item):
    #                         break
    #                     else:
    #                         for element in item:
    #                             quote = str(element)
    #                             if "Deleted Scene" in quote:
    #                                 break
    #                             else:
    #                                 quote = re.split(r".*?\<b>(.*)</br>.*", quote)
    #                                 for part in quote:
    #                                     part = re.sub(r'\[.*?\]', '', part)
    #                                     if part == "<br/>":
    #                                         break
    #                                     elif part == "\n" or part == "\r\n\t\t\t\t\t" or part == "\r\n\t\t\t\t":
    #                                         break
    #                                     else:
    #                                         i += 1
    #                                         part = part.replace("<b>", "").replace("</b>", "").replace("'", "").replace(":","").replace("â€¦","").replace("<i>","").replace("</i>","").replace("â€™","").replace("\n","")
    #                                         print str(i) + part
    #                                         if i % 2 == 0:
    #                                             transcript[(i - 1) / 2:((i - 1) / 2) + 1, 1:2] = part
    #                                         else:
    #                                             transcript[(i - 1) / 2:((i - 1) / 2) + 1, 0:1] = part
    #
    #                 for row in transcript:
    #                     if row[0] != None:
    #                         name = row[0]
    #                         print name
    #                         line = row[1]
    #                         print line
    #                         writer.writerow([name, line])
    # else:
    #     print "Season 9"
    #     for episode in range(1,24):
    #         if episode in range(0, 10):
    #             url = "http://www.officequotes.net/no9-0%d.php" % (episode)
    #
    #             html = urlopen(url).read()
    #             soup = BeautifulSoup(html, "lxml")
    #
    #             episode = soup.find_all("b")
    #             seasonEpisodeNumber = str(episode[11]).replace("<b>", "").replace("</b>", "").replace(" ", "").replace(
    #                 "<br/>", "").replace("\r", "").replace("\t", "").replace('"', "").replace("\n", "")
    #
    #             with open('/Applications/MAMP/htdocs/theoffice/spreadsheets/Season9/%s.csv' % (seasonEpisodeNumber),
    #                       'a') as csvfile:
    #
    #                 writer = csv.writer(csvfile, delimiter='|',
    #                                     quotechar='|', quoting=csv.QUOTE_MINIMAL)
    #
    #                 script = soup.find_all("div", {"class": "quote"})
    #
    #                 numberOfLines = 0
    #
    #                 for item in script:
    #                     for element in item:
    #                         quote = str(element)
    #                         quote = re.split(r".*?\<b>(.*)</br>.*", quote)
    #                         for part in quote:
    #                             if part == "<br/>":
    #                                 pass
    #                             elif part == "\n":
    #                                 pass
    #                             else:
    #                                 numberOfLines += 1
    #
    #                 transcript = np.empty([numberOfLines / 2, 2], dtype=object)
    #
    #                 i = 0
    #
    #                 for item in script:
    #                     if "Deleted Scene" in str(item):
    #                         break
    #                     else:
    #                         for element in item:
    #                             quote = str(element)
    #                             if "Deleted Scene" in quote:
    #                                 break
    #                             else:
    #                                 quote = re.split(r".*?\<b>(.*)</br>.*", quote)
    #                                 for part in quote:
    #                                     part = re.sub(r'\[.*?\]', '', part)
    #                                     if part == "<br/>":
    #                                         break
    #                                     elif part == "\n" or part == "\r\n\t\t\t\t\t" or part == "\r\n\t\t\t\t":
    #                                         break
    #                                     else:
    #                                         i += 1
    #                                         part = part.replace("<b>", "").replace("</b>", "").replace("'", "").replace(":","").replace("â€¦","").replace("<i>","").replace("</i>","").replace("â€™","").replace("\n","")
    #                                         print str(i) + part
    #                                         if i % 2 == 0:
    #                                             transcript[(i - 1) / 2:((i - 1) / 2) + 1, 1:2] = part
    #                                         else:
    #                                             transcript[(i - 1) / 2:((i - 1) / 2) + 1, 0:1] = part
    #
    #                 for row in transcript:
    #                     if row[0] != None:
    #                         name = row[0]
    #                         print name
    #                         line = row[1]
    #                         print line
    #                         writer.writerow([name, line])
    #         else:
    #             url = "http://www.officequotes.net/no9-%d.php" % (episode)
    #
    #             html = urlopen(url).read()
    #             soup = BeautifulSoup(html, "lxml")
    #
    #             episode = soup.find_all("b")
    #             seasonEpisodeNumber = str(episode[11]).replace("<b>", "").replace("</b>", "").replace(" ", "").replace(
    #                 "<br/>", "").replace("\r", "").replace("\t", "").replace('"', "").replace("\n", "")
    #
    #             with open('/Applications/MAMP/htdocs/theoffice/spreadsheets/Season9/%s.csv' % (seasonEpisodeNumber),
    #                       'a') as csvfile:
    #
    #                 writer = csv.writer(csvfile, delimiter='|',
    #                                     quotechar='|', quoting=csv.QUOTE_MINIMAL)
    #
    #                 script = soup.find_all("div", {"class": "quote"})
    #
    #                 numberOfLines = 0
    #
    #                 for item in script:
    #                     for element in item:
    #                         quote = str(element)
    #                         quote = re.split(r".*?\<b>(.*)</br>.*", quote)
    #                         for part in quote:
    #                             if part == "<br/>":
    #                                 pass
    #                             elif part == "\n" or part == "\r\n\t\t\t\t\t" or part == "\r\n\t\t\t\t":
    #                                 pass
    #                             else:
    #                                 numberOfLines += 1
    #
    #                 transcript = np.empty([numberOfLines / 2, 2], dtype=object)
    #
    #                 i = 0
    #
    #                 for item in script:
    #                     if "Deleted Scene" in str(item):
    #                         break
    #                     else:
    #                         for element in item:
    #                             quote = str(element)
    #                             if "Deleted Scene" in quote:
    #                                 break
    #                             else:
    #                                 quote = re.split(r".*?\<b>(.*)</br>.*", quote)
    #                                 for part in quote:
    #                                     part = re.sub(r'\[.*?\]', '', part)
    #                                     if part == "<br/>":
    #                                         break
    #                                     elif part == "\n":
    #                                         break
    #                                     else:
    #                                         i += 1
    #                                         part = part.replace("<b>", "").replace("</b>", "").replace("'", "").replace(":","").replace("â€¦","").replace("<i>","").replace("</i>","").replace("â€™","").replace("\n","")
    #                                         print str(i) + part
    #                                         if i % 2 == 0:
    #                                             transcript[(i - 1) / 2:((i - 1) / 2) + 1, 1:2] = part
    #                                         else:
    #                                             transcript[(i - 1) / 2:((i - 1) / 2) + 1, 0:1] = part
    #
    #                 for row in transcript:
    #                     if row[0] != None:
    #                         name = row[0]
    #                         print name
    #                         line = row[1]
    #                         print line
    #                         writer.writerow([name, line])