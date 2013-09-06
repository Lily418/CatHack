from guess_language import guess_language

class CatStreamListener:
	"""For the contents of data see https://dev.twitter.com/docs/platform-objects/tweets"""
	
	def tweetReceived(self, data):
		if 'text' in data:
			if self.filterTweet(data):
				self.pushTweet(data)

	def filterTweet(self, data):

		messageInLowercase = data['text'].lower() 		

		if data['user']['followers_count'] < 1000:
			return False

		if "cat" not in messageInLowercase and "cats" not in messageInLowercase:
			return False

		if "RT" in data['text']:
			return False		
		
		
		
		return True
		

	def pushTweet(self, data):
		print(data['text'].encode('utf-8'))
