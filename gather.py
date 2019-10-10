import pickle
import sys

print('gathering ' + sys.argv[1] + ' data from ' + sys.argv[2] + ' pkl files')

gathered = {}

for x in range(int(sys.argv[2])):
    filename = sys.argv[1] + str(x)
    with open(filename, 'rb') as fp:
        data = pickle.load( fp )
    print('gathering ' + str(len(data.keys())) + 'keys from ' + filename)
    overlap = len( gathered.keys() & data.keys() )
    if overlap > 0:
        print('warning!: ' + overlap + ' overlapping key(s)!')
    gathered.update(data)
    print('so far gathered ' + str(len(gathered.keys())) + ' keys')

print('=== finished gathering ' + str(len(gathered.keys())) + ' keys! ===')

filename = sys.argv[1] + 'g' + sys.argv[2]
with open(filename, 'wb') as fp:
    pickle.dump(gathered, fp)