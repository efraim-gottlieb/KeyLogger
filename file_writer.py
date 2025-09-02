from datetime import datetime

#  כתיבת מערך של ההקשות בתוך קובץ עם חתימת זמן
class FileWriter:
    # פתיחת קובץ
    def __init__(self,file_name = 'file_key.txt'):
        self.file_name = file_name

    def send_data(self,list_key):
        # הוספת חתימת זמן
        timestamp = datetime.now(). strftime("%Y-%m-%d  %H:%M:%S")
        # כתיבת ההקשות וחתימת הזמן לתוך הקובץ
        with open(self.file_name, 'a', encoding="utf-8") as f:
            f.write(f'{timestamp}  - {list_key} \n')


if __name__ == '__main__':
    aa = FileWriter()
    print(aa.file_name)
    print(aa.send_data("חמלחנהון[נעעעי"))

    with open(aa.file_name, 'r', encoding="utf-8") as f:
        print(f.read())
