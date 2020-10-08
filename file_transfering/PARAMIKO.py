import paramiko

ssh=paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname="",username="",password="",port=22)

sftp_client = ssh.open_sftp()

def get_file():
    remotepath=""
    localpath=""
    sftp_client.get(remotepath,localpath) #getting file from remote server
    #print(dir(sftp_client)) # to see command
    #sftp_client.chdir("path") # change directory
    #print(sftp_client.getcwd()) # change current directory

def put_file():
    remotepath=""
    localpath=""
    sftp_client.put(localpath,remotepath)

#get_file()
#put_file() #that's it
sftp.close()

ssh.close()
