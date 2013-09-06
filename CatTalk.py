from threading import Thread
from StreamRequest import StreamRequest 
from CatStreamListener import CatStreamListener

streamRequest = StreamRequest.createStream("cat, cats",  CatStreamListener());
tweetStream = Thread(target=streamRequest.startStream)
tweetStream.start()

blocking = True

while blocking:
	s = input('--> ')
	if s == "exit":
		blocking = False

streamRequest.close()
