#!/usr/bin/python

from BaseHTTPServer import BaseHTTPRequestHandler

class pathHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        message_parts = [
                '%s' % self.path.split('/')[-1],
        ]
        message_parts.append('')
        message = '\r\n'.join(message_parts)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(message)
        return

if __name__ == '__main__':
    from BaseHTTPServer import HTTPServer
    server = HTTPServer(('localhost', 3000), pathHandler)
    print 'Starting server, use <Ctrl-C> to stop'
    server.serve_forever()
