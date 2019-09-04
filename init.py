import netParams # import parameters file
import cfg

import json

from netpyne import sim  # import netpyne init module
from neuron import h

#sim.createSimulateAnalyze(netParams = netParams.netParams, simConfig = cfg.simConfig)  # create and simulate network(pops, cells, conns, rxd, stims, simData) = sim.create(netParams.netParams, cfg.simConfig, output=True)

###############################################################################
# create, simulate, and analyse network
###############################################################################

(pops, cells, conns, rxd, stims, simData) = sim.create(netParams.netParams, cfg.simConfig, output=True)


PYcells = sim.net.cells[  0:100]
INcells = sim.net.cells[100:300]
TCcells = sim.net.cells[300:400]
REcells = sim.net.cells[400:500]

PYsomas = [ x.secs['soma']['hObj'] for x in PYcells ]
INsomas = [ x.secs['soma']['hObj'] for x in INcells ]
TCsomas = [ x.secs['soma']['hObj'] for x in TCcells ]
REsomas = [ x.secs['soma']['hObj'] for x in REcells ]

RETCgababsyns = [ [ ] ] * 100
RETCnetcons = []
for i in range(100):
  for j in range(i-5, i+5+1):
    jbound = j
    if (jbound < 0):
        jbound = abs(j) - 1
    if (jbound > 99): 
        jbound = 2 * 100 - jbound - 1
    ## presynaptic is RE[i], postsynaptic is TC[j]
    ## ***Note: GABAb synapses are implemented as a list of individual synapses (in contrast to other synapse types), and so are created here
    gababsyn = h.GABAb_S()                                                        #gababsyn = new GABAb_S()
    gababsyn.loc(0.5, sec = TCsomas[jbound])                                      #TC[jbound].soma gababsyn.loc(0.5)
    gababsyn.gmax = 0.04 / 11
    RETCgababsyns[jbound].append(gababsyn)                                        #TC[jbound].gababpost.append(gababsyn)
    ncon = h.NetCon( REsomas[i](0.5)._ref_v, gababsyn, 0, 2, 1, sec = REsomas[i]) #RE[i].soma TC[jbound].REgabablist.append(new NetCon(&v(0.5), gababsyn, 0, axondelay, 1))
    RETCnetcons.append(ncon)

INPYgababsyns = [ [ ] ] * 100
INPYnetcons = []
for i in range(100):
  for j in range(i-5, i+5+1):
    jbound = j
    if (jbound < 0):
        jbound = abs(j) - 1
    if (jbound > 99):
        jbound = 2 * 100 - jbound - 1
    ## presynaptic is IN[i], postsynaptic is PY[j]
    ## ***Note: GABAb synapses are implemented as a list of individual synapses (in contrast to other synapse types), and so are created here
    gababsyn = h.GABAb_S()                                                         #gababsyn = new GABAb_S()
    gababsyn.loc(0.5, sec = PYsomas[jbound])                                       #PY[jbound].soma gababsyn.loc(0.5)
    gababsyn.gmax = 0.03 / 11
    INPYgababsyns[jbound].append(gababsyn)                                         #PY[jbound].gababpost.append(gababsyn) 
    ncon = h.NetCon( INsomas[i](0.5)._ref_v, gababsyn, 0, 2, 1, sec = INsomas[i])  #IN[i].soma PY[jbound].INgabablist.append(new NetCon(&v(0.5), gababsyn, 0, axondelay, 1))
    INPYnetcons.append(ncon)
    #add for new set of IN cells
    gababsyn = h.GABAb_S()
    gababsyn.loc(0.5, sec = PYsomas[jbound])                                              #PY[jbound].soma gababsyn.loc(0.5)
    gababsyn.gmax = 0.03 / 11
    INPYgababsyns[jbound].append(gababsyn)                                                #PY[jbound].gababpost.append(gababsyn) 
    ncon = h.NetCon( INsomas[i+100](0.5)._ref_v, gababsyn, 0, 2, 1, sec = INsomas[i+100]) #IN[i+100].soma PY[jbound].INgabablist.append(new NetCon(&v(0.5), gababsyn, 0, axondelay, 1))
    INPYnetcons.append(ncon)

PYg = h.Vector()
PYg.record(INPYgababsyns[11][0]._ref_g)
PYi = h.Vector()
PYi.record(INPYgababsyns[11][0]._ref_i)
TCg = h.Vector()
TCg.record(RETCgababsyns[11][0]._ref_g)
TCi = h.Vector()
TCi.record(RETCgababsyns[11][0]._ref_i)


"""
sim.simulate()
sim.analyze()

ncl = h.List("NetCon")
GABAbP = h.List("GABAb_S")
GABAb = [x for x in ncl if 'GABAb' in str(x.syn())]

#precellRE = [x for x in asy if x.precell().tags['cellType'] == 'RE']
#postcellTC = [x for x in asy if x.postcell().tags['cellType'] == 'TC']
#precellIN = [x for x in asy if x.precell().tags['cellType'] == 'IN']
#postcellPY = [x for x in asy if x.postcell().tags['cellType'] == 'PY']
#print( 'RE->:%d'%(len(precellRE)) )
#print( '->TC:%d'%(len(postcellTC)))
#print( 'IN->:%d'%(len(precellIN)) )
#print( '->PY:%d'%(len(postcellPY)))

if (randInit):
    rgh = sim.h.Random()
    rk1 = sim.h.Random()
    rgh.normal(17.5,0.0008)        #random number generator behaves weirdly for very small numbers, so multiply by 10^-6 below
    rk1.normal(40,0.003)
    for i in range(N_TC):
        print(rgh.repick())
        a.append(rgh.repick() * 1e-6)
        b.append(rgh.repick() * 1e-6)        
        sim.net.cells[200+i].secs.soma.mechs.iar.ghbar = rgh.repick() * 1e-6
        sim.net.cells[200+i].secs.soma.pointps.kleak_0.gmax = rk1.repick() * 1e-4
        #print("TC(",i,") gh:", sim.net.cells[200+i].secs.soma.mechs.iar.ghbar, " gmax:", sim.net.cells[200+i].secs.soma.pointps.kleak_0.gmax)

##### sim.simulate() ################
##### sim.runSim()   ################

###############################################################################
### Run Simulation
###############################################################################
sim.pc.barrier()
sim.timing('start', 'runTime')
sim.preRun()
#sim.h.init()

sim.pc.set_maxstep(10)
#sim.h.stdinit()
sim.h.dt = 0.1 # Fixed dt
sim.h.fcurrent()
#sim.h.cvode.re_init()
sim.h.frecord_init()

#printPYinfo(sim.net.cells[0])
#printINinfo(sim.net.cells[100])
#printTCinfo(sim.net.cells[200])
#printREinfo(sim.net.cells[300])
#printWeight()


if sim.rank == 0: print('\nRunning simulation for %s ms...'%sim.cfg.duration)
sim.pc.psolve(sim.cfg.duration)

sim.pc.barrier() # Wait for all hosts to get to this point
sim.timing('stop', 'runTime')
if sim.rank==0:
    print('  Done; run time = %0.2f s; real-time ratio: %0.2f.' %
        (sim.timingData['runTime'], sim.cfg.duration/1000/sim.timingData['runTime']))
########################################
sim.gatherData()                  # gather spiking data and cell info from each node
#####################################
sim.analyze()
"""


