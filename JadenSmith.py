"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
* Author: Taylor Cochran
* File Name: JadenSmith.py
* Date Created: 2017/09/09
* Last Modified: 2017/09/16
* Python 2.7
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
 				ALGORYTHM

* 1. Collect Jason Smith tweets and random Tweets
* 2. Test the AI using new tweets that are either from Jason or not
* 3. Anything that is less than 85 certain or wrong should be added to the training data for 	next time to further improve the AI

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""



'''MODULES'''
from watson_developer_cloud import Natural_Language_Classifier_v1
import json 


'''CLASS'''
class JadenSmith:

	'''FUNCTIONS'''
	def enterUserLogin(self, user, password):
		natural_language_classifier = Natural_Language_Classifier_v1(
			username = user,
			password = password)

	def trainClassifier(self, directory):
		# the training data must be on your machine
		with open(directory, 'rb') as training_data:
			classifier = natural_language_classifier.create(
				training_data=training_data,
				name='Jaden_Smith_Tweets',
				language='en')
		
		return json.dumps(classifier, indent=2)


	def testClassifer(self, classiferID, tweet):
		classes = natural_language_classifier.classify(classiferID,
			tweet)
		return json.dumps(classes, indent=2)


	def deleteClassifier(self, classiferID):
		classes.natural_language_classifier.remove(classiferID)



