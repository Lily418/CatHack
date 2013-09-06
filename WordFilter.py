class WordFilter:
	"""A really simple swear filter, the word list isn't massive and it doesn't handle unicode bypasses or any other simple transforms
	perhaps consider forking https://github.com/jared-mess/profanity-filter which is where I took the word list from"""
	
	def __init__(self):
		"""Word Source should be a file path with each word to filter on a new line"""
		f = open ("badwords.txt","r")
		
		self.wordList = set()
		for line in iter(f):
			self.wordList.add(line)

	
	def textIsClean(self, text):
		for word in self.wordList:
			if word in text:
				return False

		return True
