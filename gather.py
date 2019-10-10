import pickle
import sys

print('gathering section data in ' + sys.argv[1] + ' pkl files')

gathered = {}

for x in range(int(sys.argv[1])):
    filename = 'secs' + str(x)
    with open(filename, 'rb') as fp:
        data = pickle.load( fp )
    print('gathering ' + str(len(data.keys())) + ' secs from ' + filename)
    gathered.update(data)
    print('so far gathered ' + str(len(gathered.keys())) + 'secs')

print('=== finished gathering ' + str(len(gathered.keys())) + ' secs! ===')

filename = 'secsg' + sys.argv[1]
with open(filename, 'wb') as fp:
    pickle.dump(gathered, fp)