from ncclient import manager
import http.server

# ホスト名を変更するときの書き方

# netconf_data = """
# <config>
#    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
#        <hostname>R1</hostname>
#    </native>
# </config>"""

address = ('', 10000)  # localhost を記入すると上手くいかない


class MyHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        pass

    def do_POST(self):
        print('path = {}'.format(self.path))
        print(self.path)
        print('headers\r\n-----\r\n{}-----'.format(self.headers))

        # print(self.headers['content-length'])
        content_length = int(self.headers['content-length'])

        # content_length 読みだす長さを指定しないと, rfile.read() で待ち続けてしまう
        print('body = {}'.format(self.rfile.read(content_length).decode('utf-8')))
        netconf_data = self.rfile.read(content_length).decode('utf-8')

        # ncclient でネットワーク機器への接続処理
        with manager.connect(
            host="172.16.0.100",
            port="830",
            username="ryo",
            password="cisco",
            hostkey_verify=False
        ) as m:
            netconf_reply = m.edit_config(netconf_data, target="running")

        self.send_response(200)
        self.send_header('Content-Type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(b'Hello, from do_POST')


with http.server.HTTPServer(address, MyHTTPRequestHandler) as httpd:
    print('待機中・・・')
    httpd.serve_forever()
