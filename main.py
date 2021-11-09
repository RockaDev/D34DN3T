import subprocess
from time import sleep
import yaml
import getpass
import requests
import sys
import os
import time
import random

class bcolors:
    HEADER    = '\033[95m'
    OKBLUE    = '\033[94m'
    OKGREEN   = '\033[92m'
    WARNING   = '\033[93m'
    FAIL      = '\033[91m'
    BOLD      = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC      = '\033[0m'
# Bold
    BBlack="\[\033[1;30m\]"       # Black
    BRed="\[\033[1;31m\]"         # Red
    BGreen="\[\033[1;32m\]"       # Green
    BYellow="\[\033[1;33m\]"      # Yellow
    BBlue="\[\033[1;34m\]"        # Blue
    BPurple="\[\033[1;35m\]"      # Purple
    BCyan="\[\033[1;36m\]"        # Cyan
    BWhite="\[\033[1;37m\]"       # White
# Regular Colors
    Black="\[\033[0;30m\]"        # Black
    Red="\[\033[0;31m\]"          # Red
    Green="\[\033[0;32m\]"        # Green
    Yellow="\[\033[0;33m\]"       # Yellow
    Blue="\[\033[0;34m\]"         # Blue
    Purple="\[\033[0;35m\]"       # Purple
    Cyan="\[\033[0;36m\]"         # Cyan
    White="\[\033[0;37m\]"        # White

subprocess.run("clear")

L = print(bcolors.BOLD + bcolors.OKGREEN + """ 
                                                                                
                                                                                
                                                                              
                      .....  ..  .. .. .....  .............                     
                      .,,,,  ,,,,,,,,,,,,,,,,.,,,,,,..,,,,,                     
                      ,********* *,***********.****** * ***                     
                      **/****/*//**//******/***///***/*/.*/                     
                      ///(/   *((/./, ((/ (/(/((((/.  *((/(                     
                      (((((        *(.((((((##,       .((((                     
                      #####           ##/##,           ####                     
                    .%#%###,         (#####%.         /%%#%#%                   
                      .&%%%%%%%%%%%&.%%%%%%%%%%%%%%%&%%%%%%                     
                            &&&&&&&&&&*   *&%&&&&&&&&/                          
                              (&@@@@@&      &@@@@@@                             
                              &@@@@*@@@@@@(%@@&@@@@&                            
                             &@(@@@@@@@@@@@@@@@@@@&@   .                        
                         .***       ,#&@@@@&,.      .***                        
                          .##,######(###,(#(###########                         
                                ,&%&&&&&*&&%&&&#&                               
                                      .,@@/                                     
                                                                                
                                                                                
                                                                                
        /@@#%%       /&@*        //  .&@@%%%    &@    %%     *&@(#&&@@@@@@@&    
       ,%%&&%%%,  %%  %%%     /%%%&  %%%%%%%% .%%%#  ,%%  %%  &%%.  .%%%&%%/    
       .##    ##  *#  .##    (####(  ##(   ### ####  *##  .%   ##    ###        
        /(    //     /((    //* (/,  (/*   //. /(//* *(/     /((     ///        
        **   **,   *****   **   **   **,   **  ** **  **   ,****.    .**        
        .. %% ..        ..  ......... ..%%..    .  ....        ...    ..        
                                                                                
""")


def progressBar():
    rnd = random.uniform(0.009,0.02)
    for i in range(65+1):
        time.sleep(rnd)
        sys.stdout.write(('*'*i)+(''*(65-i))+("\r [ %d"%i+"% ] "))
        sys.stdout.flush()
progressBar()

subprocess.run("clear")

def showMainTemp():
    title = print(bcolors.FAIL + """

▓█████▄ ▓█████ ▄▄▄      ▓█████▄  ███▄    █ ▓█████▄▄▄█████▓
▒██▀ ██▌▓█   ▀▒████▄    ▒██▀ ██▌ ██ ▀█   █ ▓█   ▀▓  ██▒ ▓▒
░██   █▌▒███  ▒██  ▀█▄  ░██   █▌▓██  ▀█ ██▒▒███  ▒ ▓██░ ▒░
░▓█▄   ▌▒▓█  ▄░██▄▄▄▄██ ░▓█▄   ▌▓██▒  ▐▌██▒▒▓█  ▄░ ▓██▓ ░ 
░▒████▓ ░▒████▒▓█   ▓██▒░▒████▓ ▒██░   ▓██░░▒████▒ ▒██▒ ░ 
 ▒▒▓  ▒ ░░ ▒░ ░▒▒   ▓▒█░ ▒▒▓  ▒ ░ ▒░   ▒ ▒ ░░ ▒░ ░ ▒ ░░   
 ░ ▒  ▒  ░ ░  ░ ▒   ▒▒ ░ ░ ▒  ▒ ░ ░░   ░ ▒░ ░ ░  ░   ░    
 ░ ░  ░    ░    ░   ▒    ░ ░  ░    ░   ░ ░    ░    ░      
   ░       ░  ░     ░  ░   ░             ░    ░  ░        
 ░                       ░                                
      
                                        by D34DN3T
""")

showMainTemp()


global MD4
global MD5
global SHA1
global SHA224
global SHA256
global SHA384
global SHA512

conf = yaml.safe_load(open('application.yml'))
cfg = conf['user']['a']
loadcfg = conf['user']['b']

def sendMessage():
    phoneNumber = input(str(bcolors.ENDC + "Phone number (ex. +432xxxxxxxxx): "))
    phoneMessage = input(str("Message: "))
    resp = requests.post('https://textbelt.com/text', {
    'phone': str(phoneNumber),
    'message': str(phoneMessage),
    'key': '5dbf294f3693ce0d9adb19bb911cac3e0737dd43Qc3MH8GhqUauZ4MjpbHv9JYCf',
    })
    print(resp.json())

def crackhash():
    hashtype = input(str(bcolors.ENDC + "Enter hash type [MD4,MD5,SHA1,SHA224,SHA256,SHA384,SHA512] >> "))
    hashWordList = input(str("Do you want to use custom wordlist or default[rockyou] | enter Y=custom/n=default >> "))
    if hashtype == "MD5" and hashWordList == "Y" or hashWordList == "y":
        customWordlist = input(str("Full path to wordlist >> "))
        inputHash = input(str("Enter the hash here >> "))
        subprocess.run(["hashcat", "-a", "3", "-m", "0", str(inputHash), str(customWordlist)])
    elif hashtype == "MD4" and hashWordList == "Y" or hashWordList == "y":
        customWordlist = input(str("Full path to wordlist >> "))
        inputHash = input(str("Enter the hash here >> "))
        subprocess.run(["hashcat", "-a", "3", "-m", "900", str(inputHash), str(customWordlist)])
    elif hashtype == "SHA1" and hashWordList == "Y" or hashWordList == "y":
        customWordlist = input(str("Full path to wordlist >> "))
        inputHash = input(str("Enter the hash here >> "))
        subprocess.run(["hashcat", "-a", "3", "-m", "100", str(inputHash), str(customWordlist)])
    elif hashtype == "SHA224" and hashWordList == "Y" or hashWordList == "y":
        customWordlist = input(str("Full path to wordlist >> "))
        inputHash = input(str("Enter the hash here >> "))
        subprocess.run(["hashcat", "-a", "3", "-m", "1300", str(inputHash), str(customWordlist)])
    elif hashtype == "SHA256" and hashWordList == "Y" or hashWordList == "y":
        customWordlist = input(str("Full path to wordlist >> "))
        inputHash = input(str("Enter the hash here >> "))
        subprocess.run(["hashcat", "-a", "3", "-m", "1400", str(inputHash), str(customWordlist)])
    elif hashtype == "SHA384" and hashWordList == "Y" or hashWordList == "y":
        customWordlist = input(str("Full path to wordlist >> "))
        inputHash = input(str("Enter the hash here >> "))
        subprocess.run(["hashcat", "-a", "3", "-m", "10800", str(inputHash), str(customWordlist)])
    elif hashtype == "SHA512" and hashWordList == "Y" or hashWordList == "y":
        customWordlist = input(str("Full path to wordlist >> "))
        inputHash = input(str("Enter the hash here >> "))
        subprocess.run(["hashcat", "-a", "3", "-m", "1700", str(inputHash), str(customWordlist)])
    elif hashtype == "MD4" and hashWordList == "n":
        inputHash = input(str("Enter the hash here >> "))
        subprocess.run(["hashcat", "-a", "3", "-m", "900", str(inputHash), "/usr/share/wordlists/rockyou.txt"])
    elif hashtype == "MD5" and hashWordList == "n":
        inputHash = input(str("Enter the hash here >> "))
        subprocess.run(["hashcat", "-a", "3", "-m", "0", str(inputHash), "/usr/share/wordlists/rockyou.txt"])
    elif hashtype == "SHA1" and hashWordList == "n":
        inputHash = input(str("Enter the hash here >> "))
        subprocess.run(["hashcat", "-a", "3", "-m", "100", str(inputHash), "/usr/share/wordlists/rockyou.txt"])
    elif hashtype == "SHA224" and hashWordList == "n":
        inputHash = input(str("Enter the hash here >> "))
        subprocess.run(["hashcat", "-a", "3", "-m", "1300", str(inputHash), "/usr/share/wordlists/rockyou.txt"])
    elif hashtype == "SHA256" and hashWordList == "n":
        inputHash = input(str("Enter the hash here >> "))
        subprocess.run(["hashcat", "-a", "3", "-m", "1400", str(inputHash), "/usr/share/wordlists/rockyou.txt"])
    elif hashtype == "SHA384" and hashWordList == "n":
        inputHash = input(str("Enter the hash here >> "))
        subprocess.run(["hashcat", "-a", "3", "-m", "10800", str(inputHash), "/usr/share/wordlists/rockyou.txt"])
    elif hashtype == "SHA512" and hashWordList == "n":
        inputHash = input(str("Enter the hash here >> "))
        subprocess.run(["hashcat", "-a", "3", "-m", "1700", str(inputHash), "/usr/share/wordlists/rockyou.txt"])
    else:
        print("Wrong asnwer, please try again.")

def nmapscan():
    nmaptarget = input(str(bcolors.ENDC + "IP ADDRESS >> "))
    nmapPortScan = input(str("With or without ports? [y=with,n=without] >> "))
    if nmapPortScan == "n":
        subprocess.run(["nmap", "-sn", str(nmaptarget)])
    elif nmapPortScan == "y":
        subprocess.run(["nmap", str(nmaptarget)])
    else:
        print("Wrong answer.")


def accespoint():
    apinstall = input(str(bcolors.ENDC + "Is create_ap installed on your device? [Y/n] >> "))
    try:
        if apinstall == "Y" or apinstall == "y":
            apinterface = input(str("Enter interface [default: wlan0, wlan1] >> "))
            apname = input(str("Enter name of the access point >> "))
            subprocess.run(["create_ap", str(apinterface), str(apinterface), str(apname)])
        elif apinstall == "n":
            subprocess.run(["git","clone","https://github.com/oblique/create_ap"])
            sleep(1)
            subprocess.run(["make","install"], cwd="create_ap")
        else:
            print("Wrong answer, please try again.")
    except e:
        print(f"Error {e}")

def portScanner():
    ask_for_ip_address = input(str(bcolors.ENDC + "\nTARGET IP >> "))
    ask_for_port_range = input(str("PORT RANGE [X-XXXXX] >> "))
    subprocess.run([f"python3","portscan.py",ask_for_ip_address,"--ports",ask_for_port_range],cwd="scanners")

def commands():
    menuText = input(bcolors.BOLD + bcolors.WARNING + """
<[1]> SSH LOGIN                 <[4]> FAST NMAP SCAN             <[8]> FAST NETWORK SCAN
<[2]> LISTEN ON ANY PORT        <[5]> CRACK HASH                 <[9]> FAST PORT SCAN
<[3]> CREATE ACCESS POINT       <[6]> SEND ANONYMOUS MESSAGE     <[10]> UPCOMING..
<[99]> EXIT                     <[7]> KILLN3T

CHOOSE: """)
    if menuText == "1":
        askName = input(str(bcolors.ENDC + "NAME >> "))
        askTarget = input(str(bcolors.ENDC + "TARGET >> "))
        a_a_a = "@"
        subprocess.run([f"ssh", str(askName+f"{a_a_a}"+askTarget)])
        
    elif menuText == "99":
        print(bcolors.OKGREEN + """
Goodbye!""")
        exit()
        
    elif menuText == "2":
        listenOn = input(str(bcolors.ENDC + "PORT >> "))
        subprocess.run(["nc","-lvnp",str(listenOn)])
        
    elif menuText == "3":
        accespoint()
        
    elif menuText == "4":
        nmapscan()
        
    elif menuText == "5":
        crackhash()

    elif menuText == "6":
        sendMessage()

    elif menuText == "7":
        subprocess.run(["clear"])
        subprocess.call(["sudo","python3","killnet.py"], cwd="KillN3T")
        
    elif menuText == "8":
        print(bcolors.ENDC + "")
        subprocess.run(["python3","scan.py"],cwd="scanners")

    elif menuText == "9":
        portScanner()
        
    else:
        print(bcolors.FAIL + """
Invalid option, please try again!
""")



def loginShow():
    username = getpass.getpass(bcolors.BOLD + bcolors.OKBLUE + "Enter username: ")
    password = getpass.getpass("Enter password: ")
    if username == cfg:
        print("")
    else:
        print(bcolors.FAIL + """
Wrong username or password!""")
        exit()
    if password == loadcfg:
        print("Succesfully logged in.")
        while True:
            commands()
    else:
        print(bcolors.FAIL + """
Wrong username or password!""")
        exit()
        

if __name__ == '__main__':
    loginShow()