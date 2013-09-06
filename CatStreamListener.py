from guess_language import guess_language
from re import search
from WordFilter import WordFilter

class CatStreamListener:
	"""For the contents of data see https://dev.twitter.com/docs/platform-objects/tweets"""

	def __init__(self):
		self.wordFilter = WordFilter()

	
	
	def tweetReceived(self, data):
		if 'text' in data:
			if self.filterTweet(data):
				self.pushTweet(data)

	def filterTweet(self, data):

		messageInLowercase = data['text'].lower()		

		if data['user']['followers_count'] < 2000:
			return False

		if search("cat", messageInLowercase) == None and search("cats", messageInLowercase) == None:
			return False

		if search("RT", data['text']) != None:
			return False

		if guess_language(data['text']) != "en":
			return False

		if self.wordFilter.textIsClean(messageInLowercase) == False:
			return False
		
		
		return True
		

	def pushTweet(self, data):
		print(data['text'])
		return;
