import pickle
import sys

with open(sys.argv[1], 'rb') as sim1fp:
    sim1 = pickle.load( sim1fp )

with open(sys.argv[2], 'rb') as sim2fp:
    sim2 = pickle.load( sim2fp )

dur = min(len(sim1['pyv']['bound']), len(sim2['pyv']['bound'])) - 1

print('comparing pkl files: ' + sys.argv[1] + '<=>' + sys.argv[2])


print('===pyv===')
deltas = [ [x , sim1['pyv']['bound'][x] - sim2['pyv']['bound'][x] ] for x in range(dur) ]
deltas = [ [x, y] for [x, y] in deltas if y != 0 ]
print("bound: " + str(deltas[0])) if len(deltas)!=0 else print("bound: all values match!")

deltas = [ [x , sim1['pyv']['mid'][x] - sim2['pyv']['mid'][x] ] for x in range(dur) ]
deltas = [ [x, y] for [x, y] in deltas if y != 0 ]
print("mid: " + str(deltas[0])) if len(deltas)!=0 else print("mid: all values match!")

print('===inv===')
deltas = [ [x , sim1['inv']['bound'][x] - sim2['inv']['bound'][x] ] for x in range(dur) ]
deltas = [ [x, y] for [x, y] in deltas if y != 0 ]
print("bound: " + str(deltas[0])) if len(deltas)!=0 else print("bound: all values match!")

deltas = [ [x , sim1['inv']['mid'][x] - sim2['inv']['mid'][x] ] for x in range(dur) ]
deltas = [ [x, y] for [x, y] in deltas if y != 0 ]
print("mid: " + str(deltas[0])) if len(deltas)!=0 else print("mid: all values match!")

print('===tcv===')
deltas = [ [x , sim1['tcv']['bound'][x] - sim2['tcv']['bound'][x] ] for x in range(dur) ]
deltas = [ [x, y] for [x, y] in deltas if y != 0 ]
print("bound: " + str(deltas[0])) if len(deltas)!=0 else print("bound: all values match!")

deltas = [ [x , sim1['tcv']['mid'][x] - sim2['tcv']['mid'][x] ] for x in range(dur) ]
deltas = [ [x, y] for [x, y] in deltas if y != 0 ]
print("mid: " + str(deltas[0])) if len(deltas)!=0 else print("mid: all values match!")

print('===rev===')
deltas = [ [x , sim1['rev']['bound'][x] - sim2['rev']['bound'][x] ] for x in range(dur) ]
deltas = [ [x, y] for [x, y] in deltas if y != 0 ]
print("bound: " + str(deltas[0])) if len(deltas)!=0 else print("bound: all values match!")

deltas = [ [x , sim1['rev']['mid'][x] - sim2['rev']['mid'][x] ] for x in range(dur) ]
deltas = [ [x, y] for [x, y] in deltas if y != 0 ]
print("mid: " + str(deltas[0])) if len(deltas)!=0 else print("mid: all values match!")