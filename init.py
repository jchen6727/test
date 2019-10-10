import netParams # import parameters file
import cfg
import pickle
import json

from netpyne import sim  # import netpyne init module
from neuron import h

###############################################################################
# create, simulate, and analyse network
###############################################################################
#sim.createSimulateAnalyze(netParams = netParams.netParams, simConfig = cfg.simConfig)
sim.create(netParams = netParams.netParams, simConfig = cfg.simConfig)
sim.pc.barrier()

###############################################################################
# debug
###############################################################################

###############################################################################
# print out data from psections
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

###############################################################################
# print out data from netcons
###############################################################################
##data = {}
##conns = list(h.List('NetCon'))
##for conn in conns:
##    if str(conn.pre()).startswith('VecStim'):
##        preGid = 'VecStim'
##    elif conn.precell(): 
##        preGid = conn.precell().gid
##    else:
##        preGid = 'ERROR!'
##        print("=================================hey somethings wrong!=================================")
##        print(conn.precell())
##    postGid = conn.postcell().gid
##    sec_loc = str(conn.postseg()).split('.' , 1)[1]
##    sec = sec_loc.split('(')[0]
##    loc = sec_loc.split('(')[1][:-1]
##    weight = conn.weight[0]
##    delay = conn.delay if weight > 0.0 else 0.0
##    Cmax = conn.syn().Cmax
##    Cdur = conn.syn().Cdur
##    Alpha = conn.syn().Alpha
##    Beta = conn.syn().Beta
##    Erev = conn.syn().Erev
##    gmax = conn.syn().gmax
##    key = '%s_%s_%s_%s_%s_%s_%s_%s_%s_%s' % (str(preGid), str(postGid), sec, str(loc), str(Cmax), str(Cdur), str(Alpha), str(Beta), str(Erev), str(gmax))
##    if key in data:
##        data[key].append([weight, delay])
##    else:
##        data[key] = [[weight, delay]]
##
##filename = 'nets' + str(sim.rank) + '.json'
##with open(filename, 'w') as fp:
##    json.dump(data, fp)












sim.pc.barrier()
sim.simulate()
sim.pc.barrier()
sim.analyze()
sim.pc.barrier()

quit()