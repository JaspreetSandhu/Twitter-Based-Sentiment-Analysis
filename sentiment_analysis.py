#Sentiment Analysis
#By: Jaspreet Sandhu
#Student: 251036035
#Due: November 14, 2018
         

def compute_tweets(x, y):
    try: #Attempts to open files entered in 'main.py', excepts an IOError and return an empty list if error is faced
        tweets = open(x, "r", encoding="utf-8")
    except IOError:
        return([])
        
    try:
        keywords = open(y, "r", encoding="utf-8")
    except IOError:
        return([])

    #Introduction of some variables to be used in the code, helps the reader make further sense of my work
    easternList = [0,0]
    centralList = [0,0]
    mountainList = [0,0]
    pacificList = [0,0]
    lineList = []
    
    for line in keywords: #for loop goes through each line in the keywords file, stripping the end-line characters and spliting the lines at the comma (either side of comma is added to a single list)
        line = line.rstrip()
        l = line.split(",")
        lineList.append(l[0]) #'lineList' holds values of list, making it a larger list with words and scores alternating (i.e. [word, score, word, score, ...])
        lineList.append(l[1])
    
    lineNum = 1
    for i in tweets:
        lineNum += 1

    ctr = lineNum #number of lines in the tweets file is calculated, so the program knows hoe many times to execute

    tweets.seek(0) #since the tweets file had already been run through when determining total number of lines, this function resets the position we are at from the last to the first (at index 0)

    while ctr != 1: #until the last line has been run through
        tweetList = []
        j = tweets.readline()
        j = j.rstrip()
        tweetList = j.split(" ", 5) #each line is split at the sapce for a total of 5 times, seperating each component in the line (latitude, longitude, value, date,  time, text)
        tweetList.remove(tweetList[4]) #the irrelevant compnents of the line list are removed (value, date, time)
        tweetList.remove(tweetList[3])
        tweetList.remove(tweetList[2])
        tweetList = list_format(tweetList) #executes 'list_format" function with tweetList as parameter

        zone = timezone(float(tweetList[0]),float(tweetList[1])) #time zone is determined using the latitude and longitude in the function

        eachWord = tweetList[2:] #since tweetList[2] marks the start of each word in the list, everything past that would be the rest of the words in the tweet
        totalScore = happiness_score(eachWord, lineList) #uses function 'happiness_score' to determine the tweet's score
        
        if totalScore > 0: #if the line consists of at least one keyword
            if zone == "Eastern":
                easternList[0] += totalScore #each region's list would be a tuple containing the score and count at index 0 and 1 respectively
                easternList[1] += 1

            elif zone == "Central":
                centralList[0] += totalScore
                centralList[1] += 1

            elif zone == "Mountain":
                mountainList[0] += totalScore
                mountainList[1] += 1

            elif zone == "Pacific":
                pacificList[0] += totalScore
                pacificList[1] += 1

        ctr -=1 #counter is decreased by 1 so the program processes the following line
        
    if easternList[1] != 0: #prevents division by zero error by firs tchecking if the counter is greater than 0 
        easternList[0] = easternList[0]/easternList[1] #the score is converted to an average by dividing it by the total count for each region

    if centralList[1] != 0:
        centralList[0] = centralList[0]/centralList[1]

    if mountainList[1] != 0:
        mountainList[0] = mountainList[0]/mountainList[1]

    if pacificList[1] != 0:
        pacificList[0] = pacificList[0]/pacificList[1]


    masterList = (easternList, centralList, mountainList, pacificList) #Each list is a tuple which is added to the larger list called 'masterList'


    tweets.close() #both files that were read are closed
    keywords.close()

    return masterList #list of tuples is returned


    

def list_format(tweetList):
    emptyList = [] #empty list will hold characters that are valid characters
    symbols = ",[]<>?:;{}|\+=/*&^%$#@!\"()\'_" #characters to avoid keeping
    for i in range(0, 2): #only for the longitude and latitude parts of the list
        tempVar = tweetList[i] #temporary variable is set to list at position i, so the index can be accessed within that as done below
        copyVar = tempVar
        for q in range(0, len(tempVar)):
            if tempVar[q] in symbols: 
                copyVar = copyVar.strip(tempVar[q]) #if particular character is in the string of invalid characters, it is removed
        if copyVar not in emptyList:
            emptyList.append(copyVar) #adds all characters that are not invalid

    for w in range(2, len(tweetList)):
        if tweetList[w] not in emptyList:
            emptyList.append(tweetList[w]) #essentially replaces first two components of list with new ones


    tweetList = emptyList


    text = tweetList[2] #text variable is assigned to part of list that contains tweet's contents
    text = text.lower()
    textList = text.split() #sentence is split into individual words 
    for d in range(0, len(textList)):
        wrd = textList[d]
        tempText = ""
        for f in range(0, len(wrd)):
            if wrd[f].isalpha():
                tempText += wrd[f] #new string only appends character if it is in the alphabet
        textList[d] = tempText #old word is replaced with new one that has invalid characters removed

    tweetList.remove(tweetList[2])
    for g in range(0, len(textList)):
        tweetList.append(textList[g]) #index 2 is removed, and each word is added as a new index


    return tweetList


def timezone(latitude,longitude):
    a = -67.444574 #endpoints of each region are assigned simple variable names
    b = -87.518395
    c = -101.998892
    d = -115.236428
    e = -125.242264

    latMax = 49.189787
    latMin = 24.660845

    if latitude < latMax and latitude > latMin: #only proceeds if tweet is within specified latitude
        if longitude < a and longitude >= b:
            zone = "Eastern"

        elif longitude < b and longitude >= c:
            zone = "Central"

        elif longitude < c and longitude >= d:
            zone = "Mountain"

        elif longitude < d and longitude >= e:
            zone = "Pacific"

        else:
            zone = "None"

    else:
        zone = "None"

    return zone #string is returned as a zone

    
def happiness_score(eachWord, lineList):
    num = 0
    total = 0
    tempTotal = 0
    for f in range(0, len(eachWord)):
        for h in range(0, len(lineList), 2):
            if eachWord[f] == lineList[h]: #if word exitsts in the set of keywords
                tempTotal += int(lineList[h+1])
                num += 1 #number of keyword occurences increases by 1 each time one is encountered

    if num > 0:
        total = tempTotal/num #each tweets total is the total score divided by nuimber of keyword occurences
    return(total)





            
