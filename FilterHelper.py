import re

def removeLinks(text):
	"""This Regex taken from http://stackoverflow.com/questions/11331982/how-to-remove-any-url-within-a-string-in-python"""
	return re.sub(r'^https?:\/\/.*[\r\n]*', '', text, flags=re.MULTILINE)
