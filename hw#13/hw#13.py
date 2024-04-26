
email = 'Desh288diesh@gmail.com'
# email = 'Desh288diesh.gmail@com'
# email = '@desh288dieshgmail.com'
# email = 'desh288diesh@gmailcom.'
# email = 'desh_288diesh@gmail.com'
# email = 'desh288diesh@gmail.co_m'
# email = 'desh288@diesh@gmail.com'
# email = 'desh288diesh@gmail.c.om'

check_email_1 = email.find('@') < email.find('.')
check_email_2 = email.find('@') != 0 and email.find('.') != len(email) - 1
check_email_3 = email.split("@")[0].isalnum() and email.split(".")[1].isalnum()
check_email_4 = email.count('@') == 1 and email.count('.') == 1

if check_email_1 and check_email_2 and check_email_3 and check_email_4:
    print(f'Email: {email} - is correct')
else:
    print(f'Email: {email} - is incorrect')





