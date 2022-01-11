# Programmed By Lynch, Free Tool
import requests
import os
from os import system

system("title " + "By Lynch - Duck IP Adress Information")
import colorama
from colorama import Fore

colorama.init(autoreset=True)
from time import sleep

sleep(0.5)
logo = """

  _                     _     
 | |   _   _ _ __   ___| |__  
 | |  | | | | '_ \ / __| '_ \ 
 | |__| |_| | | | | (__| | | |
 |_____\__, |_| |_|\___|_| |_|
       |___/                                    

"""
sleep(0.3)

print(Fore.CYAN+logo)
title = ("By Lynch, Telegram: @overexcited")
print(Fore.RED+title)
sleep(0.6)
ip2 = input(f"[{Fore.GREEN}?{Fore.RESET}] Ducks IP Adress: ")
response = requests.post("http://ip-api.com/batch", json=[
    {
        "query": ip2
    },
]).json()
sleep(0)
for ip_info in response:
    for k, v in ip_info.items():
        print("+-------------------+")


        print(f"\n[{Fore.GREEN}i{Fore.RESET}] " + k, v)
    print("\n")
input(f"[{Fore.GREEN}+{Fore.RESET}] Made w Love, Socials: [I] @entrysquad - [T] @overexcited")
