import re
import sys

def sortFunc(x):
    return x[4] + str(x[0]) + '0' + str(x[1])

nc1 = []
nc2 = []

for line in open(sys.argv[1]):
    rgx = re.match(r"  Created connection preGid=(.*), postGid=(.*), sec=(.*), loc=(.*), synMech=(.*), weight=(.*), delay=(.*)", line)
    if rgx != None:
        rgx = list(rgx.groups())
        preGid, postGid, sec, loc, synMech, weight, delay = rgx
        nc1.append([int(preGid), int(postGid), sec, float(loc), synMech, float(weight), float(delay)])

for line in open(sys.argv[2]):
    rgx = re.match(r"  Created connection preGid=(.*), postGid=(.*), sec=(.*), loc=(.*), synMech=(.*), weight=(.*), delay=(.*)", line)
    if rgx != None:
        rgx = list(rgx.groups())
        preGid, postGid, sec, loc, synMech, weight, delay = rgx
        nc2.append([int(preGid), int(postGid), sec, float(loc), synMech, float(weight), float(delay)])

nc1.sort(key=sortFunc)

nc2.sort(key=sortFunc)

if (nc1 == nc2)
