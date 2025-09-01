class Encrypt:
    def __init__(self,key='kodkodecycled2025'):
        self.key=key
    def encrypt_text(self,text):
        tempkey=self.key*(len(text)//len(self.key))+ self.key[:(len(text)%len(self.key))]
        self.encrypted=[]
        for x,y in zip(text,tempkey):
            self.encrypted.append(chr(ord(x)^ord(y)))
        self.encrypted=''.join(self.encrypted)
    def decrypt_text(self,text):
        tempkey=self.key*(len(text)//len(self.key))+ self.key[:(len(text)%len(self.key))]
        self.decrypted=[]
        for x,y in zip(text,tempkey):
            self.decrypted.append(chr(ord(x)^ord(y)))
        self.decrypted=''.join(self.decrypted)
if __name__==("__main__"):
    c=Encrypt()
    c.encrypt_text('my name is srulik shvadron hi am 26 age')
    b=c.encrypted
    h=Encrypt()
    c.decrypt_text(b)
    print(b)
    print(c.decrypted)