import time
from time import localtime as T, sleep

def time_stamp():
    s='*'*6
    sl='/'
    a = [s, ' ', str(T()[2]), sl, str(T()[1]), sl, str(T()[0]), ' ', str(T()[3]), ':', str(T()[4]), ':', str(T()[5]),' ', s]
    return ''.join(a)

def time_stamp2():
    s=''
    sl='.'
    a = [s, ' ', str(T()[2]), sl, str(T()[1]), sl, str(T()[0]), '_', str(T()[3]), '.', str(T()[4]), '.', str(T()[5]),' ', s]
    return ''.join(a)



if __name__ == '__main__':

    while 1:
         sleep(2)
         print(time_stamp2())

