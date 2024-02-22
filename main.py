#BONUMMASTER!! 
#t.me/BONUM.MASTER

import subprocess
import os
import time
import socket
import requests
import random
import getpass
import sys
import json
import platform
import colorama
from node_modules.colors.themes import string

#UNDERGROUND SECURITY PH! #
#UNDERGROUND SECURITY PH! #
CREATED BY = "BONUMMASTER"
#WE SAVE HUMANITY! #
#HUMAN VS AI! #

def prints(start_color, end_color, text):
    start_r, start_g, start_b = start_color
    end_r, end_g, end_b = end_color

    for i in range(len(text)):
        r = int(start_r + (end_r - start_r) * i / len(text))
        g = int(start_g + (end_g - start_g) * i / len(text))
        b = int(start_b + (end_b - start_b) * i / len(text))

        color_code = f"\033[38;2;{r};{g};{b}m"
        print(color_code + text[i], end="")
    
start_color = (255, 0, 0)
end_color = (0, 0, 255)

class Color:
	colorama.init(autoreset=True)
	LB = colorama.Fore.LIGHTBLUE_EX
	LC = colorama.Fore.LIGHTCYAN_EX
	LG = colorama.Fore.LIGHTGREEN_EX
	LR = colorama.Fore.LIGHTRED_EX
	LY = colorama.Fore.LIGHTYELLOW_EX
	RESET = colorama.Fore.RESET
	
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = r"""
	▓█UNDERGROUND SECURITY PH█▓
	▒▒▓BONUMMASTER▓  ▒░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
	░Ddos Attack▒  ▒USEC  SPIDERSEC ▒   ░ ▒ ▒░ ░ ░▒  ░ ░
	░ ░PLATOON CYBER GROUP ░    ░ ░        ░  
	░ WE SAVE HUMANITY PH░                       
"""
    CREATED BY = r"""
		BONUMMASTER USEC GODPH
    """
    prints(start_color, end_color, banner)
    prints(end_color, start_color, author)
    print("\n") 
    print(Color.LB+"           ["+Color.LR+"VVIP"+Color.LB+"]"+Color.LC+" ddosbonun"+Color.LR+"       ["+Color.LG+"VIP"+Color.LR+"]"+Color.LC+" flood")
    print("\n") 
    print(Color.LR+"           ["+Color.LG+"VIP"+Color.LR+"]"+Color.LC+" aikiller"+Color.LB+"       ["+Color.LR+"VVIP"+Color.LB+"]"+Color.LC+" socket")
    print("\n")
    
    while True:
        cnc = input(Color.LB+"╔═══"+Color.LR+"["+Color.LG+"root"+Color.LB+"@"+Color.LG+"ddosbonum"+Color.LR+"]"+Color.LB+"\n╚══> "+Color.RESET)
        if "gangbang" in cnc:
            try:
                gb = os.path.join("node_modules/randomstring", "input.py")
                subprocess.run(['python3', gb])
                sys.exit(0)
            except IndexError:
                print('just input aikiller')
        
        elif "ddosbonum" in cnc:
            try:           
                ddosbonum = os.path.join("node_modules/dashdash/etc", "input.py")
                subprocess.run(['python3', ddosbonum])
                sys.exit(0)
            except IndexError:
                print('just input ddosbonum')
                
        elif "pinoyattacker" in cnc:
            try:
                flood = os.path.join("node_modules/aws4", "input.py")
                subprocess.run(['python3', pinoyattacker])
                sys.exit(0)
            except IndexError:
                print('just input pinoyattacker')
                
        elif "raw" in cnc:
            try:
                raw = os.path.join("node_modules/asn1/lib/ber", "input.py")
                subprocess.run(['python3', raw])
                sys.exit(0)
            except IndexError:
                print('just input raw')
                
        elif "socket" in cnc:
            try:
                socket = os.path.join("node_modules/colors/lib/system", "input.py")
                subprocess.run(['python3', pinoyddos])
                sys.exit(0)
            except IndexError:
                print('just input raw')
                                
        else:
            try:
                cmmnd = cnc.split()[0]
                print("Method: [ " + cmmnd + " ] BONUMMASTER PH")
            except IndexError:
                pass
                
if author == "ddosbonum":
    main()
else:
    string.authorsalah()
