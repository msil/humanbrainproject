#imports for PyNN
from pyNN.nest import *
from retinaConnections import set3x3OnConnections,set3x3OffConnections
from retinaConnections import set6x6OnConnections, set6x6OffConnections
from retinaConnections import set9x9OnConnections,set9x9OffConnections
from v1Connections import set6x6OnToHEdgeBottomConnections, set6x6OffToHEdgeBottomConnections
from v1Connections import set9x9OffToHEdgeBottomConnections
from v1Connections import set6x6OnToSEdgeLeftConnections
from v1Connections import set3x3OnAndOffToBEdgeRightConnections, set6x6OffToBEdgeRightConnections
from v1Connections import set3x3OnToAndAngleConnections,set6x6OnToAndAngleConnections
from v1Connections import set9x9OnToAndAngleConnections
from v1Connections import set3x3OnToLessThanAngleConnections,set6x6OffToLessThanAngleConnections
from v1Connections import set9x9OnToLessThanAngleConnections
from v1Connections import set3x3OnToGreaterThanAngleConnections,set6x6OffToGreaterThanAngleConnections
from v1Connections import set9x9OnToGreaterThanAngleConnections
from v1Connections import set6x6OffToHEdgeTopConnections, set9x9OffToHEdgeTopConnections
from v1Connections import set3x3OnToSEdgeRightConnections, set3x3OffToSEdgeRightConnections
from v1Connections import set6x6OffToSEdgeRightConnections
from v1Connections import set3x3OnAndOffToBEdgeLeftConnections, set6x6OffToBEdgeLeftConnections
from v1Connections import set3x3OnToOrAngleConnections, set6x6OnToOrAngleConnections
from v1Connections import set9x9OnToOrAngleConnections
from objRecConnections import connectCA
from objRecConnections import connectHEdgeBottomToPyramid, connectSEdgeLeftToPyramid
from objRecConnections import connectBEdgeRightToPyramid, connectAndAngleToPyramid
from objRecConnections import connectLessThanAngleToPyramid, connectGreaterThanAngleToPyramid
from objRecConnections import connectHEdgeTopToStalactite, connectSEdgeRightToStalactite
from objRecConnections import connectBEdgeLeftToStalactite, connectOrAngleToStalactite



INPUT_NEURONS_HEIGHT = 50
INPUT_NEURONS_WIDTH = 50
cInputNeurons = INPUT_NEURONS_HEIGHT * INPUT_NEURONS_WIDTH 

class visionArea:

    def printPopulationFirings(self,receptorPop):
        totalNeurons = INPUT_NEURONS_HEIGHT*INPUT_NEURONS_WIDTH
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
        print "3x3 On"
        self.printPopulationFirings(self.retina3x3OnPop)
        print "3x3 Off"
        self.printPopulationFirings(self.retina3x3OffPop)
        print "6x6 On"
        self.printPopulationFirings(self.retina6x6OnPop)
        print "6x6 Off"
        self.printPopulationFirings(self.retina6x6OffPop)
        print "9x9 On"
        self.printPopulationFirings(self.retina9x9OnPop) 
        print "9x9 Off"
        self.printPopulationFirings(self.retina9x9OffPop)

    def printV1(self):
        print "HEdgeBottom"
        self.printPopulationFirings(self.v1HEdgeBottomPop)
        print "SEdgeRight"
        self.printPopulationFirings(self.v1SEdgeRightPop)
        print "BEdgeLeft"
        self.printPopulationFirings(self.v1BEdgeLeftPop)
        print "AndAngle"
        self.printPopulationFirings(self.v1AndAnglePop)
        print "LessThanAngle"
        self.printPopulationFirings(self.v1LessThanAnglePop)
        print "GreaterThanAngle"
        self.printPopulationFirings(self.v1GreaterThanAnglePop)

    def printVisionNets(self):
        print "Long Print Vision Nets"
        self.printReceptors()
        self.printV1()

    #---create neurons
    def allocateNeurons(self):
         #default a .02, b .2, c -65, d 2.0, i_offset 0
         # inp_cell_params = {'a' : 0.0, 'b' :0.2, 'c' : -65, 'd' : 0.0}
         inp_cell_params = {}
         self.inpPop = Population(cInputNeurons,IF_curr_exp(**inp_cell_params))
         # self.inpPop.initialize(v=-58.0)

         #create retinal neurons off centre different than on centre
         # retina_cell_params = {'a' : 0.2, 'b' :0.2, 'c' : -65, 'd' : 2.0}
         retina_cell_params = {}
         self.retina3x3OnPop = Population(cInputNeurons,IF_curr_exp(**retina_cell_params))
         self.retina6x6OnPop  = Population(cInputNeurons,IF_curr_exp(**retina_cell_params))
         self.retina9x9OnPop  = Population(cInputNeurons,IF_curr_exp(**retina_cell_params))

         # retina_cell_params = {'a' : 0.2, 'b' :0.2, 'c' : -65, 'd' : 2.0,'i_offset':1.0}
         retina_cell_params = {}
         self.retina3x3OffPop = Population(cInputNeurons,IF_curr_exp(**retina_cell_params))
         self.retina9x9OffPop = Population(cInputNeurons,IF_curr_exp(**retina_cell_params))

         # retina_cell_params = {'a' : 0.2, 'b' :0.2, 'c' : -65, 'd' : 2.0,'i_offset':2.0}
         retina_cell_params = {}
         self.retina6x6OffPop = Population(cInputNeurons,IF_curr_exp(**retina_cell_params))

    def allocateV1Neurons(self):
         #create V1 neurons
         # V1_c_p = {'a' : 0.2, 'b' :0.2, 'c' : -65, 'd' : 2.0}
         V1_c_p = {}
         self.v1HEdgeBottomPop = Population(cInputNeurons,IF_curr_exp(**V1_c_p))
         self.v1SEdgeLeftPop  = Population(cInputNeurons,IF_curr_exp(**V1_c_p))
         self.v1BEdgeRightPop  = Population(cInputNeurons,IF_curr_exp(**V1_c_p))
         self.v1AndAnglePop  = Population(cInputNeurons,IF_curr_exp(**V1_c_p))
         self.v1LessThanAnglePop=Population(cInputNeurons,IF_curr_exp(**V1_c_p))
         self.v1GreaterThanAnglePop = Population(cInputNeurons,IF_curr_exp(**V1_c_p))
         self.v1HEdgeTopPop  = Population(cInputNeurons,IF_curr_exp(**V1_c_p))
         self.v1SEdgeRightPop  = Population(cInputNeurons,IF_curr_exp(**V1_c_p))
         self.v1BEdgeLeftPop  = Population(cInputNeurons,IF_curr_exp(**V1_c_p))
         self.v1OrAnglePop  = Population(cInputNeurons,IF_curr_exp(**V1_c_p))

    def allocateObjRecNeurons(self):
        #create object recognition neurons
        # obj_c_p = {'a' : 0.02,'i_offset' : 2}
        obj_c_p = {}
        self.pyramidPop = Population(cInputNeurons,IF_curr_exp(**obj_c_p))
        self.stalactitePop = Population(cInputNeurons,IF_curr_exp(**obj_c_p))

    def allocateVisionNeurons(self):
        self.allocateNeurons()
        self.allocateV1Neurons()
        self.allocateObjRecNeurons()


    #----------------setup input to retina connections
    def makeInputToRetSynapses(self):
        print "Make Input to Retina Synapses"
        synapseArray = []
        #3x3On
        for row in range (1,49):
            for col in range (1,49):
                newSynapses = set3x3OnConnections(col,row)
                synapseArray = synapseArray + newSynapses
        Projection(self.inpPop,self.retina3x3OnPop,FromListConnector(synapseArray),StaticSynapse())

        #3x3Off
        synapseArray = []
        for row in range (1,49):
            for col in range (1,49):
                newSynapses = set3x3OffConnections(col,row)
                synapseArray = synapseArray + newSynapses
        Projection(self.inpPop,self.retina3x3OffPop,FromListConnector(synapseArray),StaticSynapse())

        #6x6On
        synapseArray = []
        for row in range (2,47):
            for col in range (2,47):
                newSynapses = set6x6OnConnections(col,row)
                synapseArray = synapseArray + newSynapses
        Projection(self.inpPop,self.retina6x6OnPop,FromListConnector(synapseArray),StaticSynapse())

        #6x6Off
        synapseArray = []
        for row in range (2,47):
            for col in range (2,47):
                newSynapses = set6x6OffConnections(col,row)
                synapseArray = synapseArray + newSynapses
        Projection(self.inpPop,self.retina6x6OffPop,FromListConnector(synapseArray),StaticSynapse())

        #9x9Off
        synapseArray = []
        for row in range (3,45):
            for col in range (3,45):
                newSynapses = set9x9OffConnections(col,row)
                synapseArray = synapseArray + newSynapses
        Projection(self.inpPop,self.retina9x9OffPop,FromListConnector(synapseArray),StaticSynapse())

        #9x9On
        synapseArray = []
        for row in range (3,45):
            for col in range (3,45):
                newSynapses = set9x9OnConnections(col,row)
                synapseArray = synapseArray + newSynapses
        Projection(self.inpPop,self.retina9x9OnPop,FromListConnector(synapseArray),StaticSynapse())

    #-------------------setup retina to V1 connections---
    def makeRetToV1Synapses(self):
        print "Make synapses from Ret to V1"
        #HedgeBottom
        synapseArray = []
        for row in range (0,INPUT_NEURONS_HEIGHT-1):
            for col in range (2,INPUT_NEURONS_HEIGHT-3):
                newSynapses = set6x6OnToHEdgeBottomConnections(col,row)
                synapseArray = synapseArray + newSynapses
        Projection(self.retina6x6OnPop,self.v1HEdgeBottomPop,FromListConnector(synapseArray),StaticSynapse())

        synapseArray = []
        for row in range (0,INPUT_NEURONS_HEIGHT-1):
            for col in range (2,INPUT_NEURONS_HEIGHT-3):
                newSynapses = set6x6OffToHEdgeBottomConnections(col,row)
                synapseArray = synapseArray + newSynapses
        Projection(self.retina6x6OffPop,self.v1HEdgeBottomPop,FromListConnector(synapseArray),StaticSynapse())

        synapseArray = []
        for row in range (0,INPUT_NEURONS_HEIGHT-1):
            for col in range (2,INPUT_NEURONS_HEIGHT-3):
                newSynapses = set9x9OffToHEdgeBottomConnections(col,row)
                synapseArray = synapseArray + newSynapses
        Projection(self.retina9x9OffPop,self.v1HEdgeBottomPop,FromListConnector(synapseArray),StaticSynapse())

        #SEdge Left Connections
        synapseArray = []
        for row in range (0,INPUT_NEURONS_HEIGHT):
            for col in range (0,INPUT_NEURONS_WIDTH):
                newSynapses = set6x6OnToSEdgeLeftConnections(col,row)
                synapseArray = synapseArray + newSynapses
        Projection(self.retina6x6OnPop,self.v1SEdgeLeftPop,FromListConnector(synapseArray),StaticSynapse())
        Projection(self.retina6x6OffPop,self.v1SEdgeLeftPop,FromListConnector(synapseArray),StaticSynapse())

        #rightBEdges
        synapseArray = []
        for row in range (0,INPUT_NEURONS_HEIGHT):
            for col in range (0,INPUT_NEURONS_WIDTH):
                newSynapses = set3x3OnAndOffToBEdgeRightConnections(col,row)
                synapseArray = synapseArray + newSynapses
        Projection(self.retina3x3OnPop,self.v1BEdgeRightPop,FromListConnector(synapseArray),StaticSynapse())
        Projection(self.retina3x3OffPop,self.v1BEdgeRightPop,FromListConnector(synapseArray),StaticSynapse())

        synapseArray = []
        for row in range (0,INPUT_NEURONS_HEIGHT):
            for col in range (0,INPUT_NEURONS_WIDTH):
                newSynapses = set6x6OffToBEdgeRightConnections(col,row)
                synapseArray = synapseArray + newSynapses
        Projection(self.retina6x6OffPop,self.v1BEdgeRightPop,FromListConnector(synapseArray),StaticSynapse())

        #andAngle
        synapseArray = []
        for row in range (0,INPUT_NEURONS_HEIGHT):
            for col in range (0,INPUT_NEURONS_WIDTH):
                newSynapses = set3x3OnToAndAngleConnections(col,row)
                synapseArray = synapseArray + newSynapses
        Projection(self.retina3x3OnPop,self.v1AndAnglePop,FromListConnector(synapseArray),StaticSynapse())

        synapseArray = []
        for row in range (0,INPUT_NEURONS_HEIGHT):
            for col in range (0,INPUT_NEURONS_WIDTH):
                newSynapses = set6x6OnToAndAngleConnections(col,row)
                synapseArray = synapseArray + newSynapses
        Projection(self.retina6x6OnPop,self.v1AndAnglePop,FromListConnector(synapseArray),StaticSynapse())

        synapseArray = []
        for row in range (0,INPUT_NEURONS_HEIGHT):
            for col in range (0,INPUT_NEURONS_WIDTH):
                newSynapses = set9x9OnToAndAngleConnections(col,row)
                synapseArray = synapseArray + newSynapses
        Projection(self.retina9x9OnPop,self.v1AndAnglePop,FromListConnector(synapseArray),StaticSynapse())

        #Less Than Angle
        synapseArray = []
        for row in range (0,INPUT_NEURONS_HEIGHT):
            for col in range (0,INPUT_NEURONS_WIDTH):
                newSynapses = set3x3OnToLessThanAngleConnections(col,row)
                synapseArray = synapseArray + newSynapses
        Projection(self.retina3x3OnPop,self.v1LessThanAnglePop,FromListConnector(synapseArray),StaticSynapse())

        synapseArray = []
        for row in range (0,INPUT_NEURONS_HEIGHT):
            for col in range (0,INPUT_NEURONS_WIDTH):
                newSynapses = set6x6OffToLessThanAngleConnections(col,row)
                synapseArray = synapseArray + newSynapses
        Projection(self.retina6x6OffPop,self.v1LessThanAnglePop,FromListConnector(synapseArray),StaticSynapse())
        
        synapseArray = []
        for row in range (0,INPUT_NEURONS_HEIGHT):
            for col in range (0,INPUT_NEURONS_WIDTH):
                newSynapses = set9x9OnToLessThanAngleConnections(col,row)
                synapseArray = synapseArray + newSynapses
        Projection(self.retina9x9OnPop,self.v1LessThanAnglePop,FromListConnector(synapseArray),StaticSynapse())

        #Greater Than Angle
        synapseArray = []
        for row in range (0,INPUT_NEURONS_HEIGHT):
            for col in range (0,INPUT_NEURONS_WIDTH):
                newSynapses = set3x3OnToGreaterThanAngleConnections(col,row)
                synapseArray = synapseArray + newSynapses
        Projection(self.retina3x3OnPop,self.v1GreaterThanAnglePop,FromListConnector(synapseArray),StaticSynapse())

        synapseArray = []
        for row in range (0,INPUT_NEURONS_HEIGHT):
            for col in range (0,INPUT_NEURONS_WIDTH):
                newSynapses = set6x6OffToGreaterThanAngleConnections(col,row)
                synapseArray = synapseArray + newSynapses
        Projection(self.retina6x6OffPop,self.v1GreaterThanAnglePop,FromListConnector(synapseArray),StaticSynapse())

        synapseArray = []
        for row in range (0,INPUT_NEURONS_HEIGHT):
            for col in range (0,INPUT_NEURONS_WIDTH):
                newSynapses = set9x9OnToGreaterThanAngleConnections(col,row)
                synapseArray = synapseArray + newSynapses
        Projection(self.retina9x9OnPop,self.v1GreaterThanAnglePop,FromListConnector(synapseArray),StaticSynapse())

        #topHEdges
        synapseArray = []
        for row in range (0,INPUT_NEURONS_HEIGHT-1):
            for col in range (0,INPUT_NEURONS_HEIGHT):
                newSynapses = set6x6OffToHEdgeTopConnections(col,row)
                synapseArray = synapseArray + newSynapses
        Projection(self.retina6x6OffPop,self.v1HEdgeTopPop,FromListConnector(synapseArray),StaticSynapse())

        synapseArray = []
        for row in range (0,INPUT_NEURONS_HEIGHT-1):
            for col in range (0,INPUT_NEURONS_HEIGHT):
                newSynapses = set9x9OffToHEdgeTopConnections(col,row)
                synapseArray = synapseArray + newSynapses
        Projection(self.retina9x9OffPop,self.v1HEdgeTopPop,FromListConnector(synapseArray),StaticSynapse())

        #right SEdges
        synapseArray = []
        for row in range (0,INPUT_NEURONS_HEIGHT-1):
            for col in range (0,INPUT_NEURONS_HEIGHT):
                newSynapses = set3x3OnToSEdgeRightConnections(col,row)
                synapseArray = synapseArray + newSynapses
        Projection(self.retina3x3OnPop,self.v1SEdgeRightPop,FromListConnector(synapseArray),StaticSynapse())

        synapseArray = []
        for row in range (0,INPUT_NEURONS_HEIGHT-1):
            for col in range (0,INPUT_NEURONS_HEIGHT):
                newSynapses = set3x3OffToSEdgeRightConnections(col,row)
                synapseArray = synapseArray + newSynapses
        Projection(self.retina3x3OffPop,self.v1SEdgeRightPop,FromListConnector(synapseArray),StaticSynapse())

        synapseArray = []
        for row in range (0,INPUT_NEURONS_HEIGHT-1):
            for col in range (0,INPUT_NEURONS_HEIGHT):
                newSynapses = set6x6OffToSEdgeRightConnections(col,row)
                synapseArray = synapseArray + newSynapses
        Projection(self.retina6x6OffPop,self.v1SEdgeRightPop,FromListConnector(synapseArray),StaticSynapse())

        #left BEdges
        synapseArray = []
        for row in range (0,INPUT_NEURONS_HEIGHT-1):
           for col in range (0,INPUT_NEURONS_HEIGHT):
               newSynapses = set3x3OnAndOffToBEdgeLeftConnections(col,row)
               synapseArray = synapseArray + newSynapses
        Projection(self.retina3x3OnPop,self.v1BEdgeLeftPop,FromListConnector(synapseArray),StaticSynapse())
        Projection(self.retina3x3OffPop,self.v1BEdgeLeftPop,FromListConnector(synapseArray),StaticSynapse())

        synapseArray = []
        for row in range (0,INPUT_NEURONS_HEIGHT-1):
           for col in range (0,INPUT_NEURONS_HEIGHT):
               newSynapses = set6x6OffToBEdgeLeftConnections(col,row)
               synapseArray = synapseArray + newSynapses
        Projection(self.retina6x6OffPop,self.v1BEdgeLeftPop,FromListConnector(synapseArray),StaticSynapse())

        #or Angle
        synapseArray = []
        for row in range (0,INPUT_NEURONS_HEIGHT):
            for col in range (0,INPUT_NEURONS_WIDTH):
                newSynapses = set3x3OnToOrAngleConnections(col,row)
                synapseArray = synapseArray + newSynapses
        Projection(self.retina3x3OnPop,self.v1OrAnglePop,FromListConnector(synapseArray),StaticSynapse())
        
        synapseArray = []
        for row in range (0,INPUT_NEURONS_HEIGHT):
            for col in range (0,INPUT_NEURONS_WIDTH):
                newSynapses = set6x6OnToOrAngleConnections(col,row)
                synapseArray = synapseArray + newSynapses
        Projection(self.retina6x6OnPop,self.v1OrAnglePop,FromListConnector(synapseArray),StaticSynapse())
        
        synapseArray = []
        for row in range (0,INPUT_NEURONS_HEIGHT-1):
            for col in range (0,INPUT_NEURONS_HEIGHT):
                newSynapses = set9x9OnToOrAngleConnections(col,row)
                synapseArray = synapseArray + newSynapses
        Projection(self.retina9x9OnPop,self.v1OrAnglePop,FromListConnector(synapseArray),StaticSynapse())

    #-------------------setup Object Recognion and  V1 to ObjRec connections---
    def makeV1ToObjRecSynapses(self):
        print "Make V1 to Object Recognition Synapses"

        #setup pyramid CAs
        synapseArray = []
        for cCA in range (0,25):
            newSynapses = connectCA(cCA)
            synapseArray = synapseArray + newSynapses
        Projection(self.pyramidPop,self.pyramidPop,FromListConnector(synapseArray),StaticSynapse())

        #HEdge to Pyramid
        synapseArray = connectHEdgeBottomToPyramid()
        Projection(self.v1HEdgeBottomPop,self.pyramidPop,FromListConnector(synapseArray),StaticSynapse())

        #SEdge to Pyramid
        synapseArray = connectSEdgeLeftToPyramid()
        Projection(self.v1SEdgeRightPop,self.pyramidPop,FromListConnector(synapseArray),StaticSynapse())

        #BEdge to Pyramid
        synapseArray = connectBEdgeRightToPyramid()
        Projection(self.v1BEdgeLeftPop,self.pyramidPop,FromListConnector(synapseArray),StaticSynapse())

        #And to Pyramid
        synapseArray = connectAndAngleToPyramid()
        Projection(self.v1AndAnglePop,self.pyramidPop,FromListConnector(synapseArray),StaticSynapse())

        #Less Than Angle to Pyramid
        synapseArray = connectLessThanAngleToPyramid()
        Projection(self.v1LessThanAnglePop,self.pyramidPop,FromListConnector(synapseArray),StaticSynapse())

        #Greater Than Angle to Pyramid
        synapseArray = connectGreaterThanAngleToPyramid()
        Projection(self.v1GreaterThanAnglePop,self.pyramidPop,FromListConnector(synapseArray),StaticSynapse())

        #---------------setup stalactite CAs
        synapseArray = []
        for cCA in range (0,25):
            newSynapses = connectCA(cCA)
            synapseArray = synapseArray + newSynapses
        Projection(self.stalactitePop,self.stalactitePop,FromListConnector(synapseArray),StaticSynapse())

        #HEdge to Stalactite
        synapseArray = connectHEdgeTopToStalactite()
        Projection(self.v1HEdgeTopPop,self.stalactitePop,FromListConnector(synapseArray),StaticSynapse())

        #sEdge to Stalactite
        synapseArray = connectSEdgeRightToStalactite()
        Projection(self.v1SEdgeRightPop,self.stalactitePop,FromListConnector(synapseArray),StaticSynapse())

        #bEdge to Stalactite
        synapseArray = connectBEdgeLeftToStalactite()
        Projection(self.v1BEdgeLeftPop,self.stalactitePop,FromListConnector(synapseArray),StaticSynapse())

        #orAngle to Stalactite
        synapseArray = connectOrAngleToStalactite()
        Projection(self.v1OrAnglePop,self.stalactitePop,FromListConnector(synapseArray),StaticSynapse())

    def makeVisionSynapses(self):
        self.makeInputToRetSynapses()
        self.makeRetToV1Synapses()
        self.makeV1ToObjRecSynapses()


    def setVisionRecording(self):
        self.retina3x3OffPop.record(['spikes','v'])
        self.retina3x3OffPop.record(['spikes','v'])
        self.retina6x6OnPop.record(['spikes','v'])
        self.retina6x6OffPop.record(['spikes','v'])
        self.retina9x9OnPop.record(['spikes','v'])
        self.retina9x9OffPop.record(['spikes','v'])
        self.v1HEdgeBottomPop.record(['spikes','v'])
        self.v1SEdgeRightPop.record(['spikes','v'])
        self.v1BEdgeLeftPop.record(['spikes','v'])
        self.v1AndAnglePop.record(['spikes','v'])
        self.v1LessThanAnglePop.record(['spikes','v'])
        self.v1GreaterThanAnglePop.record(['spikes','v'])
        self.pyramidPop.record(['spikes','v'])
        self.stalactitePop.record(['spikes','v'])


    def getInputPopulation(self):
        return self.inpPop

    def getPyramidPopulation(self):
        return self.pyramidPop

    def getStalactitePopulation(self):
        return self.stalactitePop
