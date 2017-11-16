
import sys



def addhours(resultDict, name, loc):
#loc = 0 workingHour
#loc = 1 outofWorkingHour
    if name in resultDict:
        resultDict[name][loc] += 1
    else:
        resultDict[name] = [0,0]
        resultDict[name][loc] += 1

    return resultDict

if __name__ == '__main__':
    authorLog = sys.argv[1]
    cntWH = 0
    cntOH = 0
    result = {} # format name: [workingHour, outofWorkingHour]
    with open(authorLog, 'r') as f:
        line = f.readline()
        while(line):
            parts = line.split(",")
            name = parts[0]
            hour = int(parts[1][11:13])
            if hour < 7 or hour >=20:
                print(line)
                cntOH += 1
                result = addhours(result, name, 1)               
            else: 
                result = addhours(result, name, 0)               
                cntWH += 1
 
            line = f.readline()
  
    print(cntWH)
    print(cntOH)
    for k in result:
        print("{} {}".format(k, result[k]))

