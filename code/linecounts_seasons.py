import re
import sys
import csv
from urllib2 import urlopen
from bs4 import BeautifulSoup
import numpy as np
import os
import string

os.chdir('/Applications/MAMP/htdocs/theoffice/spreadsheets')

reload(sys)
sys.setdefaultencoding("utf-8")

with open('/Applications/MAMP/htdocs/theoffice/spreadsheets/linecounts_seasons.csv', 'a') as csvfile:

    writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

    counts = np.zeros([1,10], dtype=object)
    characters = []

    for season in range(1,10):
        if season == 1:
            episodeNames = ["Pilot", "DiversityDay", "HealthCare","TheAlliance","Basketball","HotGirl"]
            for episode in range(01,07):
                print '/Season%s/Season%s-Episode0%s%s.csv' % (str(season), str(season), str(episode), episodeNames[episode-1])
                c = np.genfromtxt(
                    '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode0%s%s.csv' % (str(season), str(season), str(episode), episodeNames[episode-1]),
                    delimiter="|", dtype=str, skiprows=0)
                transcript = c[:]
                punc = False
                for i in range(0, len(transcript)):
                    for x in transcript[i:i+1,0:1][0][0]:
                        if x in string.punctuation:
                            punc = True
                            break
                    if len(transcript[i:i+1,0:1][0][0]) > 15 or punc == True:
                        continue
                    elif transcript[i:i+1,0:1][0][0] not in characters:
                        characters.append(transcript[i:i + 1, 0:2][0][0])
                        row = np.reshape([transcript[i:i + 1, 0:1][0][0], 1,0,0,0,0,0,0,0,0], [1, 10])
                        counts = np.append(counts, row, axis=0)
                    else:
                        for x in range(0, len(counts)):
                            if counts[x:x + 1, 0:1][0][0] == transcript[i:i + 1, 0:1][0][0]:
                                counts[x:x + 1, 1:2] = int(counts[x:x + 1, 1:2][0][0]) + 1
                                continue

        elif season == 2:
            episodeNames = ["TheDundies","SexualHarassment","OfficeOlympics","TheFire","Halloween","TheFight","TheClient","PerformanceReview","E-mailSurveillance","ChristmasParty",
                            "BoozeCruise","TheInjury","TheSecret","TheCarpet","BoysandGirls","Valentine'sDay","Dwight'sSpeech","TakeYourDaughtertoWorkDay","Michael'sBirthday","DrugTesting",
                            "ConflictResolution", "CasinoNight"]
            for episode in range(1,23):
                if episode in range(0,10):
                    print '/Season%s/Season%s-Episode0%s%s.csv' % (str(season), str(season), str(episode), episodeNames[episode - 1])
                    c = np.genfromtxt('/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode0%s%s.csv' % (str(season), str(season), str(episode), episodeNames[episode - 1]),delimiter="|", dtype=str, skiprows=0)
                    transcript = c[:]
                    punc = False
                    for i in range(0, len(transcript)):
                        for x in transcript[i:i + 1, 0:1][0][0]:
                            if x in string.punctuation:
                                punc = True
                                break
                        if len(transcript[i:i + 1, 0:1][0][0]) > 15 or punc == True:
                            continue
                        elif transcript[i:i + 1, 0:1][0][0] not in characters:
                            characters.append(transcript[i:i + 1, 0:2][0][0])
                            row = np.reshape([transcript[i:i + 1, 0:1][0][0], 0,1,0,0,0,0,0,0,0], [1, 10])
                            counts = np.append(counts, row, axis=0)
                        else:
                            for x in range(0, len(counts)):
                                if counts[x:x + 1, 0:1][0][0] == transcript[i:i + 1, 0:1][0][0]:
                                    counts[x:x + 1, 2:3] = int(counts[x:x + 1, 2:3][0][0]) + 1
                                    continue
                else:
                    print '/Season%s/Season%s-Episode%s%s.csv' % (str(season), str(season), str(episode), episodeNames[episode - 1])
                    c = np.genfromtxt('/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode%s%s.csv' % (str(season), str(season), str(episode), episodeNames[episode - 1]),
                        delimiter="|", dtype=str, skiprows=0)
                    transcript = c[:]
                    punc = False
                    for i in range(0, len(transcript)):
                        for x in transcript[i:i + 1, 0:1][0][0]:
                            if x in string.punctuation:
                                punc = True
                                break
                        if len(transcript[i:i + 1, 0:1][0][0]) > 15 or punc == True:
                            continue
                        elif transcript[i:i + 1, 0:1][0][0] not in characters:
                            characters.append(transcript[i:i + 1, 0:2][0][0])
                            row = np.reshape([transcript[i:i + 1, 0:1][0][0], 0,1,0,0,0,0,0,0,0], [1, 10])
                            counts = np.append(counts, row, axis=0)
                        else:
                            for x in range(0, len(counts)):
                                if counts[x:x + 1, 0:1][0][0] == transcript[i:i + 1, 0:1][0][0]:
                                    counts[x:x + 1, 2:3] = int(counts[x:x + 1, 2:3][0][0]) + 1
                                    continue
        elif season == 3:
            episodeNames = ["GayWitchHunt", "TheConvention","TheCoup","GriefCounseling","Initiation","Diwali","BranchClosing","TheMerger","TheConvict","ABenihanaChristmas",
                            "BackFromVacation","TravelingSalesmen","TheReturn","BenFranklin","Phyllis'Wedding","BusinessSchool","Cocktails","TheNegotiation","SafetyTraining",
                            "ProductRecall","Women'sAppreciation","BeachGames","TheJob"]
            for episode in range(1,24):
                if episode in range(0,10):
                    print '/Season%s/Season%s-Episode0%s%s.csv' % (
                        str(season), str(season), str(episode), episodeNames[episode - 1])
                    c = np.genfromtxt(
                        '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode0%s%s.csv' % (
                        str(season), str(season), str(episode), episodeNames[episode - 1]), delimiter="|", dtype=str,
                        skiprows=0)
                    transcript = c[:]
                    punc = False
                    for i in range(0, len(transcript)):
                        for x in transcript[i:i + 1, 0:1][0][0]:
                            if x in string.punctuation:
                                punc = True
                                break
                        if len(transcript[i:i + 1, 0:1][0][0]) > 15 or punc == True:
                            continue
                        elif transcript[i:i + 1, 0:1][0][0] not in characters:
                            characters.append(transcript[i:i + 1, 0:2][0][0])
                            row = np.reshape([transcript[i:i + 1, 0:1][0][0],0,0,1,0,0,0,0,0,0], [1, 10])
                            counts = np.append(counts, row, axis=0)
                        else:
                            for x in range(0, len(counts)):
                                if counts[x:x + 1, 0:1][0][0] == transcript[i:i + 1, 0:1][0][0]:
                                    counts[x:x + 1, 3:4] = int(counts[x:x + 1, 3:4][0][0]) + 1
                                    continue
                else:
                    print '/Season%s/Season%s-Episode%s%s.csv' % (
                    str(season), str(season), str(episode), episodeNames[episode - 1])
                    c = np.genfromtxt(
                        '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode%s%s.csv' % (
                        str(season), str(season), str(episode), episodeNames[episode - 1]),
                        delimiter="|", dtype=str, skiprows=0)
                    transcript = c[:]
                    punc = False
                    for i in range(0, len(transcript)):
                        for x in transcript[i:i + 1, 0:1][0][0]:
                            if x in string.punctuation:
                                punc = True
                                break
                        if len(transcript[i:i + 1, 0:1][0][0]) > 15 or punc == True:
                            continue
                        elif transcript[i:i + 1, 0:1][0][0] not in characters:
                            characters.append(transcript[i:i + 1, 0:2][0][0])
                            row = np.reshape([transcript[i:i + 1, 0:1][0][0], 0,0,1,0,0,0,0,0,0], [1, 10])
                            counts = np.append(counts, row, axis=0)
                        else:
                            for x in range(0, len(counts)):
                                if counts[x:x + 1, 0:1][0][0] == transcript[i:i + 1, 0:1][0][0]:
                                    counts[x:x + 1, 3:4] = int(counts[x:x + 1, 3:4][0][0]) + 1
                                    continue
        elif season == 4:
            episodeNames = ["FunRun","DunderMifflinInfinity","LaunchParty","Money","LocalAd","BranchWars","SurvivorMan","TheDeposition","DinnerParty","ChairModel","NightOut",
                            "DidIStutter?","JobFair","GoodbyeToby"]
            for episode in range(1,15):
                if episode in range(0,10):
                    print '/Season%s/Season%s-Episode0%s%s.csv' % (
                        str(season), str(season), str(episode), episodeNames[episode - 1])
                    c = np.genfromtxt(
                        '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode0%s%s.csv' % (
                        str(season), str(season), str(episode), episodeNames[episode - 1]), delimiter="|", dtype=str,
                        skiprows=0)
                    transcript = c[:]
                    punc = False
                    for i in range(0, len(transcript)):
                        for x in transcript[i:i + 1, 0:1][0][0]:
                            if x in string.punctuation:
                                punc = True
                                break
                        if len(transcript[i:i + 1, 0:1][0][0]) > 15 or punc == True:
                            continue
                        elif transcript[i:i + 1, 0:1][0][0] not in characters:
                            characters.append(transcript[i:i + 1, 0:2][0][0])
                            row = np.reshape([transcript[i:i + 1, 0:1][0][0], 0,0,0,1,0,0,0,0,0], [1, 10])
                            counts = np.append(counts, row, axis=0)
                        else:
                            for x in range(0, len(counts)):
                                if counts[x:x + 1, 0:1][0][0] == transcript[i:i + 1, 0:1][0][0]:
                                    counts[x:x + 1, 4:5] = int(counts[x:x + 1, 4:5][0][0]) + 1
                                    continue
                else:
                    print '/Season%s/Season%s-Episode%s%s.csv' % (
                    str(season), str(season), str(episode), episodeNames[episode - 1])
                    c = np.genfromtxt(
                        '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode%s%s.csv' % (
                        str(season), str(season), str(episode), episodeNames[episode - 1]),
                        delimiter="|", dtype=str, skiprows=0)
                    transcript = c[:]
                    punc = False
                    for i in range(0, len(transcript)):
                        for x in transcript[i:i + 1, 0:1][0][0]:
                            if x in string.punctuation:
                                punc = True
                                break
                        if len(transcript[i:i + 1, 0:1][0][0]) > 15 or punc == True:
                            continue
                        elif transcript[i:i + 1, 0:1][0][0] not in characters:
                            characters.append(transcript[i:i + 1, 0:2][0][0])
                            row = np.reshape([transcript[i:i + 1, 0:1][0][0], 0,0,0,1,0,0,0,0,0], [1, 10])
                            counts = np.append(counts, row, axis=0)
                        else:
                            for x in range(0, len(counts)):
                                if counts[x:x + 1, 0:1][0][0] == transcript[i:i + 1, 0:1][0][0]:
                                    counts[x:x + 1, 4:5] = int(counts[x:x + 1, 4:5][0][0]) + 1
                                    continue
        elif season == 5:
            episodeNames = ["WeightLoss","BusinessEthics","BabyShower","CrimeAid","EmployeeTransfer","CustomerSurvey","BusinessTrip","FrameToby","TheSurplus","MoroccanChristmas",
                            "TheDuel","PrinceFamilyPaper","StressRelief","LectureCircuitPart1","LectureCircuitPart2","BloodDrive","GoldenTicket","NewBoss","TwoWeeks","DreamTeam",
                            "MichaelScottPaperCompany","HeavyCompetition","Broke","CasualFriday","CafeDisco","CompanyPicnic"]
            for episode in range(1,27):
                if episode in range(0,10):
                    print '/Season%s/Season%s-Episode0%s%s.csv' % (
                        str(season), str(season), str(episode), episodeNames[episode - 1])
                    c = np.genfromtxt(
                        '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode0%s%s.csv' % (
                        str(season), str(season), str(episode), episodeNames[episode - 1]), delimiter="|", dtype=str,
                        skiprows=0)
                    transcript = c[:]
                    punc = False
                    for i in range(0, len(transcript)):
                        for x in transcript[i:i + 1, 0:1][0][0]:
                            if x in string.punctuation:
                                punc = True
                                break
                        if len(transcript[i:i + 1, 0:1][0][0]) > 15 or punc == True:
                            continue
                        elif transcript[i:i + 1, 0:1][0][0] not in characters:
                            characters.append(transcript[i:i + 1, 0:2][0][0])
                            row = np.reshape([transcript[i:i + 1, 0:1][0][0], 0,0,0,0,1,0,0,0,0], [1, 10])
                            counts = np.append(counts, row, axis=0)
                        else:
                            for x in range(0, len(counts)):
                                if counts[x:x + 1, 0:1][0][0] == transcript[i:i + 1, 0:1][0][0]:
                                    counts[x:x + 1, 5:6] = int(counts[x:x + 1, 5:6][0][0]) + 1
                                    continue
                else:
                    print '/Season%s/Season%s-Episode%s%s.csv' % (
                    str(season), str(season), str(episode), episodeNames[episode - 1])
                    c = np.genfromtxt(
                        '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode%s%s.csv' % (
                        str(season), str(season), str(episode), episodeNames[episode - 1]),
                        delimiter="|", dtype=str, skiprows=0)
                    transcript = c[:]
                    punc = False
                    for i in range(0, len(transcript)):
                        for x in transcript[i:i + 1, 0:1][0][0]:
                            if x in string.punctuation:
                                punc = True
                                break
                        if len(transcript[i:i + 1, 0:1][0][0]) > 15 or punc == True:
                            continue
                        elif transcript[i:i + 1, 0:1][0][0] not in characters:
                            characters.append(transcript[i:i + 1, 0:2][0][0])
                            row = np.reshape([transcript[i:i + 1, 0:1][0][0], 0,0,0,0,1,0,0,0,0], [1, 10])
                            counts = np.append(counts, row, axis=0)
                        else:
                            for x in range(0, len(counts)):
                                if counts[x:x + 1, 0:1][0][0] == transcript[i:i + 1, 0:1][0][0]:
                                    counts[x:x + 1, 5:6] = int(counts[x:x + 1, 5:6][0][0]) + 1
                                    continue
        elif season == 6:
            episodeNames = ["Gossip","TheMeeting","ThePromotion","Niagara","Mafia","TheLover","KoiPond","DoubleDate","Murder","ShareholderMeeting","Scott'sTots","SecretSanta","TheBanker",
                            "Sabre","ManagerandSalesman","TheDelivery","St.Patrick'sDay","NewLeads","HappyHour","Secretary'sDay","BodyLanguage","TheCover-Up","TheChump","Whistleblower"]
            for episode in range(1,25):
                if episode in range(0,10):
                    print '/Season%s/Season%s-Episode0%s%s.csv' % (
                        str(season), str(season), str(episode), episodeNames[episode - 1])
                    c = np.genfromtxt(
                        '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode0%s%s.csv' % (
                            str(season), str(season), str(episode), episodeNames[episode - 1]), delimiter="|", dtype=str,
                        skiprows=0)
                    transcript = c[:]
                    punc = False
                    for i in range(0, len(transcript)):
                        for x in transcript[i:i + 1, 0:1][0][0]:
                            if x in string.punctuation:
                                punc = True
                                break
                        if len(transcript[i:i + 1, 0:1][0][0]) > 15 or punc == True:
                            continue
                        elif transcript[i:i + 1, 0:1][0][0] not in characters:
                            characters.append(transcript[i:i + 1, 0:2][0][0])
                            row = np.reshape([transcript[i:i + 1, 0:1][0][0], 0,0,0,0,0,1,0,0,0], [1, 10])
                            counts = np.append(counts, row, axis=0)
                        else:
                            for x in range(0, len(counts)):
                                if counts[x:x + 1, 0:1][0][0] == transcript[i:i + 1, 0:1][0][0]:
                                    counts[x:x + 1, 6:7] = int(counts[x:x + 1, 6:7][0][0]) + 1
                                    continue
                else:
                    print '/Season%s/Season%s-Episode%s%s.csv' % (
                        str(season), str(season), str(episode), episodeNames[episode - 1])
                    c = np.genfromtxt(
                        '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode%s%s.csv' % (
                            str(season), str(season), str(episode), episodeNames[episode - 1]),
                        delimiter="|", dtype=str, skiprows=0)
                    transcript = c[:]
                    punc = False
                    for i in range(0, len(transcript)):
                        for x in transcript[i:i + 1, 0:1][0][0]:
                            if x in string.punctuation:
                                punc = True
                                break
                        if len(transcript[i:i + 1, 0:1][0][0]) > 15 or punc == True:
                            continue
                        elif transcript[i:i + 1, 0:1][0][0] not in characters:
                            characters.append(transcript[i:i + 1, 0:2][0][0])
                            row = np.reshape([transcript[i:i + 1, 0:1][0][0], 0,0,0,0,0,1,0,0,0], [1, 10])
                            counts = np.append(counts, row, axis=0)
                        else:
                            for x in range(0, len(counts)):
                                if counts[x:x + 1, 0:1][0][0] == transcript[i:i + 1, 0:1][0][0]:
                                    counts[x:x + 1, 6:7] = int(counts[x:x + 1, 6:7][0][0]) + 1
                                    continue
        elif season == 7:
            episodeNames = ["Nepotism","Counseling","Andy'sPlay","SexEd","TheSting","CostumeContest","Christening","ViewingParty","WUPHF.com","China","ClassyChristmas","Ultimatum",
                            "TheSeminar","TheSearch","PDA","ThreatLevelMidnight","ToddPacker","GarageSale","TrainingDay","Michael'sLastDundies","GoodbyeMichael","TheInnerCircle",
                            "DwightK.Schrute(Acting)Manager","SearchCommittee"]
            for episode in range(1,25):
                if episode in range(0,10):
                    print '/Season%s/Season%s-Episode0%s%s.csv' % (
                        str(season), str(season), str(episode), episodeNames[episode - 1])
                    c = np.genfromtxt(
                        '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode0%s%s.csv' % (
                            str(season), str(season), str(episode), episodeNames[episode - 1]), delimiter="|", dtype=str,
                        skiprows=0)
                    transcript = c[:]
                    punc = False
                    for i in range(0, len(transcript)):
                        for x in transcript[i:i + 1, 0:1][0][0]:
                            if x in string.punctuation:
                                punc = True
                                break
                        if len(transcript[i:i + 1, 0:1][0][0]) > 15 or punc == True:
                            continue
                        elif transcript[i:i + 1, 0:1][0][0] not in characters:
                            characters.append(transcript[i:i + 1, 0:2][0][0])
                            row = np.reshape([transcript[i:i + 1, 0:1][0][0], 0,0,0,0,0,0,1,0,0], [1, 10])
                            counts = np.append(counts, row, axis=0)
                        else:
                            for x in range(0, len(counts)):
                                if counts[x:x + 1, 0:1][0][0] == transcript[i:i + 1, 0:1][0][0]:
                                    counts[x:x + 1, 7:8] = int(counts[x:x + 1, 7:8][0][0]) + 1
                                    continue
                else:
                    print '/Season%s/Season%s-Episode%s%s.csv' % (
                        str(season), str(season), str(episode), episodeNames[episode - 1])
                    c = np.genfromtxt(
                        '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode%s%s.csv' % (
                            str(season), str(season), str(episode), episodeNames[episode - 1]),
                        delimiter="|", dtype=str, skiprows=0)
                    transcript = c[:]
                    punc = False
                    for i in range(0, len(transcript)):
                        for x in transcript[i:i + 1, 0:1][0][0]:
                            if x in string.punctuation:
                                punc = True
                                break
                        if len(transcript[i:i + 1, 0:1][0][0]) > 15 or punc == True:
                            continue
                        elif transcript[i:i + 1, 0:1][0][0] not in characters:
                            characters.append(transcript[i:i + 1, 0:2][0][0])
                            row = np.reshape([transcript[i:i + 1, 0:1][0][0], 0,0,0,0,0,0,1,0,0], [1, 10])
                            counts = np.append(counts, row, axis=0)
                        else:
                            for x in range(0, len(counts)):
                                if counts[x:x + 1, 0:1][0][0] == transcript[i:i + 1, 0:1][0][0]:
                                    counts[x:x + 1, 7:8] = int(counts[x:x + 1, 7:8][0][0]) + 1
                                    continue
        elif season == 8:
            episodeNames = ["TheList","TheIncentive","Lotto","GardenParty","Spooked","Doomsday","Pam'sReplacement","Gettysburg","Mrs.California","ChristmasWishes","Trivia","PoolParty",
                            "JuryDuty","SpecialProject","Tallahasse","AfterHours","TesttheStore","LastDayInFlorida","GetTheGirl","WelcomeParty","AngryAndy","Fundraiser","TurfWar",
                            "FreeFamilyPortraitStudio"]
            for episode in range(1,25):
                if episode in range(0,10):
                    print '/Season%s/Season%s-Episode0%s%s.csv' % (
                        str(season), str(season), str(episode), episodeNames[episode - 1])
                    c = np.genfromtxt(
                        '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode0%s%s.csv' % (
                            str(season), str(season), str(episode), episodeNames[episode - 1]), delimiter="|", dtype=str,
                        skiprows=0)
                    transcript = c[:]
                    punc = False
                    for i in range(0, len(transcript)):
                        for x in transcript[i:i + 1, 0:1][0][0]:
                            if x in string.punctuation:
                                punc = True
                                break
                        if len(transcript[i:i + 1, 0:1][0][0]) > 15 or punc == True:
                            continue
                        elif transcript[i:i + 1, 0:1][0][0] not in characters:
                            characters.append(transcript[i:i + 1, 0:2][0][0])
                            row = np.reshape([transcript[i:i + 1, 0:1][0][0], 0,0,0,0,0,0,0,1,0], [1, 10])
                            counts = np.append(counts, row, axis=0)
                        else:
                            for x in range(0, len(counts)):
                                if counts[x:x + 1, 0:1][0][0] == transcript[i:i + 1, 0:1][0][0]:
                                    counts[x:x + 1, 8:9] = int(counts[x:x + 1, 8:9][0][0]) + 1
                                    continue
                else:
                    print '/Season%s/Season%s-Episode%s%s.csv' % (
                        str(season), str(season), str(episode), episodeNames[episode - 1])
                    c = np.genfromtxt(
                        '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode%s%s.csv' % (
                            str(season), str(season), str(episode), episodeNames[episode - 1]),
                        delimiter="|", dtype=str, skiprows=0)
                    transcript = c[:]
                    punc = False
                    for i in range(0, len(transcript)):
                        for x in transcript[i:i + 1, 0:1][0][0]:
                            if x in string.punctuation:
                                punc = True
                                break
                        if len(transcript[i:i + 1, 0:1][0][0]) > 15 or punc == True:
                            continue
                        elif transcript[i:i + 1, 0:1][0][0] not in characters:
                            characters.append(transcript[i:i + 1, 0:2][0][0])
                            row = np.reshape([transcript[i:i + 1, 0:1][0][0], 0,0,0,0,0,0,0,1,0], [1, 10])
                            counts = np.append(counts, row, axis=0)
                        else:
                            for x in range(0, len(counts)):
                                if counts[x:x + 1, 0:1][0][0] == transcript[i:i + 1, 0:1][0][0]:
                                    counts[x:x + 1, 8:9] = int(counts[x:x + 1, 8:9][0][0]) + 1
                                    continue
        else:
            episodeNames = ["NewGuys","Roy'sWedding","AndysAncestry","WorkBus","HereComesTreble","TheBoat","TheWhale","TheTarget","DwightChristmas","Lice","SuitWarehouse",
                            "CustomerLoyalty","JuniorSalesman","Vandalism","CouplesDiscount","MovingOn","TheFarm","Promos","Stairmageddon","PaperAirplane","Livin'TheDream",
                            "AARM","Finale"]
            for episode in range(1,24):
                print '/Season%s/Season%s-Episode%s%s.csv' % (
                    str(season), str(season), str(episode), episodeNames[episode - 1])
                c = np.genfromtxt(
                    '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode%s%s.csv' % (
                        str(season), str(season), str(episode), episodeNames[episode - 1]),
                    delimiter="|", dtype=str, skiprows=0)
                transcript = c[:]
                punc = False
                for i in range(0, len(transcript)):
                    for x in transcript[i:i+1,0:1][0][0]:
                        if x in string.punctuation:
                            punc = True
                            break
                    if len(transcript[i:i+1,0:1][0][0]) > 15 or punc == True:
                        continue
                    elif transcript[i:i+1,0:1][0][0] not in characters:
                        characters.append(transcript[i:i + 1, 0:2][0][0])
                        row = np.reshape([transcript[i:i + 1, 0:1][0][0], 0,0,0,0,0,0,0,0,1], [1, 10])
                        counts = np.append(counts, row, axis=0)
                    else:
                        for x in range(0, len(counts)):
                            if counts[x:x + 1, 0:1][0][0] == transcript[i:i + 1, 0:1][0][0]:
                                counts[x:x + 1, 9:10] = int(counts[x:x + 1, 9:10][0][0]) + 1
                                continue


    for row in counts:
        name = row[0]
        s1 = row[1]
        s2 = row[2]
        s3 = row[3]
        s4 = row[4]
        s5 = row[5]
        s6 = row[6]
        s7 = row[7]
        s8 = row[8]
        s9 = row[9]
        writer.writerow([name, s1,s2,s3,s4,s5,s6,s7,s8,s9])