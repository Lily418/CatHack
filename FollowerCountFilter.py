class FollowerCountFilter:

	def __init__(self, requiredFollowersToPass):
		self.requiredFollowersToPass = requiredFollowersToPass;

	def filterTweet(self, data):
		return data['user']['followers_count'] > self.requiredFollowersToPass
