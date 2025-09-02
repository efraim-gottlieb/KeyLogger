import string

class SuspiciousTextChecker:
    def __init__(self, text, file_path="suspicious_words.txt"):
        self.suspicious_words = self.load_suspicious_words(file_path)
        self.text = text

    def load_suspicious_words(self, file_path):
        """טוען מילים חשודות מקובץ"""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                words = [line.strip().lower() for line in f if line.strip()]
            return set(words)
        except FileNotFoundError:
            print(f"קובץ {file_path} לא נמצא. משתמש ברשימה ריקה.")
            return set()

    def find_suspicious(self):
        """מחזיר את המילים החשודות שנמצאו בטקסט"""
        text_clean = self.text.lower().translate(str.maketrans('', '', string.punctuation))
        words = text_clean.split()
        return [w for w in words if w in self.suspicious_words]

    def is_suspicious(self):
        """בודק אם יש לפחות מילה חשודה אחת"""
        return 'suspicious' if self.find_suspicious() else 'not suspicious'

    def suspicious_score(self):
        """מחזיר אחוז המילים החשודות בטקסט"""
        text_clean = self.text.lower().translate(str.maketrans('', '', string.punctuation))
        words = text_clean.split()
        if not words:
            return 0.0
        found = self.find_suspicious()
        return len(found) / len(words)

    def suspicious_level(self):
        """מדרג את רמת החשד לפי הציון"""
        score = self.suspicious_score()
        if score == 0:
            return "תקין"
        elif score <= 0.2:
            return "נמוך"
        elif score <= 0.5:
            return "בינוני"
        else:
            return "גבוה"


# --- שימוש לדוגמה ---
if __name__ == '__main__':
    txt = "ddos hack ."
    checker = SuspiciousTextChecker(txt, "suspicious_words.txt")

    print("האם חשוד:", checker.is_suspicious())
    print("ציון חשד:", checker.suspicious_score())
    print("רמת חשד:", checker.suspicious_level())
