import os

def log(file_name, data):
    with open(file_name, 'a', encoding="utf-8") as f:
        f.write(data + "\n")

BASE_FOLDER = os.path.dirname(os.path.abspath(__file__))
DEVICES_FOLDER = os.path.join(BASE_FOLDER, "devices")

dev_name = 'meir'
dev_path = os.path.join(DEVICES_FOLDER, dev_name)
os.makedirs(dev_path, exist_ok=True)

f_name = os.path.join(dev_path, dev_name + ".txt")
log(file_name=f_name, data='123')

print(dev_path)
print(DEVICES_FOLDER)
