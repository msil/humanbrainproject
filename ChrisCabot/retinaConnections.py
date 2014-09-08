"""
All 6 retinal detector connecting functions.
"""


INPUT_NEURONS_HEIGHT = 50
INPUT_NEURONS_WIDTH = 50

DELAY = 1.0


#----------setup connections for input to 1 3x3 on centre off surround detector
def set3x3OnConnections(X,Y):
    excite = 25.0
    inhib = -2.0
    retinaNumber = INPUT_NEURONS_WIDTH*(X)+ Y
    inhib1 = (INPUT_NEURONS_WIDTH*(X-1))+Y-1 
    inhib2 = (INPUT_NEURONS_WIDTH*(X-1))+Y
    inhib3 = (INPUT_NEURONS_WIDTH*(X-1))+Y+1
    inhib4 = (INPUT_NEURONS_WIDTH*(X))+Y-1
    inhib6 = (INPUT_NEURONS_WIDTH*(X))+Y+1
    inhib7 = (INPUT_NEURONS_WIDTH*(X+1))+Y-1
    inhib8 = (INPUT_NEURONS_WIDTH*(X+1))+Y
    inhib9 = (INPUT_NEURONS_WIDTH*(X+1))+Y+1
    connector = [
        (retinaNumber, retinaNumber, excite, DELAY),
        (inhib1, retinaNumber, inhib, DELAY),
        (inhib2, retinaNumber, inhib, DELAY),
        (inhib3, retinaNumber, inhib, DELAY),
        (inhib4, retinaNumber, inhib, DELAY),
        (inhib6, retinaNumber, inhib, DELAY),
        (inhib7, retinaNumber, inhib, DELAY),
        (inhib8, retinaNumber, inhib, DELAY),
        (inhib9, retinaNumber, inhib, DELAY),
        ]
    return connector;

#----------setup connections for input to 1 3x3 off centre on surround detector
def set3x3OffConnections(X,Y):
    excite = 4.0
    inhib = -25.0
    retinaNumber = INPUT_NEURONS_WIDTH*(X)+ Y
    surround1 = (INPUT_NEURONS_WIDTH*(X-1))+Y-1 
    surround2 = (INPUT_NEURONS_WIDTH*(X-1))+Y     
    surround3 = (INPUT_NEURONS_WIDTH*(X-1))+Y+1
    surround4 = (INPUT_NEURONS_WIDTH*(X))+Y-1
    surround6 = (INPUT_NEURONS_WIDTH*(X))+Y+1
    surround7 = (INPUT_NEURONS_WIDTH*(X+1))+Y-1
    surround8 = (INPUT_NEURONS_WIDTH*(X+1))+Y
    surround9 = (INPUT_NEURONS_WIDTH*(X+1))+Y+1
    connector = [
        (retinaNumber, retinaNumber, inhib, DELAY),
        (surround1, retinaNumber, excite, DELAY),
        (surround2, retinaNumber, excite, DELAY),
        (surround3, retinaNumber, excite, DELAY),
        (surround4, retinaNumber, excite, DELAY),
        (surround6, retinaNumber, excite, DELAY),
        (surround7, retinaNumber, excite, DELAY),
        (surround8, retinaNumber, excite, DELAY),
        (surround9, retinaNumber, excite, DELAY),
        ]
    return connector;

#----------setup connections for input to 1 6x6 on centre off surround detector
def set6x6OnConnections(X,Y):
    centreWeight = 7.0
    surroundWeight = -0.6
    retinaNumber = INPUT_NEURONS_WIDTH*(X)+ Y
    topLeftCentre = INPUT_NEURONS_WIDTH*(X)+ Y
    connector = [
        (topLeftCentre, retinaNumber, centreWeight, DELAY),
        (topLeftCentre+1, retinaNumber, centreWeight, DELAY),
        (topLeftCentre+INPUT_NEURONS_WIDTH, retinaNumber, centreWeight, DELAY),
        (topLeftCentre+INPUT_NEURONS_WIDTH+1,retinaNumber,centreWeight, DELAY)
        ]
    #rows above
    for inpRow in range (X-2,X):
      for inpCol in range (Y-2,Y+4):
          inpCell = (inpRow*INPUT_NEURONS_WIDTH) + inpCol
          newConnector = [(inpCell, retinaNumber, surroundWeight, DELAY)]
          connector = connector + newConnector
    #left
    newConnector = [
        (topLeftCentre-2, retinaNumber, surroundWeight, DELAY),
        (topLeftCentre-1, retinaNumber, surroundWeight, DELAY),
        (topLeftCentre+INPUT_NEURONS_WIDTH-2,retinaNumber,surroundWeight,DELAY),
        (topLeftCentre+INPUT_NEURONS_WIDTH-1,retinaNumber,surroundWeight,DELAY)
        ]
    connector = connector + newConnector
    #right
    newConnector = [
        (topLeftCentre+2, retinaNumber, surroundWeight, DELAY),
        (topLeftCentre+3, retinaNumber, surroundWeight, DELAY),
        (topLeftCentre+INPUT_NEURONS_WIDTH+2,retinaNumber,surroundWeight,DELAY),
        (topLeftCentre+INPUT_NEURONS_WIDTH+3,retinaNumber,surroundWeight,DELAY)
        ]
    connector = connector + newConnector
    #rows below
    for inpRow in range (X+2,X+4):
      for inpCol in range (Y-2,Y+4):
          inpCell = (inpRow*INPUT_NEURONS_WIDTH) + inpCol
          newConnector = [(inpCell, retinaNumber, surroundWeight, DELAY)]
          connector = connector + newConnector

    return connector;

#----------setup connections for input to 1 6x6 off centre on surround detector
def set6x6OffConnections(X,Y):
    centreWeight = -6.0
    surroundWeight = 1.0
    retinaNumber = INPUT_NEURONS_WIDTH*(X)+ Y
    topLeftCentre = INPUT_NEURONS_WIDTH*(X)+ Y
    connector = [
        (topLeftCentre, retinaNumber, centreWeight, DELAY),
        (topLeftCentre+1, retinaNumber, centreWeight, DELAY),
        (topLeftCentre+INPUT_NEURONS_WIDTH, retinaNumber, centreWeight, DELAY),
        (topLeftCentre+INPUT_NEURONS_WIDTH+1,retinaNumber,centreWeight, DELAY)
        ]
    #rows above
    for inpRow in range (X-2,X):
      for inpCol in range (Y-2,Y+4):
          inpCell = (inpRow*INPUT_NEURONS_WIDTH) + inpCol
          newConnector = [(inpCell, retinaNumber, surroundWeight, DELAY)]
          connector = connector + newConnector
    #left
    newConnector = [
        (topLeftCentre-2, retinaNumber, surroundWeight, DELAY),
        (topLeftCentre-1, retinaNumber, surroundWeight, DELAY),
        (topLeftCentre+INPUT_NEURONS_WIDTH-2,retinaNumber,surroundWeight,DELAY),
        (topLeftCentre+INPUT_NEURONS_WIDTH-1,retinaNumber,surroundWeight,DELAY)
        ]
    connector = connector + newConnector
    #right
    newConnector = [
        (topLeftCentre+2, retinaNumber, surroundWeight, DELAY),
        (topLeftCentre+3, retinaNumber, surroundWeight, DELAY),
        (topLeftCentre+INPUT_NEURONS_WIDTH+2,retinaNumber,surroundWeight,DELAY),
        (topLeftCentre+INPUT_NEURONS_WIDTH+3,retinaNumber,surroundWeight,DELAY)
        ]
    connector = connector + newConnector
    #rows below
    for inpRow in range (X+2,X+4):
      for inpCol in range (Y-2,Y+4):
          inpCell = (inpRow*INPUT_NEURONS_WIDTH) + inpCol
          newConnector = [(inpCell, retinaNumber, surroundWeight, DELAY)]
          connector = connector + newConnector

    return connector;


#----------setup connections for input to 1 9x9 on centre off surround detector
def set9x9OnConnections(X,Y):
    centreWeight = 3.0
    surroundWeight = -0.25
    retinaNumber = INPUT_NEURONS_WIDTH*(X)+ Y
    topLeftCentre = INPUT_NEURONS_WIDTH*(X)+ Y
    connector = [
        (topLeftCentre, retinaNumber, centreWeight, DELAY),
        (topLeftCentre+1, retinaNumber, centreWeight, DELAY),
        (topLeftCentre+2, retinaNumber, centreWeight, DELAY),
        (topLeftCentre+INPUT_NEURONS_WIDTH, retinaNumber, centreWeight, DELAY),
        (topLeftCentre+INPUT_NEURONS_WIDTH+1,retinaNumber,centreWeight, DELAY),
        (topLeftCentre+INPUT_NEURONS_WIDTH+2,retinaNumber,centreWeight, DELAY),
        (topLeftCentre+(INPUT_NEURONS_WIDTH*2),retinaNumber,centreWeight,DELAY),
        (topLeftCentre+(INPUT_NEURONS_WIDTH*2)+1,retinaNumber,centreWeight,DELAY),
        (topLeftCentre+(INPUT_NEURONS_WIDTH*2)+2,retinaNumber,centreWeight,DELAY),
        ]
    #rows above
    for inpRow in range (X-3,X):
      for inpCol in range (Y-3,Y+6):
          inpCell = (inpRow*INPUT_NEURONS_WIDTH) + inpCol
          newConnector = [(inpCell, retinaNumber, surroundWeight, DELAY)]
          connector = connector + newConnector
#    #left
    newConnector = [
        (topLeftCentre-3, retinaNumber, surroundWeight, DELAY),
        (topLeftCentre-2, retinaNumber, surroundWeight, DELAY),
        (topLeftCentre-1, retinaNumber, surroundWeight, DELAY),
        (topLeftCentre+INPUT_NEURONS_WIDTH-3,retinaNumber,surroundWeight,DELAY),
        (topLeftCentre+INPUT_NEURONS_WIDTH-2,retinaNumber,surroundWeight,DELAY),
        (topLeftCentre+INPUT_NEURONS_WIDTH-1,retinaNumber,surroundWeight,DELAY),
        (topLeftCentre+(INPUT_NEURONS_WIDTH*2)-3,retinaNumber,surroundWeight,DELAY),
        (topLeftCentre+(INPUT_NEURONS_WIDTH*2)-2,retinaNumber,surroundWeight,DELAY),
        (topLeftCentre+(INPUT_NEURONS_WIDTH*2)-1,retinaNumber,surroundWeight,DELAY)
        ]
    connector = connector + newConnector
    #right
    newConnector = [
        (topLeftCentre+3, retinaNumber, surroundWeight, DELAY),
        (topLeftCentre+4, retinaNumber, surroundWeight, DELAY),
        (topLeftCentre+5, retinaNumber, surroundWeight, DELAY),
        (topLeftCentre+INPUT_NEURONS_WIDTH+3,retinaNumber,surroundWeight,DELAY),
        (topLeftCentre+INPUT_NEURONS_WIDTH+4,retinaNumber,surroundWeight,DELAY),
        (topLeftCentre+INPUT_NEURONS_WIDTH+5,retinaNumber,surroundWeight,DELAY),
        (topLeftCentre+(INPUT_NEURONS_WIDTH*2)+3,retinaNumber,surroundWeight,DELAY),
        (topLeftCentre+(INPUT_NEURONS_WIDTH*2)+4,retinaNumber,surroundWeight,DELAY),
        (topLeftCentre+(INPUT_NEURONS_WIDTH*2)+5,retinaNumber,surroundWeight,DELAY)
        ]
    connector = connector + newConnector
    #rows below
    for inpRow in range (X+3,X+6):
      for inpCol in range (Y-3,Y+6):
          inpCell = (inpRow*INPUT_NEURONS_WIDTH) + inpCol
          newConnector = [(inpCell, retinaNumber, surroundWeight, DELAY)]
          connector = connector + newConnector

    return connector;

#----------setup connections for input to 1 9x9 off centre on surround detector
def set9x9OffConnections(X,Y):
    centreWeight = -2.5
    surroundWeight = 0.5
    retinaNumber = INPUT_NEURONS_WIDTH*(X)+ Y
    topLeftCentre = INPUT_NEURONS_WIDTH*(X)+ Y
    connector = [
        (topLeftCentre, retinaNumber, centreWeight, DELAY),
        (topLeftCentre+1, retinaNumber, centreWeight, DELAY),
        (topLeftCentre+2, retinaNumber, centreWeight, DELAY),
        (topLeftCentre+INPUT_NEURONS_WIDTH, retinaNumber, centreWeight, DELAY),
        (topLeftCentre+INPUT_NEURONS_WIDTH+1,retinaNumber,centreWeight, DELAY),
        (topLeftCentre+INPUT_NEURONS_WIDTH+2,retinaNumber,centreWeight, DELAY),
        (topLeftCentre+(INPUT_NEURONS_WIDTH*2),retinaNumber,centreWeight,DELAY),
        (topLeftCentre+(INPUT_NEURONS_WIDTH*2)+1,retinaNumber,centreWeight,DELAY),
        (topLeftCentre+(INPUT_NEURONS_WIDTH*2)+2,retinaNumber,centreWeight,DELAY),
        ]
    #rows above
    for inpRow in range (X-3,X):
      for inpCol in range (Y-3,Y+6):
          inpCell = (inpRow*INPUT_NEURONS_WIDTH) + inpCol
          newConnector = [(inpCell, retinaNumber, surroundWeight, DELAY)]
          connector = connector + newConnector
#    #left
    newConnector = [
        (topLeftCentre-3, retinaNumber, surroundWeight, DELAY),
        (topLeftCentre-2, retinaNumber, surroundWeight, DELAY),
        (topLeftCentre-1, retinaNumber, surroundWeight, DELAY),
        (topLeftCentre+INPUT_NEURONS_WIDTH-3,retinaNumber,surroundWeight,DELAY),
        (topLeftCentre+INPUT_NEURONS_WIDTH-2,retinaNumber,surroundWeight,DELAY),
        (topLeftCentre+INPUT_NEURONS_WIDTH-1,retinaNumber,surroundWeight,DELAY),
        (topLeftCentre+(INPUT_NEURONS_WIDTH*2)-3,retinaNumber,surroundWeight,DELAY),
        (topLeftCentre+(INPUT_NEURONS_WIDTH*2)-2,retinaNumber,surroundWeight,DELAY),
        (topLeftCentre+(INPUT_NEURONS_WIDTH*2)-1,retinaNumber,surroundWeight,DELAY)
        ]
    connector = connector + newConnector
    #right
    newConnector = [
        (topLeftCentre+3, retinaNumber, surroundWeight, DELAY),
        (topLeftCentre+4, retinaNumber, surroundWeight, DELAY),
        (topLeftCentre+5, retinaNumber, surroundWeight, DELAY),
        (topLeftCentre+INPUT_NEURONS_WIDTH+3,retinaNumber,surroundWeight,DELAY),
        (topLeftCentre+INPUT_NEURONS_WIDTH+4,retinaNumber,surroundWeight,DELAY),
        (topLeftCentre+INPUT_NEURONS_WIDTH+5,retinaNumber,surroundWeight,DELAY),
        (topLeftCentre+(INPUT_NEURONS_WIDTH*2)+3,retinaNumber,surroundWeight,DELAY),
        (topLeftCentre+(INPUT_NEURONS_WIDTH*2)+4,retinaNumber,surroundWeight,DELAY),
        (topLeftCentre+(INPUT_NEURONS_WIDTH*2)+5,retinaNumber,surroundWeight,DELAY)
        ]
    connector = connector + newConnector
    #rows below
    for inpRow in range (X+3,X+6):
      for inpCol in range (Y-3,Y+6):
          inpCell = (inpRow*INPUT_NEURONS_WIDTH) + inpCol
          newConnector = [(inpCell, retinaNumber, surroundWeight, DELAY)]
          connector = connector + newConnector

    return connector;


