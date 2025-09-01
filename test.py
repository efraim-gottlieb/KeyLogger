from Listener import *
a = Listener()
t = threading.Thread(target=a.run)
t.start()
num = 3
while num > 0:
    time.sleep(5)
    print(a.get_keys())
    num -= 1
a.stop()
