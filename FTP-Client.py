import ftplib #import ftplib module

ftp = ftplib.FTP('') #save FTP func as ftp var
host = input    ("Input Host Server    : ") 
port = int(input("Input Port Server    : "))

ftp.connect(host,port)
username, passwords = input("\nUsername             : "),input("Password             : ")
ftp.login(user = username,passwd= passwords)



choice = input("What do you want :\n1. Upload\n2. Download\n3. Quit\nInput : ")
if choice=="Upload" or choice=="UPLOAD" or choice == "upload" or choice==1:
    def upload():
        ftp.retrlines('LIST')
        filename = input("Pick a file : ")
        ftp.storbinary('STOR '+filename, open(filename, 'rb'));
        print("\n"+filename,"uploaded successfully");
        ftp.quit()
    try:
        upload()
    except FileNotFoundError:
        print("\nUpload Failed")
        ftp.quit()

elif choice=="Download" or choice == "download" or choice == "DOWNLOAD" or choice == 2:
    def download():
        ftp.retrlines('LIST')
        filename = input("Pick a file from server : ")
        localfile = open(filename, 'wb')
        ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
        print("\n"+filename,"downloaded successfully")
        ftp.quit()
        localfile.close()
    try:
        download()
    except ftplib.error_perm:
        print("\nDownload Failed")

elif choice == "Quit" or choice == "quit" or choice == "QUIT" or choice == 3:
    print("\nProgram Finished");ftp.quit();
