import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.websocket
import json
import time
import datetime
import os, sys
import struct
import socket

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

Socket1=0
Socket2=1

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

    
    def post (self):
        WebCommand = self.get_argument ('command', '')
        WebValue = self.get_argument ('value', '')
        
        if WebCommand == 'Pi':
            if WebValue == 'Shutdown':
                if sys.platform == 'win32':
                    os.system('shutdown /s')
                else:
                    os.system('shutdown -h now')
            elif WebValue == 'Reboot':
                if sys.platform == 'win32':
                    os.system('shutdown /r')
                else:
                    os.system('shutdown -r now')
            else:
                print('No matching Pi Command')
                return
        elif WebCommand == 'Arduino':
            if WebValue == 'Reset':
                print('No matching Pi Command')
                return                
            else:
                print('No matching Arduino Command')
                return
        else:
            print('Command not recognised')


class SettingsHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('settings.html')

        
class GlenHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('Glenmorangie.html')
    def post (self):
        WebCommand = self.get_argument ('command', '')
        WebValue = self.get_argument ('value', '')
        
        if WebCommand == 'Pi':
            if WebValue == 'Shutdown':
                if sys.platform == 'win32':
                    os.system('shutdown /s')
                else:
                    os.system('shutdown -h now')
            elif WebValue == 'Reboot':
                if sys.platform == 'win32':
                    os.system('shutdown /r')
                else:
                    os.system('shutdown -r now')
            else:
                print('No matching Pi Command')
                return
        elif WebCommand == 'Arduino':
            if WebValue == 'Reset':
                print('No matching Pi Command')
                return                
            else:
                print('No matching Arduino Command')
                return
        elif WebCommand == 'Pour':
            if WebValue == '1':
                print('Drink 1 requested')
                return
            elif WebValue == '2':
                print('Drink 2 requested')
                return
            elif WebValue == '3':
                print('Drink 3 requested')
                return
            elif WebValue == '4':
                print('Drink 4 requested')
                return
            elif WebValue == '5':
                print('Drink 5 requested')
                return
            else:
                print('Unknown drink selection')
        else:
            print('Command not recognised')
            
class JackHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('Jack.html')
    def post (self):
        WebCommand = self.get_argument ('command', '')
        WebValue = self.get_argument ('value', '')
        
        if WebCommand == 'Pi':
            if WebValue == 'Shutdown':
                if sys.platform == 'win32':
                    os.system('shutdown /s')
                else:
                    os.system('shutdown -h now')
            elif WebValue == 'Reboot':
                if sys.platform == 'win32':
                    os.system('shutdown /r')
                else:
                    os.system('shutdown -r now')
            else:
                print('No matching Pi Command')
                return
        elif WebCommand == 'Arduino':
            if WebValue == 'Reset':
                print('No matching Pi Command')
                return                
            else:
                print('No matching Arduino Command')
                return
        elif WebCommand == 'Pour':
            if WebValue == '1':
                print('Drink 1 requested')
                return
            elif WebValue == '2':
                print('Drink 2 requested')
                return
            elif WebValue == '3':
                print('Drink 3 requested')
                return
            else:
                print('Unknown drink selection')
        else:
            print('Command not recognised')            


if __name__ == "__main__":

    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[
            (r"/", IndexHandler),
            (r"/settings", SettingsHandler),
            (r"/glenmorangie", GlenHandler),
            (r"/Jack", JackHandler)],
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            template_path=os.path.join(os.path.dirname(__file__), "templates"))

    
    httpServer = tornado.httpserver.HTTPServer(app)
    httpServer.listen(options.port)
    print ("Listening on port:", options.port)
    main_loop = tornado.ioloop.IOLoop.instance()
    # Schedule event (5 seconds from now)
    #main_loop.call_later(5,get_ip_address('wlan0'))
    # Start main loop
    main_loop.start()
