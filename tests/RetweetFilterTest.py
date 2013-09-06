import unittest
from RetweetFilter import RetweetFilter

class TestRetweetFilter(unittest.TestCase):

	def testTweetCacheFilter(self):
		retweetFilter = RetweetFilter()

		firstTweet = retweetFilter.checkAndCacheTweet("I like to play with my cat, my cat is cute")
		self.assertEqual(firstTweet, True)

		identicalTweet =  retweetFilter.checkAndCacheTweet("I like to play with my cat, my cat is cute") 
		self.assertEqual(identicalTweet, False)

		similarTweet = retweetFilter.checkAndCacheTweet("my cat is cute, and will rule the world someday")
		self.assertEqual(similarTweet, True)	

		#for i in range((10 ** 4) * 2):
			#self.assertEqual(retweetFilter.checkAndCacheTweet("my cat is cute, and will rule the world someday"), False)


if __name__ == '__main__':
    unittest.main()
