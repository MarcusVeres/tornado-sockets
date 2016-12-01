import os
import tornado.ioloop
import tornado.web
import tornado.template as template
import tornado.websocket

#

PORT = 8989
BASE_PATH = os.path.dirname( os.path.abspath( __file__ ))
STATIC_PATH = BASE_PATH + '/static/'

#

def make_app():
    return tornado.web.Application( handlers , **settings )

#

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # self.write("Hello, world")
        t = template.Template("<html>{{ myvalue }}</html>")
        self.write( t.generate(myvalue="XXX") )
        print t.generate( myvalue="XXX" )


class EchoWebSocket( tornado.websocket.WebSocketHandler ) :

    def open(self):
        print("WebSocket opened")

    def on_message(self, message):
        self.write_message(u"You said: " + message)

    def on_close(self):
        print("WebSocket closed")


class ClientSocket( tornado.web.RequestHandler ) :
    def get( self ) : 
        loader = template.Loader( BASE_PATH )
        response = loader.load( "templates/client.html" ).generate( myvalue = "AAA" )
        self.write( response )

#

settings = {
    'debug' : True , 
    'static_path' : STATIC_PATH
}

handlers = [ 
    ( r"/" , MainHandler ) ,
    ( r"/websocket" , EchoWebSocket ) ,
    ( r"/client" , ClientSocket ) ,
]

#

if __name__ == "__main__":
    app = make_app()
    app.listen( PORT )
    print( "running on port: %d" % PORT )
    tornado.ioloop.IOLoop.current().start()

