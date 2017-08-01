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

with open('/Applications/MAMP/htdocs/theoffice/spreadsheets/characterlines/dwight/dwight_lines6.tsv', 'a') as csvfile:

    writer = csv.writer(csvfile, delimiter='\t',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

    lines = np.zeros([0,0], dtype=object)
    #
    # for season in range(1,10):
    # #     if season == 1:
    # print "SEASON 1"
    # episodeNames = ["Pilot", "DiversityDay", "HealthCare","TheAlliance","Basketball","HotGirl"]
    # for episode in range(01,07):
    #     seasonepisode = 'Season%s-Episode0%s%s.csv' % (str(1), str(episode), episodeNames[episode-1])
    #     print seasonepisode
    #     c = np.genfromtxt(
    #         '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode0%s%s.csv' % (str(1), str(1), str(episode), episodeNames[episode-1]),
    #         delimiter="|", dtype=str, skiprows=0)
    #     transcript = c[:]
    #     for line in range(0,len(transcript)):
    #         if transcript[line:line+1,0:1][0][0].replace(" ","") == "Toby":
    #             print transcript[line:line+1,1:2][0][0]
    #             lines = np.append(lines,transcript[line:line+1,1:2][0][0])
        # elif season == 2:
    # print "SEASON 2"
    # episodeNames = ["TheDundies","SexualHarassment","OfficeOlympics","TheFire","Halloween","TheFight","TheClient","PerformanceReview","E-mailSurveillance","ChristmasParty",
    #                 "BoozeCruise","TheInjury","TheSecret","TheCarpet","BoysandGirls","Valentine'sDay","Dwight'sSpeech","TakeYourDaughtertoWorkDay","Michael'sBirthday","DrugTesting",
    #                 "ConflictResolution", "CasinoNight"]
    # for episode in range(1,23):
    #     if episode in range(0,10):
    #         seasonepisode = 'Season%s-Episode0%s%s.csv' % (str(2), str(episode), episodeNames[episode - 1])
    #         print seasonepisode
    #         c = np.genfromtxt(
    #             '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode0%s%s.csv' % (
    #             str(2), str(2), str(episode), episodeNames[episode - 1]),
    #             delimiter="|", dtype=str, skiprows=0)
    #         transcript = c[:]
    #         for line in range(0, len(transcript)):
    #             if transcript[line:line + 1, 0:1][0][0].replace(" ", "") == "Toby":
    #                 print transcript[line:line+1,1:2][0][0]
    #                 lines = np.append(lines, transcript[line:line + 1, 1:2][0][0])
    #     else:
    #         seasonepisode = 'Season%s-Episode0%s%s.csv' % (str(2), str(episode), episodeNames[episode - 1])
    #         print seasonepisode
    #         c = np.genfromtxt(
    #             '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode%s%s.csv' % (
    #             str(2), str(2), str(episode), episodeNames[episode - 1]),
    #             delimiter="|", dtype=str, skiprows=0)
    #         transcript = c[:]
    #         for line in range(0, len(transcript)):
    #             if transcript[line:line + 1, 0:1][0][0].replace(" ", "") == "Toby":
    #                 print transcript[line:line+1,1:2][0][0]
    #                 lines = np.append(lines, transcript[line:line + 1, 1:2][0][0])
    #     elif season == 3:
    # print "SEASON 3"
    # episodeNames = ["GayWitchHunt", "TheConvention","TheCoup","GriefCounseling","Initiation","Diwali","BranchClosing","TheMerger","TheConvict","ABenihanaChristmas",
    #                 "BackFromVacation","TravelingSalesmen","TheReturn","BenFranklin","Phyllis'Wedding","BusinessSchool","Cocktails","TheNegotiation","SafetyTraining",
    #                 "ProductRecall","Women'sAppreciation","BeachGames","TheJob"]
    # for episode in range(1,24):
    #     if episode in range(0,10):
    #         seasonepisode = 'Season%s-Episode0%s%s.csv' % (str(3), str(episode), episodeNames[episode - 1])
    #         print seasonepisode
    #         c = np.genfromtxt(
    #             '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode0%s%s.csv' % (
    #             str(3), str(3), str(episode), episodeNames[episode - 1]),
    #             delimiter="|", dtype=str, skiprows=0)
    #         transcript = c[:]
    #         for line in range(0, len(transcript)):
    #             if transcript[line:line + 1, 0:1][0][0].replace(" ", "") == "Toby":
    #                 print transcript[line:line+1,1:2][0][0]
    #                 lines = np.append(lines, transcript[line:line + 1, 1:2][0][0])
    #     else:
    #         seasonepisode = 'Season%s-Episode0%s%s.csv' % (str(3), str(episode), episodeNames[episode - 1])
    #         print seasonepisode
    #         c = np.genfromtxt(
    #             '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode%s%s.csv' % (
    #             str(3), str(3), str(episode), episodeNames[episode - 1]),
    #             delimiter="|", dtype=str, skiprows=0)
    #         transcript = c[:]
    #         for line in range(0, len(transcript)):
    #             if transcript[line:line + 1, 0:1][0][0].replace(" ", "") == "Toby":
    #                 print transcript[line:line+1,1:2][0][0]
    #                 lines = np.append(lines, transcript[line:line + 1, 1:2][0][0])
    #     elif season == 4:
    # print "SEASON 4"
    # episodeNames = ["FunRun","DunderMifflinInfinity","LaunchParty","Money","LocalAd","BranchWars","SurvivorMan","TheDeposition","DinnerParty","ChairModel","NightOut",
    #                 "DidIStutter?","JobFair","GoodbyeToby"]
    # for episode in range(1,15):
    #     if episode in range(0,10):
    #         seasonepisode = 'Season%s-Episode0%s%s.csv' % (str(4), str(episode), episodeNames[episode - 1])
    #         print seasonepisode
    #         c = np.genfromtxt(
    #             '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode0%s%s.csv' % (
    #             str(4), str(4), str(episode), episodeNames[episode - 1]),
    #             delimiter="|", dtype=str, skiprows=0)
    #         transcript = c[:]
    #         for line in range(0, len(transcript)):
    #             if transcript[line:line + 1, 0:1][0][0].replace(" ", "") == "Toby":
    #                 print transcript[line:line+1,1:2][0][0]
    #                 lines = np.append(lines, transcript[line:line + 1, 1:2][0][0])
    #     else:
    #         seasonepisode = 'Season%s-Episode%s%s.csv' % (str(4), str(episode), episodeNames[episode - 1])
    #         print seasonepisode
    #         c = np.genfromtxt(
    #             '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode%s%s.csv' % (
    #             str(4), str(4), str(episode), episodeNames[episode - 1]),
    #             delimiter="|", dtype=str, skiprows=0)
    #         transcript = c[:]
    #         for line in range(0, len(transcript)):
    #             if transcript[line:line + 1, 0:1][0][0].replace(" ", "") == "Toby":
    #                 print transcript[line:line+1,1:2][0][0]
    #                 lines = np.append(lines, transcript[line:line + 1, 1:2][0][0])
    #     elif season == 5:
    # print "SEASON 5"
    # episodeNames = ["WeightLoss","BusinessEthics","BabyShower","CrimeAid","EmployeeTransfer","CustomerSurvey","BusinessTrip","FrameToby","TheSurplus","MoroccanChristmas",
    #                 "TheDuel","PrinceFamilyPaper","StressRelief","LectureCircuitPart1","LectureCircuitPart2","BloodDrive","GoldenTicket","NewBoss","TwoWeeks","DreamTeam",
    #                 "MichaelScottPaperCompany","HeavyCompetition","Broke","CasualFriday","CafeDisco","CompanyPicnic"]
    # for episode in range(1,27):
    #     if episode in range(0,10):
    #         seasonepisode = 'Season%s-Episode0%s%s.csv' % (str(5), str(episode), episodeNames[episode - 1])
    #         print seasonepisode
    #         c = np.genfromtxt(
    #             '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode0%s%s.csv' % (
    #             str(5), str(5), str(episode), episodeNames[episode - 1]),
    #             delimiter="|", dtype=str, skiprows=0)
    #         transcript = c[:]
    #         for line in range(0, len(transcript)):
    #             if transcript[line:line + 1, 0:1][0][0].replace(" ", "") == "Toby":
    #                 print transcript[line:line+1,1:2][0][0]
    #                 lines = np.append(lines, transcript[line:line + 1, 1:2][0][0])
    #     else:
    #         seasonepisode = 'Season%s-Episode%s%s.csv' % (str(5), str(episode), episodeNames[episode - 1])
    #         print seasonepisode
    #         c = np.genfromtxt(
    #             '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode%s%s.csv' % (
    #             str(5), str(5), str(episode), episodeNames[episode - 1]),
    #             delimiter="|", dtype=str, skiprows=0)
    #         transcript = c[:]
    #         for line in range(0, len(transcript)):
    #             if transcript[line:line + 1, 0:1][0][0].replace(" ", "") == "Toby":
    #                 print transcript[line:line+1,1:2][0][0]
    #                 lines = np.append(lines, transcript[line:line + 1, 1:2][0][0])
    #     elif season == 6:
    print "SEASON 6"
    episodeNames = ["Gossip","TheMeeting","ThePromotion","Niagara","Mafia","TheLover","KoiPond","DoubleDate","Murder","ShareholderMeeting","Scott'sTots","SecretSanta","TheBanker",
                    "Sabre","ManagerandSalesman","TheDelivery","St.Patrick'sDay","NewLeads","HappyHour","Secretary'sDay","BodyLanguage","TheCover-Up","TheChump","Whistleblower"]
    for episode in range(1,25):
        if episode in range(0,10):
            seasonepisode = 'Season%s-Episode0%s%s.csv' % (str(6), str(episode), episodeNames[episode - 1])
            print seasonepisode
            c = np.genfromtxt(
                '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode0%s%s.csv' % (
                str(6), str(6), str(episode), episodeNames[episode - 1]),
                delimiter="|", dtype=str, skiprows=0)
            transcript = c[:]
            for line in range(0, len(transcript)):
                if transcript[line:line + 1, 0:1][0][0].replace(" ", "") == "Dwight":
                    print transcript[line:line+1,1:2][0][0]
                    lines = np.append(lines, transcript[line:line + 1, 1:2][0][0])
        else:
            seasonepisode = 'Season%s-Episode0%s%s.csv' % (str(6), str(episode), episodeNames[episode - 1])
            print seasonepisode
            c = np.genfromtxt(
                '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode%s%s.csv' % (
                str(6), str(6), str(episode), episodeNames[episode - 1]),
                delimiter="|", dtype=str, skiprows=0)
            transcript = c[:]
            for line in range(0, len(transcript)):
                if transcript[line:line + 1, 0:1][0][0].replace(" ", "") == "Dwight":
                    print transcript[line:line+1,1:2][0][0]
                    lines = np.append(lines, transcript[line:line + 1, 1:2][0][0])
    #     elif season == 7:
    # print "SEASON 7"
    # episodeNames = ["Nepotism","Counseling","Andy'sPlay","SexEd","TheSting","CostumeContest","Christening","ViewingParty","WUPHF.com","China","ClassyChristmas","Ultimatum",
    #                 "TheSeminar","TheSearch","PDA","ThreatLevelMidnight","ToddPacker","GarageSale","TrainingDay","Michael'sLastDundies","GoodbyeMichael","TheInnerCircle",
    #                 "DwightK.Schrute(Acting)Manager","SearchCommittee"]
    # for episode in range(1,25):
    #     if episode in range(0,10):
    #         seasonepisode = 'Season%s-Episode0%s%s.csv' % (str(7), str(episode), episodeNames[episode - 1])
    #         print seasonepisode
    #         c = np.genfromtxt(
    #             '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode0%s%s.csv' % (
    #             str(7), str(7), str(episode), episodeNames[episode - 1]),
    #             delimiter="|", dtype=str, skiprows=0)
    #         transcript = c[:]
    #         for line in range(0, len(transcript)):
    #             if transcript[line:line + 1, 0:1][0][0].replace(" ", "") == "Dwight":
    #                 print transcript[line:line+1,1:2][0][0]
    #                 lines = np.append(lines, transcript[line:line + 1, 1:2][0][0])
    #     else:
    #         seasonepisode = 'Season%s-Episode0%s%s.csv' % (str(7), str(episode), episodeNames[episode - 1])
    #         print seasonepisode
    #         c = np.genfromtxt(
    #             '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode%s%s.csv' % (
    #             str(7), str(7), str(episode), episodeNames[episode - 1]),
    #             delimiter="|", dtype=str, skiprows=0)
    #         transcript = c[:]
    #         for line in range(0, len(transcript)):
    #             if transcript[line:line + 1, 0:1][0][0].replace(" ", "") == "Dwight":
    #                 print transcript[line:line+1,1:2][0][0]
    #                 lines = np.append(lines, transcript[line:line + 1, 1:2][0][0])
    #     elif season == 8:
    # print "SEASON 8"
    # episodeNames = ["TheList","TheIncentive","Lotto","GardenParty","Spooked","Doomsday","Pam'sReplacement","Gettysburg","Mrs.California","ChristmasWishes","Trivia","PoolParty",
    #                 "JuryDuty","SpecialProject","Tallahasse","AfterHours","TesttheStore","LastDayInFlorida","GetTheGirl","WelcomeParty","AngryAndy","Fundraiser","TurfWar",
    #                 "FreeFamilyPortraitStudio"]
    # for episode in range(1,25):
    #     if episode in range(0,10):
    #         seasonepisode = 'Season%s-Episode0%s%s.csv' % (str(8), str(episode), episodeNames[episode - 1])
    #         print seasonepisode
    #         c = np.genfromtxt(
    #             '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode0%s%s.csv' % (
    #             str(8), str(8), str(episode), episodeNames[episode - 1]),
    #             delimiter="|", dtype=str, skiprows=0)
    #         transcript = c[:]
    #         for line in range(0, len(transcript)):
    #             if transcript[line:line + 1, 0:1][0][0].replace(" ", "") == "Toby":
    #                 print transcript[line:line+1,1:2][0][0]
    #                 lines = np.append(lines, transcript[line:line + 1, 1:2][0][0])
    #     else:
    #         seasonepisode = 'Season%s-Episode0%s%s.csv' % (str(8), str(episode), episodeNames[episode - 1])
    #         print seasonepisode
    #         c = np.genfromtxt(
    #             '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode%s%s.csv' % (
    #             str(8), str(8), str(episode), episodeNames[episode - 1]),
    #             delimiter="|", dtype=str, skiprows=0)
    #         transcript = c[:]
    #         for line in range(0, len(transcript)):
    #             if transcript[line:line + 1, 0:1][0][0].replace(" ", "") == "Toby":
    #                 print transcript[line:line+1,1:2][0][0]
    #                 lines = np.append(lines, transcript[line:line + 1, 1:2][0][0])
    #     else:
    # print "SEASON 9"
    # episodeNames = ["NewGuys","Roy'sWedding","AndysAncestry","WorkBus","HereComesTreble","TheBoat","TheWhale","TheTarget","DwightChristmas","Lice","SuitWarehouse",
    #                 "CustomerLoyalty","JuniorSalesman","Vandalism","CouplesDiscount","MovingOn","TheFarm","Promos","Stairmageddon","PaperAirplane","Livin'TheDream",
    #                 "AARM","Finale"]
    # for episode in range(1,24):
    #     seasonepisode = 'Season%s-Episode0%s%s.csv' % (str(9), str(episode), episodeNames[episode-1])
    #     print seasonepisode
    #     c = np.genfromtxt(
    #         '/Applications/MAMP/htdocs/theoffice/spreadsheets/Season%s/Season%s-Episode%s%s.csv' % (str(9), str(9), str(episode), episodeNames[episode-1]),
    #         delimiter="|", dtype=str, skiprows=0)
    #     transcript = c[:]
    #     for line in range(0,len(transcript)):
    #         if transcript[line:line+1,0:1][0][0].replace(" ","") == "Toby":
    #             print transcript[line:line+1,1:2][0][0]
    #             lines = np.append(lines,transcript[line:line+1,1:2][0][0])
    #
    for row in lines:
        print row
        writer.writerow([row])