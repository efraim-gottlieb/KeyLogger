from encryption import *

###     the dictionary of the encryption     ###
my_key = {'e' : '@','f':'!','r':'+','a':'^','i':'`','m':'%'}

###     encrypt text        ###
text = 'efraim'
print(encrypt_text(text,my_key))


###     unencrypt text      ###
text = '@!+^`%'
print(unencrypt_text(text,my_key))
