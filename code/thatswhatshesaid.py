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

with open('/Applications/MAMP/htdocs/theoffice/spreadsheets/thatswhatshesaid.csv', 'a') as csvfile:

    writer = csv.writer(csvfile, delimiter='|',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

    counts = np.zeros([46,3], dtype=object)
    count = 0

    for season in range(1,10):
        if season == 1:
            episodeNames = ["Pilot", "DiversityDay", "HealthCare","TheAlliance","Basketball","HotGirl"]
            for episode in range(01,07):
                seasonepisode = 'Season%s-Episode0%s%s.csv' % (str(season), str(episode), episodeNames[episode-1])
                print seasonepisode
                c = np.genfromtxt(
                    '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode0%s%s.csv' % (str(season), str(season), str(episode), episodeNames[episode-1]),
                    delimiter="|", dtype=str, skiprows=0)
                transcript = c[:]
                for line in range(0,len(transcript)):
                    if "she said" in transcript[line:line+1,1:2][0][0]:
                        count +=1
                        lines = []
                        lines.append(transcript[line-2:line-1,1:2][0][0])
                        lines.append(transcript[line-1:line,1:2][0][0])
                        lines.append(transcript[line:line+1,1:2][0][0])
                        lines.append(transcript[line+1:line+2,1:2][0][0])
                        counts[count:count+1,0:1] = seasonepisode
                        counts[count:count+1,1:2] = str(lines)
                        counts[count:count + 1, 2:3] = transcript[line:line + 1, 0:1][0][0]
        elif season == 2:
            episodeNames = ["TheDundies","SexualHarassment","OfficeOlympics","TheFire","Halloween","TheFight","TheClient","PerformanceReview","E-mailSurveillance","ChristmasParty",
                            "BoozeCruise","TheInjury","TheSecret","TheCarpet","BoysandGirls","Valentine'sDay","Dwight'sSpeech","TakeYourDaughtertoWorkDay","Michael'sBirthday","DrugTesting",
                            "ConflictResolution", "CasinoNight"]
            for episode in range(1,23):
                if episode in range(0,10):
                    seasonepisode = 'Season%s-Episode0%s%s.csv' % (str(season), str(episode), episodeNames[episode - 1])
                    print seasonepisode
                    c = np.genfromtxt(
                        '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode0%s%s.csv' % (
                        str(season), str(season), str(episode), episodeNames[episode - 1]),
                        delimiter="|", dtype=str, skiprows=0)
                    transcript = c[:]
                    for line in range(0, len(transcript)):
                        if "she said" in transcript[line:line + 1, 1:2][0][0]:
                            count +=1
                            lines = []
                            lines.append(transcript[line - 2:line - 1, 1:2][0][0])
                            lines.append(transcript[line - 1:line, 1:2][0][0])
                            lines.append(transcript[line:line + 1, 1:2][0][0])
                            lines.append(transcript[line + 1:line + 2, 1:2][0][0])
                            counts[count:count + 1, 0:1] = seasonepisode
                            counts[count:count + 1, 1:2] = str(lines)
                            counts[count:count + 1, 2:3] = transcript[line:line + 1, 0:1][0][0]
                else:
                    seasonepisode = 'Season%s-Episode0%s%s.csv' % (str(season), str(episode), episodeNames[episode - 1])
                    print seasonepisode
                    c = np.genfromtxt(
                        '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode%s%s.csv' % (
                        str(season), str(season), str(episode), episodeNames[episode - 1]),
                        delimiter="|", dtype=str, skiprows=0)
                    transcript = c[:]
                    for line in range(0, len(transcript)):
                        if "she said" in transcript[line:line + 1, 1:2][0][0]:
                            count+=1
                            lines = []
                            lines.append(transcript[line - 2:line - 1, 1:2][0][0])
                            lines.append(transcript[line - 1:line, 1:2][0][0])
                            lines.append(transcript[line:line + 1, 1:2][0][0])
                            lines.append(transcript[line + 1:line + 2, 1:2][0][0])
                            counts[count:count + 1, 0:1] = seasonepisode
                            counts[count:count + 1, 1:2] = str(lines)
                            counts[count:count + 1, 2:3] = transcript[line:line + 1, 0:1][0][0]
        elif season == 3:
            episodeNames = ["GayWitchHunt", "TheConvention","TheCoup","GriefCounseling","Initiation","Diwali","BranchClosing","TheMerger","TheConvict","ABenihanaChristmas",
                            "BackFromVacation","TravelingSalesmen","TheReturn","BenFranklin","Phyllis'Wedding","BusinessSchool","Cocktails","TheNegotiation","SafetyTraining",
                            "ProductRecall","Women'sAppreciation","BeachGames","TheJob"]
            for episode in range(1,24):
                if episode in range(0,10):
                    seasonepisode = 'Season%s-Episode0%s%s.csv' % (str(season), str(episode), episodeNames[episode - 1])
                    print seasonepisode
                    c = np.genfromtxt(
                        '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode0%s%s.csv' % (
                        str(season), str(season), str(episode), episodeNames[episode - 1]),
                        delimiter="|", dtype=str, skiprows=0)
                    transcript = c[:]
                    for line in range(0, len(transcript)):
                        if "she said" in transcript[line:line + 1, 1:2][0][0]:
                            count+=1
                            lines = []
                            lines.append(transcript[line - 2:line - 1, 1:2][0][0])
                            lines.append(transcript[line - 1:line, 1:2][0][0])
                            lines.append(transcript[line:line + 1, 1:2][0][0])
                            lines.append(transcript[line + 1:line + 2, 1:2][0][0])
                            counts[count:count + 1, 0:1] = seasonepisode
                            counts[count:count + 1, 1:2] = str(lines)
                            counts[count:count + 1, 2:3] = transcript[line:line + 1, 0:1][0][0]
                else:
                    seasonepisode = 'Season%s-Episode0%s%s.csv' % (str(season), str(episode), episodeNames[episode - 1])
                    print seasonepisode
                    c = np.genfromtxt(
                        '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode%s%s.csv' % (
                        str(season), str(season), str(episode), episodeNames[episode - 1]),
                        delimiter="|", dtype=str, skiprows=0)
                    transcript = c[:]
                    for line in range(0, len(transcript)):
                        if "she said" in transcript[line:line + 1, 1:2][0][0]:
                            count+=1
                            lines = []
                            lines.append(transcript[line - 2:line - 1, 1:2][0][0])
                            lines.append(transcript[line - 1:line, 1:2][0][0])
                            lines.append(transcript[line:line + 1, 1:2][0][0])
                            lines.append(transcript[line + 1:line + 2, 1:2][0][0])
                            counts[count:count + 1, 0:1] = seasonepisode
                            counts[count:count + 1, 1:2] = str(lines)
                            counts[count:count + 1, 2:3] = transcript[line:line + 1, 0:1][0][0]
        elif season == 4:
            episodeNames = ["FunRun","DunderMifflinInfinity","LaunchParty","Money","LocalAd","BranchWars","SurvivorMan","TheDeposition","DinnerParty","ChairModel","NightOut",
                            "DidIStutter?","JobFair","GoodbyeToby"]
            for episode in range(1,15):
                if episode in range(0,10):
                    seasonepisode = 'Season%s-Episode0%s%s.csv' % (str(season), str(episode), episodeNames[episode - 1])
                    print seasonepisode
                    c = np.genfromtxt(
                        '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode0%s%s.csv' % (
                        str(season), str(season), str(episode), episodeNames[episode - 1]),
                        delimiter="|", dtype=str, skiprows=0)
                    transcript = c[:]
                    for line in range(0, len(transcript)):
                        if "she said" in transcript[line:line + 1, 1:2][0][0]:
                            count+=1
                            lines = []
                            lines.append(transcript[line - 2:line - 1, 1:2][0][0])
                            lines.append(transcript[line - 1:line, 1:2][0][0])
                            lines.append(transcript[line:line + 1, 1:2][0][0])
                            lines.append(transcript[line + 1:line + 2, 1:2][0][0])
                            counts[count:count + 1, 0:1] = seasonepisode
                            counts[count:count + 1, 1:2] = str(lines)
                            counts[count:count + 1, 2:3] = transcript[line:line + 1, 0:1][0][0]
                else:
                    seasonepisode = 'Season%s-Episode0%s%s.csv' % (str(season), str(episode), episodeNames[episode - 1])
                    print seasonepisode
                    c = np.genfromtxt(
                        '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode%s%s.csv' % (
                        str(season), str(season), str(episode), episodeNames[episode - 1]),
                        delimiter="|", dtype=str, skiprows=0)
                    transcript = c[:]
                    for line in range(0, len(transcript)):
                        if "she said" in transcript[line:line + 1, 1:2][0][0]:
                            count+=1
                            lines = []
                            lines.append(transcript[line - 2:line - 1, 1:2][0][0])
                            lines.append(transcript[line - 1:line, 1:2][0][0])
                            lines.append(transcript[line:line + 1, 1:2][0][0])
                            lines.append(transcript[line + 1:line + 2, 1:2][0][0])
                            counts[count:count + 1, 0:1] = seasonepisode
                            counts[count:count + 1, 1:2] = str(lines)
                            counts[count:count + 1, 2:3] = transcript[line:line + 1, 0:1][0][0]
        elif season == 5:
            episodeNames = ["WeightLoss","BusinessEthics","BabyShower","CrimeAid","EmployeeTransfer","CustomerSurvey","BusinessTrip","FrameToby","TheSurplus","MoroccanChristmas",
                            "TheDuel","PrinceFamilyPaper","StressRelief","LectureCircuitPart1","LectureCircuitPart2","BloodDrive","GoldenTicket","NewBoss","TwoWeeks","DreamTeam",
                            "MichaelScottPaperCompany","HeavyCompetition","Broke","CasualFriday","CafeDisco","CompanyPicnic"]
            for episode in range(1,27):
                if episode in range(0,10):
                    seasonepisode = 'Season%s-Episode0%s%s.csv' % (str(season), str(episode), episodeNames[episode - 1])
                    print seasonepisode
                    c = np.genfromtxt(
                        '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode0%s%s.csv' % (
                        str(season), str(season), str(episode), episodeNames[episode - 1]),
                        delimiter="|", dtype=str, skiprows=0)
                    transcript = c[:]
                    for line in range(0, len(transcript)):
                        if "she said" in transcript[line:line + 1, 1:2][0][0]:
                            count+=1
                            lines = []
                            lines.append(transcript[line - 2:line - 1, 1:2][0][0])
                            lines.append(transcript[line - 1:line, 1:2][0][0])
                            lines.append(transcript[line:line + 1, 1:2][0][0])
                            lines.append(transcript[line + 1:line + 2, 1:2][0][0])
                            counts[count:count + 1, 0:1] = seasonepisode
                            counts[count:count + 1, 1:2] = str(lines)
                            counts[count:count + 1, 2:3] = transcript[line:line + 1, 0:1][0][0]
                else:
                    seasonepisode = 'Season%s-Episode0%s%s.csv' % (str(season), str(episode), episodeNames[episode - 1])
                    print seasonepisode
                    c = np.genfromtxt(
                        '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode%s%s.csv' % (
                        str(season), str(season), str(episode), episodeNames[episode - 1]),
                        delimiter="|", dtype=str, skiprows=0)
                    transcript = c[:]
                    for line in range(0, len(transcript)):
                        if "she said" in transcript[line:line + 1, 1:2][0][0]:
                            count+=1
                            lines = []
                            lines.append(transcript[line - 2:line - 1, 1:2][0][0])
                            lines.append(transcript[line - 1:line, 1:2][0][0])
                            lines.append(transcript[line:line + 1, 1:2][0][0])
                            lines.append(transcript[line + 1:line + 2, 1:2][0][0])
                            counts[count:count + 1, 0:1] = seasonepisode
                            counts[count:count + 1, 1:2] = str(lines)
                            counts[count:count + 1, 2:3] = transcript[line:line + 1, 0:1][0][0]
        elif season == 6:
            episodeNames = ["Gossip","TheMeeting","ThePromotion","Niagara","Mafia","TheLover","KoiPond","DoubleDate","Murder","ShareholderMeeting","Scott'sTots","SecretSanta","TheBanker",
                            "Sabre","ManagerandSalesman","TheDelivery","St.Patrick'sDay","NewLeads","HappyHour","Secretary'sDay","BodyLanguage","TheCover-Up","TheChump","Whistleblower"]
            for episode in range(1,25):
                if episode in range(0,10):
                    seasonepisode = 'Season%s-Episode0%s%s.csv' % (str(season), str(episode), episodeNames[episode - 1])
                    print seasonepisode
                    c = np.genfromtxt(
                        '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode0%s%s.csv' % (
                        str(season), str(season), str(episode), episodeNames[episode - 1]),
                        delimiter="|", dtype=str, skiprows=0)
                    transcript = c[:]
                    for line in range(0, len(transcript)):
                        if "she said" in transcript[line:line + 1, 1:2][0][0]:
                            count+=1
                            lines = []
                            lines.append(transcript[line - 2:line - 1, 1:2][0][0])
                            lines.append(transcript[line - 1:line, 1:2][0][0])
                            lines.append(transcript[line:line + 1, 1:2][0][0])
                            lines.append(transcript[line + 1:line + 2, 1:2][0][0])
                            counts[count:count + 1, 0:1] = seasonepisode
                            counts[count:count + 1, 1:2] = str(lines)
                            counts[count:count + 1, 2:3] = transcript[line:line + 1, 0:1][0][0]
                else:
                    seasonepisode = 'Season%s-Episode0%s%s.csv' % (str(season), str(episode), episodeNames[episode - 1])
                    print seasonepisode
                    c = np.genfromtxt(
                        '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode%s%s.csv' % (
                        str(season), str(season), str(episode), episodeNames[episode - 1]),
                        delimiter="|", dtype=str, skiprows=0)
                    transcript = c[:]
                    for line in range(0, len(transcript)):
                        if "she said" in transcript[line:line + 1, 1:2][0][0]:
                            count+=1
                            lines = []
                            lines.append(transcript[line - 2:line - 1, 1:2][0][0])
                            lines.append(transcript[line - 1:line, 1:2][0][0])
                            lines.append(transcript[line:line + 1, 1:2][0][0])
                            lines.append(transcript[line + 1:line + 2, 1:2][0][0])
                            counts[count:count + 1, 0:1] = seasonepisode
                            counts[count:count + 1, 1:2] = str(lines)
                            counts[count:count + 1, 2:3] = transcript[line:line + 1, 0:1][0][0]
        elif season == 7:
            episodeNames = ["Nepotism","Counseling","Andy'sPlay","SexEd","TheSting","CostumeContest","Christening","ViewingParty","WUPHF.com","China","ClassyChristmas","Ultimatum",
                            "TheSeminar","TheSearch","PDA","ThreatLevelMidnight","ToddPacker","GarageSale","TrainingDay","Michael'sLastDundies","GoodbyeMichael","TheInnerCircle",
                            "DwightK.Schrute(Acting)Manager","SearchCommittee"]
            for episode in range(1,25):
                if episode in range(0,10):
                    seasonepisode = 'Season%s-Episode0%s%s.csv' % (str(season), str(episode), episodeNames[episode - 1])
                    print seasonepisode
                    c = np.genfromtxt(
                        '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode0%s%s.csv' % (
                        str(season), str(season), str(episode), episodeNames[episode - 1]),
                        delimiter="|", dtype=str, skiprows=0)
                    transcript = c[:]
                    for line in range(0, len(transcript)):
                        if "she said" in transcript[line:line + 1, 1:2][0][0]:
                            count+=1
                            lines = []
                            lines.append(transcript[line - 2:line - 1, 1:2][0][0])
                            lines.append(transcript[line - 1:line, 1:2][0][0])
                            lines.append(transcript[line:line + 1, 1:2][0][0])
                            lines.append(transcript[line + 1:line + 2, 1:2][0][0])
                            counts[count:count + 1, 0:1] = seasonepisode
                            counts[count:count + 1, 1:2] = str(lines)
                            counts[count:count + 1, 2:3] = transcript[line:line + 1, 0:1][0][0]
                else:
                    seasonepisode = 'Season%s-Episode0%s%s.csv' % (str(season), str(episode), episodeNames[episode - 1])
                    print seasonepisode
                    c = np.genfromtxt(
                        '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode%s%s.csv' % (
                        str(season), str(season), str(episode), episodeNames[episode - 1]),
                        delimiter="|", dtype=str, skiprows=0)
                    transcript = c[:]
                    for line in range(0, len(transcript)):
                        if "she said" in transcript[line:line + 1, 1:2][0][0]:
                            count+=1
                            lines = []
                            lines.append(transcript[line - 2:line - 1, 1:2][0][0])
                            lines.append(transcript[line - 1:line, 1:2][0][0])
                            lines.append(transcript[line:line + 1, 1:2][0][0])
                            lines.append(transcript[line + 1:line + 2, 1:2][0][0])
                            counts[count:count + 1, 0:1] = seasonepisode
                            counts[count:count + 1, 1:2] = str(lines)
                            counts[count:count + 1, 2:3] = transcript[line:line + 1, 0:1][0][0]
        elif season == 8:
            episodeNames = ["TheList","TheIncentive","Lotto","GardenParty","Spooked","Doomsday","Pam'sReplacement","Gettysburg","Mrs.California","ChristmasWishes","Trivia","PoolParty",
                            "JuryDuty","SpecialProject","Tallahasse","AfterHours","TesttheStore","LastDayInFlorida","GetTheGirl","WelcomeParty","AngryAndy","Fundraiser","TurfWar",
                            "FreeFamilyPortraitStudio"]
            for episode in range(1,25):
                if episode in range(0,10):
                    seasonepisode = 'Season%s-Episode0%s%s.csv' % (str(season), str(episode), episodeNames[episode - 1])
                    print seasonepisode
                    c = np.genfromtxt(
                        '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode0%s%s.csv' % (
                        str(season), str(season), str(episode), episodeNames[episode - 1]),
                        delimiter="|", dtype=str, skiprows=0)
                    transcript = c[:]
                    for line in range(0, len(transcript)):
                        if "she said" in transcript[line:line + 1, 1:2][0][0]:
                            count+=1
                            lines = []
                            lines.append(transcript[line - 2:line - 1, 1:2][0][0])
                            lines.append(transcript[line - 1:line, 1:2][0][0])
                            lines.append(transcript[line:line + 1, 1:2][0][0])
                            lines.append(transcript[line + 1:line + 2, 1:2][0][0])
                            counts[count:count + 1, 0:1] = seasonepisode
                            counts[count:count + 1, 1:2] = str(lines)
                            counts[count:count + 1, 2:3] = transcript[line:line + 1, 0:1][0][0]
                else:
                    seasonepisode = 'Season%s-Episode0%s%s.csv' % (str(season), str(episode), episodeNames[episode - 1])
                    print seasonepisode
                    c = np.genfromtxt(
                        '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode%s%s.csv' % (
                        str(season), str(season), str(episode), episodeNames[episode - 1]),
                        delimiter="|", dtype=str, skiprows=0)
                    transcript = c[:]
                    for line in range(0, len(transcript)):
                        if "she said" in transcript[line:line + 1, 1:2][0][0]:
                            count+=1
                            lines = []
                            lines.append(transcript[line - 2:line - 1, 1:2][0][0])
                            lines.append(transcript[line - 1:line, 1:2][0][0])
                            lines.append(transcript[line:line + 1, 1:2][0][0])
                            if episode == 18:
                                pass
                            else:
                                lines.append(transcript[line + 1:line + 2, 1:2][0][0])
                            counts[count:count + 1, 0:1] = seasonepisode
                            counts[count:count + 1, 1:2] = str(lines)
                            counts[count:count + 1, 2:3] = transcript[line:line + 1, 0:1][0][0]
        else:
            episodeNames = ["NewGuys","Roy'sWedding","AndysAncestry","WorkBus","HereComesTreble","TheBoat","TheWhale","TheTarget","DwightChristmas","Lice","SuitWarehouse",
                            "CustomerLoyalty","JuniorSalesman","Vandalism","CouplesDiscount","MovingOn","TheFarm","Promos","Stairmageddon","PaperAirplane","Livin'TheDream",
                            "AARM","Finale"]
            for episode in range(1,24):
                seasonepisode = 'Season%s-Episode0%s%s.csv' % (str(season), str(episode), episodeNames[episode-1])
                print seasonepisode
                c = np.genfromtxt(
                    '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode%s%s.csv' % (str(season), str(season), str(episode), episodeNames[episode-1]),
                    delimiter="|", dtype=str, skiprows=0)
                transcript = c[:]
                for line in range(0,len(transcript)):
                    if "she said" in transcript[line:line+1,1:2][0][0]:
                        count+=1
                        lines = []
                        lines.append(transcript[line-2:line-1,1:2][0][0])
                        lines.append(transcript[line-1:line,1:2][0][0])
                        lines.append(transcript[line:line+1,1:2][0][0])
                        lines.append(transcript[line+1:line+2,1:2][0][0])
                        counts[count:count+1,0:1] = seasonepisode
                        counts[count:count+1,1:2] = str(lines)
                        counts[count:count + 1, 2:3] = transcript[line:line + 1, 0:1][0][0]

    for row in counts:
        print row[0]
        print row[1]
        writer.writerow([row[0],row[1],row[2]])