import os;

def createStringCommand(String):
    return "echo "+String;

def shellexec(command):
    return os.system(command);

def checkFileExist(pathToFile):
    exists = os.path.isfile(pathToFile);
    if exists:
        return True;
    else:
        return False;

def getCurrentDirectory():
    return os.getcwd();

host = "dev.pi";
username = "pi";
encrypted = "";

if(checkFileExist(getCurrentDirectory()+"/encrypted.txt")==True):
    encrypted = createStringCommand("File Is Exist");
else :
    encrypted = "openssl aes-256-cbc -salt -a -e -in plaintext.txt -out encrypted.txt"


scpCommand = "scp encrypted.txt "+username+"@"+host+":/home/"+username;

Command = [
    createStringCommand("Check File Existences"), 
    encrypted, 
    createStringCommand("echo Prepare To Send"), 
    scpCommand
];

for execute in Command:
    shellexec(execute);