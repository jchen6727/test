from netpyne import specs, sim
netParams = specs.NetParams()   # object of class NetParams to store the network parameters

netParams.defaultThreshold, netParams.defaultDelay, celsius, v_init = 0, 2, 36, -70
netParams.popParams['EA'] = {'cellType': 'EA', 'numCells': 20, 'cellModel': 'HH_EA'} 
netParams.popParams['EB'] = {'cellType': 'EB', 'numCells': 20, 'cellModel': 'HH_EB'} 

netParams.cellParams['EArule'] =netParams.importCellParams(label='EArule', conds={'cellType': 'EA', 'cellModel': 'HH_EA'}, fileName='EA.tem', cellName='sEA')
netParams.cellParams['EArule']['secs']['soma']['vinit']=v_init
netParams.cellParams['EBrule'] = netParams.importCellParams(label='EBrule', conds={'cellType': 'EB', 'cellModel': 'HH_EB'}, fileName='EB.tem', cellName='sEB')
netParams.cellParams['EBrule']['secs']['soma']['vinit']=v_init

netParams.synMechParams['AMPA_S'] = {'mod': 'AMPA_S', 'Alpha': 0.94, 'Beta': 0.18, 'Cmax': 0.5, 'Cdur': 0.3, 'Erev': 0}
cLthalamic = [[0, 0],[0, 0],[0, 1],[1, 0],[1, 1],[1, 2],[2, 1],[2, 2],[2, 3],[3, 2],[3, 3],[3, 4],[4, 3],[4, 4],[4, 5],[5, 4],[5, 5],[5, 6],[6, 5],[6, 6],[6, 7],[7, 6],[7,7],
  [7, 8],[8, 7],[8, 8],[8, 9],[9, 8],[9, 9],[9, 10],[10, 9],[10, 10],[10, 11],[11, 10],[11, 11],[11, 12],[12, 11],[12, 12],[12, 13],[13, 12],[13, 13],[13, 14],[14, 13],[14,14],
  [14, 15],[15, 14],[15, 15],[15, 16],[16, 15],[16, 16],[16, 17],[17, 16],[17, 17],[17, 18],[18, 17],[18, 18],[18, 19],[19, 18],[19, 19],[19, 19]]
netParams.connParams['EA->EA'] = { 'preConds': {'popLabel': 'EA'}, 'postConds': {'popLabel': 'EB'}, 'weight': 0.2/3, 'delay': 2, 'sec': 'soma', 'loc': 0.5, 'threshold': 0,
    'synMech': 'AMPA_S', 'connList': cLthalamic}
netParams.connParams['EB->EB'] = {'preConds': {'popLabel': 'EB'}, 'postConds': {'popLabel': 'EB'}, 'weight': 0.2/ 3, 'delay': 2, 'sec': 'soma', 'loc': 0.5, 'threshold': 0,
    'synMech': 'AMPA_S', 'connList': cLthalamic}
