#main.py
#By: Jaspreet Sandhu
#Student: 251036035
#Due: November 14, 2018

from sentiment_analysis import * #everything imported from 'sentiment_analysis' module

x = input("Enter the tweets file: ") #prompts user for files containing tweets and keywords respectively
y = input("Enter the keywords file: ")

finalList = compute_tweets(x, y) #uses tweets and keywords files as parameters for 'compute_tweets' function found in 'sentiment_analysis', holding results in 'finalList' variable

if len(finalList) > 0: #below lines only run if 'compute_tweets(x, y)' returns something other than an empty list (if file names are correct)
    easternList = finalList[0] #list for each region is assigned its respective tuble
    centralList = finalList[1]
    mountList = finalList[2]
    pacificList = finalList[3]

    print("""
The average happiness scores calculated for each region are:
_____________________________________________________________
""")
    print("Eastern: ", easternList[0], "with Count: ", easternList[1])
    print()
    print("Central: ", centralList[0], "with Count: ", centralList[1])
    print()
    print("Mountain: ", mountList[0],  "with Count: ", mountList[1])
    print()
    print("Pacific: ", pacificList[0], "with Count: ", pacificList[1])

    #Above lines printed to display results in a readable and more organized fashion 
      

