"""
The vision class without the connections.
"""

#imports for PyNN
from pyNN.utility import get_script_args, normalized_filename
from neo.io import PyNNTextIO
from pyNN.nest import *
#from pyNN.spiNNaker import *

from nealParams import *
from retinaConnections import get3x3OnExcite, get3x3OnInhib
from retinaConnections import get3x3OffExcite,get3x3OffInhib
from retinaConnections import get6x6OnExcite, get6x6OnInhib
from retinaConnections import get6x6OffExcite, get6x6OffInhib
from retinaConnections import get9x9OnExcite, get9x9OnInhib
from retinaConnections import get9x9OffExcite,get9x9OffInhib


from v1Connections import getHEdgeBottomFrom3x3OffExcite
from v1Connections import getHEdgeBottomFrom9x9OffInhib
from v1Connections import getHEdgeTopFrom3x3OffExcite
from v1Connections import getHEdgeTopFrom9x9OffInhib


class visionArea:

    def __init__(self, simName):
        self.simulator_name = simName
        self.threeOn = False
        self.threeOff = True
        self.sixOn = False
        self.sixOff = False
        self.nineOn = False
        self.nineOff = True

        self.hEdgeTop = True
        self.hEdgeBottom = True

    def nealProjection(self,preNeurons,postNeurons, connectorList,inhExc):
        if self.simulator_name == 'spiNNaker':
            Projection(preNeurons, postNeurons, connectorList,target=inhExc)
        elif self.simulator_name == 'nest':
            Projection(preNeurons, postNeurons, connectorList)
        else:
            print 'bad simulator for nealProjection'

    #------print functions
    def printPopulationFirings(self,receptorPop):
        totalNeurons = neuronsPerSubnet
        for neuronNum in range (0,totalNeurons-1):
            if (neuronNum < totalNeurons):
                outAssembly = Assembly(receptorPop[neuronNum,(neuronNum+1)])
            else: 
                outAssembly = Assembly(receptorPop[neuronNum,0])
            outDat = outAssembly.get_data()
            seg = outDat.segments[0]
            spikeTrains = seg.spiketrains
            if len(spikeTrains) > 0:
                times = spikeTrains[0].times
                if len(times) > 0:
                    print neuronNum, len(times),
                    for time in times:
                        base = time.base
                        print base,
                    print " "

    def printReceptors(self):
        if self.threeOn:
            print "3x3 On"
            self.printPopulationFirings(self.threeOnCells)
        if self.threeOff:
            print "3x3 Off"
            self.printPopulationFirings(self.threeOffCells)
        if self.sixOn:
            print "6x6 On"
            self.printPopulationFirings(self.sixOnCells)
        if self.sixOff:
            print "6x6 Off"
            self.printPopulationFirings(self.sixOffCells)
        if self.nineOn:
            print "9x9 On"
            self.printPopulationFirings(self.nineOnCells)
        if self.nineOff:
            print "9x9 Off"
            self.printPopulationFirings(self.nineOffCells)

    def printV1(self):
        if self.hEdgeTop:
            print "HEdgeBottom"
            self.printPopulationFirings(self.hEdgeBottomCells)
        if self.hEdgeTop:
            print "HEdgeTop"
            self.printPopulationFirings(self.hEdgeTopCells)


    def printFact(self,factCells):
        for neuronNum in range (0,4):
            outAssembly = Assembly(factCells[neuronNum,(neuronNum+1)])
            outDat = outAssembly.get_data()
            seg = outDat.segments[0]
            spikeTrains = seg.spiketrains
            if len(spikeTrains) > 0:
                times = spikeTrains[0].times
                if len(times) > 0:
                    print neuronNum, len(times),
                    for time in times:
                        base = time.base
                        print base,
                    print " "
        
    def printObjects(self):
        print 'Pyramid Left'
        self.printFact(self.pyramidLeftCells)
        print 'Pyramid Right'
        self.printFact(self.pyramidRightCells)
        print 'Stalactite Left'
        self.printFact(self.stalactiteLeftCells)
        print 'Stalactite Right'
        self.printFact(self.stalactiteRightCells)

    def printVisionNets(self):
        if self.simulator_name == 'spiNNaker':
            self.threeOnCells.print_v('results/IF_curr_exp1_%s.v' % self.simulator_name)
            self.threeOnCells.printSpikes('results/spikes3N.sp')
            self.inputCells.printSpikes('results/spikesI.sp')
            self.threeOffCells.printSpikes('results/spikes3F.sp')
            self.sixOnCells.printSpikes('results/spikes6N.sp')
            self.sixOffCells.printSpikes('results/spikes6F.sp')
            self.nineOnCells.printSpikes('results/spikes9N.sp')
            self.nineOffCells.printSpikes('results/spikes9F.sp')
            self.hEdgeTopCells.printSpikes('results/spikesHT.sp')
            self.hEdgeBottomCells.printSpikes('results/spikesHB.sp')
        elif self.simulator_name == 'nest':
            #self.printReceptors()
            #self.printV1()
            self.printObjects()
        elif self.simulator_name == 'out':
            print '3On'
            outAss = Assembly(self.threeOnCells[4,1411])
            #outDat = self.threeOnCells.get_data()
            outDat = outAss.get_data()
            for seg in outDat.segments:
                print(seg.spiketrains)
            print '3Off'
            #outAss = Assembly(self.threeOffCells[4,1411])
            outDat = self.threeOffCells.get_data()
            #outDat = outAss.get_data()
            for seg in outDat.segments:
                print(seg.spiketrains)


    #---create neurons
    def allocateVisualInputNeurons(self):
        cell_params = {'tau_refrac' : 3.0, 'v_rest' : -65.0,
               'v_thresh' : -51.0,  'tau_syn_E'  : 2.0, 
               'tau_syn_I': 5.0,    'v_reset'    : -70.0, 
               'i_offset' : 0.1}

        self.inputCells=Population(neuronsPerSubnet, IF_curr_exp, cell_params)


    def allocateRetinaNeurons(self):
        cell_params = {'tau_refrac' : 3.0, 'v_rest' : -65.0,
               'v_thresh' : -51.0,  'tau_syn_E'  : 2.0, 
               'tau_syn_I': 5.0,    'v_reset'    : -70.0, 
               'i_offset' : 0.1}
        if self.threeOn:
            self.threeOnCells=Population(neuronsPerSubnet,IF_curr_exp,cell_params)
        else:
            self.threeOnCells=Population(1,IF_curr_exp,cell_params)

        cell_params = {'tau_refrac' : 3.0, 'v_rest' : -65.0,
               'v_thresh' : -51.0,  'tau_syn_E'  : 2.0, 
               'tau_syn_I': 5.0,    'v_reset'    : -70.0, 
               'i_offset' : -1.0}
        if self.threeOff:
            self.threeOffCells=Population(neuronsPerSubnet,IF_curr_exp,cell_params)
        else:
            self.threeOffCells=Population(1,IF_curr_exp,cell_params)
        if self.nineOn:
            self.nineOnCells = Population(neuronsPerSubnet,IF_curr_exp,cell_params)
        else:
            self.nineOnCells = Population(1,IF_curr_exp,cell_params)
        if self.nineOff:
            self.nineOffCells= Population(neuronsPerSubnet,IF_curr_exp,cell_params)
        else:
            self.nineOffCells= Population(1,IF_curr_exp,cell_params)

        cell_params = {'tau_refrac' : 3.0, 'v_rest' : -65.0,
               'v_thresh' : -51.0,  'tau_syn_E'  : 2.0, 
               'tau_syn_I': 5.0,    'v_reset'    : -70.0, 
               'i_offset' : 0.0}
        if self.sixOn:
            self.sixOnCells = Population(neuronsPerSubnet,IF_curr_exp, cell_params)
        else:
            self.sixOnCells = Population(1,IF_curr_exp, cell_params)
        if self.sixOff:
            self.sixOffCells= Population(neuronsPerSubnet,IF_curr_exp, cell_params)
        else:
            self.sixOffCells= Population(1,IF_curr_exp, cell_params)
        

    def allocateV1Neurons(self):
        cell_params = {'tau_refrac' : 3.0, 'v_rest' : -65.0,
               'v_thresh' : -51.0,  'tau_syn_E'  : 2.0, 
               'tau_syn_I': 5.0,    'v_reset'    : -70.0, 
               'i_offset' : 0.1}
        if self.hEdgeBottom:
            self.hEdgeBottomCells=Population(neuronsPerSubnet,IF_curr_exp,cell_params)
        else:
            self.hEdgeBottomCells=Population(1,IF_curr_exp,cell_params)
        if self.hEdgeTop:
            self.hEdgeTopCells=Population(neuronsPerSubnet,IF_curr_exp,cell_params)
        else:
            self.hEdgeTopCells=Population(1,IF_curr_exp,cell_params)


    def allocateObjRecNeurons(self):
        cell_params = {'tau_refrac' : 3.0, 'v_rest' : -65.0,
               'v_thresh' : -51.0,  'tau_syn_E'  : 2.0, 
               'tau_syn_I': 5.0,    'v_reset'    : -70.0, 
               'i_offset' : 0.1}
        self.pyramidLeftCells=Population(5,IF_curr_exp,cell_params)
        self.pyramidRightCells=Population(5,IF_curr_exp,cell_params)
        self.stalactiteLeftCells=Population(5,IF_curr_exp,cell_params)
        self.stalactiteRightCells=Population(5,IF_curr_exp,cell_params)
        
#set up clamped input

    def allocateVisionNeurons(self):
        self.allocateVisualInputNeurons()
        self.allocateRetinaNeurons()
        #self.allocateNeurons()
        self.allocateV1Neurons()
        self.allocateObjRecNeurons()


    #----------------setup input to retina connections
    def makeInputToRetSynapses(self):
        #3x3On
        if self.threeOn:
            excConnectorList = get3x3OnExcite()
            excConnector = FromListConnector(excConnectorList) 
            self.nealProjection(self.inputCells,self.threeOnCells, excConnector,'excitatory')
            inhConnectorList = get3x3OnInhib()
            inhConnector = FromListConnector(inhConnectorList)
            self.nealProjection(self.inputCells,self.threeOnCells, inhConnector,'inhibitory')

        #3x3Off
        if self.threeOff:
            excConnectorList = get3x3OffExcite()
            excConnector = FromListConnector(excConnectorList)
            self.nealProjection(self.inputCells, self.threeOffCells, excConnector,'excitatory')
            inhConnectorList = get3x3OffInhib()
            inhConnector = FromListConnector(inhConnectorList)
            self.nealProjection(self.inputCells, self.threeOffCells, inhConnector,'inhibitory')

        #6x6On
        if self.sixOn:
            excConnectorList = get6x6OnExcite()
            excConnector = FromListConnector(excConnectorList) 
            self.nealProjection(self.inputCells, self.sixOnCells, excConnector,'excitatory')
            inhConnectorList = get6x6OnInhib()
            inhConnector = FromListConnector(inhConnectorList)
            self.nealProjection(self.inputCells, self.sixOnCells, inhConnector,'inhibitory')

        #6x6Off
        if self.sixOff:
            excConnectorList = get6x6OffExcite()
            excConnector = FromListConnector(excConnectorList) 
            self.nealProjection(self.inputCells, self.sixOffCells, excConnector,'excitatory')
            inhConnectorList = get6x6OffInhib()
            inhConnector = FromListConnector(inhConnectorList)
            self.nealProjection(self.inputCells, self.sixOffCells, inhConnector,'inhibitory')

        #9x9On
        if self.nineOn:
            excConnectorList = get9x9OnExcite()
            excConnector = FromListConnector(excConnectorList) 
            self.nealProjection(self.inputCells, self.nineOnCells, excConnector,'excitatory')
            inhConnectorList = get9x9OnInhib()
            inhConnector = FromListConnector(inhConnectorList)
            self.nealProjection(self.inputCells, self.nineOnCells, inhConnector,'inhibitory')

        #9x9off
        if self.nineOff:
            excConnectorList = get9x9OffExcite()
            excConnector = FromListConnector(excConnectorList) 
            self.nealProjection(self.inputCells, self.nineOffCells, excConnector,'excitatory')
            inhConnectorList = get9x9OffInhib()
            inhConnector = FromListConnector(inhConnectorList)
            self.nealProjection(self.inputCells, self.nineOffCells, inhConnector,'inhibitory')


    #-------------------setup retina to V1 connections---
    def makeRetToV1Synapses(self):
        if self.hEdgeBottom:
            excConnectorList = getHEdgeBottomFrom3x3OffExcite()
            excConnector = FromListConnector(excConnectorList) 
            self.nealProjection(self.threeOffCells,self.hEdgeBottomCells, excConnector,'excitatory')
            inhConnectorList = getHEdgeBottomFrom9x9OffInhib()
            inhConnector = FromListConnector(inhConnectorList)
            self.nealProjection(self.nineOffCells, self.hEdgeBottomCells, inhConnector,'inhibitory')

        if self.hEdgeTop:
            excConnectorList = getHEdgeTopFrom3x3OffExcite()
            excConnector = FromListConnector(excConnectorList) 
            self.nealProjection(self.threeOffCells,self.hEdgeTopCells, excConnector,'excitatory')
            inhConnectorList = getHEdgeTopFrom9x9OffInhib()
            inhConnector = FromListConnector(inhConnectorList)
            self.nealProjection(self.nineOffCells, self.hEdgeTopCells, inhConnector,'inhibitory')


    #-------------------setup Object Recognion and  V1 to ObjRec connections---
    def connectV1FeatureToObject (self, synWeight,leftStart, rightEnd):
        connector = []
        for cRow in range (0,INPSIZE):
            for cCol in range (int(INPSIZE*leftStart),int(INPSIZE*rightEnd)):
                for toNeuron in range (0,5):
                    fromNeuron = cRow*INPSIZE+ cCol
                    connector=connector+[(fromNeuron,toNeuron,synWeight,DELAY)]
        return connector

    #main proc
    def makeV1ToObjRecSynapses(self):
        connectorList = self.connectV1FeatureToObject(3.0,0,0.4)
        connector = FromListConnector(connectorList) 
        self.nealProjection(self.hEdgeBottomCells,self.pyramidLeftCells,connector,'excitatory')
        self.nealProjection(self.hEdgeTopCells,self.stalactiteLeftCells,connector,'excitatory')
        connectorList = self.connectV1FeatureToObject(3.0,0.6,1.0)
        connector = FromListConnector(connectorList) 
        self.nealProjection(self.hEdgeBottomCells,self.pyramidRightCells,connector,'excitatory')
        self.nealProjection(self.hEdgeTopCells,self.stalactiteRightCells,connector,'excitatory')

    def makeObjRecSynapses(self):
        #new pyramid CA connections
        synWeight = 5.0
        connect(self.pyramidLeftAPop, self.pyramidLeftBPop,weight=synWeight, delay=DELAY)
        connect(self.pyramidLeftBPop, self.pyramidLeftAPop,weight=synWeight, delay=DELAY)
        connect(self.pyramidRightAPop, self.pyramidRightBPop,weight=synWeight, delay=DELAY)
        connect(self.pyramidRightBPop, self.pyramidRightAPop,weight=synWeight, delay=DELAY)
        connect(self.stalactiteLeftAPop,self.stalactiteLeftBPop,weight=synWeight,delay=DELAY)
        connect(self.stalactiteLeftBPop,self.stalactiteLeftAPop,weight=synWeight,delay=DELAY)
        connect(self.stalactiteRightAPop,self.stalactiteRightBPop,weight=synWeight,delay=DELAY)
        connect(self.stalactiteRightBPop,self.stalactiteRightAPop,weight=synWeight,delay=DELAY)

        #the vision object position facts are mutually exclusive
        inhibWeight = -3.0
        connect(self.pyramidLeftAPop,self.pyramidRightAPop,weight=inhibWeight,delay=DELAY)
        connect(self.pyramidLeftAPop,self.stalactiteLeftAPop,weight=inhibWeight,delay=DELAY)
        connect(self.pyramidLeftAPop,self.stalactiteRightAPop,weight=inhibWeight,delay=DELAY)
        connect(self.pyramidRightAPop,self.pyramidLeftAPop,weight=inhibWeight,delay=DELAY)
        connect(self.pyramidRightAPop,self.stalactiteLeftAPop,weight=inhibWeight,delay=DELAY)
        connect(self.pyramidRightAPop,self.stalactiteRightAPop,weight=inhibWeight,delay=DELAY)
        connect(self.stalactiteLeftAPop,self.pyramidLeftAPop,weight=inhibWeight,delay=DELAY)
        connect(self.stalactiteLeftAPop,self.pyramidRightAPop,weight=inhibWeight,delay=DELAY)
        connect(self.stalactiteLeftAPop,self.stalactiteRightAPop,weight=inhibWeight,delay=DELAY)
        connect(self.stalactiteRightAPop,self.pyramidLeftAPop,weight=inhibWeight,delay=DELAY)
        connect(self.stalactiteRightAPop,self.pyramidRightAPop,weight=inhibWeight,delay=DELAY)
        connect(self.stalactiteRightAPop,self.stalactiteLeftAPop,weight=inhibWeight,delay=DELAY)


    def makeVisionSynapses(self):
        self.makeRetToV1Synapses()
        self.makeInputToRetSynapses()
        self.makeV1ToObjRecSynapses()
        #undoneself.makeObjRecSynapses()
        
    #--- input functions
    def setInput(self,imagePixels,inputSource):
        weight = 20.0
        connectors = []

        for onPixel in imagePixels:
            connectors = connectors + [(0,onPixel,weight,DELAY)]

        #print connectors
        excConnector = FromListConnector(connectors)
        self.nealProjection(inputSource,self.inputCells,excConnector,'excitatory')
        return connectors

    #---- recording functions
    def setVisionRecording(self):
        if self.simulator_name == 'spiNNaker':
            self.inputCells.record()
            self.threeOnCells.record()
            self.threeOffCells.record()
            self.sixOnCells.record()
            self.sixOffCells.record()
            self.nineOnCells.record()
            self.nineOffCells.record()
            self.hEdgeBottomCells.record()
            self.hEdgeTopCells.record()
            self.pyramidLeftCells.record()
            self.pyramidRightCells.record()
            self.stalactiteLeftCells.record()
            self.stalactiteRightCells.record()
        elif self.simulator_name == 'nest':
            self.threeOnCells.record('spikes')
            self.threeOffCells.record('spikes')
            self.sixOnCells.record('spikes')
            self.sixOffCells.record('spikes')
            self.nineOnCells.record('spikes')
            self.nineOffCells.record('spikes')
            self.hEdgeBottomCells.record('spikes')
            self.hEdgeTopCells.record('spikes')
            self.pyramidLeftCells.record('spikes')
            self.pyramidRightCells.record('spikes')
            self.stalactiteLeftCells.record('spikes')
            self.stalactiteRightCells.record('spikes')


    #-cover functions to return internal values
    def getInputPopulation(self):
        return self.inpPop

    def getLeftPyramid(self):
        return self.pyramidLeftAPop

    def getRightPyramid(self):
        return self.pyramidRightAPop

    def getLeftStalactite(self):
        return self.stalactiteLeftAPop

    def getRightStalactite(self):
        return self.stalactiteRightAPop


