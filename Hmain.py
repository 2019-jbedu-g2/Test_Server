from http.server import  BaseHTTPRequestHandler, HTTPServer
import urllib
from urllib.parse import urlparse

class ncbot_RequestHandler(BaseHTTPRequestHandler):
    '''
    def do_POST(self):
        print("path: %sn" % self.path)

        o = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(o.query)

        print(params)

        self.wfile.write(bytes("Hello Client" , "utf8"))
        return
'''
    def do_GET(self):
        # parsed_path = urlparse(self.path)
        # message_parts = ['hello Client']
        # message = '<br>'.join(message_parts)
        # self.send_response(200)
        # self.end_headers()
        # self.wfile.write(message.encode('utf-8'))
        # return None
        self.route()
    def route(self):
        # 요청 값에 따라 처리할 함수를 중계함.
        if self.path == '':
            self.blank()
        elif self.path == '/hello':
            self.hello()
        elif self.path == '/test':
            self.test()
        elif self.path == '/python':
            self.python()
        elif self.path == '/barcode1':
            self.barcode1()
        elif self.path == '/barcode2':
            self.barcode2()
        else:
            self.reponse_404_not_found()
    def blank(self):
        self.response(200,'hello world')
    def hello(self):
        self.response(200,'안녕하세요!')
    def test(self):
        self.response(200,'테스트 성공!')
    def python(self):
        self.response(200,'파이썬 서버 테스트')
    def barcode1(self):
        self.response(200,'8802342034956')
    def barcode2(self):
        self.response(200,'8809683905938')
    def response_404_not_found(self):
        self.response(404,'요청하신 문서를 찾을 수 없습니다.')
    def response(self,status_code,body):
        #상태코드 전송
        self.send_response(status_code)

        #헤더 전송
        self.send_header('Content-type','text/plain; charset=utf-8')
        self.end_headers()

        #본문 전송
        self.wfile.write(body.encode('utf-8'))

# 테스트입니다
def run():
    print('Starting server')
    server_address = ('192.168.0.8', 8081)
    httpd = HTTPServer(server_address, ncbot_RequestHandler)

    print("Running the server")
    httpd.serve_forever()

run()