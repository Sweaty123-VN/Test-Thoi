import requests
from pystyle import Colorate, Colors, Center
from os import system
from time import sleep
import colorama
from colorama import Fore



print(f'''{Fore.MAGENTA}
\t\t██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗
\t\t██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝
\t\t██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝ 
\t\t██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗ 
\t\t╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗
\t\t ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
''')
msg = input(f">> {Fore.RESET} Type Your MSG For Spam : ")
webhook = input(f">> {Fore.RESET} Type Your Webhook Link :")
while True:
        try:
            data = requests.post(webhook, json={'content': msg})
            if data.status_code == 204:
                print(f"{Fore.RESET} Send {msg}")
        except:
            print("Bad Webhook :" + webhook)
            time.sleep(5)
            exit = menu2()