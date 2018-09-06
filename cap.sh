#!/bin/bash

outfile=${1}$(date +%F_%H-%M-%S).png
tmp="${outfile#http://}"
tmp="${tmp#https://}"
outfile=${tmp//\/}

echo $outfile

/home/doug/node/bin/node /home/doug/cap.js --url=${1} --f="$outfile"
mv "$outfile" /var/www/html/ss/


python3 lineUsertool.py -s tome.txt -m 'last capture-> http://doug.rareodds.com/ss/'$outfile
