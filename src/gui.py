import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
#sender and receiver = " " 
def sendingToMail(song_title,sender_mail,receiver,sender_mail_pass):
message = MIMEMultipart()
message["From"] = sender_mail
message["To"] = receiver
message["Subject"] = song_title #song title
lyrics =fetch_lyrics(song_artist, song_title)
messageBody = MIMEText(lyric,"plain")
message.attach(messageBody)
try:
    mail = smtplib.SMTP("smtp.gmail.com",587)
    mail.ehlo()
    mail.starttls()
    mail.login(sender_mail,sender_mail_pass) 
    mail.sendmail(message["From"],message["To"],message.as_string())
    print("Lyric has been sended")
    mail.close()
except Exception as e:
    print(e)
