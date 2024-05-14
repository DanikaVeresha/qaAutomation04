"""Task 28. Email address validator using regular expressions"""
import re


def email_validator(email: str):
    """Function to validate email address using regular expressions"""
    email_pattern_true = (
        r'^\w[^@_.!#$%^&*:()-+=\|/`~?>\'\<;\[\"\]\,{}]'
        r'+@\w[^@_.!#$%^&*:()-+=\|/`~?>\'\<;\[\"\]\,{}]'
        r'+\.\w[^@_.!#$%^&*:()-+=\|/`~?>\'\<;\[\"\]\,{}]+$'
    )
    email_pattern_false = (
        r'^_|_$'
    )

    if re.findall(email_pattern_true, email) and not re.findall(email_pattern_false, email):
        print(f'Email verification result: {email} - "True"')

    else:
        print(f'Email verification result: {email} - "False"')


email_validator('aaa123@bbb.ccc')       # True
print('---------------------------------')
email_validator('@aaa123@bbb.ccc')
email_validator('aaa123@bbb.ccc.')
email_validator('@aaa123@bbb.ccc.')
email_validator('aaa123bbb.ccc@')
email_validator('.aaa123bbb.ccc')
print('---------------------------------')
email_validator('aaa123.bbb@ccc')
print('---------------------------------')
email_validator('aaa123@@bbb.ccc')
email_validator('aaa123@bbb..ccc')
email_validator('aaa123@@bbb..ccc')
print('---------------------------------')
email_validator('aaa123@bbb.c.c.c')
email_validator('a@aa@123@bbb.ccc')
email_validator('a@aa@123@bbb.c.c.c')
print('---------------------------------')
email_validator(' aaa123 @b bb.ccc ')
email_validator(' aaa123@bbb.ccc ')
email_validator(' ')
print('---------------------------------')
email_validator('aaa123@@bbb.ccc')
email_validator('aaa123@bbb..ccc')
print('---------------------------------')
email_validator('_aaa123@bbb.ccc')
email_validator('aaa123@bbb.ccc_')
email_validator('!aaa123@bbb.ccc')
email_validator('#aaa123@bbb.ccc')
email_validator('~aaa123@bbb.ccc')
email_validator('aaa123@bbb.ccc$')
email_validator('aaa123@bbb.ccc|')
email_validator('[aaa123@bbb.ccc')
print('---------------------------------')
email_validator('aaa_123@bbb.ccc')
email_validator('aaa#123@bbb.ccc')
email_validator('aaa*123@bbb.ccc')
email_validator('a#a%a*1&2)3@b:bb].c-c+c')
email_validator('aaa:123@bbb.ccc')
print('-------------Examples email from hw#13------------------')
email_validator('aaa277@bbb.ccc')   # var: True
email_validator('@aaa277bbbccc.')
email_validator('@aaa277bbbccc')
email_validator('.aaa277bbbccc')
email_validator('aaa277bbbccc@')
email_validator ('aaa277bbbccc.')
email_validator('@aaa277@bbb.ccc')
email_validator('aaa277@bbbccc')
email_validator('aaa277@bbb.ccc.')
email_validator('aaa277bbb.ccc')
email_validator('aaa277@bbbccc')
email_validator('aaa277@bbb.c.cc')
email_validator('aaa@277@b  bb.ccc')
email_validator('a_aa@bbb.cc/c')
email_validator('_aaa@bbb.ccc')
email_validator('aaa@bbb..c@c@c')
email_validator('aaa.bbb.ccc@c@c.c')
