# "requests" module is used to request data from the web.
# "re" module is for regular expressions
# "os" module pulls OS specific commands

import requests, re, os

cls = lambda: os.system("cls")
# this is a simple way to define a Anonymous Function
# if the function were to have a value of x, it would be..
# lambda x: x

cls()
theTao = requests.get('http://www.sacred-texts.com/tao/taote.htm').text.split('<h2>')
title = re.sub('<[^<]+?>|\\r','', theTao[0])

try:
    cls()
    print (title)
    page = int(input ("Lookup page number (1-81):\n\npg #: "))
    Tao = re.sub('<[^<]+?>|\\r','', theTao[page])
    if page == 0:
        print ("This page don't exist.\n")
    else:
        page <= 81
        print ("\n" + Tao)
except:                               # If after trying to run this part of the script fails, run this.
    print ("This page don't exist.\n")
