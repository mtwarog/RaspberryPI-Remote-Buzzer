import string,cgi,time, sys, subprocess 
from os import curdir, sep
import BaseHTTPServer
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

#Paths to python and buzzer script
python_src = '/usr/bin/python'
buzzer_src = '/home/pi/Desktop/buzzer/buzzer.py'

class MyHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        global rootnode
        try:
            ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
            if ctype == 'multipart/form-data':
                query=cgi.parse_multipart(self.rfile, pdict)
            self.send_response(301)
            
            self.end_headers()
            
            import subprocess

       	    cmd = [python_src, buzzer_src, '200', '2']
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE) 
        except :
            pass

ServerClass  = BaseHTTPServer.HTTPServer

if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 8000
server_address = ('0.0.0.0', port)

httpd = ServerClass(server_address, MyHandler)

sa = httpd.socket.getsockname()
print "Serving HTTP on", sa[0], "port", sa[1], "..."
httpd.serve_forever()