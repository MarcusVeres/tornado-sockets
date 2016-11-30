import tornado.ioloop
import tornado.web
import tornado.template as template
import tornado.websocket

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
        loader = template.Loader( "/Users/marcus.veres/learning/tornado/m1/" )
        response = loader.load( "templates/client.html" ).generate( myvalue = "AAA" )
        self.write( response )


def make_app():
    return tornado.web.Application([
        ( r"/" , MainHandler ) ,
        ( r"/websocket" , EchoWebSocket ) ,
        ( r"/client" , ClientSocket ) ,
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen( 8989 )
    tornado.ioloop.IOLoop.current().start()

