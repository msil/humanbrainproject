"""
Connections from the Retina to V1
The hEdgeBottom, sEdgeLeft, bEdgeRight, andAngle, lessThanAngle,
greaterThanAngle, HedgeTop, sEdgeRight, bEdgeLeft and orAngle
Connection Functions
"""

INPUT_NEURONS_HEIGHT = 50
INPUT_NEURONS_WIDTH = 50

DELAY = 1.0

#----------setup connections 6x6 on to HEdgeBottom (bottom of a solid)
def set6x6OnToHEdgeBottomConnections(Col,Row):
    weight = 4.0
    #don't input off top
    if (Row == 0): return []
    #don't output off bottom
    if (Row == INPUT_NEURONS_HEIGHT): return []
    connector = []
    toNeuron = (Row)*50+Col
    startAddCol = Col-2
    if (startAddCol < 0): startAddCol = 0
    endAddCol = Col+3
    if (endAddCol > INPUT_NEURONS_WIDTH): endAddCol = INPUT_NEURONS_WIDTH
    for addCol in range (startAddCol,endAddCol):
        fromNeuron = ((Row-1)*50)+addCol
        newConnector = [(fromNeuron, toNeuron, weight, DELAY)]
        connector = connector + newConnector
    return connector

#setup connections 6x6off to HEdgeBottom (bottom of a solid)
#2 on either side and self (5) up 
def set6x6OffToHEdgeBottomConnections(Col,Row):
    weight = 4.0
    #don't input off top
    if (Row == 0): return []
    #don't output off bottom
    if (Row == INPUT_NEURONS_HEIGHT): return []
    connector = []
    toNeuron = (Row)*50+Col
    startAddCol = Col-2
    if (startAddCol < 0): startAddCol = 0
    endAddCol = Col+3
    if (endAddCol > INPUT_NEURONS_WIDTH): endAddCol = INPUT_NEURONS_WIDTH
    for addCol in range (startAddCol,endAddCol):
        fromNeuron = ((Row+1)*50)+addCol
        newConnector = [(fromNeuron, toNeuron, weight, DELAY)]
        connector = connector + newConnector
    return connector

#setup connections 9x9off to HEdgeBottom (bottom of a solid)
#2 on either side and self (5) up one 
def set9x9OffToHEdgeBottomConnections(Col,Row):
    weight = 3.0
    #don't input off top
    if (Row == 0): return []
    #don't output off bottom
    if (Row == INPUT_NEURONS_HEIGHT): return []
    connector = []
    toNeuron = (Row)*50+Col
    startAddCol = Col-2
    if (startAddCol < 0): startAddCol = 0
    endAddCol = Col+3
    if (endAddCol > INPUT_NEURONS_WIDTH): endAddCol = INPUT_NEURONS_WIDTH
    for addCol in range (startAddCol,endAddCol):
        fromNeuron = ((Row+1)*50)+addCol
        newConnector = [(fromNeuron, toNeuron, weight, DELAY)]
        connector = connector + newConnector
    return connector

#----------setup connections 6x6 to SEdgeLeft (left of a solid)
#connections from self one to right then 3 above 2 below sloping
def set6x6OnToSEdgeLeftConnections(Col,Row):
    if (Row <3): return []
    if (Row > INPUT_NEURONS_HEIGHT -3): return []
    if (Col < 2): return []
    if (Col > INPUT_NEURONS_WIDTH -4): return []

    weight = 4.0
    inhibWeight = -4.0 # inhibit right sEdges well to the rigft
    toNeuron = (Row)*50+Col
    row1Off = (Row-3)*INPUT_NEURONS_WIDTH + Col+3
    row1Left = (Row-3)*INPUT_NEURONS_WIDTH + Col+2
    row1Right = (Row-3)*INPUT_NEURONS_WIDTH + Col+1
    row2Off = (Row-2)*INPUT_NEURONS_WIDTH + Col+2
    row2Left = (Row-2)*INPUT_NEURONS_WIDTH + Col+1
    row2Right = (Row-2)*INPUT_NEURONS_WIDTH + Col
    row3Off = (Row-1)*INPUT_NEURONS_WIDTH + Col+2
    row3Left = (Row-1)*INPUT_NEURONS_WIDTH + Col+1
    row3Right = (Row-1)*INPUT_NEURONS_WIDTH + Col
    ownRowOff = Row*INPUT_NEURONS_WIDTH + Col+1
    ownRowLeft = toNeuron
    ownRowRight = toNeuron - 1
    row5Off = (Row+1)*INPUT_NEURONS_WIDTH + Col+1
    row5Left = (Row+1)*INPUT_NEURONS_WIDTH + Col
    row5Right = (Row+1)*INPUT_NEURONS_WIDTH + Col-1
    row6Off = (Row+2)*INPUT_NEURONS_WIDTH + Col
    row6Left = (Row+2)*INPUT_NEURONS_WIDTH + Col-1
    row6Right = (Row+2)*INPUT_NEURONS_WIDTH + Col-2
    connector = [
        (row1Off, toNeuron, inhibWeight, DELAY),
        (row1Left, toNeuron, weight, DELAY),
        (row1Right, toNeuron, weight, DELAY),
        (row2Off, toNeuron, inhibWeight, DELAY),
        (row2Left, toNeuron, weight, DELAY),
        (row2Right, toNeuron, weight, DELAY),
        (row3Off, toNeuron, inhibWeight, DELAY),
        (row3Left, toNeuron, weight, DELAY),
        (row3Right, toNeuron, weight, DELAY),        
        (ownRowOff, toNeuron, inhibWeight, DELAY),
        (ownRowLeft, toNeuron, weight, DELAY),
        (ownRowRight, toNeuron, weight, DELAY),
        (row5Off, toNeuron, inhibWeight, DELAY),
        (row5Left, toNeuron, weight, DELAY),
        (row5Right, toNeuron, weight, DELAY),        
        (row6Off, toNeuron, inhibWeight, DELAY),
        (row6Left, toNeuron, weight, DELAY),
        (row6Right, toNeuron, weight, DELAY)]
    return connector


#----------setup connections BEdgeRight \(on right of a solid)
#setup connections 3x3 on to BEdgeRight (right of a solid)
#connections from self one to left then 3 above 2 below sloping
def set3x3OnAndOffToBEdgeRightConnections(Col,Row):
    if (Row < 3): return []
    if (Row > INPUT_NEURONS_HEIGHT -3): return []
    if (Col < 3): return []
    if (Col > INPUT_NEURONS_WIDTH -3): return []

    weight = 6.0
    inhibWeight = -4.0 # inhibit things well to the left
    toNeuron = (Row)*50+Col
    row1Off = (Row-3)*INPUT_NEURONS_WIDTH + Col-3
    row1Left = (Row-3)*INPUT_NEURONS_WIDTH + Col-2
    row1Right = (Row-3)*INPUT_NEURONS_WIDTH + Col-1
    row2Off = (Row-2)*INPUT_NEURONS_WIDTH + Col-2
    row2Left = (Row-2)*INPUT_NEURONS_WIDTH + Col-1
    row2Right = (Row-2)*INPUT_NEURONS_WIDTH + Col
    row3Off = (Row-1)*INPUT_NEURONS_WIDTH + Col-2
    row3Left = (Row-1)*INPUT_NEURONS_WIDTH + Col-1
    row3Right = (Row-1)*INPUT_NEURONS_WIDTH + Col
    ownRowOff = Row*INPUT_NEURONS_WIDTH + Col-1
    ownRowLeft = toNeuron
    ownRowRight = toNeuron + 1
    row5Off = (Row+1)*INPUT_NEURONS_WIDTH + Col-1
    row5Left = (Row+1)*INPUT_NEURONS_WIDTH + Col
    row5Right = (Row+1)*INPUT_NEURONS_WIDTH + Col+1
    row6Off = (Row+2)*INPUT_NEURONS_WIDTH + Col
    row6Left = (Row+2)*INPUT_NEURONS_WIDTH + Col+1
    row6Right = (Row+2)*INPUT_NEURONS_WIDTH + Col+2
    connector = [
        (row1Off, toNeuron, inhibWeight, DELAY),
        (row1Left, toNeuron, weight, DELAY),
        (row1Right, toNeuron, weight, DELAY),
        (row2Off, toNeuron, inhibWeight, DELAY),
        (row2Left, toNeuron, weight, DELAY),
        (row2Right, toNeuron, weight, DELAY),
        (row3Off, toNeuron, inhibWeight, DELAY),
        (row3Left, toNeuron, weight, DELAY),
        (row3Right, toNeuron, weight, DELAY),        
        (ownRowOff, toNeuron, inhibWeight, DELAY),
        (ownRowLeft, toNeuron, weight, DELAY),
        (ownRowRight, toNeuron, weight, DELAY),
        (row5Off, toNeuron, inhibWeight, DELAY),
        (row5Left, toNeuron, weight, DELAY),
        (row5Right, toNeuron, weight, DELAY),        
        (row6Off, toNeuron, inhibWeight, DELAY),
        (row6Left, toNeuron, weight, DELAY),
        (row6Right, toNeuron, weight, DELAY)]
    return connector

#setup connections 6x6 off to BEdgeRight (right of a solid)
#connections from self one to left then 3 above 2 below sloping
def set6x6OffToBEdgeRightConnections(Col,Row):
    if (Row < 3): return []
    if (Row > INPUT_NEURONS_HEIGHT -3): return []
    if (Col < 3): return []
    if (Col > INPUT_NEURONS_WIDTH -3): return []

    weight = 6.0
    inhibWeight = -4.0 # inhibit things well to the left
    toNeuron = (Row)*50+Col
    row1Off = (Row-3)*INPUT_NEURONS_WIDTH + Col-3
    row1Left = (Row-3)*INPUT_NEURONS_WIDTH + Col-2
    row1Right = (Row-3)*INPUT_NEURONS_WIDTH + Col-1
    row2Off = (Row-2)*INPUT_NEURONS_WIDTH + Col-2
    row2Left = (Row-2)*INPUT_NEURONS_WIDTH + Col-1
    row2Right = (Row-2)*INPUT_NEURONS_WIDTH + Col
    row3Off = (Row-1)*INPUT_NEURONS_WIDTH + Col-2
    row3Left = (Row-1)*INPUT_NEURONS_WIDTH + Col-1
    row3Right = (Row-1)*INPUT_NEURONS_WIDTH + Col
    ownRowOff = Row*INPUT_NEURONS_WIDTH + Col-1
    ownRowLeft = toNeuron
    ownRowRight = toNeuron + 1
    row5Off = (Row+1)*INPUT_NEURONS_WIDTH + Col-1
    row5Left = (Row+1)*INPUT_NEURONS_WIDTH + Col
    row5Right = (Row+1)*INPUT_NEURONS_WIDTH + Col+1
    row6Off = (Row+2)*INPUT_NEURONS_WIDTH + Col
    row6Left = (Row+2)*INPUT_NEURONS_WIDTH + Col+1
    row6Right = (Row+2)*INPUT_NEURONS_WIDTH + Col+2
    connector = [
        (row1Off, toNeuron, inhibWeight, DELAY),
        (row1Left, toNeuron, weight, DELAY),
        (row1Right, toNeuron, weight, DELAY),
        (row2Off, toNeuron, inhibWeight, DELAY),
        (row2Left, toNeuron, weight, DELAY),
        (row2Right, toNeuron, weight, DELAY),
        (row3Off, toNeuron, inhibWeight, DELAY),
        (row3Left, toNeuron, weight, DELAY),
        (row3Right, toNeuron, weight, DELAY),        
        (ownRowOff, toNeuron, inhibWeight, DELAY),
        (ownRowLeft, toNeuron, weight, DELAY),
        (ownRowRight, toNeuron, weight, DELAY),
        (row5Off, toNeuron, inhibWeight, DELAY),
        (row5Left, toNeuron, weight, DELAY),
        (row5Right, toNeuron, weight, DELAY),        
        (row6Off, toNeuron, inhibWeight, DELAY),
        (row6Left, toNeuron, weight, DELAY),
        (row6Right, toNeuron, weight, DELAY)]
    return connector


#----------setup connections 3x3 on to And Angle 
#connections from self to own and above row and on either side for 6 in total
#inhibit below
def set3x3OnToAndAngleConnections(Col,Row):
    if (Row > INPUT_NEURONS_HEIGHT -2): return []
    if (Row < 1): return []
    if (Col < 1): return []
    if (Col > INPUT_NEURONS_WIDTH-2): return []

    weight = 5.0
    inhibWeight = -5.0

    toNeuron = (Row*50)+Col
    connector = [(toNeuron-INPUT_NEURONS_WIDTH-1,toNeuron,inhibWeight,DELAY),
                 (toNeuron-INPUT_NEURONS_WIDTH,toNeuron,inhibWeight,DELAY),
                 (toNeuron-INPUT_NEURONS_WIDTH+1,toNeuron,inhibWeight,DELAY)
                 ]
    for addRow in range (Row,Row+2):
      for addCol in range (Col-1,Col+2):
        fromNeuron = ((addRow)*50)+addCol
        newConnector = [(fromNeuron, toNeuron, weight, DELAY)]
        connector = connector + newConnector
    return connector

#setup connections 6x6 on to And Angle 
#connections from self to own and above rows and on either side for 6 in total
#inhib two below on either side (60
def set6x6OnToAndAngleConnections(Col,Row):
    if (Row > INPUT_NEURONS_HEIGHT -2): return []
    if (Row < 2): return []
    if (Col < 1): return []
    if (Col > INPUT_NEURONS_WIDTH-2): return []

    weight = 4.0
    inhibWeight = -5.0

    toNeuron = (Row*50)+Col
    connector = []
    for addRow in range (Row,Row+2):
      for addCol in range (Col-1,Col+2):
        fromNeuron = ((addRow)*50)+addCol
        newConnector = [(fromNeuron, toNeuron, weight, DELAY)]
        connector = connector + newConnector
    for addRow in range (Row-2,Row-1):
      for addCol in range (Col-1,Col+2):
        fromNeuron = ((addRow)*50)+addCol
        newConnector = [(fromNeuron, toNeuron, inhibWeight, DELAY)]
        connector = connector + newConnector
    return connector

#setup connections 9x9 on to And Angle 
#connections from self to above two rows and on either side for 6 in total
#inhib own row
def set9x9OnToAndAngleConnections(Col,Row):
    if (Row > INPUT_NEURONS_HEIGHT -3): return []
    if (Col < 1): return []
    if (Col > INPUT_NEURONS_WIDTH-2): return []

    weight = 4.0
    inhibWeight = -8.0

    toNeuron = (Row*50)+Col
    connector = [(toNeuron-1,toNeuron,inhibWeight,DELAY),
                 (toNeuron,toNeuron,inhibWeight,DELAY),
                 (toNeuron+1,toNeuron,inhibWeight,DELAY) 
                 ]
    for addRow in range (Row+1,Row+3):
      for addCol in range (Col-1,Col+2):
        fromNeuron = ((addRow)*50)+addCol
        newConnector = [(fromNeuron, toNeuron, weight, DELAY)]
        connector = connector + newConnector
    
    return connector

#-----setup connections 3x3 on to Less Than Angle 
#connections from self and two left self and two two below (9) one inhib right of that. (3)
def set3x3OnToLessThanAngleConnections(Col,Row):
    if (Row > INPUT_NEURONS_HEIGHT-4): return [] #don't go off bottom
    if (Col < 2): return []     #don't go off left

    weight = 6.0
    toNeuron = (Row*50)+Col
    connector = []
    for addRow in range (Row,Row+3):
        fromNeuron = ((addRow)*50)+Col
        newConnectors = [(fromNeuron -1, toNeuron, weight, DELAY),
                        (fromNeuron, toNeuron, weight, DELAY)]
        connector = connector + newConnectors
    return connector

#connect 6x6off from self and one one right self and two below (6) one inhib right of that. (3)
def set6x6OffToLessThanAngleConnections(Col,Row):
    if (Row > INPUT_NEURONS_HEIGHT-4): return [] #don't go off bottom
    if (Col < 1): return []     #don't go off left
    if (Col > INPUT_NEURONS_WIDTH -2): return []     #don't go off right

    weight = 5.0
    inhibWeight = -10.0
    toNeuron = (Row*50)+Col
    connector = []
    for addRow in range (Row,Row+3):
        fromNeuron = ((addRow)*50)+Col
        newConnectors = [(fromNeuron-1, toNeuron, inhibWeight, DELAY),
                        (fromNeuron, toNeuron, weight, DELAY),
                        (fromNeuron+1, toNeuron, weight, DELAY)]
        connector = connector + newConnectors
    return connector

#connect 9x9on from one left self and two below(4) one inhib right of that(2).
def set9x9OnToLessThanAngleConnections(Col,Row):
    if (Row < 2): return [] #don't go off bottom
    if (Col < 1): return []     #don't go off left
    if (Col > INPUT_NEURONS_WIDTH-1): return []     #don't go off right

    weight = 6.0
    inhibWeight = -6.0
    toNeuron = (Row*50)+Col
    connector = []
    for addRow in range (Row-3,Row-1):
        fromNeuron = ((addRow)*50)+Col
        newConnectors = [(fromNeuron-1, toNeuron, inhibWeight, DELAY),
                        (fromNeuron, toNeuron, weight, DELAY),
                        (fromNeuron+1, toNeuron, weight, DELAY)]
        connector = connector + newConnectors
    return connector

#----------setup connections 3x3 on to Greater Than Angle 
#conns from self and two right above and below (9)
def set3x3OnToGreaterThanAngleConnections(Col,Row):
    if (Row < 1): return [] #don't go off top
    if (Row > INPUT_NEURONS_HEIGHT-2): return [] #don't go off bottom
    if (Col > INPUT_NEURONS_WIDTH-3): return [] #don't go off right

    weight = 9.0

    toNeuron = (Row*50)+Col
    connector =  []
    for addRow in range (Row-1,Row+2):
        fromNeuron = ((addRow)*50)+Col
        newConnector = [(fromNeuron, toNeuron, weight, DELAY),
                        (fromNeuron+1, toNeuron, weight, DELAY),
                        (fromNeuron+2, toNeuron, weight, DELAY)
                        ]
        connector = connector + newConnector
    return connector

#connect 6x6off connect two to right inhib self two rows above (4,2)
def set6x6OffToGreaterThanAngleConnections(Col,Row):
    if (Row > INPUT_NEURONS_HEIGHT-3): return []     #don't go off bottom
    if (Col < 2): return [] #don't go off left

    weight = 4.0
    inhibWeight = -9.0
    toNeuron = (Row*50)+Col
    connector =  []
    for addRow in range (Row+1,Row+3):
        fromNeuron = ((addRow)*50)+Col
        newConnector = [(fromNeuron, toNeuron, inhibWeight, DELAY),
                        (fromNeuron-1, toNeuron, weight, DELAY),
                        (fromNeuron-2, toNeuron, weight, DELAY)
                        ]
        connector = connector + newConnector
    return connector


#connect 9x9on from left two, inhib from self two rows above (4,2)
def set9x9OnToGreaterThanAngleConnections(Col,Row):
    if (Row < 3): return [] #don't go off top
    if (Col < 2): return [] #don't go off left

    weight = 4.0
    inhibWeight = -9.0

    toNeuron = (Row*50)+Col
    connector = []
    for addRow in range (Row-2,Row):
        fromNeuron = ((addRow)*50)+Col
        newConnectors = [(fromNeuron-2, toNeuron, weight, DELAY),
                        (fromNeuron-1, toNeuron, weight, DELAY),
                        (fromNeuron, toNeuron, inhibWeight, DELAY)]
        connector = connector + newConnectors
    return connector


#---------Connections for Stalactite V1 detectors
#----------setup connections 6x6off to HEdgeTop (top of a solid)
#one above and 2 on either side for 5
def set6x6OffToHEdgeTopConnections(Col,Row):
    weight = 10.0
    #don't output off bottom
    if (Row == INPUT_NEURONS_HEIGHT): return []
    connector = []
    toNeuron = (Row)*50+Col
    startAddCol = Col-2
    if (startAddCol < 0): startAddCol = 0
    endAddCol = Col+3
    if (endAddCol > INPUT_NEURONS_WIDTH): endAddCol = INPUT_NEURONS_WIDTH
    for addCol in range (startAddCol,endAddCol):
        fromNeuron = ((Row+1)*50)+addCol
        newConnector = [(fromNeuron, toNeuron, weight, DELAY)]
        connector = connector + newConnector
    return connector

#setup connections 9x9 off to HEdgeTop (top of a solid)
#positiive to same space, inhibit below
def set9x9OffToHEdgeTopConnections(Col,Row):
    weight = 5.0
    inhibWeight = -10
    #don't output off bottom
    if (Row == INPUT_NEURONS_HEIGHT): return []
    connector = []
    toNeuron = (Row)*50+Col
    fromNeuron = (Row*50)+Col
    connector = [(fromNeuron, toNeuron, weight, DELAY)]
    fromNeuron = ((Row+1)*50)+Col
    newConnector = [(fromNeuron, toNeuron, inhibWeight, DELAY)]
    connector = connector + newConnector
    return connector

#----------setup connections to SEdgeRight (right of a solid)
#set up connections from 3x3on to SEdgeRight\
#the right of a solid.  Have connections from three above, own and below row.
#Each has two excite on right and one inhib on left.  One right above one left
#below. (6,3)
def set3x3OnToSEdgeRightConnections(Col,Row):
    if (Row < 4): return [] #don't go off top
    if (Row > INPUT_NEURONS_HEIGHT-5): return [] #don't go off bottom
    if (Col < 4): return []     #don't go off left
    if (Col > INPUT_NEURONS_WIDTH-5): return []     #don't go off right

    weight = 5.0
    inhibWeight = -5.0
    toNeuron = (Row)*50+Col
    connector = []
    for addRow in range (-3,4):
        fromNeuron = ((Row+addRow)*50)+(Col-addRow)
        if (addRow == -3):
            fromNeuron = fromNeuron-1
        newConnectors = [(fromNeuron -1, toNeuron, inhibWeight, DELAY),
                        (fromNeuron, toNeuron, weight, DELAY),
                        (fromNeuron+1, toNeuron, weight, DELAY)]
        connector = connector + newConnectors
    return connector
    
#Set up connections from 3x3off to SEdgeRight\
#the right of a solid.  Have connections from above, own and below row.
#Each has two excite on right and one inhib on left.  One right above one left
#below. (6,3)
def set3x3OffToSEdgeRightConnections(Col,Row):
    if (Row < 2): return [] #don't go off top
    if (Row > INPUT_NEURONS_HEIGHT-3): return [] #don't go off bottom
    if (Col < 2): return []     #don't go off left
    if (Col > INPUT_NEURONS_WIDTH-3): return []     #don't go off right

    weight = 5.0
    inhibWeight = -5.0
    toNeuron = (Row)*50+Col
    connector = []
    for addRow in range (Row-1,Row+2):
        fromNeuron = ((addRow)*50)+Col
        if (addRow == Row +1):
                fromNeuron = fromNeuron-1
        else:
            if (addRow == Row -1):
                fromNeuron = fromNeuron+1
        newConnectors = [(fromNeuron -1, toNeuron, inhibWeight, DELAY),
                        (fromNeuron, toNeuron, weight, DELAY),
                        (fromNeuron+1, toNeuron, weight, DELAY)]
        connector = connector + newConnectors
    return connector
    
#6x6off to SEdgeRight the right of a solid.  Have connections from three above,
#own and below row. Each has two excite on right and one inhib on left.
#One right above one left below. (6,3)
def set6x6OffToSEdgeRightConnections(Col,Row):
    if (Row < 4): return [] #don't go off top
    if (Row > INPUT_NEURONS_HEIGHT-5): return [] #don't go off bottom
    if (Col < 4): return []     #don't go off left
    if (Col > INPUT_NEURONS_WIDTH-5): return []     #don't go off right

    weight = 4.0
    inhibWeight = -5.0
    toNeuron = (Row)*50+Col
    connector = []
    for addRow in range (-3,4):
        fromNeuron = ((Row+addRow)*50)+(Col-addRow)
        if (addRow == -3):
            fromNeuron = fromNeuron-1
        newConnectors = [(fromNeuron -1, toNeuron, inhibWeight, DELAY),
                        (fromNeuron, toNeuron, weight, DELAY),
                        (fromNeuron+1, toNeuron, weight, DELAY)]
        connector = connector + newConnectors
    return connector


#----------setup connections to BEdgeLeft \ (left of a solid)
#set up connections from 3x3on, and 3x3off to BEdgeLeft\
#the left of a solid.  Have connections from above, own and below row.
#Each has two excite on left and one inhib on right.  One left above one right
#below. (6,3)
def set3x3OnAndOffToBEdgeLeftConnections(Col,Row):
    if (Row < 2): return [] #don't go off top
    if (Row > INPUT_NEURONS_HEIGHT-3): return [] #don't go off bottom
    if (Col < 2): return []     #don't go off left
    if (Col > INPUT_NEURONS_WIDTH-3): return []     #don't go off right

    weight = 10.0
    inhibWeight = -5.0
    toNeuron = (Row)*50+Col
    connector = []
    for addRow in range (Row-1,Row+2):
        fromNeuron = ((addRow)*50)+Col
        if (addRow == Row +1):
                fromNeuron = fromNeuron+1
        else:
            if (addRow == Row -1):
                fromNeuron = fromNeuron-1
        newConnectors = [(fromNeuron -1, toNeuron, weight, DELAY),
                        (fromNeuron, toNeuron, weight, DELAY),
                        (fromNeuron+1, toNeuron, inhibWeight, DELAY)]
        connector = connector + newConnectors
    return connector

    
#6x6off to BEdgeLeft the left of a solid.  Have connections from above, own
#and below row. Each has two excite on left and one inhib on right.
#One left above one right below. (6,3)
def set6x6OffToBEdgeLeftConnections(Col,Row):
    if (Row < 2): return [] #don't go off top
    if (Row > INPUT_NEURONS_HEIGHT-3): return [] #don't go off bottom
    if (Col < 2): return []     #don't go off left
    if (Col > INPUT_NEURONS_WIDTH-3): return []     #don't go off right

    weight = 3.0
    inhibWeight = -5.0
    toNeuron = (Row)*50+Col
    connector = []
    for addRow in range (Row-1,Row+2):
        fromNeuron = ((addRow)*50)+Col
        if (addRow == Row +1):
                fromNeuron = fromNeuron+1
        else:
            if (addRow == Row -1):
                fromNeuron = fromNeuron-1
        newConnectors = [(fromNeuron -1, toNeuron, weight, DELAY),
                        (fromNeuron, toNeuron, weight, DELAY),
                        (fromNeuron+1, toNeuron, inhibWeight, DELAY)]
        connector = connector + newConnectors
    return connector

#----------setup connections 3x3 on to or angle
#Connections from left, self and right, from above,self and down one,
#inhib one more down(9,3)
def set3x3OnToOrAngleConnections(Col,Row):
    if (Row < 1): return [] #don't go off top
    if (Row > INPUT_NEURONS_HEIGHT-4): return [] #don't go off bottom
    if (Col < 1): return []     #don't go off left
    if (Col > INPUT_NEURONS_WIDTH-2): return []     #don't go off right
    
    weight = 7.0
    inhibWeight = -9.0
    toNeuron = (Row)*50+Col
    connector = []
    for addRow in range (Row-1,Row+3):
        fromNeuron = ((addRow)*50)+Col
        if (addRow == Row +2):
            connWeight = inhibWeight
        else:
            connWeight = weight
        newConnectors = [(fromNeuron -1, toNeuron, connWeight, DELAY),
                        (fromNeuron, toNeuron, connWeight, DELAY),
                        (fromNeuron+1, toNeuron, connWeight, DELAY)]
        connector = connector + newConnectors
    return connector


#----------setup connections 6x6 on to or angle
#Connections from left, self and right, from two above, inhib own row (6,3)
def set6x6OnToOrAngleConnections(Col,Row):
    if (Row < 1): return [] #don't go off top
    if (Row > INPUT_NEURONS_HEIGHT-3): return [] #don't go off bottom
    if (Col < 1): return []     #don't go off left
    if (Col > INPUT_NEURONS_WIDTH-2): return []     #don't go off right
    
    weight = 3.0
    inhibWeight = -3.0
    toNeuron = (Row)*50+Col
    connector = []
    for addRow in range (Row-2,Row+1):
        fromNeuron = ((addRow)*50)+Col
        if (addRow == Row):
            connWeight = inhibWeight
        else:
            connWeight = weight
        newConnectors = [(fromNeuron -1, toNeuron, connWeight, DELAY),
                        (fromNeuron, toNeuron, connWeight, DELAY),
                        (fromNeuron+1, toNeuron, connWeight, DELAY)]
        connector = connector + newConnectors
    return connector


#----------setup connections 9x9on to or angle
#Connections from left, self and right, from three above, inhib from one above (6,3)
def set9x9OnToOrAngleConnections(Col,Row):
    if (Row > INPUT_NEURONS_HEIGHT-4): return [] #don't go off bottom
    if (Col < 1): return []     #don't go off left
    if (Col > INPUT_NEURONS_WIDTH-2): return []     #don't go off right
    
    weight = 3.0
    inhibWeight = -3.0
    toNeuron = (Row)*50+Col
    connector = []
    for addRow in range (Row-3,Row):
        fromNeuron = ((addRow)*50)+Col
        if (addRow == Row-1):
            connWeight = inhibWeight
        else:
            connWeight = weight
        newConnectors = [(fromNeuron -1, toNeuron, connWeight, DELAY),
                        (fromNeuron, toNeuron, connWeight, DELAY),
                        (fromNeuron+1, toNeuron, connWeight, DELAY)]
        connector = connector + newConnectors
    return connector
