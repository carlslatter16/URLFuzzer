#!/usr/bin/python3
import requests

HOST="http://127.0.0.1"
PORT= 80
WORDLIST="directory-list-lowercase-2.3-medium.txt"
EXTLIST = ["/", ".html", "php"]
DIRLIST = [(HOST + ":" + str(PORT) + "/")]
VERBOSE = False

def checkURL(WORD, EXTENSION, DIR):
    try:
        global DIRNUM
        URL = DIRLIST[DIR]
        siteRequest = requests.head(URL + WORD.rstrip() + EXTENSION)

        if VERBOSE == True:
            print("Trying..." + siteRequest.url)
        if (siteRequest.url.endswith("/")) & (siteRequest.status_code == 200):
            DIRLIST.append(siteRequest.url)
            print(siteRequest.url + " - 200 Directory Responce")
        elif siteRequest.status_code == 200:
            print(siteRequest.url + " - 200 File Responce")
    except requests.ConnectionError:
        print("Connection Error...")


def getWords():
    DIRNUM = 0
    with open(WORDLIST, "r") as file:
        for x in DIRLIST:
            file.seek(0)
            for line in file:
                for i in EXTLIST:
                    checkURL(line, i, DIRNUM)
            DIRNUM=DIRNUM+1
    file.close()
    
    print("---Diagnostics---")
    print("--Dirs Found--")
    for a in DIRLIST:
        print(a)
    print(DIRNUM)


getWords()

