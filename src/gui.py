import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
from bs4 import BeautifulSoup
import requests, re
#sender and receiver = " "
def fetch_lyrics(song_artist, song_title):
    google_base_url = "https://www.google.com/search"

    new_artist_name = song_artist.replace(" ", "+")
    new_title = song_title.replace(" ", "+")

    p = {"q" : [new_artist_name, new_title, "metrolyrics"]}
    page = requests.get(google_base_url, params=p)
    page.encode = 'utf-8'
    soup = BeautifulSoup(page.text, 'html.parser')
    href = soup.find("h3", class_="r").a.get('href')
    url = re.search("q=(.*?)&", href).group(1)

    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    return "\n\n".join(i.text for i in soup.findAll("p", class_='verse'))

def sendingToMail(song_title,song_Artist,sender_mail,sender_mail_pass,receiver):    
    message = MIMEMultipart()    
    message["From"] = sender_mail    
    message["To"] = receiver    
    message["Subject"] = song_title #song title    
    lyrics = fetch_lyrics(song_Artist,song_title)
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
