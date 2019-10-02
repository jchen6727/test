"""
netParams.py 

netParams is a dict containing a set of network parameters using a standardized structure

simConfig is a dict containing a set of simulation configurations using a standardized structure

refs:
Destexhe, A., Contreras, D., & Steriade, M. (1998). Mechanisms underlying the 
synchronizing action of corticothalamic feedback through inhibition of thalamic 
relay cells. Journal of neurophysiology, 79(2), 999-1016.

Destexhe, A. (1998). Spike-and-wave oscillations based on the properties of 
GABAB receptors. Journal of Neuroscience, 18(21), 9099-9111.


Contributors: xxx@xxxx.com
"""

from netpyne import specs
from netpyne import sim

netParams = specs.NetParams()   # object of class NetParams to store the network parameters


import random as rnd
import numpy as np

import json
from settings import nav_type, drug, dose

def mkConnList( n, diam ):
    connList = []
    for i in range(n):
        for j in range(i-diam, i+diam+1):
            jbound = j                      # boundary cell conditions
            if (jbound < 0):
                jbound = abs(j) - 1
            if (jbound > (n-1)):
                jbound = 2 * n - jbound - 1
            connList.append( [i, jbound] )
    return connList

###############################################################################
#
# MPI HH TUTORIAL PARAMS
#
###############################################################################

stimtime = 10050

randInit = True
selfConn = False

ININweight = 0.00

gabaapercent = 0.1
gababpercent = 1


PYPY    = 1
PYIN    = 1
ININa   = 1
INPYa   = 1
INPYb   = 1

TCRE    = 1
RETCa   = 1
RETCb   = 1
RERE    = 1

PYTC    = 1
PYRE    = 1
TCPY    = 1
TCIN    = 1


###############################################################################
# NETWORK PARAMETERS
###############################################################################

ncorticalcells = 100
nthalamiccells = 100
narrowdiam = 5
widediam = 10


nRERE = 2 * narrowdiam + 1
nRETC = 2 * narrowdiam + 1
nTCRE = 2 * narrowdiam + 1
nPYPY = 2 * narrowdiam + 1
nINPY = 2 * narrowdiam + 1
nPYIN = 2 * narrowdiam + 1
nPYRE = 2 * widediam + 1
nPYTC = 2 * widediam + 1
nTCPY = 2 * widediam + 1

netParams.xspacing = 20 # um
netParams.yspacing = 100 # um

netParams.axondelay = 2

netParams.defaultThreshold = 0

###############################################################################
# LOAD NETCONS
###############################################################################
with open('netcons.json', 'r') as fp:
    netcons = json.load(fp)

###############################################################################
# Population parameters
###############################################################################
### Cortical Cells
netParams.popParams['PY'] = {'cellType': 'PY', 'numCells': ncorticalcells, 'cellModel': 'HH_PY'} #, 'ynormRange': [0.1, 0.3]} #, 'yRange': [1*netParams.yspacing,1*netParams.yspacing], 'gridSpacing': netParams.xspacing}
netParams.popParams['IN'] = {'cellType': 'IN', 'numCells': (ncorticalcells * 2), 'cellModel': 'HH_IN'} #, 'ynormRange': [0.35, 0.55]} #, 'yRange': [2*netParams.yspacing,2*netParams.yspacing], 'gridSpacing': netParams.xspacing} 

### Thalamic cells    
netParams.popParams['TC'] = {'cellType': 'TC', 'numCells': nthalamiccells, 'cellModel': 'HH_TC'} #, 'ynormRange': [0.65, 0.75]} #, 'yRange': [2+3*netParams.yspacing,2+3*netParams.yspacing], 'gridSpacing': netParams.xspacing}
netParams.popParams['RE'] = {'cellType': 'RE', 'numCells': nthalamiccells, 'cellModel': 'HH_RE'} #, 'ynormRange': [0.8, 0.9]} #, 'yRange': [2+4*netParams.yspacing,2+4*netParams.yspacing], 'gridSpacing': netParams.xspacing}


###############################################################################
# Cell parameters list
###############################################################################
celsius = 36
v_init = -70

### PY (single compartment)
PYcellRule = netParams.importCellParams(label='PYrule', conds={'cellType': 'PY', 'cellModel': 'HH_PY'},	fileName='sPY.tem', cellName='sPY')

### TC (Destexhe et al., 1996; Bazhenov et al.,2002)
TCcellRule = netParams.importCellParams(label='TCrule', conds={'cellType': 'TC', 'cellModel': 'HH_TC'}, fileName='TC.tem', cellName='sTC')

### RE (Destexhe et al., 1996; Bazhenov et al.,2002)
REcellRule = netParams.importCellParams(label='RErule', conds={'cellType': 'RE', 'cellModel': 'HH_RE'}, fileName='RE.tem', cellName='sRE')

### IN (single compartment)
INcellRule = netParams.importCellParams(label='INrule', conds={'cellType': 'IN', 'cellModel': 'HH_IN'},	fileName='sIN.tem', cellName='sIN')

PYcellRule['secs']['soma']['vinit']=v_init
netParams.cellParams['PYrule'] = PYcellRule

TCcellRule['secs']['soma']['vinit']=v_init
netParams.cellParams['TCrule'] = TCcellRule

REcellRule['secs']['soma']['vinit']=v_init
netParams.cellParams['RErule'] = REcellRule

INcellRule['secs']['soma']['vinit']=v_init
netParams.cellParams['INrule'] = INcellRule




###############################################################################
# Synaptic mechanism parameters
###############################################################################

PYgmax = 0.03/nINPY # gmax instead of weight for GABAB due to nonlinearity
TCgmax = 0.04/nRETC # gmax instead of weight for GABAB due to nonlinearity

# AMPA_S
netParams.synMechParams['AMPA_S'] = {'mod': 'AMPA_S', 'Alpha': 0.94, 'Beta': 0.18, 'Cmax': 0.5, 'Cdur': 0.3, 'Erev': 0}
netParams.synMechParams['AMPA_S_PYPY'] = {'mod': 'AMPA_S', 'Alpha': 0.94, 'Beta': 0.18, 'Cmax': 0.5, 'Cdur': 0.3, 'Erev': 0}

# GABAa_S
netParams.synMechParams['GABAA_S'] = {'mod': 'GABAa_S', 'Alpha': 20, 'Beta': 0.162, 'Cmax': 0.5, 'Cdur': 0.3, 'Erev': -85}

# GABAb_S
netParams.synMechParams['GABAB_S1'] = {'mod': 'GABAb_S', 'Cmax': 0.5, 'Cdur': 0.3, 'K1': 0.09, 'K2': 0.0012, 'K3': 0.18, 'K4': 0.034, 'KD': 100, 'n': 4, 'Erev': -95, 'gmax': PYgmax }
netParams.synMechParams['GABAB_S2'] = {'mod': 'GABAb_S', 'Cmax': 0.5, 'Cdur': 0.3, 'K1': 0.09, 'K2': 0.0012, 'K3': 0.18, 'K4': 0.034, 'KD': 100, 'n': 4, 'Erev': -95, 'gmax': TCgmax }


###############################################################################
# Stimulation parameters
###############################################################################

# IClamp PY
netParams.stimSourceParams['Input_1'] = {'type': 'IClamp', 'del': stimtime, 'dur': 100, 'amp': 0.7}
# smallPY=1
netParams.stimTargetParams['Input_1->PY'] = {'source': 'Input_1', 'sec':'soma', 'loc': 0.5, 
                                              'conds': {'pop':'PY', 'cellList': [i*int(ncorticalcells/5-1)+11 for i in range(int(ncorticalcells/20))]}}

###############################################################################
# Connectivity parameters
###############################################################################

####################### intra cortical projections ############################
cLthalamic = mkConnList( nthalamiccells, narrowdiam)



###########################################################
##   Glutamate AMPA receptors in synapses from TC to RE  ##
###########################################################

netParams.connParams['TC->RE'] = {
    'preConds': {'popLabel': 'TC'}, 
    'postConds': {'popLabel': 'RE'},
    #'weight': 0.018182,     # TCRE*0.2/(N_RE*TC_RE_AMPA_Prob+1),         # (Destexhe, 1998)  
    'weight': 0.2/nTCRE,         # (Destexhe, 1998)  
    'sec': 'soma',
    'delay': netParams.axondelay, 
    'loc': 0.5,
    'threshold': 0,
    'synMech': 'AMPA_S',
    #'probability': '1.0 if dist_x <= narrowdiam*xspacing else 0.0'}   
    #'probability': TC_RE_AMPA_Prob}
    'connList': cLthalamic}
    #'connList': netcons['AMPA_S']['sTCsRE']}

###########################################################
##   GABAa receptors in intra-RE synapses                ##
###########################################################

netParams.connParams['RE->RE'] = {
    'preConds': {'popLabel': 'RE'}, 
    'postConds': {'popLabel': 'RE'},
    #'weight': 0.018182,        # RERE*0.2/(N_RE*RE_RE_GABAA_Prob+1),            # (Destexhe, 1998)
    'weight': 0.2/nRERE,            # (Destexhe, 1998)
    'delay': netParams.axondelay, 
    'loc': 0.5,
    'sec': 'soma',
    #'threshold': 0,
    'synMech': 'GABAA_S',
    #'synsPerConn': 1,
    #'probability': '1.0 if dist_x <= narrowdiam*xspacing else 0.0'}   
    #'probability': RE_RE_GABAA_Prob}
    'connList': cLthalamic}
    #'connList': netcons['GABAa_S']['sREsRE']} 

###########################################################
##   GABAa receptors in in synapses from RE to TC cells  ##
###########################################################

netParams.connParams['RE->TC_GABAA'] = {
    'preConds': {'popLabel': 'RE'}, 
    'postConds': {'popLabel': 'TC'},
    #'weight': 0.00182 * gabaapercent,   # RETCa*gabaapercent*0.02/(N_TC*RE_TC_GABAA_Prob+1),         # (Destexhe, 1998)
    'weight': gabaapercent*0.02/nRETC,                    # (Destexhe, 1998)
    'sec': 'soma',
    'delay': netParams.axondelay, 
    'loc': 0.5,
    'synMech': 'GABAA_S',
    #'probability': '1.0 if dist_x <= narrowdiam*xspacing else 0.0'}   
    #'probability': RE_TC_GABAA_Prob}
    'connList': cLthalamic}
    #'connList': netcons['GABAa_S']['sREsTC']} 
