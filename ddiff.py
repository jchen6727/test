import pickle
import sys
from deepdiff import DeepDiff
from pprint import pprint

with open(sys.argv[1], 'rb') as fp:
    source = pickle.load(fp)

with open(sys.argv[2], 'rb') as fp:
    target = pickle.load(fp)

ddiff = DeepDiff(source, target)
if not ddiff:
    print("ddiff results: " + sys.argv[1] + ' ' + sys.argv[2] + " match!")
else:
    print("ddiff results: " + sys.argv[1] + ' ' + sys.argv[2] + " do not match!")
    pprint(ddiff)
