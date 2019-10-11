from netpyne import specs
simConfig = specs.SimConfig()

simConfig.trans = 0000
simConfig.dt = 0.1 # / 4
simConfig.steps_per_ms = 1/simConfig.Dt
simConfig.npoints = 6000# * 4
simConfig.duration = 400
simConfig.hParams['celsius'], simConfig.hParams['v_init']  = 36, -70

simConfig.recordCells = [x for x in range(0, 40, 5)]
simConfig.recordTraces = {'V_soma':{'sec':'soma','loc':0.5,'var':'v'}}
simConfig.recordStim = True
simConfig.recordStep = simConfig.dt 
simConfig.saveFolder, simConfig.simLabel = "data", "sim"

