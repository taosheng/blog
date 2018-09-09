#!/bin/bash

outfile=${1}$(date +%F_%H-%M-%Si.%3N).png
tmp="${outfile#http://}"
tmp="${tmp#https://}"
outfile=${tmp//\/}

echo $outfile

/home/doug/node/bin/node /home/doug/cap2.js --url=${1} --f="$outfile"  --d=${2}
mv "$outfile"* /var/www/html/news/



python3 lineUsertool.py -s tonews.txt -m '今日新聞截圖'${3}' http://doug.rareodds.com/news/'$outfile
