from time import localtime as T, sleep

def time_stamp():
    s='*'*6
    sl='/'
    a = [s, ' ', str(T()[2]), sl, str(T()[1]), sl, str(T()[0]), ' ', str(T()[3]), ':', str(T()[4]), ':', str(T()[5]),' ', s]
    return ''.join(a)



###     add text to memory      ###
def add_time():
    sleep(2)
    stamp = (time_stamp())
    return stamp


if __name__ == '__main__':

    while 1:
        add_time()
         # sleep(2)
         # print(time_stamp())
