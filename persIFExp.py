"""
This IF_curr_alpha model fires every 4 ms. persistently.
"""

from pyNN.utility import get_script_args, normalized_filename
#from neo.io import NeoHdf5IO
from neo.io import PyNNTextIO
#from neo import io

DELAY = 1.0

SIM_LENGTH = 100

simulator_name = get_script_args(1)[0]  
exec("from pyNN.%s import *" % simulator_name)

setup(timestep=DELAY,min_delay=DELAY,max_delay=DELAY,debug=True)


#input neurons 
#default 
cell_params = {}
redPop = Population(5,IF_curr_exp(**cell_params))
    
#set up clamped input
pulse = DCSource(amplitude=3.0, start=0.0, stop=10)
inputAssembly = Assembly(redPop[0,1,2,3,4])
pulse.inject_into(inputAssembly)


#setup connections
#synWeight = 1.0
synWeight = 0.9

#setup synapses for peristent CAs
connect(redPop, redPop, weight=synWeight, delay=DELAY)


#setup recording
redPop.record(['spikes','v'])

print redPop[0].get_parameters()

run(SIM_LENGTH)
print "Red"
outAss =  Assembly(redPop[0,1])
outDat = outAss.get_data()
for seg in outDat.segments:
    print(seg.spiketrains)


end()
