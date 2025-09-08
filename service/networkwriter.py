import requests

class NetworkWriter:
    def send_data(self, data, url='http://127.0.0.1:5000/api/upload'):
        response = requests.post(url, json=data)
        return response

if __name__ == '__main__':
    c = NetworkWriter()
    payload = {
        "machine": "efraim",
        "data": "זה תוכן הלוג שלי"
    }
    b = c.send_data(payload)
    print(b.status_code)
    print(b.text)
