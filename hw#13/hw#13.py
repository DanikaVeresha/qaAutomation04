# email = ' '
email = 'aaa@bbb.ccc'

# email = '@aaabbbccc.'
# email = '@aaabbbccc'
# email = '.aaabbbccc'
# email = 'aaabbbccc@'
# email = 'aaabbbccc.'

# email = 'aaa@bbbccc'
# email = 'aaabbb.ccc'
# email = 'aaa@bb@b.ccc'
# email = 'aaa@bbb.c.cc'
# email = 'aaabbbccc'

# email = 'a@aa@@bbbccc'
# email = 'aaabbb...ccc'
# email = 'a@aab@bb@.ccc'
# email = 'aaa@bbb.c.c.c'

# email = 'a_aa@bbb.cc/c'
# email = '_aaa@bbb.ccc/'

# email = 'aaa@bbb.c@c@c'
# email = 'aaa.bbb.ccc@cc.c'

condition_0 = (email != '') # True

condition_1 = email.find('@') < email.find('.') # True
condition_2 = email.find('.') > email.find('@') # False

condition_3 = email.find('@') != 0 and email.find('.') != len(email) - 1 # True
condition_4 = email.find('@') == 0 and email.find('.') == len(email) - 1 # False
condition_5 = email.find('@') == 0 or email.find('.') == len(email) - 1 # False
condition_6 = email.find('.') == 0 or email.find('@') == len(email) - 1 # False

condition_7 = email.replace('@', '').replace('.', '').isalnum() # True

condition_8 = email.count('@') == 1 and email.count('.') == 1 # True
condition_9 = email.count('@') == 0 and email.count('.') == 0 # False
condition_10 = email.count('.') > 1 and email.count('@') > 1 # False
condition_11 = email.count('.') == 0 or email.count('@') >= 1 # False
condition_12 = email.count('.') >= 1 or email.count('@') == 0 # False

successful_check_email = (condition_0 and condition_1 and condition_3 and condition_7
                          and condition_8)
unsuccesful_check_email = (condition_2 or condition_4 or condition_5 or condition_6
                           or condition_9 or condition_10 or condition_11 or condition_12)

try:
    if successful_check_email:
        print(f'Email: {email} - is correct "True"')
    elif unsuccesful_check_email:
        print(f'Email: {email} - is incorrect "False"')
    else:
        print(f'Email: {email} - test case not covered')
except ValueError as ve:
    print(ve)









