class KeywordFilter:

	def __init__(self, keywords, requiredKeywordCount):
		self.keywords = keywords
		self.requiredKeywordCount = requiredKeywordCount

	def filterTweet(self, data):

		keywordCount = 0
		for keyword in self.keywords:
			if keyword in data['text']:
				keywordCount += 1
				if keywordCount >= self.requiredKeywordCount:
					return True
		
		return False
