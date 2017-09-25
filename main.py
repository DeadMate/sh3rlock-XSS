import requesocks
import os
import sys
from argparse import ArgumentParser
from checker import XssCheck
from functools import partial
from greeting import greetingFunc
from clint.textui import colored
from multiprocessing import Pool
from multiprocessing import cpu_count

greetingFunc()
sys.tracebacklimit = 0
yes = {'yes', 'y'}
no = {'no','n'}
useProxy = False
proxyHost = ""
proxyPort = 0
choice = raw_input("Do you want to use Tor Proxy? Please respond with y/n\n").lower()
if choice in yes:
    os.system("service tor start")
    useProxy = True
    proxyHost = "localhost"
    proxyPort = 9050
    #session = requesocks.session()
    #session.proxies = {'http': 'socks5://localhost:9050', 'https': 'socks5://localhost:9050'}
    #response = session.get('http://httpbin.org/ip')
    #print colored.red("\nYour IP for this TOR session is: ") + response.text[16:-4] + ("\n")
elif choice in no:
    pass
else:
    sys.stdout.write ("Please chose one of the options")
parser = ArgumentParser()
parser.add_argument("-u", "--url", dest="UrlFile", required=True,
                    help="Open specified file")
args = parser.parse_args()
UrlFile = args.UrlFile
with open(UrlFile) as url_file:
    url_array = url_file.read().splitlines()
with open ('xss.txt') as xss_file:
    xss_array = xss_file.read().splitlines()
numOfCombinations = len(url_array) * len(xss_array)
exploits = [url + xss for url in url_array for xss in xss_array]
with open('vulnerable.txt', 'a') as outfile:
    Pool(cpu_count()).map(partial(XssCheck,echo=True,useProxy=useProxy,proxyHost=proxyHost,proxyPort=proxyPort,outfile=outfile),exploits)
    outfile.close()
