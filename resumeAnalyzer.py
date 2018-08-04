# import library
import string
import re
import csv
import glob
# First lets create a variable that will hold a list of the documents
# here is moe info on lists: https://docs.python.org/3/tutorial.datastruc
#tures.html

# Lets create all the different lists that will be needed
# 1. A list to hold the data in each resume
resumeData = []
# 2. A list to hold the filename/Person's name of resume
listOfNames = []
# 3. A list to keep track of the score from: Business & Finance Lexicon
businessAndFinanceScore = []
# 4. A list to keep track of the score from: Computer & Technology Lexicon
computerAndTechnologyScore = []
# 5. A list to keep track of the score from: Entertainment & Sports Lexicon
entertainmentAndSportsScore = []
# 6. A list to keep track of the score from: Medical & Healthcare Lexicon
medicalAndHealthCareScore = []
# 7. A list to keep track of the score from: Government & Politics Lexicon
governmentAndPoliticsScore = []
# 8. A list to keep track of the score from: Architecture & Engineering Lexicon
architectureAndEngineeringScore = []
# create a list that will keep track of the calculated score for each item
overallSentimentScore = []
# create a list that will keep track of the post processed resume data
postProcessedResumeData= []


# we want to process several documents an treat all of the data
# in the file as a single item (useful for making comaprisons of file to file)
# we could do someting like this:
for eachFile in glob.glob("Resumes/*.txt"):
    with open(eachFile, 'r') as myFile:
        resumeData.append(myFile.read().replace('\n', ' '))
    listOfNames.append(eachFile.replace('Resumes\\','').replace('.txt',''))
    

# read in the different types of Lexicons for the different types of jobs/industries
with open('positive.txt', 'r') as myFile:
    posWords = myFile.read().split('\n')
with open('negative.txt', 'r') as myFile:
    negWords = myFile.read().split('\n')
with open('businessAndFinance.txt', 'r') as myFile:
    businessAndFinanceWords = myFile.read().split('\n')
with open('computerAndTechnology.txt', 'r') as myFile:
    computerAndTechnologyWords = myFile.read().split('\n')
with open('entertainmentAndSports.txt', 'r') as myFile:
    entertainmentAndSportsWords = myFile.read().split('\n')
with open('medicalAndHealthCare.txt', 'r') as myFile:
    medicalAndHealthCareWords = myFile.read().split('\n')
with open('governmentAndPolitics.txt', 'r') as myFile:
    governmentAndPoliticsWords = myFile.read().split('\n')    
with open('architectureAndEgineering.txt', 'r') as myFile:
    architectureAndEngineeringWords = myFile.read().split('\n')


# create a loop that will read through each item, clean up the data
for item in resumeData:
    # reset the couner to 0, otherwise, your numbers would reflect the prior iteration of the loops
    posCounter = 0
    negCounter = 0
    businessAndFinanceCounter = 0
    computerAndTechnologyCounter = 0
    entertainmentAndSportsCounter = 0
    medicalAndHealthCareCounter = 0
    governmentAndPoliticsCounter = 0
    architectureAndEngineeringCounter = 0

    # look at the data before cleaning
    print("\npre-processed: " + ((item[:50] + '...') if len(item) > 100 else item))

    # lets clean up the data
    # remove starting and trailing whitespace and new lines with a strip function
    item = item.lower().strip()

    # remove HTML (must be done before removing puncuation
    item = re.sub("<.*?>", "", item)
    item = re.sub("<[^<]+?>", "", item)

    # remove puncuation
    for eachPunctuation in list(string.punctuation):
        item = item.replace(eachPunctuation, "")

    # look at the data after cleanning it
    print("post-processed: " + ((item[:50] + '...') if len(item) > 50 else item))

    # split the item up into a list of words to look at ech word and increment the approproiate counter
    words = item.split(" ")
    for eachWord in words:
        if eachWord in posWords:
          posCounter = posCounter + 1
        if eachWord in negWords:
          negCounter = negCounter + 1
        # This is going through the lexicon and counting the words  
        if eachWord in businessAndFinanceWords:
          businessAndFinanceCounter = businessAndFinanceCounter + 1
        if eachWord in computerAndTechnologyWords:
          computerAndTechnologyCounter = computerAndTechnologyCounter + 1
        if eachWord in entertainmentAndSportsWords:
          entertainmentAndSportsCounter = entertainmentAndSportsCounter + 1
        if eachWord in medicalAndHealthCareWords:
          medicalAndHealthCareCounter = medicalAndHealthCareCounter + 1
        if eachWord in governmentAndPoliticsWords:
          governmentAndPoliticsCounter = governmentAndPoliticsCounter + 1  
        if eachWord in architectureAndEngineeringWords:
          architectureAndEngineeringCounter = architectureAndEngineeringCounter + 1
          
    # keep track of the score in the list overallScore list variable
    overallSentimentScore.append(posCounter - negCounter)
    # Sending the score to the overall list
    businessAndFinanceScore.append(businessAndFinanceCounter)
    computerAndTechnologyScore.append(computerAndTechnologyCounter)
    entertainmentAndSportsScore.append(entertainmentAndSportsCounter)
    medicalAndHealthCareScore.append(medicalAndHealthCareCounter)
    governmentAndPoliticsScore.append(governmentAndPoliticsCounter)
    architectureAndEngineeringScore.append(architectureAndEngineeringCounter)
    # keep track of the post-processed item in the postProcessedSeveralListItems list (relative to the overallScore)
    postProcessedResumeData.append((item[:50] + '...') if len(item) > 50 else item)

    # look at the state for the post-processed item
    print("How many words: " + str(len(words)))
    print("Sentiment Score: " + str(posCounter - negCounter))
    print("Business & Finance Score: " + str(businessAndFinanceCounter))
    print("Computer & Technology Score: " + str(computerAndTechnologyCounter))
    print("Entertainment & Sports Score: " + str(entertainmentAndSportsCounter))
    print("Medical & Health Care Score: " + str(medicalAndHealthCareCounter))
    print("Government & Politics Score: " + str(governmentAndPoliticsCounter))
    print("Architecture & Engineering Score: " + str(architectureAndEngineeringCounter))

# use a zip function that will combine the 2 list items (think of this as creating a column
# of data with the "overallScore" and a column with the "postProcessedSeveralListItems")
combinedListOfItems = zip(listOfNames, overallSentimentScore, businessAndFinanceScore, computerAndTechnologyScore, entertainmentAndSportsScore, medicalAndHealthCareScore, governmentAndPoliticsScore, architectureAndEngineeringScore, postProcessedResumeData)

# finally, generate a csv file that has 2 column headings and then each row of data from combinedListOfItems
with open('sentimentkb619814.csv', 'w', newline='') as myFile:
    writer = csv.writer(myFile)
    writer.writerow(('Applicant Name', 'Sentiment Score', 'Business and Finance Score', 'Computer & Technology Score', 'Entertainment & Sports Score', 'Medical & Health Care Score', 'Government & Politics Score', 'Architecture & Engineering Score: ', 'Resume Data'))
    for row in combinedListOfItems:
        writer.writerow(row)








          
