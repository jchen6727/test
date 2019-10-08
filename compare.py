import pickle
import sys

print('comparing pkl files: ' + sys.argv[1] + '<=>' + sys.argv[2])

with open(sys.argv[1], 'rb') as sim1fp:
    pkl1 = pickle.load( sim1fp )
sim1 = pkl1['simData']['V_soma']

with open(sys.argv[2], 'rb') as sim2fp:
    pkl2 = pickle.load( sim2fp )
sim2 = pkl2['simData']['V_soma']

dur = len(sim1[ list(sim1.keys())[0] ])
for cell in sim1.keys():
    print('=== ' + cell + ' ===')
    deltas = [ [x , sim1[cell][x] - sim2[cell][x] ] for x in range(dur) ]
    deltas = [ [x, y] for [x, y] in deltas if y != 0 ]
    print("deltas: " + str(deltas[0])) if len(deltas)!=0 else print("deltas: all values match!")
