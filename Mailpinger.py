import smtplib
## (╯°□°)╯︵ ┻━┻   << thego0n@MaL7
#sumVARS
gmail_user = 'yourgmail'
gmail_password = 'yourpassword'
port = 465
count = 0
def SENDY():
    sent_from = gmail_user
    to = ['YOURTARGET@MAIL.com']
    subject = 'YOUR SUBJECT'
    body = '////ADD YOUR MESSAGE HERE (HTML IS POSSIBLE)///'
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
        print('email sent - all is well..NEXT!')
    except:
        print('Something went wrong...')
while count < 301:
    SENDY()
    count += 1  # count = count + 1
