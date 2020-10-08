import pysftp as sftp

def sftpExample():
    try:
        s=sftp.Connection(host="192.168.1.193",username="pi",password="rahi")
        remotepath="/home/pi/Desktop/gsm/video.mp4"
        localpath="/home/rahi/Videos/aurthohin"
        s.put(localpath,remotepath) # for putting file to server
        #s.get(remotepath,localpath) # for getting file from server
    except Exception as e:
        print(str(e))
sftpExample()
