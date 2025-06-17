from encryption import *
"""
this is an example of using the encryption function

"""

###     the dictionary of the encryption     ###
my_key = {'e' : '@','f':'!','r':'+','a':'^','i':'`','m':'%'}

###     convert text to an encrypt text        ###
text = 'efraim'
print(encrypt_text(text,my_key))


###     convert text to an unencrypt text      ###
text = '@!+^`%'
print(unencrypt_text(text,my_key))
