from smtplib import SMTP

import requests
from bs4 import BeautifulSoup #to send email
import smtplib
#email body
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

samay=datetime.datetime.now()

content=''  #where we will place the content of the email


def news(url):
    print('excracting news')
    cnt = ''
    cnt +=('<b> Top Stories:</b>\n'+'<br>'+'-'*50+'<br>')
    response= requests.get(url)
    content = response.content
    soup= BeautifulSoup(content,'html.parser')
    for i,tag in enumerate(soup.find_all('td',attrs={'class':'title','valign':''})):
        a= (str(i+1)+' :: '+tag.text + "\n"+ '<br>')
        if tag.text != 'More':
                cnt +=a
        else:
            ''

    return(cnt)


cnt = news('https://news.ycombinator.com/')
content += cnt
content += ('<br>-------<br>')
content +=('<br><br>End of Message')

print('composing email...')
SERVER='smtp.gmail.com'
PORT= 587
FROM ='testtworked@gmail.com'
TO = 'testtworked@gmail.com'
PASS = 'lolokaybye'

msg=MIMEMultipart()
msg['Subject']= ' Top news stories HN [Automated Email]'+''+str(samay.day) + '-' + str(samay.month) + '-' + str(samay.year)
msg['From']= FROM
msg['To']= TO

msg.attach(MIMEText(content, 'html'))

print('initialising the server..')

server = smtplib.SMTP(SERVER, PORT)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.login(FROM,PASS)
server.sendmail(FROM, TO, msg.as_string())

print('email sent...')

server.quit()









