"""
Bug: it doesn't print if you run 1000 or 2000 ms.

This does the full thing:  it views from the retina, through V1,
to pyramid detection, then sets a fact on.  It also has the planning in.
So, it does the commands that are activated.  This can be set in the
short version in runNoCallBack, or all can be tested with the RunCallBack
version.
"""

#imports for PyNN
from pyNN.utility import get_script_args

#imports for image reading
import numpy
from PIL import Image
#Other NEAL files and functions

from visionClass import visionArea

INPUT_NEURONS_HEIGHT = 50
INPUT_NEURONS_WIDTH = 50

DELAY = 1.0
output_filename='cabot1_out.dat'
SIM_LENGTH = 300.0
#SIM_LENGTH = 2000.0 #For the full plan test

CA_HEIGHT = 10
CA_WIDTH = 10


#------set up object to fact connections----------
#-every neuron of the left 20 of the object turns on the left flag
def leftObjectTurnsLeftFactOn ():
    synWeight = 3.0
    connector = []
    for cRow in range (0,INPUT_NEURONS_HEIGHT):
        for cCol in range (0,int(INPUT_NEURONS_WIDTH*0.4)):
            fromNeuron=cRow*INPUT_NEURONS_WIDTH+cCol
            toNeuron = cCol % 5
            connector = connector + [(fromNeuron,toNeuron,synWeight,DELAY)]
    return connector
    
#-every neuron of the right 20 of the object turns on the left flag
def rightObjectTurnsLeftFactOn ():
    synWeight = 3.0
    connector = []
    for cRow in range (0,INPUT_NEURONS_HEIGHT):
        for cCol in range (int(INPUT_NEURONS_WIDTH*0.6),INPUT_NEURONS_WIDTH):
            fromNeuron=cRow*INPUT_NEURONS_WIDTH+cCol
            toNeuron = cCol % 5
            connector = connector + [(fromNeuron,toNeuron,synWeight,DELAY)]
    return connector
    
#-every neuron of the object turns on the fact
def objectTurnsObjectFactOn ():
    synWeight = 3.0
    connector = []
    for cRow in range (0,INPUT_NEURONS_HEIGHT):
        for cCol in range (0,int(INPUT_NEURONS_WIDTH)):
            fromNeuron=cRow*INPUT_NEURONS_WIDTH+cCol
            toNeuron = cCol % 5
            connector = connector + [(fromNeuron,toNeuron,synWeight,DELAY)]
    return connector
    


#----------------functions for setting plan connections
def setStandardOscillatorConnector(oscPart1,oscPart2,weight):
	connect(oscPart1,oscPart2,weight, DELAY)

def setPlanConnections():
    weight = 6.0
    synWeight = 6.0
    inhibitW = -5.25
    synWeightCoeff = 0.25

    #connections for goals
    setStandardOscillatorConnector(goalTL_1,goalTL_2,weight)
    setStandardOscillatorConnector(goalTL_2,goalTL_1,weight)
    setStandardOscillatorConnector(goalTR_1,goalTR_2,weight)
    setStandardOscillatorConnector(goalTR_2,goalTR_1,weight)
    setStandardOscillatorConnector(goalBack_1,goalBack_2,weight)
    setStandardOscillatorConnector(goalBack_2,goalBack_1,weight)
    setStandardOscillatorConnector(goalForward_1,goalForward_2,weight)
    setStandardOscillatorConnector(goalForward_2,goalForward_1,weight)
    setStandardOscillatorConnector(goal_move_left1_1,goal_move_left1_2,weight)
    setStandardOscillatorConnector(goal_move_left1_2,goal_move_left1_1,weight)
    setStandardOscillatorConnector(goal_move_left2_1,goal_move_left2_2,weight)
    setStandardOscillatorConnector(goal_move_left2_2,goal_move_left2_1,weight)
    setStandardOscillatorConnector(goal_move_right1_1,goal_move_right1_2,weight)
    setStandardOscillatorConnector(goal_move_right1_2,goal_move_right1_1,weight)
    setStandardOscillatorConnector(goal_move_right2_1,goal_move_right2_2,weight)
    setStandardOscillatorConnector(goal_move_right2_2,goal_move_right2_1,weight)
    setStandardOscillatorConnector(goal_pyramid_1,goal_pyramid_2,weight)
    setStandardOscillatorConnector(goal_pyramid_2,goal_pyramid_1,weight)


    #connect compound goals to second part of goals
    setStandardOscillatorConnector(goal_move_left1_1,goal_move_left2_1,synWeightCoeff*synWeight)
    setStandardOscillatorConnector(goal_move_left1_2,goal_move_left2_1,synWeightCoeff*synWeight)
    setStandardOscillatorConnector(goal_move_right1_1,goal_move_right2_1,synWeightCoeff*synWeight)
    setStandardOscillatorConnector(goal_move_right1_2,goal_move_right2_1,synWeightCoeff*synWeight)

    #connections for modules
    setStandardOscillatorConnector(moduleTL_1,moduleTL_2,weight)
    setStandardOscillatorConnector(moduleTL_2,moduleTL_1,weight)
    setStandardOscillatorConnector(moduleTR_1,moduleTR_2,weight)
    setStandardOscillatorConnector(moduleTR_2,moduleTR_1,weight)
    setStandardOscillatorConnector(moduleBack_1,moduleBack_2,weight)
    setStandardOscillatorConnector(moduleBack_2,moduleBack_1,weight)
    setStandardOscillatorConnector(moduleForward_1,moduleForward_2,weight)
    setStandardOscillatorConnector(moduleForward_2,moduleForward_1,weight)

    #connections between modules and goals
    setStandardOscillatorConnector(goalTL_1,moduleTL_2,weight)
    setStandardOscillatorConnector(goalTL_2,moduleTL_1,weight)
    setStandardOscillatorConnector(goalTL_1,moduleTL_1,weight)
    setStandardOscillatorConnector(goalTL_2,moduleTL_2,weight)
    setStandardOscillatorConnector(goalTR_1,moduleTR_2,weight)
    setStandardOscillatorConnector(goalTR_2,moduleTR_1,weight)
    setStandardOscillatorConnector(goalTR_1,moduleTR_1,weight)
    setStandardOscillatorConnector(goalTR_2,moduleTR_2,weight)
    setStandardOscillatorConnector(goalBack_1,moduleBack_2,weight)
    setStandardOscillatorConnector(goalBack_2,moduleBack_1,weight)
    setStandardOscillatorConnector(goalBack_1,moduleBack_1,weight)
    setStandardOscillatorConnector(goalBack_2,moduleBack_2,weight)
    setStandardOscillatorConnector(goalForward_1,moduleForward_2,weight)
    setStandardOscillatorConnector(goalForward_2,moduleForward_1,weight)
    setStandardOscillatorConnector(goalForward_1,moduleForward_1,weight)
    setStandardOscillatorConnector(goalForward_2,moduleForward_2,weight)
    setStandardOscillatorConnector(goal_move_left1_1,moduleTL_2,weight)
    setStandardOscillatorConnector(goal_move_left1_2,moduleTL_1,weight)
    setStandardOscillatorConnector(goal_move_left1_1,moduleTL_1,weight)
    setStandardOscillatorConnector(goal_move_left1_2,moduleTL_2,weight)
    setStandardOscillatorConnector(goal_move_left2_1,moduleForward_2,weight)
    setStandardOscillatorConnector(goal_move_left2_2,moduleForward_1,weight)
    setStandardOscillatorConnector(goal_move_left2_1,moduleForward_1,weight)
    setStandardOscillatorConnector(goal_move_left2_2,moduleForward_2,weight)
    setStandardOscillatorConnector(goal_move_right1_1,moduleTR_2,weight)
    setStandardOscillatorConnector(goal_move_right1_2,moduleTR_1,weight)
    setStandardOscillatorConnector(goal_move_right1_1,moduleTR_1,weight)
    setStandardOscillatorConnector(goal_move_right1_2,moduleTR_2,weight)
    setStandardOscillatorConnector(goal_move_right2_1,moduleForward_2,weight)
    setStandardOscillatorConnector(goal_move_right2_2,moduleForward_1,weight)
    setStandardOscillatorConnector(goal_move_right2_1,moduleForward_1,weight)
    setStandardOscillatorConnector(goal_move_right2_2,moduleForward_2,weight)

    #connections between goal_pyramid (find the pyramid) and modules.
    #very weak and passive, since pyramid could be either left or right
    setStandardOscillatorConnector(goal_pyramid_1, moduleTR_1, synWeightCoeff*synWeight)
    setStandardOscillatorConnector(goal_pyramid_1, moduleTR_2, synWeightCoeff*synWeight)
    setStandardOscillatorConnector(goal_pyramid_2, moduleTR_1, synWeightCoeff*synWeight)
    setStandardOscillatorConnector(goal_pyramid_2, moduleTR_2, synWeightCoeff*synWeight)
    setStandardOscillatorConnector(goal_pyramid_1, moduleTL_1, synWeightCoeff*synWeight)
    setStandardOscillatorConnector(goal_pyramid_1, moduleTL_2, synWeightCoeff*synWeight)
    setStandardOscillatorConnector(goal_pyramid_2, moduleTL_1, synWeightCoeff*synWeight)
    setStandardOscillatorConnector(goal_pyramid_2,moduleTL_2,synWeightCoeff*synWeight)

    #facts have stronger weights and more bias, excite the **_1  lead to spike
    synWeightCoeff = 0.75
    chrisWeight = 1.0
    setStandardOscillatorConnector(leftFactAPop,moduleTL_1,chrisWeight)
    setStandardOscillatorConnector(leftFactBPop,moduleTL_1,chrisWeight)
    setStandardOscillatorConnector(rightFactAPop,moduleTR_1,chrisWeight)
    setStandardOscillatorConnector(rightFactBPop,moduleTR_1,chrisWeight)

    #facts inhibit modules
    chrisInhib = -3.0
    setStandardOscillatorConnector(leftFactAPop,moduleTR_1,chrisInhib)
    setStandardOscillatorConnector(leftFactAPop,moduleTR_2,chrisInhib)
    setStandardOscillatorConnector(rightFactAPop,moduleTL_1,chrisInhib)
    setStandardOscillatorConnector(rightFactAPop,moduleTL_2,chrisInhib)

    #to and from actions
    setStandardOscillatorConnector(moduleTL_1, TL, synWeight)
    setStandardOscillatorConnector(moduleTL_2, TL, synWeight)
    setStandardOscillatorConnector(TL,moduleTL_1, inhibitW)
    setStandardOscillatorConnector(TL,moduleTL_2, inhibitW)
    setStandardOscillatorConnector(TL,goalTL_1, inhibitW)
    setStandardOscillatorConnector(TL,goalTL_2, inhibitW)

    setStandardOscillatorConnector(moduleTR_1, TR, synWeight)
    setStandardOscillatorConnector(moduleTR_2, TR, synWeight)
    setStandardOscillatorConnector(TR,moduleTR_1, inhibitW)
    setStandardOscillatorConnector(TR,moduleTR_2, inhibitW)
    setStandardOscillatorConnector(TR,goalTR_1, inhibitW)
    setStandardOscillatorConnector(TR,goalTR_2, inhibitW)

    setStandardOscillatorConnector(moduleBack_1, back, synWeight)
    setStandardOscillatorConnector(moduleBack_2, back, synWeight)
    setStandardOscillatorConnector(back,moduleBack_1, inhibitW)
    setStandardOscillatorConnector(back,moduleBack_2, inhibitW)
    setStandardOscillatorConnector(back,goalBack_1, inhibitW)
    setStandardOscillatorConnector(back,goalBack_2, inhibitW)

    setStandardOscillatorConnector(moduleForward_1, forward, synWeight)
    setStandardOscillatorConnector(moduleForward_2, forward, synWeight)
    setStandardOscillatorConnector(forward,moduleForward_1, inhibitW)
    setStandardOscillatorConnector(forward,moduleForward_2, inhibitW)
    setStandardOscillatorConnector(forward,goalForward_1, inhibitW)
    setStandardOscillatorConnector(forward,goalForward_2, inhibitW)

    #action left and forward for move left
    synWeightCoeff=0.75
    setStandardOscillatorConnector(TL, goal_move_left2_1, synWeightCoeff*synWeight)
    setStandardOscillatorConnector(TL, goal_move_left2_2, synWeightCoeff*synWeight)
    setStandardOscillatorConnector(TL, goal_move_left1_1, inhibitW)
    setStandardOscillatorConnector(TL, goal_move_left1_2, inhibitW)
    setStandardOscillatorConnector(forward, goal_move_left2_1, inhibitW)
    setStandardOscillatorConnector(forward, goal_move_left2_2, inhibitW)

    setStandardOscillatorConnector(TR, goal_move_right2_1, synWeightCoeff*synWeight)
    setStandardOscillatorConnector(TR, goal_move_right2_2, synWeightCoeff*synWeight)
    setStandardOscillatorConnector(TR, goal_move_right1_1, inhibitW)
    setStandardOscillatorConnector(TR, goal_move_right1_2, inhibitW)
    setStandardOscillatorConnector(forward, goal_move_right2_1, inhibitW)
    setStandardOscillatorConnector(forward, goal_move_right2_2, inhibitW)

    #actions turn off facts too (thanks Ian)
    setStandardOscillatorConnector(TR, rightFactAPop, inhibitW)
    setStandardOscillatorConnector(TR, rightFactBPop, inhibitW)
    setStandardOscillatorConnector(TL, leftFactAPop, inhibitW)
    setStandardOscillatorConnector(TL, leftFactBPop, inhibitW)

    #actions turn off pyramid goals sJA
    setStandardOscillatorConnector(TL, goal_pyramid_1, inhibitW)
    setStandardOscillatorConnector(TL, goal_pyramid_2, inhibitW)
    #eja
    setStandardOscillatorConnector(TR, goal_pyramid_1, inhibitW)
    setStandardOscillatorConnector(TR, goal_pyramid_2, inhibitW)

#-------------Print out neuron by neuron the firing times
def print_spikes(of, label, pop):
	print "\n\n%s\n" % label
	of.write("\n%s\n" % label)
	outDat = pop.get_data()
	for seg in outDat.segments:
		print(seg.spiketrains)
		of.write("\n%s\n" % str(seg.spiketrains))

#------Image Stuff
def openImageFile():
    try: 
#pyramid        im = Image.open("ed_3screenshot.jpg")
#stalactite        im = Image.open("ed_screenshot826.jpg") #stalactite
        im = Image.open("pyr1.jpg") 
    except:
        print "fail to open image"

    im = im.crop((0,0,600,600))
    #print im.size

    #shrink it
    size = (INPUT_NEURONS_WIDTH,INPUT_NEURONS_HEIGHT)
    im.thumbnail(size)

    #get the pixels
    pixels = im.load()

    ##convert rgb to grey scale
    inputMatrix = numpy.zeros((50,50))
    for inpRow in range (0,50):
        for inpCol in range (0,50):
            rgb = pixels[inpCol,inpRow]
            for i in range (0,3):
                inputMatrix[inpCol,inpRow] += rgb[i]
                inputMatrix[inpCol,inpRow]/=3
        
    ##set result image array
    resultImage = numpy.zeros((50,50))
    THRESHOLD = 50
    resultImageArray = []
    for outRow in range (0,50):
        for outColumn in range (0,50):
            if inputMatrix[outColumn,outRow] < THRESHOLD :
                #print outRow, outColumn
                pixelOn = (outRow*INPUT_NEURONS_WIDTH)+outColumn
                resultImageArray = resultImageArray + [pixelOn]

    return resultImageArray

#stimulus
def setInputs():
        pulse0 =DCSource(amplitude=55,start=0.0,stop=10.0)
	ML_Assembly = Assembly(goal_move_left1_1[0,1,2,3,4])
	pulse0.inject_into(ML_Assembly)
	pulse1 =DCSource(amplitude=55,start=100.0,stop=110.0)
	TP_Assembly = Assembly(goal_pyramid_1[0,1,2,3,4])
        pulse1.inject_into(TP_Assembly)
	pulse2 =DCSource(amplitude=55,start=200.0,stop=210.0)
	back_Assembly = Assembly(goalBack_1[0,1,2,3,4])
	pulse2.inject_into(back_Assembly)

def setInputs2():
        pulse0 =DCSource(amplitude=55,start=0.0,stop=10.0)
	TR_Assembly = Assembly(goalTR_1[0,1,2,3,4])
	pulse0.inject_into(TR_Assembly)
	pulse1 =DCSource(amplitude=55,start=100.0,stop=110.0)
	TL_Assembly = Assembly(goalTL_1[0,1,2,3,4])
        pulse1.inject_into(TL_Assembly)
	pulse2 =DCSource(amplitude=55,start=200.0,stop=210.0)
	forward_Assembly = Assembly(goalForward_1[0,1,2,3,4])
	pulse2.inject_into(forward_Assembly)
	pulse3 =DCSource(amplitude=55,start=300.0,stop=310.0)
	back_Assembly = Assembly(goalBack_1[0,1,2,3,4])
	pulse3.inject_into(back_Assembly)
	pulse4 =DCSource(amplitude=55,start=400.0,stop=410.0)
	move_left1_Assembly = Assembly(goal_move_left1_1[0,1,2,3,4])
	pulse4.inject_into(move_left1_Assembly)
	pulse5 = DCSource(amplitude=55, start=500.0, stop=510.0)
	move_right1_Assembly = Assembly(goal_move_right1_1[0,1,2,3,4])
	pulse5.inject_into(move_right1_Assembly)
	pulse6 = DCSource(amplitude=55, start=600.0, stop=610.0)
	move_left1_Assembly = Assembly(goal_move_left1_1[0,1,2,3,4])
	pulse6.inject_into(move_left1_Assembly)
	pulse7 = DCSource(amplitude=55, start=700.0, stop=710.0)
	pulse7.inject_into(TR_Assembly)
	pulse8 = DCSource(amplitude=55, start=800.0, stop=810.0)
	pulse8.inject_into(TL_Assembly)
	pulse9 =DCSource(amplitude=55,start=900.0,stop=910.0)
	forward_Assembly = Assembly(goalForward_1[0,1,2,3,4])
	pulse9.inject_into(forward_Assembly)
	pulse10 =DCSource(amplitude=55, start=1000.0,stop=1010.0)
	pulse10.inject_into(TR_Assembly)
	pulse11 =DCSource(amplitude=55,start=1100.0,stop=1110.0)
	pulse11.inject_into(TL_Assembly)
	pulse12 =DCSource(amplitude=55,start=1200.0,stop=1210.0)
	TP_Assembly = Assembly(goal_pyramid_1[0,1,2,3,4])
	pulse12.inject_into(TP_Assembly)
	pulse13 =DCSource(amplitude=55,start=1300.0,stop=1310.0)
	pulse13.inject_into(TP_Assembly)
	pulse14 =DCSource(amplitude=55,start=1400.0,stop=1410.0)
	pulse14.inject_into(TR_Assembly)
	pulse15 =DCSource(amplitude=55,start=1500.0,stop=1510.0)
	pulse15.inject_into(TL_Assembly)

        
def runNoCallBack():
    #set up clamped input from image
    # pulseVis = DCSource(amplitude=0.0038, start=0.0, stop=SIM_LENGTH)
    # pulseVis = DCSource(amplitude=0.38, start=0.0, stop=SIM_LENGTH)
    pulseVis = DCSource(amplitude=58, start=0.0, stop=SIM_LENGTH)
    inputAssembly = Assembly(vision.getInputPopulation()[imagePixels])
    pulseVis.inject_into(inputAssembly)

    #pulseGoal = DCSource(amplitude=0.0038, start=0.0, stop=10)
    #goalInputAssembly = Assembly(goal_move_left1_1[0,1,2,3,4])
    #goalInputAssembly = Assembly(goal_pyramid_1[0,1,2,3,4])
    #pulseGoal.inject_into(goalInputAssembly)

    run(SIM_LENGTH)

#------------Main Body---------------
simulator_name = get_script_args(1)[0]  
exec("from pyNN.%s import *" % simulator_name)

setup(timestep=DELAY,min_delay=DELAY,max_delay=DELAY,debug=0)

#----------------create neurons
#input neurons
cInputNeurons = INPUT_NEURONS_HEIGHT * INPUT_NEURONS_WIDTH 

vision = visionArea()
vision.allocateVisionNeurons()

#create fact neurons (for vision)
# fact_cell_params = {'a': 0.05, 'd': 0,'i_offset' : 2}
fact_cell_params = {}
leftFactAPop = Population(5,IF_curr_exp(**fact_cell_params))
leftFactBPop = Population(5,IF_curr_exp(**fact_cell_params))
rightFactAPop = Population(5,IF_curr_exp(**fact_cell_params))
rightFactBPop = Population(5,IF_curr_exp(**fact_cell_params))
pyramidFactAPop = Population(5,IF_curr_exp(**fact_cell_params))
pyramidFactBPop = Population(5,IF_curr_exp(**fact_cell_params))
stalactiteFactAPop = Population(5,IF_curr_exp(**fact_cell_params))
stalactiteFactBPop = Population(5,IF_curr_exp(**fact_cell_params))
    

##create plan neurons
#  cell_params = {'a' : 0.05}
cell_params = {}
goalTL_1 = Population(5,IF_curr_exp(**cell_params))
goalTL_2 = Population(5,IF_curr_exp(**cell_params))

goalTR_1 = Population(5, IF_curr_exp(**cell_params))
goalTR_2 = Population(5, IF_curr_exp(**cell_params))

goalBack_1 = Population(5,IF_curr_exp(**cell_params))
goalBack_2 = Population(5,IF_curr_exp(**cell_params))

goalForward_1 = Population(5, IF_curr_exp(**cell_params))
goalForward_2 = Population(5, IF_curr_exp(**cell_params))

goal_move_left1_1 = Population(5, IF_curr_exp(**cell_params))
goal_move_left1_2 = Population(5, IF_curr_exp(**cell_params))

goal_move_left2_1 = Population(5, IF_curr_exp(**cell_params))
goal_move_left2_2 = Population(5, IF_curr_exp(**cell_params))

goal_move_right1_1 = Population(5, IF_curr_exp(**cell_params))
goal_move_right1_2 = Population(5, IF_curr_exp(**cell_params))

goal_move_right2_1 = Population(5, IF_curr_exp(**cell_params))
goal_move_right2_2 = Population(5, IF_curr_exp(**cell_params))


goal_pyramid_1 = Population(5, IF_curr_exp(**cell_params))
goal_pyramid_2 = Population(5, IF_curr_exp(**cell_params))


#FACTS	see facts in vision 

#modules 
moduleTL_1 = Population(5,IF_curr_exp(**cell_params))
moduleTL_2 = Population(5,IF_curr_exp(**cell_params))
moduleTR_1 = Population(5, IF_curr_exp(**cell_params))
moduleTR_2 = Population(5, IF_curr_exp(**cell_params))
moduleBack_1 = Population(5,IF_curr_exp(**cell_params))
moduleBack_2 = Population(5,IF_curr_exp(**cell_params))
moduleForward_1 = Population(5, IF_curr_exp(**cell_params))
moduleForward_2 = Population(5, IF_curr_exp(**cell_params))


#output/actions
TL = Population(1, IF_curr_exp(**cell_params))
TR = Population(1, IF_curr_exp(**cell_params))
back = Population(1, IF_curr_exp(**cell_params))
forward = Population(1, IF_curr_exp(**cell_params))

#---------setup connections
vision.makeVisionSynapses()

#setup fact connections
synWeight = 5.0
connect(leftFactAPop, leftFactBPop, weight=synWeight, delay=DELAY)
connect(leftFactBPop, leftFactAPop, weight=synWeight, delay=DELAY)
connect(rightFactAPop, rightFactBPop, weight=synWeight, delay=DELAY)
connect(rightFactBPop, rightFactAPop, weight=synWeight, delay=DELAY)
connect(pyramidFactAPop, pyramidFactBPop, weight=synWeight, delay=DELAY)
connect(pyramidFactBPop, pyramidFactAPop, weight=synWeight, delay=DELAY)
connect(stalactiteFactAPop, stalactiteFactBPop, weight=synWeight, delay=DELAY)
connect(stalactiteFactBPop, stalactiteFactAPop, weight=synWeight, delay=DELAY)


#-------connect objects to facts
synapseArray = leftObjectTurnsLeftFactOn()
Projection(vision.getPyramidPopulation(),leftFactAPop,FromListConnector(synapseArray),StaticSynapse())
Projection(vision.getStalactitePopulation(),leftFactAPop,FromListConnector(synapseArray),StaticSynapse())

synapseArray = rightObjectTurnsLeftFactOn()
Projection(vision.getPyramidPopulation(),rightFactAPop,FromListConnector(synapseArray),StaticSynapse())
Projection(vision.getStalactitePopulation(),rightFactAPop,FromListConnector(synapseArray),StaticSynapse())

synapseArray = objectTurnsObjectFactOn()
Projection(vision.getPyramidPopulation(),pyramidFactAPop,FromListConnector(synapseArray),StaticSynapse())
Projection(vision.getStalactitePopulation(),stalactiteFactAPop,FromListConnector(synapseArray),StaticSynapse())


print "Plan Connections"
setPlanConnections()

#turn on the inputs
setInputs()

#-------------------setup recording
#inpPop.record(['spikes','v'])
vision.setVisionRecording()
leftFactAPop.record(['spikes','v'])
rightFactAPop.record(['spikes','v'])
pyramidFactAPop.record(['spikes','v'])
stalactiteFactAPop.record(['spikes','v'])
back.record('spikes')
forward.record('spikes')
TR.record('spikes')
TL.record('spikes')

#comment - open file
of = open(output_filename, 'w')

#print inpPop[0].get_parameters()

#open image file
imagePixels = openImageFile()
#print imagePixels

runNoCallBack()

#--------------print results

print "left fact"
outAss = Assembly(leftFactAPop[0,1])
outDat = outAss.get_data()
for seg in outDat.segments:
    print(seg.spiketrains)
#    print(seg.analogsignalarrays)

print "right fact"
outAss = Assembly(rightFactAPop[0,1])
outDat = outAss.get_data()
for seg in outDat.segments:
    print(seg.spiketrains)
#    print(seg.analogsignalarrays)

print "pyramid fact"
outAss = Assembly(pyramidFactAPop[0,1])
outDat = outAss.get_data()
for seg in outDat.segments:
    print(seg.spiketrains)

print "stalactite fact"
outAss = Assembly(stalactiteFactAPop[0,1])
outDat = outAss.get_data()
for seg in outDat.segments:
    print(seg.spiketrains)

#print "pyramid"
#outAss = Assembly(pyramidPop[821,520])
#outDat = outAss.get_data()
#for seg in outDat.segments:
#    print(seg.spiketrains)
#print "stalactite"
#outAss = Assembly(stalactitePop[821,520])
#outDat = outAss.get_data()
#for seg in outDat.segments:
#    print(seg.spiketrains)



print_spikes(of,"Pop Back", back)
print_spikes(of,"Pop Forward", forward)
print_spikes(of,"Pop Turn Right", TR)
print_spikes(of,"Pop Turn Left", TL)

#vision.printVisionNets()


end()

