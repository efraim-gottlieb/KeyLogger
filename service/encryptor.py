class Encrypt:
    def __init__(self, key):
        self.key = key
    def decrypt(self, data):
        return "".join(chr(ord(c) ^ self.key) for c in data)

    def encrypt(self, data):
        return "".join(chr(ord(c) ^ self.key) for c in data)