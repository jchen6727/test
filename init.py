import netParams # import parameters file
import cfg
import pickle

from netpyne import sim  # import netpyne init module
from neuron import h

###############################################################################
# create, simulate, and analyse network
###############################################################################
sim.createSimulateAnalyze(netParams = netParams.netParams, simConfig = cfg.simConfig)

sim.pc.barrier()

###############################################################################
# debug
###############################################################################
data = {}
remove = ['cell', 'regions','species', 'point_processes', 'hoc_internal_name', 'name']
removeMorph = ['parent', 'trueparent']
for c in sim.net.cells:
    icell = str(c).split('_')[-1]
    data[icell] = {}
    cellType =  c.tags['cellType']
    for isec, sec in enumerate(c.secs.values()):
        name = cellType + '_' + str(sec['hObj'].name()).split('.')[-1]
        data[icell][ name] = sec['hObj'].psection()
        for key in remove:
            if key in data[icell][name]:
                del data[icell][name][key]
        for key in removeMorph:
            if key in data[icell][name]['morphology']:
                del data[icell][name]['morphology'][key]

filename = 'secs' + str(sim.rank)
with open(filename, 'wb') as fp:
    pickle.dump(data, fp)

quit()