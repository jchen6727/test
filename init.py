import netParams # import parameters file
import cfg
import pickle
import json

from netpyne import sim  # import netpyne init module
from neuron import h

sim.createSimulateAnalyze(netParams = netParams.netParams, simConfig = cfg.simConfig)
sim.pc.barrier()
quit()