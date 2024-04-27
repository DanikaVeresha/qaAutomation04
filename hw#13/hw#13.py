# email = ' '
email = 'aaa277@bbb.ccc' # True
# email = '@aaa277bbbccc.'
# email = '@aaa277bbbccc'
# email = '.aaa277bbbccc'
# email = 'aaa277bbbccc@'
# email = 'aaa277bbbccc.'
# email = '@aaa277@bbb.ccc'
# email = 'aaa277@bbbccc'
# email = 'aaa277@bbb.ccc.'
# email = 'aaa277bbb.ccc'
# email = 'aaa277@bbbccc'
# email = 'aaa277@bbb.c.cc'
# email = 'aaa@277@bbb.ccc'

# email = 'a_aa@bbb.cc/c'
# email = '_aaa@bbb.ccc/'

# email = 'aaa@bbb..c@c@c'
# email = 'aaa.bbb.ccc@c@c.c'

check_email = (email != ' '
               and (email.find('@') < email.find('.'))
               and email.find('@') != 0
               and email.find('.') != len(email) - 1
               and (email.replace('@', '').replace('.', '').isalnum())
               and email.count('@') == 1
               and email.count('.') == 1
               and email.count('@') != 0
               and email.count('.') != 0)

if check_email:
    print(f'Result check email: {email} - "True"')
else:
    print(f'Result check email: {email} - "False"')











