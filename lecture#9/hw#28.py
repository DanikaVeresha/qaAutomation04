"""Task 28. Email address validator using regular expressions"""


import re


def email_validator(email: str):
    """Function to validate email address using regular expressions"""
    email_pattern_true = r'^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+$'

    if re.findall(email_pattern_true, email):
        return f'Email verification result: {email} - "True"'
    else:
        return f'Email verification result: {email} - "False"'


print(email_validator('aaa123@bbb.ccc'))  # True
print(email_validator('123@bbb.ccc')) # True
print('-----Email isn`t starts with @/.and isn`t ends @/.-----')
print(email_validator('@aaa123@bbb.ccc'))
print(email_validator('aaa123@bbb.ccc.'))
print(email_validator('.aaa123@bbb.ccc'))
print(email_validator('aaa123@bbb.ccc@'))
print(email_validator('@aaa123@bbb.ccc.'))
print('-----Email has more than one @/.-----')
print(email_validator('.aaa123bbb.ccc'))
print(email_validator('@aaa123bbb@ccc'))
print(email_validator('aaa123@@bbb.ccc'))
print(email_validator('aaa123@bbb..ccc'))
print('-----Email has space-----')
print(email_validator('aaa 123@bbb.ccc'))
print('-----In email . stands before @-----')
print(email_validator('aaa123.bbb@ccc'))
print('-----Email has more one ./@-----')
print(email_validator('aaa123@@bbb.ccc'))
print(email_validator('aaa123@bbb..ccc'))
print(email_validator('aaa123@@bbb..ccc'))
print('-----Email has more one ./@-----')
print(email_validator('aaa123@bbb.c.c.c'))
print(email_validator('a@aa@123@bbb.ccc'))
print(email_validator('a@aa@123@bbb.c.c.c'))
print('-----Email has space/empty-----')
print(email_validator(' aaa123 @b bb.ccc '))
print(email_validator(' aaa123@bbb.ccc '))
print(email_validator(' '))
print('-----Email has more one ./@-----')
print(email_validator('aaa123@@bbbccc'))
print(email_validator('aaa123bbb..ccc'))
print('-----Email starts/ends with special characters-----')
print(email_validator('_aaa123@bbb.ccc'))
print(email_validator('aaa123@bbb.ccc_'))
print(email_validator('!aaa123@bbb.ccc'))
print(email_validator('aaa123@bbb.ccc#'))
print(email_validator('~aaa123@bbb.ccc'))
print(email_validator('aaa123@bbb.ccc$'))
print(email_validator('aaa123@bbb.ccc|'))
print(email_validator('[aaa123@bbb.ccc'))
print('-----Email has special characters-----')
print(email_validator('aaa_123@bbb.ccc'))
print(email_validator('aaa#123@bbb.ccc'))
print(email_validator('aaa*123@bbb.ccc'))
print(email_validator('a#a%a*1&2)3@b:bb].c-c+c'))
print(email_validator('"aaa✳123@bbb.ccc"'))
print(email_validator('"aaa№123@bbb.ccc"'))


