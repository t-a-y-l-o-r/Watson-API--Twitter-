# Watson-API--Twitter-
Classifies tweets as either Jaden Smith or Not Smith


## Functions 
    enterUserLoginc(user, password)
**EXPLINATION:** This function accepts the user name and password provided by the Watson website

    trainClassifier(directory)
**EXPLINATION:** This function accepts the absolute directory path to the training data for the classifier. The file should be .csv. Returns a json formatted classifer ID with some additionaly data. The training process can take several minutes

    testClassifer(classiferID, tweet)
**EXPLINATION:** Once the classifier is finished training this function can be called, passing both the ID acquired from trainClassifier() and a tweet. (Strings). The function will return a json formatted list containing the Classifer ID, tweet, and most confident answer. Additioanlly it will display a break down of each clissifer and their confidence levels as a double.

    deleteClassifier(classifierID)
**EXPLINATION:** After all testing has been completed and/or the AI should be retrained this function will delete the classifier matching the passed ID. Does not return anything.  
   


    
