from netpyne import specs
from netpyne import sim

netParams = specs.NetParams()   # object of class NetParams to store the network parameters

###############################################################################
# NETWORK PARAMETERS
###############################################################################

netParams.defaultThreshold = 0
netParams.defaultDelay = 2

###############################################################################
# Population parameters
###############################################################################
    
netParams.popParams['TC'] = {'cellType': 'TC', 'numCells': 20, 'cellModel': 'HH_TC'} 
netParams.popParams['RE'] = {'cellType': 'RE', 'numCells': 20, 'cellModel': 'HH_RE'} 

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
# Connection List
###############################################################################

cLthalamic = [[0, 0],[0, 0],[0, 1],[1, 0],[1, 1],[1, 2],[2, 1],[2, 2],[2, 3],[3, 2],[3, 3],[3, 4],[4, 3],[4, 4],[4, 5],[5, 4],[5, 5],[5, 6],[6, 5],[6, 6],[6, 7],[7, 6],[7, 7],[7, 8],[8, 7],[8, 8],[8, 9],[9, 8],[9, 9],[9, 10],[10, 9],[10, 10],[10, 11],[11, 10],[11, 11],[11, 12],[12, 11],[12, 12],[12, 13],[13, 12],[13, 13],[13, 14],[14, 13],[14, 14],[14, 15],[15, 14],[15, 15],[15, 16],[16, 15],[16, 16],[16, 17],[17, 16],[17, 17],[17, 18],[18, 17],[18, 18],[18, 19],[19, 18],[19, 19],[19, 19]]

###########################################################
##   Glutamate AMPA receptors in synapses from TC to RE  ##
###########################################################

netParams.connParams['TC->TC'] = {
    'preConds': {'popLabel': 'TC'}, 
    'postConds': {'popLabel': 'RE'},
    'weight': 0.2/ 3,         # (Destexhe, 1998)  
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
    'weight': 0.2/ 3,            # (Destexhe, 1998)
    'delay': 2,
    'loc': 0.5,
    'sec': 'soma',
    'threshold': 0,
    'synMech': 'AMPA_S',
    'connList': cLthalamic}