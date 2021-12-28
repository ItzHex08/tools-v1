import os
import sys
import time
import json
import urllib2
import base64
from termcolor import cprint, colored
from datetime import datetime, timedelta
from base64 import *

r = "\33[31;1m"
y = "\33[33;1m"
g = "\33[32;1m"
w = "\33[37;1m"

def internet():
        try:
                r = request.get("https://google.com")
        except:
                time.sleep(1)
                print( (datetime.now() + timedelta()).strftime(g+'['+y+'%H:%M:%S'+g+'] '+r)+"Error No Connection!")
                os.system("exit")

def main():
        time.sleep(1)
        try:
                internet()
                file_tools = open("version.dev", "w")
