import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
from bs4 import BeautifulSoup
import requests, re
from fetch_lyrics import fetch_lyrics
from PyQt5 import QtWidgets
#sender and receiver = " "
class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.yaziAlani = QtWidgets.QTextEdit()
        self.yaziAlani.setText(fetch_lyrics("hozier","take me to church"))
        self.yaziAlani.setReadOnly(True)
        self.temizle = QtWidgets.QPushButton("Clear")
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.yaziAlani)
        v_box.addWidget(self.temizle)
        self.setLayout(v_box)
        self.temizle.clicked.connect(self.click)
        self.setWindowTitle("Lyric")
        self.show()
    
    def click(self):
        self.yaziAlani.clear()

app = QtWidgets.QApplication(sys.argv)
pencere = Window()
sys.exit(app.exec_())

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
# Example : sendingToMail("take me to church","hozier","senin adresin","seninm sifren","gonderilcek adres")
