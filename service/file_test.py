def log(file_name, data):
    file_name = 'logs/' + file_name
    data = data
    with open(file_name, 'a', encoding="utf-8") as f:
        f.write(data)

if __name__ == '__main__':
    log('12','34')