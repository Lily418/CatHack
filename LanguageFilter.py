from guess_language import guess_language
from FilterHelper import removeLinks

class LanguageFilter:
	def __init__(self, language):
		"""The language should be a ISO 639-1 code of a language supported by https://bitbucket.org/spirit/guess_language"""
		self.language = language

	def filterTweet(self, data):
		return guess_language(removeLinks(data['text'])) == self.language
