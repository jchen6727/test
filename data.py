import pickle
import sys

with open('data/sim.pkl', 'rb') as fp:
    nppkl = pickle.load( fp )

v = {}
for cell in nppkl['simData']['V_soma'].keys():
    v[cell] = [x for x in nppkl['simData']['V_soma'][cell]]

with open(sys.argv[1], 'wb') as fp:
    pickle.dump(v, fp)

print('pkl file created: ' + sys.argv[1])