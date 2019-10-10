Demonstration of issue arising in multicore simulations -- multicore on 4 processors behaves differently than multicore on 1 processor.

command:
./test 4 1

demonstrates the issue by running multicore simulation of netpyne model on 4 cores then 1 core and comparing voltage output

connection data printed by simConfig.verbose is saved to conns4 (4 cores) and conns1 (1 core)

simulation data to sim4 (4 cores) and sim1 (1 core)

compare.py checks that the voltage data is identical between sim1 and sim4

parseConns.py checks that the connection data is identical between conns1 and conns4

gather.py gathers section data from psection from multicore simulations

ddiff.py runs a deep diff of any data structures

can also do

./test 2 1

to see that 2 core and 1 core simulation match

./test 4 2

to see that 4 core and 2 core simulation do not match

