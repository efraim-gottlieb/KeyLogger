from encryption import *
"""
this is an example of using the encryption function

"""

###     the dictionary of the encryption     ###
my_key = {'e' : '@','f':'!','r':'+','a':'^','i':'`','m':'%'}

###     encrypt text        ###
text = 'efraim'
print(encrypt_text(text,my_key))


###     unencrypt text      ###
text = '@!+^`%'
print(unencrypt_text(text,my_key))
