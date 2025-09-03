import socket
import uuid
import requests

def get_system_info():
    # שם מחשב
    hostname = socket.gethostname()

    # כתובת IP פנימית
    try:
        ip_address = socket.gethostbyname(hostname)
    except:
        ip_address = None

    # כתובת MAC
    mac_num = uuid.getnode()
    mac_address = ":".join(["%02x" % ((mac_num >> ele) & 0xff)
                            for ele in range(0, 8*6, 8)][::-1])

    # מיקום לפי IP חיצוני
    location = {}
    try:
        external_ip = requests.get("https://api.ipify.org").text
        res = requests.get(f"https://ipinfo.io/{external_ip}/json")
        if res.status_code == 200:
            data = res.json()
            location = {
                "ip": data.get("ip"),
                "city": data.get("city"),
                "region": data.get("region"),
                "country": data.get("country"),
                "loc": data.get("loc")  # לדוגמה: "31.7683,35.2137"
            }
    except Exception as e:
        location = {"error": str(e)}

    return {
        "computer_name": hostname,
        "ip_address": ip_address,
        "mac_address": mac_address,
        "location": location
    }


if __name__ == "__main__":
    info = get_system_info()
    for k, v in info.items():
        print(f"{k}: {v}")
