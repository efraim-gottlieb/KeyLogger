from random import randint
class Encrypt:
    def __init__(self,key='kodkodecycled2025'):
        self.key=key
        if key=='RAND':
            self.key=''
            while len(self.key)<=100:
                self.key+=str(randint(0,100))
    def xor_encrypt(self, text):
        self.tempkey = self.key * (len(text) // len(self.key)) + self.key[:(len(text) % len(self.key))]
        self.t_encrypted = ''.join(chr(ord(x) ^ ord(y)) for x, y in zip(text, self.tempkey))
    def encrypt_text(self,text):
        self.xor_encrypt(text)
        self.encrypted = self.t_encrypted

    def decrypt_text(self, text):
        self.xor_encrypt(text)
        self.decrypted = self.t_encrypted


if __name__==("__main__"):
    c=Encrypt()
    c.encrypt_text('my name is srulik shvadron i am 26 age')
    b=c.encrypted
    c.decrypt_text(b)
    r=Encrypt('RAND')
    r.encrypt_text('my name is srulik shvadron i am 26 age')
    b=r.encrypted
    r.decrypt_text(b)
    s = Encrypt('hii ')
    s.encrypt_text('my name is srulik shvadron i am 26 age')
    b = s.encrypted
    s.decrypt_text(b)

    print(f'c: {c.encrypted}\n{c.decrypted}\n'
          f'r: {r.encrypted}\n{r.decrypted}\n'
          f's: {s.encrypted}\n{s.decrypted}\n')






