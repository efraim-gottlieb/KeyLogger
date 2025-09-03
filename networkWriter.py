import requests
class NetworkWriter:
    def send_data(self,data,url):
        self.url=url
        self.status=requests.post(url,data)
        return self.status

if __name__==('__main__'):
    c=NetworkWriter()
    c.send_data('{tt:tt}','http://127.0.0.1:5000/tasks')