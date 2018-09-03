#!/bin/sh


ls -R *| grep ".js" > tmpjs

basep=`wc -l tmpjs | awk '{print $1}' `
echo $basep

for i in `cat tmpjs | cut -d . -f 1`; do
    grep $i -r * | grep import | wc -l >> allnos
done

python3 countEntropy.py $basep allnos
rm allnos
