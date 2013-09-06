import re

from guess_language import guess_language
from re import search
from WordFilter import WordFilter
from RetweetFilter import RetweetFilter


class CatStreamListener:
	"""For the contents of data see https://dev.twitter.com/docs/platform-objects/tweets"""

	def __init__(self):
		self.wordFilter = WordFilter()
		self.retweetFilter = RetweetFilter()

	
	
	def tweetReceived(self, data):
		if 'text' in data:
			if self.filterTweet(data):
				self.pushTweet(data)

	def filterTweet(self, data):

		messageInLowercase = data['text'].lower()	
		messageWithoutUrls = self.removeLinks(messageInLowercase)	

		if data['user']['followers_count'] < 2000:
			return False

		if search("cat", messageInLowercase) == None and search("cats", messageInLowercase) == None:
			return False

		if guess_language(messageWithoutUrls) != "en":
			print("NOT ENGLISH: " +  data['text'])
			return False

		if self.wordFilter.textIsClean(messageInLowercase) == False:
			print("SENSORED: " +  data['text'])
			return False

		if not self.retweetFilter.checkAndCacheTweet(messageWithoutUrls):
			print("RETWEET: " +  data['text'])
			return False
		
		
		return True
		

	def pushTweet(self, data):
		print(data['text'])
		return;

	def removeLinks(self, text):
		"""This Regex taken from http://stackoverflow.com/questions/11331982/how-to-remove-any-url-within-a-string-in-python"""
		return re.sub(r'^https?:\/\/.*[\r\n]*', '', text, flags=re.MULTILINE)
