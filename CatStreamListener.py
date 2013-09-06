from WordFilter import WordFilter
from RetweetFilter import RetweetFilter
from KeywordFilter import KeywordFilter
from LanguageFilter import LanguageFilter
from FollowerCountFilter import FollowerCountFilter

class CatStreamListener:
	"""For the contents of data see https://dev.twitter.com/docs/platform-objects/tweets"""

	def __init__(self):
		self.filters = list()
		self.filters.append(FollowerCountFilter(2000))
		self.filters.append(WordFilter())
		self.filters.append(KeywordFilter(("cat", "cats"), 1))
		self.filters.append(LanguageFilter("en"))
		self.filters.append(RetweetFilter(10 ** 4))

	
	
	def tweetReceived(self, data):
		if 'text' in data:
			if self.filterTweet(data):
				self.pushTweet(data)

	def filterTweet(self, data):
		
		for f in self.filters:
			if not f.filterTweet(data):
				return False


		return True
		

	def pushTweet(self, data):
		print(data['text'])
		return;


