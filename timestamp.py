def get_timestamp():
    import time
    my_time = time.localtime()
    year = (my_time[0])
    month = (my_time[1])
    day = (my_time[2])
    hour = (my_time[3])
    minute = (my_time[4])
    time = (f"{year}/{month}/{day}\n{hour}:{minute}")
    s = (len(str(year))+len(str(month))+len(str(day))+3) * '-'
    timestamp = (f'{s}\n{time}\n{s}')
    return [my_time,timestamp]


if __name__ == '__main__':
    ###     graphic stamp       ###
    print(get_timestamp()[1])

    ###     text stamp      ###
    print(get_timestamp()[0])

