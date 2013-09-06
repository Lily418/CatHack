import unittest

from WordFilter import WordFilter

class TestWordFilter(unittest.TestCase):

	def testTextIsClean(self):
		wordFilter = WordFilter()
		self.assertEqual(wordFilter.textIsClean("FUCK"), False)
		self.assertEqual(wordFilter.textIsClean("pissed matched i get really pissed off when my cat doesn't sleep with me"), False)
		self.assertEqual(wordFilter.textIsClean("I love my cat"), True)

if __name__ == '__main__':
    unittest.main()
