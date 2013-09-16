from flask import Flask, render_template, request
from socketio import socketio_manage
from socketio.namespace import BaseNamespace
from werkzeug.wsgi import SharedDataMiddleware
from socketio.server import SocketIOServer
from time import sleep
from threading import Thread
import os
 
class CatNamespace(BaseNamespace):
    def onCatTweet(self, msg):
        self.emit("catTweet", msg);
        
        
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('cat.html')

@app.route("/socket.io/<path:path>")
def run_socketio(path):
    socketio_manage(request.environ, {'': CatNamespace})

def broadcastTweet(server, tweetMessage):
    pkt = {"type" : "event", "name" : "tweet", "args" : tweetMessage, "endpoint": "/CatTweets"}
    
    for sessid, socket in server.sockets.iteritems():
        socket.send_packet(pkt)

def streamTweets(server): 
    while True:
        sleep(2);
        broadcastTweet(server, "Hello Socket.IO")
        print("Broadcast");

    
if __name__ == '__main__':
    
    app = SharedDataMiddleware(app, {
        '/': os.path.join(os.path.dirname(__file__), 'static')
        })
    
    app.debug = True
    
    socketIOServer = SocketIOServer(('0.0.0.0', 8080), app, namespace="socket.io", policy_server=False)
    
    thread = Thread(target = streamTweets, args=[socketIOServer])
    thread.start()
    
    print('Listening on http://localhost:8080')
    socketIOServer.serve_forever()
    
    

        