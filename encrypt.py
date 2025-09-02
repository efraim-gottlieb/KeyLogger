from random import randint
class Encryption:
    def __init__(self,key='kodkodecycled2025'):
        self.key=key
        if key=='RAND':
            self.key=''
            while len(self.key)<=100:
                self.key+=str(randint(0,100))
    def xor_encrypt(self, text):
        """מגדיר אורך של מפתח ומעביר על הtext"""
        self.tempkey = self.key * (len(text) // len(self.key)) + self.key[:(len(text) % len(self.key))]
        self.t_encrypted = ''.join(chr(ord(x) ^ ord(y)) for x, y in zip(text, self.tempkey))
    def encrypt_text(self,text):
        self.xor_encrypt(text)
        self.encrypted = self.t_encrypted

    def decrypt_text(self, text):
        self.xor_encrypt(text)
        self.decrypted = self.t_encrypted

    def encrypt_file(self,file):
        self.file=file
        with open(self.file,'r') as f:
            data=f.read()
        self.xor_encrypt(data)
        encrypt_data=self.t_encrypted
        with open('encrypt_file.txt', 'w') as f:
            f.write(encrypt_data)

    def decrypt_file(self, file):
        self.file = file
        with open(self.file, 'r') as f:
            data = f.read()
        self.xor_encrypt(data)
        decrypt_data = self.t_encrypted
        with open('decrypt_file.txt', 'w') as f:
            f.write(decrypt_data)



if __name__==("__main__"):
    c=Encryption()
    c.encrypt_text('hii  ')
    b=c.encrypted
    c.decrypt_text(b)
    r=Encryption('RAND')
    r.encrypt_text('my name is srulik shvadron i am 26 age')
    b=r.encrypted
    r.decrypt_text(b)
    s = Encryption('עי ')
    s.encrypt_text('my name is srulik shvadron i am 26 age')
    b = s.encrypted
    s.decrypt_text(b)
    f=Encryption()
    f.encrypt_file('test.txt')
    f.decrypt_file('encrypt_file.txt')


    print(f'c: {c.encrypted}{len(c.encrypted)}\n{c.decrypted}\n'
          f'r: {r.encrypted}\n{r.decrypted}\n'
          f's: {s.encrypted}\n{s.decrypted}\n')






