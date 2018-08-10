from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests, re,sys,smtplib, os
from bs4 import BeautifulSoup
from fetch_lyrics import fetch_lyrics
from PyQt5 import QtWidgets
#sender and receiver = " "
class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.lyric_area = QtWidgets.QTextEdit()
        self.lyric_area.setText(fetch_lyrics("hozier","take me to church"))
        self.lyric_area.setReadOnly(True)
        self.save_lyric = QtWidgets.QPushButton("Save Lyric")
        self.buton =QtWidgets.QPushButton("Send to My Mail")
        
        h_box =QtWidgets.QHBoxLayout()
        h_box.addWidget(self.buton)
        h_box.addWidget(self.save_lyric)
        
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.lyric_area)
        v_box.addLayout(h_box)
        
        self.setLayout(v_box)
        self.setWindowTitle("Lyric")
        self.show()
    def save(self):
          file_name = QtWidgets.QFileDialog.getSaveFileName(self,"Save Lyric",os.getenv("HOME"))

           with open(file_name[0],"w") as file:

                file.write(self.lyric_area.toPlainText())
    def click(self):
        #sendingToMail(fill the blanks)
        pass
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
