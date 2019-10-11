Demonstration of an issue arising in multicore simulations that seems to be linked to dt = 0.1
Multicore run on 4 processors behaves differently than multicore run on 1 processor.

command:
./test 1 4

demonstrates the issue by running multicore simulation of netpyne model on 1 cores then 4 cores and comparing voltage output
change dt to either 0.05 or 0.025 and the simulation output matches

has an init, cfg and netParams python file describing network in netpyne, associated mod files for the cells and channels

as well as a compare python file that compares simulation output

there is a debugging branch which contains additional code for debugging

git checkout debugging