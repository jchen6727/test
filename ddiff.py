import pickle
import sys
from deepdiff import DeepDiff
from pprint import pprint

with open(sys.argv[1], 'rb') as fp:
    source = pickle.load(fp)

with open(sys.argv[2], 'rb') as fp:
    target = pickle.load(fp)

ddiff = DeepDiff(source, target)
pprint(ddiff)
