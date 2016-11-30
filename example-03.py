import tornado.ioloop
import tornado.web
import tornado.template as template

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # self.write("Hello, world")
        t = template.Template("<html>{{ myvalue }}</html>")
        self.write( t.generate(myvalue="XXX") )
        print t.generate( myvalue="XXX" )

class UsesTemplate( tornado.web.RequestHandler ) :
    def get( self ) : 
        loader = template.Loader( "/Users/marcus.veres/learning/tornado/m1/" )
        response = loader.load( "templates/test.html" ).generate( myvalue = "AAA" )
        self.write( response )

def make_app():
    return tornado.web.Application([
        ( r"/" , MainHandler ) ,
        ( r"/tpl" , UsesTemplate ) ,
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen( 9595 )
    tornado.ioloop.IOLoop.current().start()

