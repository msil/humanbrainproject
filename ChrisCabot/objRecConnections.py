DELAY = 1.0

INPUT_NEURONS_HEIGHT = 50
INPUT_NEURONS_WIDTH = 50

CA_HEIGHT = 10
CA_WIDTH = 10

#----------------setup connections-----------------
#setup CAs in the pyramid and stalactite net
def connectCA (CANum):
    CASize = CA_WIDTH*CA_HEIGHT
    CARow = CANum/5
    CACol = CANum%5
    synWeight = 3.0
    numSynapses = 10
    connector = []
    for cRow in range (0,CA_HEIGHT):
        for cCol in range (0,CA_WIDTH):
            fromNeuron=cRow*INPUT_NEURONS_WIDTH+cCol
            fromNeuron=fromNeuron+(CARow*CA_HEIGHT*INPUT_NEURONS_WIDTH)
            fromNeuron = fromNeuron + (CACol*CA_WIDTH)
            for cSynapse in range (0,numSynapses):
                toCol = cCol + cSynapse + 1
                toRow = cRow
                if (toCol>=CA_WIDTH) :
                    toCol = toCol - 10
                    toRow = toRow + 1
                if (toRow>=CA_HEIGHT) :
                    toRow = toRow - 10
                toNeuron=toRow*INPUT_NEURONS_WIDTH+toCol
                toNeuron=toNeuron+(CARow*CA_HEIGHT*INPUT_NEURONS_WIDTH)
                toNeuron = toNeuron + (CACol*CA_WIDTH)
                connector = connector + [(fromNeuron,toNeuron,synWeight,DELAY)]

    return connector

#add connections up 5 and over one both ways (15)
def connectHEdgeBottomToPyramid ():
    totalNeurons = INPUT_NEURONS_HEIGHT*INPUT_NEURONS_WIDTH
    synWeight = 10.0
    connector = []
    for cNeuron in range (INPUT_NEURONS_WIDTH*10,totalNeurons):
       fromRow = cNeuron/50
       fromCol = cNeuron % 50
       for toRow in range(fromRow-5,fromRow):
          for toCol in range (fromCol-1,fromCol + 2):
             toNeuron = toRow*50+toCol
             connector = connector + [(cNeuron,toNeuron,synWeight,DELAY)]
    return connector

#add connections down left (7:30) 5 and over one both ways (15)
def connectSEdgeLeftToPyramid ():
    totalNeurons = INPUT_NEURONS_HEIGHT*INPUT_NEURONS_WIDTH
    synWeight = 10.0
    connector = []
    for cNeuron in range (5,totalNeurons-(INPUT_NEURONS_WIDTH*10)):
       fromRow = cNeuron/50
       fromCol = cNeuron % 50
       if fromCol < 5:
          continue
       for rowChange in range(1,6):
          toRow = fromRow+rowChange
          for toCol in range (fromCol-rowChange-1,fromCol-rowChange + 2):
             toNeuron = toRow*50+toCol
             connector = connector + [(cNeuron,toNeuron,synWeight,DELAY)]
    return connector
 
#bedge
#add connections down right (4:30) 5 and over one both ways (15)
def connectBEdgeRightToPyramid ():
    totalNeurons = INPUT_NEURONS_HEIGHT*INPUT_NEURONS_WIDTH
    synWeight = 10.0
    connector = []
    for cNeuron in range (0,totalNeurons-(INPUT_NEURONS_WIDTH*10)):
       fromRow = cNeuron/50
       fromCol = cNeuron % 50
       if fromCol > 45:
          continue
       for rowChange in range(1,6):
          toRow = fromRow+rowChange
          for toCol in range (fromCol+rowChange-1,fromCol+rowChange + 2):
             toNeuron = toRow*50+toCol
             connector = connector + [(cNeuron,toNeuron,synWeight,DELAY)]
    return connector

#add connections down 5 and over one both ways (15)
def connectAndAngleToPyramid ():
    totalNeurons = INPUT_NEURONS_HEIGHT*INPUT_NEURONS_WIDTH
    synWeight = 10.0
    connector = []
    for cNeuron in range (0,totalNeurons-(INPUT_NEURONS_WIDTH*10)):
       fromRow = cNeuron/50
       fromCol = cNeuron % 50
       for toRow in range(fromRow+1,fromRow+6):
          for toCol in range (fromCol-1,fromCol + 2):
             toNeuron = toRow*50+toCol
             connector = connector + [(cNeuron,toNeuron,synWeight,DELAY)]
    return connector
       
#add connections up right (1:30) 5 and over one both ways (15)
def connectLessThanAngleToPyramid ():
    totalNeurons = INPUT_NEURONS_HEIGHT*INPUT_NEURONS_WIDTH
    synWeight = 10.0
    connector = []
    for cNeuron in range (INPUT_NEURONS_WIDTH*5,totalNeurons):
       fromRow = cNeuron/50
       fromCol = cNeuron % 50
       if fromCol > 45:
          continue
       for rowChange in range(-5,0):
          toRow = fromRow+rowChange
          for toCol in range (fromCol-rowChange-1,fromCol-rowChange + 2):
             toNeuron = toRow*50+toCol
             connector = connector + [(cNeuron,toNeuron,synWeight,DELAY)]
    return connector
   
#add connections up left (half ten) 5 and over one both ways (15)
def connectGreaterThanAngleToPyramid ():
    totalNeurons = INPUT_NEURONS_HEIGHT*INPUT_NEURONS_WIDTH
    synWeight = 10.0
    connector = []
    for cNeuron in range (INPUT_NEURONS_WIDTH*5,totalNeurons):
       fromRow = cNeuron/50
       fromCol = cNeuron % 50
       if fromCol < 6:
          continue
       for rowChange in range(-5,0):
          toRow = fromRow+rowChange
          for toCol in range (fromCol+rowChange-1,fromCol+rowChange + 2):
             toNeuron = toRow*50+toCol
             connector = connector + [(cNeuron,toNeuron,synWeight,DELAY)]
    return connector
   

#add connections down 5 and over one both ways (15)
def connectHEdgeTopToStalactite ():
    totalNeurons = INPUT_NEURONS_HEIGHT*INPUT_NEURONS_WIDTH
    synWeight = 10.0
    connector = []
    for cNeuron in range (0,totalNeurons-(INPUT_NEURONS_WIDTH*10)):
       fromRow = cNeuron/50
       fromCol = cNeuron % 50
       for toRow in range(fromRow+1,fromRow+6):
          for toCol in range (fromCol-1,fromCol + 2):
             toNeuron = toRow*50+toCol
             connector = connector + [(cNeuron,toNeuron,synWeight,DELAY)]
    return connector

#add connections up left (half ten) 5 and over one both ways (15)
def connectSEdgeRightToStalactite ():
    totalNeurons = INPUT_NEURONS_HEIGHT*INPUT_NEURONS_WIDTH
    synWeight = 10.0
    connector = []
    for cNeuron in range (INPUT_NEURONS_WIDTH*5,totalNeurons):
       fromRow = cNeuron/50
       fromCol = cNeuron % 50
       if fromCol < 6:
          continue
       for rowChange in range(-5,0):
          toRow = fromRow+rowChange
          for toCol in range (fromCol+rowChange-1,fromCol+rowChange + 2):
             toNeuron = toRow*50+toCol
             connector = connector + [(cNeuron,toNeuron,synWeight,DELAY)]
    return connector
   

#add connections up right (1:30) 5 and over one both ways (15)
def connectBEdgeLeftToStalactite():
    totalNeurons = INPUT_NEURONS_HEIGHT*INPUT_NEURONS_WIDTH
    synWeight = 10.0
    connector = []
    for cNeuron in range (INPUT_NEURONS_WIDTH*5,totalNeurons):
       fromRow = cNeuron/50
       fromCol = cNeuron % 50
       if fromCol > 45:
          continue
       for rowChange in range(-5,0):
          toRow = fromRow+rowChange
          for toCol in range (fromCol-rowChange-1,fromCol-rowChange + 2):
             toNeuron = toRow*50+toCol
             connector = connector + [(cNeuron,toNeuron,synWeight,DELAY)]
    return connector

#add connections up 5 and over one both ways (15)
def connectOrAngleToStalactite ():
    totalNeurons = INPUT_NEURONS_HEIGHT*INPUT_NEURONS_WIDTH
    synWeight = 10.0
    connector = []
    for cNeuron in range (INPUT_NEURONS_WIDTH*10,totalNeurons):
       fromRow = cNeuron/50
       fromCol = cNeuron % 50
       for toRow in range(fromRow-5,fromRow):
          for toCol in range (fromCol-1,fromCol + 2):
             toNeuron = toRow*50+toCol
             connector = connector + [(cNeuron,toNeuron,synWeight,DELAY)]
    return connector
