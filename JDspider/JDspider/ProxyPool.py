import requests
import json


class Proxy(object):
    def __init__(self):
        self.url = 'http://127.0.0.1:8000/?types=0&protocol=0&count=10&country=国内'

    def get_ip(self):
        r = requests.get(self.url)
        ip_ports = json.loads(r.text)
        print(ip_ports)
        ip_list = []
        for ip in ip_ports:
            ip_list.append({'http': 'http://%s:%s' % (ip[0], ip[1]), 'https': 'https://%s:%s' % (ip[0], ip[1])})
        return ip_list

if __name__ == '__main__':
    ip = Proxy()
    ip.get_ip()