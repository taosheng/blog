#!/usr/bin/env python3

import sys
import os
import datetime
import configparser
import subprocess
from zohoemail import sendZohoMail 


today = datetime.datetime.now().strftime("%Y%m%d")
wwwroot = '/var/www/html/ss/'
def createFolder(p):
    if not os.path.exists(p):
        os.makedirs(p)


if __name__ == '__main__':
    print("hanle a user job for screenshoot")
    config = configparser.ConfigParser()
    config.read(sys.argv[1])
    session = config['DEFAULT']
    print(dir(session))
    username = session['name']
    email = session['email']
    urls = session['urls'].split(',')
    workingfolder = wwwroot + username + "/"+today
    createFolder(workingfolder)
    gapRat = 3
    cnt = 1
    for url in urls:
        print(url)
        print("call cap.js")
        outfilename = url.replace('http://','').replace('https://','').replace('/','')
        outfilename = outfilename + "_" + today + str(cnt) + ".png"
        capargs = ['/home/doug/node/bin/node','cap.js', '--url='+url, '--f='+outfilename,'--d=17']
        p = subprocess.run(capargs)
        cnt += 1
        mvargs = ['mv',outfilename,workingfolder]
        p = subprocess.run(mvargs)
     
    location = "http://doug.rareodds.com/ss/" + username + "/"+today
    sendZohoMail(email, "定期網頁截圖", location)
