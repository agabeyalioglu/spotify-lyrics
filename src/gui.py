import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
from bs4 import BeautifulSoup
import requests, re
from fetch_lyrics import fetch_lyrics
#sender and receiver = " "

def sendingToMail(song_title, song_Artist, sender_mail, sender_mail_pass, receiver):    
    message = MIMEMultipart()    
    message["From"] = sender_mail    
    message["To"] = receiver    
    message["Subject"] = song_title #song title    
    lyrics = song_title + "\n" + fetch_lyrics(song_Artist, song_title)
    messageBody = MIMEText(lyrics,"plain")    
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
sendingToMail("take me to church","hozier","senin adresin","seninm sifren","gonderilcek adres")
