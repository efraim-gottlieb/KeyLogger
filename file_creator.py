from datetime import datetime

#  כתיבת מערך של ההקשות בתוך קובץ עם חתימת זמן
class File:
    # פתיחת קובץ
    def __init__(self,file_name):
        self.file_name = file_name
        self.data = None
    def send_data(self,data):
        # !!הוספת חתימת זמן
        timestamp = datetime.now(). strftime("%Y-%m-%d  %H:%M:%S")
        # כתיבת ההקשות וחתימת הזמן לתוך הקובץ
        with open(self.file_name, 'a', encoding="utf-8") as f:
            # f.write(f'{timestamp}  - {list_key} \n')
            f.write(f'{self.data}')


if __name__ == '__main__':
    aa = File('e')
    aa.send_data('22')
