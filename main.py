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
from lcd import *

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

Socket1=0
Socket2=1

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')
        lcd_string("Index Requested",LCD_LINE_1)
    
    def post (self):
        WebCommand = self.get_argument ('command', '')
        WebValue = self.get_argument ('value', '')
        
        if WebCommand == 'Pi':
            if WebValue == 'Shutdown':
                if sys.platform == 'win32':
                    os.system('shutdown /s')
                else:
                    lcd_string("Shutting down...",LCD_LINE_2)
                    os.system('shutdown -h now')
            elif WebValue == 'Reboot':
                if sys.platform == 'win32':
                    os.system('shutdown /r')
                else:
                    lcd_string("Rebooting...",LCD_LINE_2)
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

            
class GlenHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('Glenmorangie.html')
        lcd_string("Drinks Dispenser",LCD_LINE_1)
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

class TestHandler(tornado.web.RequestHandler):
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


class IsaacHandler(tornado.web.RequestHandler):
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
            
class SocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print("WebSocket opened")

    def on_message(self, requested):
        response = "Socket" + requested
        #self.write_message(u"You said: " + )
        print(response)
        self.write_message(response)

    def on_close(self):
        print("WebSocket closed")


def UpdateIPs():
    lcd_string("LAN: " + get_ip_address('eth0'),LCD_LINE_3)
    lcd_string("WLAN: " + get_ip_address('wlan0'),LCD_LINE_4)    


if __name__ == "__main__":
    lcd_init()
    lcd_string("Server Running...",LCD_LINE_1)
    lcd_string("   ",LCD_LINE_2)
    lcd_string("LAN: " + get_ip_address('eth0'),LCD_LINE_3)
    lcd_string("WLAN: " + get_ip_address('wlan0'),LCD_LINE_4)
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[
            (r"/", IndexHandler),
            (r"/isaac", IsaacHandler),
            (r"/socket", SocketHandler),
            (r"/glenmorangie", GlenHandler),
            (r"/test", TestHandler)],
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            template_path=os.path.join(os.path.dirname(__file__), "templates"))

    
    httpServer = tornado.httpserver.HTTPServer(app)
    httpServer.listen(options.port)
    print ("Listening on port:", options.port)
    main_loop = tornado.ioloop.IOLoop.instance()
    # Schedule event (5 seconds from now)
    main_loop.call_later(5, UpdateIPs)
    # Start main loop
    main_loop.start()
