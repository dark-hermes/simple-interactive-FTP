from ftplib import FTP

ftp = FTP('')
host, port = input("Input Server Host : "), int(input("Input Server Port[21] : ")
ftp.connect('host','port')
ftp.login()

def upload():
 ftp.retrlines('LIST')
 filename = input("\nWhich file you like to upload : ") #Input a file name with it's extension in the same directory with this file or you can use relative URL
 ftp.storbinary('STOR '+filename, open(filename, 'rb'))
 ftp.quit()

def download():
 ftp.retrlines('LIST')
 filename = input("\nWhich file you like to download : ") #Input a file name with it's extension in server directory
 localfile = open(filename, 'wb')
 ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
 ftp.quit()
 localfile.close()

choice = input("What do you want :\n1. Upload File\n2. Download File\n3. Quit\nYour Choice : ")
if((choice == 1)or(choice=="Upload")or(choice=="upload")or(choice=="UPLOAD")):
 upload()

elif((choice==2)or(choice=="download")or(choice=="DOWNLOAD")or(choice=="Download")):
 download()
 
elif(choice==3)or(choice=="Quit")or(choice=="quit")or(choice=="QUIT"):
 ftp.quit()
 


