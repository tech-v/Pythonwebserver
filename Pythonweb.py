from http.server import BaseHTTPRequestHandler, HTTPServer
import time
class GETHTTP(BaseHTTPRequestHandler):
	def do_GET(self):
			self.send_response(200)
			self.send_header("Content-Type", "text/plain")
			self.end_headers()
			self.wfile.write(bytes("Hello Guys this is the python web server","utf-8"))
			
			
if __name__ == "__main__":
	webServer = HTTPServer(("192.168.19.21",8080),GETHTTP)
	print("running")
	
	try:
		webServer.serve_forever()
	except KeyboardInterrupt:
		pass
	
	webServer.server_close()
	print("Bye")
