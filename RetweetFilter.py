from collections import deque
from re import search

class RetweetFilter:

	def __init__(self):
		self.tweetCache = deque()

	def checkAndCacheTweet(self, text):

		wordList = list()		
				
		for word in text.split():
			if search("[a-z]+", word) != None:
				wordList.append(word)
			
		
		for tweet in self.tweetCache:
			newWords = 0			
			for word in wordList:
				if word not in tweet:
					newWords += 1
						
			originalContentIndex = newWords / len(wordList)
			if originalContentIndex < 0.5:
				return False			
				


		
		if len(self.tweetCache) < 10 ** 4:
			self.tweetCache.append(wordList)
		else:
			self.tweetCache.popleft()
			self.tweetCache.append(wordList)

		return True
