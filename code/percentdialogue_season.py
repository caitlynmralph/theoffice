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

with open('/Applications/MAMP/htdocs/theoffice/spreadsheets/percentdialogue_season.csv', 'a') as csvfile:

    writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

    counts = np.zeros([51,9], dtype=object)

    characters = ["Total lines","Michael","Dwight","Jim","Pam","Andy","Angela","Kevin","Erin","Oscar","Ryan","Darryl","Phyllis","Jan","Toby","Kelly","Stanley","Meredith","Holly","David","Nellie",
                  "Creed","Gabe","Robert","Karen","Charles","Roy","Clark","Jo","Deangelo","Pete","ToddPacker","Everyone","Carol","Donna","Katy","Danny","Josh","Val","Helene","Nate",
                  "SenatorLipton","Jessica","Hank","Trevor","CaptainJack","Grotti","Man","Cathy","Host","Lester"]

    characters = np.reshape(characters,[len(characters),1])

    counts = np.append(characters,counts,axis=1)

    seasons = ["Characters","Season1","Season2","Season3","Season4","Season5","Season6","Season7","Season8","Season9"]

    seasons = np.reshape(seasons,[1,len(seasons)])

    counts = np.append(seasons,counts,axis=0)

    for season in range(1,10):
        if season == 1:
            episodeNames = ["Pilot", "DiversityDay", "HealthCare","TheAlliance","Basketball","HotGirl"]
            seasoncount = 0
            for episode in range(01,07):
                print '/Season%s/Season%s-Episode0%s%s.csv' % (str(season), str(season), str(episode), episodeNames[episode-1])
                c = np.genfromtxt(
                    '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode0%s%s.csv' % (str(season), str(season), str(episode), episodeNames[episode-1]),
                    delimiter="|", dtype=str, skiprows=0)
                transcript = c[:]
                seasoncount += len(transcript)
            counts[1:2,season:season+1] = seasoncount
            for episode in range(01,07):
                c = np.genfromtxt(
                    '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode0%s%s.csv' % (
                    str(season), str(season), str(episode), episodeNames[episode - 1]),
                    delimiter="|", dtype=str, skiprows=0)
                transcript = c[:]
                for line in range(0,len(transcript)):
                    for character in range(1,len(characters)):
                        if transcript[line:line+1,0:1][0][0].replace(" ","") == characters[character]:
                            counts[character+1:character+2,season:season+1] = int(counts[character+1:character+2,season:season+1]) + 1
        elif season == 2:
            episodeNames = ["TheDundies","SexualHarassment","OfficeOlympics","TheFire","Halloween","TheFight","TheClient","PerformanceReview","E-mailSurveillance","ChristmasParty",
                            "BoozeCruise","TheInjury","TheSecret","TheCarpet","BoysandGirls","Valentine'sDay","Dwight'sSpeech","TakeYourDaughtertoWorkDay","Michael'sBirthday","DrugTesting",
                            "ConflictResolution", "CasinoNight"]
            seasoncount = 0
            for episode in range(1,23):
                if episode in range(0,10):
                    print '/Season%s/Season%s-Episode0%s%s.csv' % (str(season), str(season), str(episode), episodeNames[episode - 1])
                    c = np.genfromtxt('/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode0%s%s.csv' % (str(season), str(season), str(episode), episodeNames[episode - 1]),delimiter="|", dtype=str, skiprows=0)
                    transcript = c[:]
                    seasoncount += len(transcript)
                else:
                    print '/Season%s/Season%s-Episode%s%s.csv' % (
                    str(season), str(season), str(episode), episodeNames[episode - 1])
                    c = np.genfromtxt(
                        '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode%s%s.csv' % (
                        str(season), str(season), str(episode), episodeNames[episode - 1]),
                        delimiter="|", dtype=str, skiprows=0)
                    transcript = c[:]
                    seasoncount += len(transcript)
                counts[1:2, season:season + 1] = seasoncount
            for episode in range(1, 23):
                if episode in range(0,10):
                    print '/Season%s/Season%s-Episode0%s%s.csv' % (
                    str(season), str(season), str(episode), episodeNames[episode - 1])
                    c = np.genfromtxt(
                        '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode0%s%s.csv' % (
                        str(season), str(season), str(episode), episodeNames[episode - 1]), delimiter="|", dtype=str,
                        skiprows=0)
                    transcript = c[:]
                    for line in range(0, len(transcript)):
                        for character in range(1, len(characters)):
                            if transcript[line:line + 1, 0:1][0][0].replace(" ", "") == characters[character]:
                                counts[character + 1:character + 2, season:season + 1] = int(
                                    counts[character + 1:character + 2, season:season + 1]) + 1
                else:
                    print '/Season%s/Season%s-Episode%s%s.csv' % (str(season), str(season), str(episode), episodeNames[episode - 1])
                    c = np.genfromtxt('/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode%s%s.csv' % (str(season), str(season), str(episode), episodeNames[episode - 1]),
                        delimiter="|", dtype=str, skiprows=0)
                    transcript = c[:]
                    for line in range(0, len(transcript)):
                        for character in range(1, len(characters)):
                            if transcript[line:line + 1, 0:1][0][0].replace(" ", "") == characters[character]:
                                counts[character + 1:character + 2, season:season + 1] = int(
                                    counts[character + 1:character + 2, season:season + 1]) + 1
        elif season == 3:
            episodeNames = ["GayWitchHunt", "TheConvention","TheCoup","GriefCounseling","Initiation","Diwali","BranchClosing","TheMerger","TheConvict","ABenihanaChristmas",
                            "BackFromVacation","TravelingSalesmen","TheReturn","BenFranklin","Phyllis'Wedding","BusinessSchool","Cocktails","TheNegotiation","SafetyTraining",
                            "ProductRecall","Women'sAppreciation","BeachGames","TheJob"]
            seasoncount = 0
            for episode in range(1,24):
                if episode in range(0,10):
                    print '/Season%s/Season%s-Episode0%s%s.csv' % (
                        str(season), str(season), str(episode), episodeNames[episode - 1])
                    c = np.genfromtxt(
                        '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode0%s%s.csv' % (
                        str(season), str(season), str(episode), episodeNames[episode - 1]), delimiter="|", dtype=str,
                        skiprows=0)
                    transcript = c[:]
                    seasoncount += len(transcript)
                else:
                    print '/Season%s/Season%s-Episode%s%s.csv' % (
                        str(season), str(season), str(episode), episodeNames[episode - 1])
                    c = np.genfromtxt(
                        '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode%s%s.csv' % (
                            str(season), str(season), str(episode), episodeNames[episode - 1]),
                        delimiter="|", dtype=str, skiprows=0)
                    transcript = c[:]
                    seasoncount += len(transcript)
                counts[1:2, season:season + 1] = seasoncount
            for episode in range(1, 24):
                if episode in range(0,10):
                    print '/Season%s/Season%s-Episode0%s%s.csv' % (
                        str(season), str(season), str(episode), episodeNames[episode - 1])
                    c = np.genfromtxt(
                        '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode0%s%s.csv' % (
                        str(season), str(season), str(episode), episodeNames[episode - 1]), delimiter="|", dtype=str,
                        skiprows=0)
                    transcript = c[:]
                    for line in range(0, len(transcript)):
                        for character in range(1, len(characters)):
                            if transcript[line:line + 1, 0:1][0][0].replace(" ", "") == characters[character]:
                                counts[character + 1:character + 2, season:season + 1] = int(
                                    counts[character + 1:character + 2, season:season +1]) + 1
                else:
                    print '/Season%s/Season%s-Episode%s%s.csv' % (
                    str(season), str(season), str(episode), episodeNames[episode - 1])
                    c = np.genfromtxt(
                        '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode%s%s.csv' % (
                        str(season), str(season), str(episode), episodeNames[episode - 1]),
                        delimiter="|", dtype=str, skiprows=0)
                    transcript = c[:]
                    for line in range(0, len(transcript)):
                        for character in range(1, len(characters)):
                            if transcript[line:line + 1, 0:1][0][0].replace(" ", "") == characters[character]:
                                counts[character + 1:character + 2, season:season + 1] = int(
                                    counts[character + 1:character + 2, season:season + 1]) + 1
        elif season == 4:
            episodeNames = ["FunRun","DunderMifflinInfinity","LaunchParty","Money","LocalAd","BranchWars","SurvivorMan","TheDeposition","DinnerParty","ChairModel","NightOut",
                            "DidIStutter?","JobFair","GoodbyeToby"]
            seasoncount = 0
            for episode in range(1,15):
                if episode in range(0,10):
                    print '/Season%s/Season%s-Episode0%s%s.csv' % (
                        str(season), str(season), str(episode), episodeNames[episode - 1])
                    c = np.genfromtxt(
                        '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode0%s%s.csv' % (
                        str(season), str(season), str(episode), episodeNames[episode - 1]), delimiter="|", dtype=str,
                        skiprows=0)
                    transcript = c[:]
                    seasoncount += len(transcript)
                else:
                    print '/Season%s/Season%s-Episode%s%s.csv' % (
                        str(season), str(season), str(episode), episodeNames[episode - 1])
                    c = np.genfromtxt(
                        '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode%s%s.csv' % (
                            str(season), str(season), str(episode), episodeNames[episode - 1]),
                        delimiter="|", dtype=str, skiprows=0)
                    transcript = c[:]
                    seasoncount += len(transcript)
                counts[1:2, season:season + 1] = seasoncount
            for episode in range(1, 15):
                if episode in range(0,10):
                    print '/Season%s/Season%s-Episode0%s%s.csv' % (
                        str(season), str(season), str(episode), episodeNames[episode - 1])
                    c = np.genfromtxt(
                        '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode0%s%s.csv' % (
                        str(season), str(season), str(episode), episodeNames[episode - 1]), delimiter="|", dtype=str,
                        skiprows=0)
                    transcript = c[:]
                    for line in range(0, len(transcript)):
                        for character in range(1, len(characters)):
                            if transcript[line:line + 1, 0:1][0][0].replace(" ", "") == characters[character]:
                                counts[character + 1:character + 2, season:season + 1] = int(
                                    counts[character + 1:character + 2, season:season + 1]) + 1
                else:
                    print '/Season%s/Season%s-Episode%s%s.csv' % (
                    str(season), str(season), str(episode), episodeNames[episode - 1])
                    c = np.genfromtxt(
                        '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode%s%s.csv' % (
                        str(season), str(season), str(episode), episodeNames[episode - 1]),
                        delimiter="|", dtype=str, skiprows=0)
                    transcript = c[:]
                    for line in range(0, len(transcript)):
                        for character in range(1, len(characters)):
                            if transcript[line:line + 1, 0:1][0][0].replace(" ", "") == characters[character]:
                                counts[character + 1:character + 2, season:season + 1] = int(
                                    counts[character + 1:character + 2, season:season + 1]) + 1
        elif season == 5:
            episodeNames = ["WeightLoss","BusinessEthics","BabyShower","CrimeAid","EmployeeTransfer","CustomerSurvey","BusinessTrip","FrameToby","TheSurplus","MoroccanChristmas",
                            "TheDuel","PrinceFamilyPaper","StressRelief","LectureCircuitPart1","LectureCircuitPart2","BloodDrive","GoldenTicket","NewBoss","TwoWeeks","DreamTeam",
                            "MichaelScottPaperCompany","HeavyCompetition","Broke","CasualFriday","CafeDisco","CompanyPicnic"]
            seasoncount = 0
            for episode in range(1,27):
                if episode in range(0,10):
                    print '/Season%s/Season%s-Episode0%s%s.csv' % (
                        str(season), str(season), str(episode), episodeNames[episode - 1])
                    c = np.genfromtxt(
                        '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode0%s%s.csv' % (
                        str(season), str(season), str(episode), episodeNames[episode - 1]), delimiter="|", dtype=str,
                        skiprows=0)
                    transcript = c[:]
                    seasoncount += len(transcript)
                else:
                    print '/Season%s/Season%s-Episode%s%s.csv' % (
                        str(season), str(season), str(episode), episodeNames[episode - 1])
                    c = np.genfromtxt(
                        '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode%s%s.csv' % (
                            str(season), str(season), str(episode), episodeNames[episode - 1]),
                        delimiter="|", dtype=str, skiprows=0)
                    transcript = c[:]
                    seasoncount += len(transcript)
                counts[1:2, season:season + 1] = seasoncount
            for episode in range(1, 27):
                if episode in range(0, 10):
                    print '/Season%s/Season%s-Episode0%s%s.csv' % (
                        str(season), str(season), str(episode), episodeNames[episode - 1])
                    c = np.genfromtxt(
                        '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode0%s%s.csv' % (
                            str(season), str(season), str(episode), episodeNames[episode - 1]), delimiter="|",
                        dtype=str,
                        skiprows=0)
                    transcript = c[:]
                    for line in range(0, len(transcript)):
                        for character in range(1, len(characters)):
                            if transcript[line:line + 1, 0:1][0][0].replace(" ", "") == characters[character]:
                                counts[character + 1:character + 2, season:season+1] = int(
                                    counts[character + 1:character + 2, season:season+1]) + 1
                else:
                    print '/Season%s/Season%s-Episode%s%s.csv' % (
                    str(season), str(season), str(episode), episodeNames[episode - 1])
                    c = np.genfromtxt(
                        '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode%s%s.csv' % (
                        str(season), str(season), str(episode), episodeNames[episode - 1]),
                        delimiter="|", dtype=str, skiprows=0)
                    transcript = c[:]
                    for line in range(0, len(transcript)):
                        for character in range(1, len(characters)):
                            if transcript[line:line + 1, 0:1][0][0].replace(" ", "") == characters[character]:
                                counts[character + 1:character + 2, season:season +1] = int(
                                    counts[character + 1:character + 2, season:season + 1]) + 1
        elif season == 6:
            episodeNames = ["Gossip","TheMeeting","ThePromotion","Niagara","Mafia","TheLover","KoiPond","DoubleDate","Murder","ShareholderMeeting","Scott'sTots","SecretSanta","TheBanker",
                            "Sabre","ManagerandSalesman","TheDelivery","St.Patrick'sDay","NewLeads","HappyHour","Secretary'sDay","BodyLanguage","TheCover-Up","TheChump","Whistleblower"]
            seasoncount = 0
            for episode in range(1,25):
                if episode in range(0,10):
                    print '/Season%s/Season%s-Episode0%s%s.csv' % (
                        str(season), str(season), str(episode), episodeNames[episode - 1])
                    c = np.genfromtxt(
                        '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode0%s%s.csv' % (
                            str(season), str(season), str(episode), episodeNames[episode - 1]), delimiter="|", dtype=str,
                        skiprows=0)
                    transcript = c[:]
                    seasoncount += len(transcript)
                else:
                    print '/Season%s/Season%s-Episode%s%s.csv' % (
                        str(season), str(season), str(episode), episodeNames[episode - 1])
                    c = np.genfromtxt(
                        '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode%s%s.csv' % (
                            str(season), str(season), str(episode), episodeNames[episode - 1]),
                        delimiter="|", dtype=str, skiprows=0)
                    transcript = c[:]
                    seasoncount += len(transcript)
                counts[1:2, season:season + 1] = seasoncount
            for episode in range(1, 25):
                if episode in range(0,10):
                    print '/Season%s/Season%s-Episode0%s%s.csv' % (
                        str(season), str(season), str(episode), episodeNames[episode - 1])
                    c = np.genfromtxt(
                        '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode0%s%s.csv' % (
                            str(season), str(season), str(episode), episodeNames[episode - 1]), delimiter="|", dtype=str,
                        skiprows=0)
                    transcript = c[:]
                    for line in range(0, len(transcript)):
                        for character in range(1, len(characters)):
                            if transcript[line:line + 1, 0:1][0][0].replace(" ", "") == characters[character]:
                                counts[character + 1:character + 2, season:season+1] = int(
                                    counts[character + 1:character + 2, season:season + 1]) + 1
                else:
                    print '/Season%s/Season%s-Episode%s%s.csv' % (
                        str(season), str(season), str(episode), episodeNames[episode - 1])
                    c = np.genfromtxt(
                        '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode%s%s.csv' % (
                            str(season), str(season), str(episode), episodeNames[episode - 1]),
                        delimiter="|", dtype=str, skiprows=0)
                    transcript = c[:]
                    for line in range(0, len(transcript)):
                        for character in range(1, len(characters)):
                            if transcript[line:line + 1, 0:1][0][0].replace(" ", "") == characters[character]:
                                counts[character + 1:character + 2, season:season+1] = int(
                                    counts[character + 1:character + 2, season:season+1]) + 1
        elif season == 7:
            episodeNames = ["Nepotism","Counseling","Andy'sPlay","SexEd","TheSting","CostumeContest","Christening","ViewingParty","WUPHF.com","China","ClassyChristmas","Ultimatum",
                            "TheSeminar","TheSearch","PDA","ThreatLevelMidnight","ToddPacker","GarageSale","TrainingDay","Michael'sLastDundies","GoodbyeMichael","TheInnerCircle",
                            "DwightK.Schrute(Acting)Manager","SearchCommittee"]
            seasoncount = 0
            for episode in range(1,25):
                if episode in range(0,10):
                    print '/Season%s/Season%s-Episode0%s%s.csv' % (
                        str(season), str(season), str(episode), episodeNames[episode - 1])
                    c = np.genfromtxt(
                        '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode0%s%s.csv' % (
                            str(season), str(season), str(episode), episodeNames[episode - 1]), delimiter="|", dtype=str,
                        skiprows=0)
                    transcript = c[:]
                    seasoncount += len(transcript)
                else:
                    print '/Season%s/Season%s-Episode%s%s.csv' % (
                        str(season), str(season), str(episode), episodeNames[episode - 1])
                    c = np.genfromtxt(
                        '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode%s%s.csv' % (
                            str(season), str(season), str(episode), episodeNames[episode - 1]),
                        delimiter="|", dtype=str, skiprows=0)
                    transcript = c[:]
                    seasoncount += len(transcript)
                counts[1:2, season:season + 1] = seasoncount
            for episode in range(1, 25):
                if episode in range(0,10):
                    print '/Season%s/Season%s-Episode0%s%s.csv' % (
                        str(season), str(season), str(episode), episodeNames[episode - 1])
                    c = np.genfromtxt(
                        '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode0%s%s.csv' % (
                            str(season), str(season), str(episode), episodeNames[episode - 1]), delimiter="|", dtype=str,
                        skiprows=0)
                    transcript = c[:]
                    for line in range(0, len(transcript)):
                        for character in range(1, len(characters)):
                            if transcript[line:line + 1, 0:1][0][0].replace(" ", "") == characters[character]:
                                counts[character + 1:character + 2, season:season + 1] = int(
                                    counts[character + 1:character + 2, season:season + 1]) + 1
                else:
                    print '/Season%s/Season%s-Episode%s%s.csv' % (
                        str(season), str(season), str(episode), episodeNames[episode - 1])
                    c = np.genfromtxt(
                        '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode%s%s.csv' % (
                            str(season), str(season), str(episode), episodeNames[episode - 1]),
                        delimiter="|", dtype=str, skiprows=0)
                    transcript = c[:]
                    for line in range(0, len(transcript)):
                        for character in range(1, len(characters)):
                            if transcript[line:line + 1, 0:1][0][0].replace(" ", "") == characters[character]:
                                counts[character + 1:character + 2, season:season + 1] = int(
                                    counts[character + 1:character + 2, season:season + 1]) + 1
        elif season == 8:
            episodeNames = ["TheList","TheIncentive","Lotto","GardenParty","Spooked","Doomsday","Pam'sReplacement","Gettysburg","Mrs.California","ChristmasWishes","Trivia","PoolParty",
                            "JuryDuty","SpecialProject","Tallahasse","AfterHours","TesttheStore","LastDayInFlorida","GetTheGirl","WelcomeParty","AngryAndy","Fundraiser","TurfWar",
                            "FreeFamilyPortraitStudio"]
            seasoncount = 0
            for episode in range(1,25):
                if episode in range(0,10):
                    print '/Season%s/Season%s-Episode0%s%s.csv' % (
                        str(season), str(season), str(episode), episodeNames[episode - 1])
                    c = np.genfromtxt(
                        '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode0%s%s.csv' % (
                            str(season), str(season), str(episode), episodeNames[episode - 1]), delimiter="|", dtype=str,
                        skiprows=0)
                    transcript = c[:]
                    seasoncount += len(transcript)
                else:
                    print '/Season%s/Season%s-Episode%s%s.csv' % (
                        str(season), str(season), str(episode), episodeNames[episode - 1])
                    c = np.genfromtxt(
                        '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode%s%s.csv' % (
                            str(season), str(season), str(episode), episodeNames[episode - 1]),
                        delimiter="|", dtype=str, skiprows=0)
                    transcript = c[:]
                    seasoncount += len(transcript)
                counts[1:2, season:season + 1] = seasoncount
            for episode in range(1, 25):
                if episode in range(0,10):
                    print '/Season%s/Season%s-Episode0%s%s.csv' % (
                        str(season), str(season), str(episode), episodeNames[episode - 1])
                    c = np.genfromtxt(
                        '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode0%s%s.csv' % (
                            str(season), str(season), str(episode), episodeNames[episode - 1]), delimiter="|", dtype=str,
                        skiprows=0)
                    transcript = c[:]
                    for line in range(0, len(transcript)):
                        for character in range(1, len(characters)):
                            if transcript[line:line + 1, 0:1][0][0].replace(" ", "") == characters[character]:
                                counts[character + 1:character + 2, season:season + 1] = int(
                                    counts[character + 1:character + 2, season:season + 1]) + 1
                else:
                    print '/Season%s/Season%s-Episode%s%s.csv' % (
                        str(season), str(season), str(episode), episodeNames[episode - 1])
                    c = np.genfromtxt(
                        '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode%s%s.csv' % (
                            str(season), str(season), str(episode), episodeNames[episode - 1]),
                        delimiter="|", dtype=str, skiprows=0)
                    transcript = c[:]
                    for line in range(0, len(transcript)):
                        for character in range(1, len(characters)):
                            if transcript[line:line + 1, 0:1][0][0].replace(" ", "") == characters[character]:
                                counts[character + 1:character + 2, season:season + 1] = int(
                                    counts[character + 1:character + 2, season:season + 1]) + 1
        else:
            episodeNames = ["NewGuys","Roy'sWedding","AndysAncestry","WorkBus","HereComesTreble","TheBoat","TheWhale","TheTarget","DwightChristmas","Lice","SuitWarehouse",
                            "CustomerLoyalty","JuniorSalesman","Vandalism","CouplesDiscount","MovingOn","TheFarm","Promos","Stairmageddon","PaperAirplane","Livin'TheDream",
                            "AARM","Finale"]
            seasoncount = 0
            for episode in range(1,24):
                print '/Season%s/Season%s-Episode%s%s.csv' % (
                    str(season), str(season), str(episode), episodeNames[episode - 1])
                c = np.genfromtxt(
                    '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode%s%s.csv' % (
                        str(season), str(season), str(episode), episodeNames[episode - 1]),
                    delimiter="|", dtype=str, skiprows=0)
                transcript = c[:]
                seasoncount += len(transcript)
            counts[1:2, season:season + 1] = seasoncount
            for episode in range(1, 24):
                print '/Season%s/Season%s-Episode%s%s.csv' % (
                    str(season), str(season), str(episode), episodeNames[episode - 1])
                c = np.genfromtxt(
                    '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode%s%s.csv' % (
                        str(season), str(season), str(episode), episodeNames[episode - 1]),
                    delimiter="|", dtype=str, skiprows=0)
                transcript = c[:]
                for line in range(0,len(transcript)):
                    for character in range(1,len(characters)):
                        if transcript[line:line+1,0:1][0][0].replace(" ","") == characters[character]:
                            counts[character+1:character+2,season:season+1] = int(counts[character+1:character+2,season:season+1]) + 1

    for s in range(1,10):
        for c in range(1,len(characters)):
            # print counts[0:1,e:e+1]
            counts[c + 1:c + 2, s:s + 1] = float(counts[c+1:c+2,s:s+1]) / float(counts[1:2,s:s+1])

    for row in counts:
        # print row
        writer.writerow(row)