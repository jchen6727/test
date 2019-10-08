from netpyne import specs
from netpyne import sim

netParams = specs.NetParams()   # object of class NetParams to store the network parameters

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

###############################################################################
# NETWORK PARAMETERS
###############################################################################

nthalamiccells = 20
narrowdiam = 1

nRETC = 2 * narrowdiam + 1 # for weight
nTCRE = 2 * narrowdiam + 1 # for weight

netParams.defaultThreshold = 0
netParams.defaultDelay = 2
###############################################################################
# Population parameters
###############################################################################

### Thalamic cells    
netParams.popParams['TC'] = {'cellType': 'TC', 'numCells': nthalamiccells, 'cellModel': 'HH_TC'} #, 'ynormRange': [0.65, 0.75]} #, 'yRange': [2+3*netParams.yspacing,2+3*netParams.yspacing], 'gridSpacing': netParams.xspacing}
netParams.popParams['RE'] = {'cellType': 'RE', 'numCells': nthalamiccells, 'cellModel': 'HH_RE'} #, 'ynormRange': [0.8, 0.9]} #, 'yRange': [2+4*netParams.yspacing,2+4*netParams.yspacing], 'gridSpacing': netParams.xspacing}

###############################################################################
# Cell parameters list
###############################################################################
celsius = 36
v_init = -70

### TC (Destexhe et al., 1996; Bazhenov et al.,2002)
TCcellRule = netParams.importCellParams(label='TCrule', conds={'cellType': 'TC', 'cellModel': 'HH_TC'}, fileName='TC.tem', cellName='sTC')

### RE (Destexhe et al., 1996; Bazhenov et al.,2002)
REcellRule = netParams.importCellParams(label='RErule', conds={'cellType': 'RE', 'cellModel': 'HH_RE'}, fileName='RE.tem', cellName='sRE')

TCcellRule['secs']['soma']['vinit']=v_init
netParams.cellParams['TCrule'] = TCcellRule

REcellRule['secs']['soma']['vinit']=v_init
netParams.cellParams['RErule'] = REcellRule

###############################################################################
# Synaptic mechanism parameters
###############################################################################

# AMPA_S
netParams.synMechParams['AMPA_S'] = {'mod': 'AMPA_S', 'Alpha': 0.94, 'Beta': 0.18, 'Cmax': 0.5, 'Cdur': 0.3, 'Erev': 0}

###############################################################################
# Connectivity parameters
###############################################################################

cLthalamic = mkConnList( nthalamiccells, narrowdiam)

###########################################################
##   Glutamate AMPA receptors in synapses from TC to RE  ##
###########################################################

netParams.connParams['TC->RE'] = {
    'preConds': {'popLabel': 'TC'}, 
    'postConds': {'popLabel': 'RE'},
    'weight': 0.2/nTCRE,         # (Destexhe, 1998)  
    'sec': 'soma',
    'delay': 2,
    'loc': 0.5,
    'threshold': 0,
    'synMech': 'AMPA_S',
    'connList': cLthalamic}

###########################################################
##   GABAa receptors in intra-RE synapses                ##
###########################################################

netParams.connParams['RE->RE'] = {
    'preConds': {'popLabel': 'RE'}, 
    'postConds': {'popLabel': 'RE'},
    'weight': 0.2/nRETC,            # (Destexhe, 1998)
    'delay': 2,
    'loc': 0.5,
    'sec': 'soma',
    'threshold': 0,
    'synMech': 'AMPA_S',
    'connList': cLthalamic}

