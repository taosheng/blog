#!/usr/bin/env python3

import sys
import os
import datetime
import configparser


today = datetime.datetime.now().strftime("%Y%m%d")
wwwroot = '/var/www/html/ss/'
def createFolder(p):
    p = wwwroot+p    
    if not os.path.exists(p):
        os.makedirs(p)


if __name__ == '__main__':
    print("hanle a user job for screenshoot")
    config = configparser.ConfigParser()
    config.read(sys.argv[1])
    session = config['DEFAULT']
    print(dir(session))
    print(session['name'])
    print(session['email'])
    print(session['urls'])
    createFolder(session['name']+"/"+today)
