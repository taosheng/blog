
import sys
import math

numfile = sys.argv[2]
num = int(sys.argv[1])
tmp = 0
with open(numfile, 'rt') as f:
    for line in f:
        cnt = int(line.strip())
        if cnt == 0:
            continue
        p = float(cnt/num)
        en = p*math.log(p,2)
        tmp = tmp + en

print(tmp)

