#------------------------------------------------------------------------------
# SIMULATION CONFIGURATION
#------------------------------------------------------------------------------

from netpyne import specs

simConfig = specs.SimConfig()   # object of class SimConfig to store the simulation configuration

TNUM = 20

celsius = 36
v_init = -70
# Simulation parameters
simConfig.trans = 0000
simConfig.Dt = 0.1
simConfig.steps_per_ms = 1/simConfig.Dt
simConfig.npoints = 6000

graphstart = 0
graphstop  = simConfig.npoints / 10

simConfig.duration = simConfig.npoints * simConfig.Dt # simConfig.trans + simConfig.npoints * simConfig.Dt # Duration of the simulation, in ms
simConfig.dt = simConfig.Dt # Internal integration timestep to use
simConfig.hParams['celsius'] = celsius
simConfig.hParams['v_init'] = v_init
simConfig.verbose = True  # show detailed messages 

# Recording 
simConfig.recordCells = [x for x in range(0, TNUM*2, int(TNUM/2))]

simConfig.recordTraces = {'V_soma':{'sec':'soma','loc':0.5,'var':'v'}}
simConfig.recordStim = True  # record spikes of cell stims
simConfig.recordStep = 0.1 # Step size in ms to save data (eg. V traces, LFP, etc)


# Saving
simConfig.simLabel = "sim"
simConfig.saveFolder = "data"
simConfig.saveFileStep = 1000 # step size in ms to save data to disk
simConfig.savePickle = True # Whether or not to write spikes etc. to a .mat file

# netParams


simConfig.runStopAt = simConfig.duration

