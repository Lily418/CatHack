import creds
from twython import TwythonStreamer

class StreamRequest(TwythonStreamer):
    """A class for using the Twitter streaming API"""
	
    streamListener = None
	
    @staticmethod
    def createStream(words, streamListener):
        stream = StreamRequest(creds.APP_KEY, creds.APP_SECRET, creds.OAUTH_TOKEN, creds.OAUTH_TOKEN_SECRET)
        stream.words = words
        stream.streamListener = streamListener
        return stream

    def startStream(self):
        self.statuses.filter(track=self.words)

    def on_success(self, data):
        if 'text' in data:
            self.streamListener.tweetReceived(data)

    def on_error(self, status_code, data):
        print(status_code)

    def close(self):
        self.disconnect()
