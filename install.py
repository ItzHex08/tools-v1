import os
import time
import requests
import base64
import sys
from datetime import datetime, timedelta

g = "\33[32;1m"
r = "\33[31;1m"
y = "\33[33;1m"
w = "\33[37;1m"

Windows = "cls"
Android = "clear"

def installing():
        time.sleep(1)
        try:
                device = input("Choose Our Device [Windows/Android]: ")
                if device == 'Windows':
                        time.sleep(1)
                        print((datetime.now() + timedelta()).strftime('[%H:%M:%S]') + " Setup Your Device "+device+" ...")
                        time.sleep(5)
                        os.system("cls")
                        print((datetime.now() + timedelta()).strftime('[%H:%M:%S]') + " Checking Our Connection ...")
                        request = requests.get("https://github.com/ItzHex08/tools-v1")
                        print((datetime.now() + timedelta()).strftime('[%H:%M:%S]') + " Installing Tools ...")
                elif device == 'Android':
                        time.sleep(1)
                        print((datetime.now() + timedelta()).strftime('[%H:%M:%S]') + " setup Your Device "+device+" ...")
                        time.sleep(5)
                        os.system("clear")
                        print((datetime.now() + timedelta()).strftime('[%H:%M:%S]') + " Checking Our Connection ...")
                        request = requests.get("https://github.com/ItzHex08/tools-v1")
                        print((datetime.now() + timedelta()).strftime('[%H:%M:%S]') + " Installing Tools ...")
                else:
                        time.sleep(1)
                        print((datetime.now() + timedelta()).strftime('[%H:%M:%S]') + " Device Not Found!")
        except requests.exceptions.ConnectionError:
                time.sleep(1)
                print((datetime.now() + timedelta()).strftime('[%H:%M:%S]') + " Installing Failed, No Connection Error!")
installing()