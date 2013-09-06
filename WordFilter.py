from re import search
from re import escape
from os.path import expanduser

class WordFilter:
	"""A really simple swear filter, the word list isn't massive and it doesn't handle unicode bypasses or any other simple transforms
	perhaps consider forking https://github.com/jared-mess/profanity-filter which is where I took the word list from or using a better lib"""
	
	textFileLocation = expanduser("~") + "/CatHack/"

	def __init__(self):
		"""Word Source should be a file path with each word to filter on a new line"""
		
		self.wordList = set()
		self.addWordListToFilter(WordFilter.textFileLocation + "badwords.txt")
		self.addWordListToFilter(WordFilter.textFileLocation + "advertisementwordlist.txt")

	def addWordListToFilter(self, filePath):

		try:		
			f = open (filePath,"r")
			for line in iter(f):
				self.wordList.add(escape(line.strip()))
		finally:
			f.close()
	
	def textIsClean(self, text):
		text = text.lower()
		for word in self.wordList:
			if search("\b" + word, text + "\b") != None:
				return False

		return True

	def filterTweet(self, data):
		return self.textIsClean(data["text"])

		
