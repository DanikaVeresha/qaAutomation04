
email = 'desh288diesh@gmail.com'

check_email = (email.find('@') < email.find('.') and
               email.find('.') != -1 and email.find('@') != 0 and
               (email.isalnum() or email.isascii()) and
               email.count('@') == 1 and email.count('.') == 1)

if check_email:
    print(f'Email: {email} - is correct\n'
          f'Result checking email: {check_email}')
else:
    print(f'Email: {email} - is incorrect\n'
          f'Result checking email: {check_email}')


