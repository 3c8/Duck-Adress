# Programmed By Lynch, Free Tool
import requests
import os
from os import system

system("title " + "Programmed By Lynch - IP Adress Information")
import colorama
from colorama import Fore

colorama.init(autoreset=True)
from time import sleep

logo = """
  _                     _     
 | |   _   _ _ __   ___| |__  
 | |  | | | | '_ \ / __| '_ \ 
 | |__| |_| | | | | (__| | | |
 |_____\__, |_| |_|\___|_| |_|
       |___/                                    
"""

print(Fore.CYAN+logo)
title = ("Made w Love By Lynch, [i]: @l7up")
print(Fore.RED+title) 
ip2 = input(f"[{Fore.GREEN}?{Fore.RESET}] Ducks IP Adress: ")

response = requests.post("http://ip-api.com/batch", json=[
    {
        "query": ip2
    },
]).json()
sleep(0)
for ip_info in response:
    for k, v in ip_info.items():


        print("+" + "-" * 10 + "Successfully" + "-" * 10 + "+")
        print(f"\n[{Fore.CYAN}i{Fore.RESET}] " + k, v)
    print("\n")
input(f"[{Fore.MAGENTA}${Fore.RESET}] Press ENTER To Exit...") 
