#!/bin/bash

outfile=${1}$(date +%F_%H-%M-%Si.%3N).png
tmp="${outfile#http://}"
tmp="${tmp#https://}"
outfile=${tmp//\/}

echo $outfile

if [ $# -ge 2 ]
then
    echo ${2}
    /home/doug/node/bin/node /home/doug/cap2.js --url=${1} --f="$outfile"  --d=${2}
    mv "$outfile"* /var/www/html/ss/
else
    /home/doug/node/bin/node /home/doug/cap2.js --url=${1} --f="$outfile" --d=6
    mv "$outfile" /var/www/html/ss/
fi



python3 lineUsertool.py -s tome.txt -m 'last capture-> http://doug.rareodds.com/ss/'$outfile
