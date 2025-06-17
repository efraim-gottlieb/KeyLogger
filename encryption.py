"""

encrypt and unencrypt text
this file is only an example of a method to encrypt text

"""
def encrypt_text(text,encrypt_key):
    encrypt_text =  ''
    counter = 0
    #print(0,'% completed')
    for i in text:
        counter += 1
        percent = 100 // len(text) * counter
        if percent != 100:
            #print(percent,'% completed')
            pass
        encrypt_text += encrypt_key[i]
    #print(100,'% completed')
    #print('Yor text is now encoded!')
    return encrypt_text



def unencrypt_text(text,encrypt_key):
    unencrypt_key = {}
    for i in encrypt_key.keys():
        unencrypt_key[encrypt_key[i]] = i
    un_encrypt_text =  ''
    counter = 0
    #print(0,'% completed')
    for i in text:
        counter += 1
        percent = 100 // len(text) * counter
        if percent != 100:
            #print(percent,'% completed')
            pass
        un_encrypt_text += unencrypt_key[i]
    # print(100,'% completed')
    # print('Yor text is now unencoded!')
    return un_encrypt_text



if __name__ == '__main__':
    pass
