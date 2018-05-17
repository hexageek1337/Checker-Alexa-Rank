#! /usr/bin/python
import sys
import pycurl
from bs4 import BeautifulSoup
try:
    # python 3
    from urllib.parse import urlencode
except ImportError:
    # python 2
    from urllib import urlencode
try:
    from io import BytesIO
except ImportError:
    from StringIO import StringIO as BytesIO

def banner():
	'''
	````
	Github Profile : https://github.com/hexageek1337
	Github Project : https://github.com/hexageek1337/Checker-Alexa-Rank ( 17-05-2018 )
	Created by Denny Septian
	
	````
	'''
	print '''
 -----------------------------------------------------------
|                         ( Checker Alexa Rank Website )   |____
|      #     #  #####                                           |
|      #     # #     # #    #   ##    ####   ####  #    #       |
|      #     #       #  #  #   #  #  #    # #    # ##   #       |
|      #######  #####    ##   #    # #      #    # # #  #       |
|      #     #       #   ##   ###### #  ### #    # #  # #       |
|      #     # #     #  #  #  #    # #    # #    # #   ##       |
|      #     #  #####  #    # #    #  ####   ####  #    #       |
|                                                               |
|                            Powered by Cyber Merah Putih       |
|                                  ( Denny Septian )            |
|                                                               |
 ----------------------------------------------------------------'''

banner()
URLWEB = raw_input("| Input url your site (example : github.com) : ")
buffer = BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, "http://data.alexa.com/data?cli=10&dat=snbamz&url="+URLWEB)
c.setopt(c.WRITEDATA, buffer)
c.perform()

# HTTP response code, e.g. 200.
print("----------------------------------------")
if c.getinfo(c.RESPONSE_CODE) == 200:
	print('| [+] Response Status : %d ( Found )' % c.getinfo(c.RESPONSE_CODE))
else:
	print('| [+] Response Status : %d ( Fail )' % c.getinfo(c.RESPONSE_CODE))
# Elapsed time for the transfer.
print('| [+] Response time : %f' % c.getinfo(c.TOTAL_TIME))
print("----------------------------------------")

# getinfo must be called before close.
c.close()

body = buffer.getvalue()

y = BeautifulSoup(body, "html.parser")
print("| [+] Country : "+y.findAll("country")[0]["name"])
print("| [+] Global Rank : "+y.findAll("popularity")[0]["text"])
print("| [+] Country Rank : "+y.findAll("country")[0]["rank"])
print("----------------------------------------")