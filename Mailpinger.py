import smtplib
## (╯°□°)╯︵ ┻━┻   << thego0n@MaL7
#sumVARS
gmail_user = 'yourgmail'
gmail_password = 'yourpassword'
port = 465
count = 0
def SENDY():
    sent_from = gmail_user
    to = ['mail@mail.xom']
    subject = 'justa subject'
    body = '///////////add my spiel here////'
    email_text = """\
    From: %s
    To: %s
    Subject: %s
    %s
    """ % (sent_from, ", ".join(to), subject, body)
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', port)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()
        print('one step closer to heaven baby')
    except:
        print('Something went wrong...')
while count < 1000000:
    SENDY()
    count += 1  # count = count + 1