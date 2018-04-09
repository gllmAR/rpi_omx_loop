from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import os

hostName = "localhost"
hostPort = 80

class Http_Remote_Server(BaseHTTPRequestHandler):


	def do_GET(self):
		# description,url,command
		DATA = [
			["home", "/", "echo $HOSTNAME"],
			["simulate sensor 0", "/sensor_0", "sendosc 127.0.1 5005 /gpio i 0"],
			["simulate sensor 1", "/sensor_1", "sendosc 127.0.1 5005 /gpio i 1"],
			["reload looper", "/reload_looper", "sudo systemctl restart rpi_omx_loop"],
			["reload remote", "/reload_remote", "sudo systemctl restart http_remote"],
			["reboot", "/reboot", "sudo reboot"],
			["shutdown", "/shutdown", "sudo shutdown now -h"],
		]
		def serve_home():
			self.wfile.write(bytes("<html><head><title>REMOTE_CTL</title></head>", "utf-8"))
			self.wfile.write(bytes("<body><b><p>REMOTE_CTL</p></b>", "utf-8"))
			for EDATA in (DATA):
				self.wfile.write(bytes("<a href=%s>%s</a><br><br> " % (EDATA[1], EDATA[0]) , "utf-8"))
			self.wfile.write(bytes("<p>You accessed path: %s</p>" % self.path, "utf-8"))
			self.wfile.write(bytes("</body></html>", "utf-8"))

		def serve_function(COMMAND, DESCRIPTION):
			RESULT = os.popen(COMMAND).read()
			self.wfile.write(bytes('<html>', "utf-8"))
			self.wfile.write(bytes('  <head>', "utf-8"))
			self.wfile.write(bytes('    <title>'+DESCRIPTION+'</title>', "utf-8"))
			self.wfile.write(bytes('  </head>', "utf-8"))
			self.wfile.write(bytes('  <body>', "utf-8"))
			self.wfile.write(bytes(DESCRIPTION+' successfull.<br>', "utf-8"))
			self.wfile.write(bytes(str(RESULT)+'<br>', "utf-8"))
			self.wfile.write(bytes('  </body>', "utf-8"))
			self.wfile.write(bytes('</html>', "utf-8"))

		self.send_response(200)
		self.send_header("Content-type", "text/html")
		self.end_headers()

		serve_home()

		for EDATA in (DATA):
			if self.path == EDATA[1] or self.path == EDATA[1]+'/':
				serve_function(EDATA[2], EDATA[0])

myServer = HTTPServer(('', hostPort), Http_Remote_Server)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

try:
	myServer.serve_forever()
except KeyboardInterrupt:
	pass

myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))

