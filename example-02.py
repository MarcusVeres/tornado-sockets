import tornado.ioloop
import tornado.web 

# starts the server 
def main():
    app = make_app()
    app.listen( 8888 )
    IOLoop.current().start()


# if the python interpreter is running that module (the source file) as the main program, it sets the special __name__ variable to have a value "__main__". 
# if this file is being imported from another module, __name__ will be set to the module's name.
# basically, if this file is imported as a module, we don't want to execute the main function, because we're just importing it for functionality
# if we are calling this program from the command line, we *want* to run the script, and therefore will run main()
if __name__ == "__main__" : 
    main()

