import thread
from StreamRequest import StreamRequest 
from CatStreamListener import CatStreamListener

streamRequest = StreamRequest.createStream("cat, cats",  CatStreamListener());
thread.start_new_thread(streamRequest.startStream, ())

blocking = True

while blocking:
	s = raw_input('--> ')
	if s == "exit":
		blocking = False

streamRequest.close()
