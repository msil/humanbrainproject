
from nealParams import *

def addNewConn(pre,post,weight):
    if (pre >= 0) and (pre <  neuronsPerSubnet):
        return [(pre,post,weight,DELAY)]
    else:
        return []

def get3x3OnExcite():
    weight = 15.0
    connectors = []
    for inpNeuron in range (0,neuronsPerSubnet):
        connectors = connectors + [(inpNeuron,inpNeuron,weight,DELAY)]

    return connectors

def get3x3OnInhib():
    weight = -3.0
    connectors = []
    for inpNeuron in range (0,neuronsPerSubnet):
        col = inpNeuron % INPSIZE
        if (col > 0):
            newConn = addNewConn(inpNeuron-INPSIZE-1,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron-1,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+INPSIZE-1,inpNeuron,weight)
            connectors = connectors + newConn
        newConn = addNewConn(inpNeuron-INPSIZE,inpNeuron,weight)
        connectors = connectors + newConn
        newConn = addNewConn(inpNeuron+INPSIZE,inpNeuron,weight)
        connectors = connectors + newConn
        if (col < (INPSIZE-1)):
            newConn = addNewConn(inpNeuron-INPSIZE+1,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+1,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+INPSIZE+1,inpNeuron,weight)
            connectors = connectors + newConn

    #print connectors
    return connectors


def get3x3OffInhib():
    weight = -15.0
    connectors = []
    for inpNeuron in range (0,neuronsPerSubnet):
        connectors = connectors + [(inpNeuron,inpNeuron,weight,DELAY)]

    return connectors

def get3x3OffExcite():
    weight = 1.5
    connectors = []
    for inpNeuron in range (0,neuronsPerSubnet):
        col = inpNeuron % INPSIZE
        if (col > 0):
            newConn = addNewConn(inpNeuron-INPSIZE-1,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron-1,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+INPSIZE-1,inpNeuron,weight)
            connectors = connectors + newConn
        newConn = addNewConn(inpNeuron-INPSIZE,inpNeuron,weight)
        connectors = connectors + newConn
        newConn = addNewConn(inpNeuron+INPSIZE,inpNeuron,weight)
        connectors = connectors + newConn
        if (col < (INPSIZE-1)):
            newConn = addNewConn(inpNeuron-INPSIZE+1,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+1,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+INPSIZE+1,inpNeuron,weight)
            connectors = connectors + newConn

    return connectors

def get6x6OnExcite():
    weight = 2.0
    connectors = []
    for inpNeuron in range (0,neuronsPerSubnet):
        col = inpNeuron % INPSIZE
        newConn = addNewConn(inpNeuron,inpNeuron,weight)
        connectors = connectors + newConn
        newConn = addNewConn(inpNeuron+INPSIZE,inpNeuron,weight)
        connectors = connectors + newConn
        if (col < (INPSIZE-1)):
            newConn = addNewConn(inpNeuron+1,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+INPSIZE+1,inpNeuron,weight)
            connectors = connectors + newConn


    #print connectors
    return connectors

def get6x6OnInhib():
    weight = -0.3
    connectors = []

    for inpNeuron in range (0,neuronsPerSubnet):
        col = inpNeuron % INPSIZE
        newConn = addNewConn(inpNeuron-(2*INPSIZE),inpNeuron,weight)
        connectors = connectors + newConn
        newConn = addNewConn(inpNeuron-INPSIZE,inpNeuron,weight)
        connectors = connectors + newConn
        newConn = addNewConn(inpNeuron+(2*INPSIZE),inpNeuron,weight)
        connectors = connectors + newConn
        newConn = addNewConn(inpNeuron+(3*INPSIZE),inpNeuron,weight)
        connectors = connectors + newConn
        if (col > 1):
            newConn = addNewConn(inpNeuron-(2*INPSIZE)-2,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron-INPSIZE-2,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron-2,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+INPSIZE-2,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(2*INPSIZE)-2,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(3*INPSIZE)-2,inpNeuron,weight)
            connectors = connectors + newConn
        if (col > 0):
            newConn = addNewConn(inpNeuron-(2*INPSIZE)-1,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron-INPSIZE-1,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron-1,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+INPSIZE-1,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(2*INPSIZE)-1,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(3*INPSIZE)-1,inpNeuron,weight)
            connectors = connectors + newConn
        if (col < (INPSIZE-1)): 
            newConn = addNewConn(inpNeuron-(2*INPSIZE)+1,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron-INPSIZE+1,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(2*INPSIZE)+1,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(3*INPSIZE)+1,inpNeuron,weight)
            connectors = connectors + newConn
        if (col < (INPSIZE-2)): 
            newConn = addNewConn(inpNeuron-(2*INPSIZE)+2,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron-INPSIZE+2,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+2,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(1*INPSIZE)+2,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(2*INPSIZE)+2,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(3*INPSIZE)+2,inpNeuron,weight)
            connectors = connectors + newConn
        if (col < (INPSIZE-3)):
            newConn = addNewConn(inpNeuron-(2*INPSIZE)+3,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron-INPSIZE+3,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+3,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+INPSIZE+3,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(2*INPSIZE)+3,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(3*INPSIZE)+3,inpNeuron,weight)
            connectors = connectors + newConn
    #print len(connectors)
    #print connectors
    return connectors


def get6x6OffInhib():
    weight = -2.0
    connectors = []
    for inpNeuron in range (0,neuronsPerSubnet):
        col = inpNeuron % INPSIZE
        newConn = addNewConn(inpNeuron,inpNeuron,weight)
        connectors = connectors + newConn
        newConn = addNewConn(inpNeuron+INPSIZE,inpNeuron,weight)
        connectors = connectors + newConn
        if (col < (INPSIZE-1)):
            newConn = addNewConn(inpNeuron+1,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+INPSIZE+1,inpNeuron,weight)
            connectors = connectors + newConn
    #print connectors
    return connectors


def get6x6OffExcite():
    weight = 0.2
    connectors = []

    for inpNeuron in range (0,neuronsPerSubnet):
        col = inpNeuron % INPSIZE
        newConn = addNewConn(inpNeuron-(2*INPSIZE),inpNeuron,weight)
        connectors = connectors + newConn
        newConn = addNewConn(inpNeuron-INPSIZE,inpNeuron,weight)
        connectors = connectors + newConn
        newConn = addNewConn(inpNeuron+(2*INPSIZE),inpNeuron,weight)
        connectors = connectors + newConn
        newConn = addNewConn(inpNeuron+(3*INPSIZE),inpNeuron,weight)
        connectors = connectors + newConn
        if (col > 1):
            newConn = addNewConn(inpNeuron-(2*INPSIZE)-2,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron-INPSIZE-2,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron-2,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+INPSIZE-2,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(2*INPSIZE)-2,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(3*INPSIZE)-2,inpNeuron,weight)
            connectors = connectors + newConn
        if (col > 0):
            newConn = addNewConn(inpNeuron-(2*INPSIZE)-1,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron-INPSIZE-1,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron-1,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+INPSIZE-1,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(2*INPSIZE)-1,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(3*INPSIZE)-1,inpNeuron,weight)
            connectors = connectors + newConn
        if (col < (INPSIZE-1)): 
            newConn = addNewConn(inpNeuron-(2*INPSIZE)+1,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron-INPSIZE+1,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(2*INPSIZE)+1,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(3*INPSIZE)+1,inpNeuron,weight)
            connectors = connectors + newConn
        if (col < (INPSIZE-2)): 
            newConn = addNewConn(inpNeuron-(2*INPSIZE)+2,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron-INPSIZE+2,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+2,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(1*INPSIZE)+2,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(2*INPSIZE)+2,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(3*INPSIZE)+2,inpNeuron,weight)
            connectors = connectors + newConn
        if (col < (INPSIZE-3)):
            newConn = addNewConn(inpNeuron-(2*INPSIZE)+3,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron-INPSIZE+3,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+3,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+INPSIZE+3,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(2*INPSIZE)+3,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(3*INPSIZE)+3,inpNeuron,weight)
            connectors = connectors + newConn
    #print len(connectors)
    #print connectors
    return connectors

def get9x9OnExcite():
    weight = 1.0
    connectors = []
    for inpNeuron in range (0,neuronsPerSubnet):
        col = inpNeuron % INPSIZE
        newConn = addNewConn(inpNeuron,inpNeuron,weight)
        connectors = connectors + newConn
        newConn = addNewConn(inpNeuron+INPSIZE,inpNeuron,weight)
        connectors = connectors + newConn
        newConn = addNewConn(inpNeuron+(2*INPSIZE),inpNeuron,weight)
        connectors = connectors + newConn
        if (col < (INPSIZE-1)):
            newConn = addNewConn(inpNeuron+1,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+INPSIZE+1,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(2*INPSIZE)+1,inpNeuron,weight)
            connectors = connectors + newConn
        if (col < (INPSIZE-2)):
            newConn = addNewConn(inpNeuron+2,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+INPSIZE+2,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(2*INPSIZE)+2,inpNeuron,weight)
            connectors = connectors + newConn

    #print connectors
    return connectors


def get9x9OnInhib():
    weight = -0.1
    connectors = []

    for inpNeuron in range (0,neuronsPerSubnet):
        col = inpNeuron % INPSIZE
        newConn = addNewConn(inpNeuron-(3*INPSIZE),inpNeuron,weight)
        connectors = connectors + newConn
        newConn = addNewConn(inpNeuron-(2*INPSIZE),inpNeuron,weight)
        connectors = connectors + newConn
        newConn = addNewConn(inpNeuron-INPSIZE,inpNeuron,weight)
        connectors = connectors + newConn
        newConn = addNewConn(inpNeuron+(3*INPSIZE),inpNeuron,weight)
        connectors = connectors + newConn
        newConn = addNewConn(inpNeuron+(4*INPSIZE),inpNeuron,weight)
        connectors = connectors + newConn
        newConn = addNewConn(inpNeuron+(5*INPSIZE),inpNeuron,weight)
        connectors = connectors + newConn
        if (col > 2):
            newConn = addNewConn(inpNeuron-(3*INPSIZE)-3,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron-(2*INPSIZE)-3,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron-INPSIZE-3,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron-3,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+INPSIZE-3,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(2*INPSIZE)-3,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(3*INPSIZE)-3,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(4*INPSIZE)-3,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(5*INPSIZE)-3,inpNeuron,weight)
            connectors = connectors + newConn
        if (col > 1):
            newConn = addNewConn(inpNeuron-(3*INPSIZE)-2,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron-(2*INPSIZE)-2,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron-INPSIZE-2,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron-2,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+INPSIZE-2,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(2*INPSIZE)-2,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(3*INPSIZE)-2,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(4*INPSIZE)-2,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(5*INPSIZE)-2,inpNeuron,weight)
            connectors = connectors + newConn
        if (col > 0):
            newConn = addNewConn(inpNeuron-(3*INPSIZE)-1,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron-(2*INPSIZE)-1,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron-INPSIZE-1,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron-1,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+INPSIZE-1,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(2*INPSIZE)-1,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(3*INPSIZE)-1,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(4*INPSIZE)-1,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(5*INPSIZE)-1,inpNeuron,weight)
            connectors = connectors + newConn
        if (col < (INPSIZE-1)): 
            newConn = addNewConn(inpNeuron-(3*INPSIZE)+1,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron-(2*INPSIZE)+1,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron-INPSIZE+1,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(3*INPSIZE)+1,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(4*INPSIZE)+1,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(5*INPSIZE)+1,inpNeuron,weight)
            connectors = connectors + newConn
        if (col < (INPSIZE-2)): 
            newConn = addNewConn(inpNeuron-(3*INPSIZE)+2,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron-(2*INPSIZE)+2,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron-INPSIZE+2,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(3*INPSIZE)+2,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(4*INPSIZE)+2,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(5*INPSIZE)+2,inpNeuron,weight)
            connectors = connectors + newConn
        if (col < (INPSIZE-3)):
            newConn = addNewConn(inpNeuron-(3*INPSIZE)+3,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron-(2*INPSIZE)+3,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron-INPSIZE+3,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+3,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+INPSIZE+3,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(2*INPSIZE)+3,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(3*INPSIZE)+3,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(4*INPSIZE)+3,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(5*INPSIZE)+3,inpNeuron,weight)
            connectors = connectors + newConn
        if (col < (INPSIZE-4)):
            newConn = addNewConn(inpNeuron-(3*INPSIZE)+4,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron-(2*INPSIZE)+4,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron-INPSIZE+4,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+4,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+INPSIZE+4,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(2*INPSIZE)+4,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(3*INPSIZE)+4,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(4*INPSIZE)+4,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(5*INPSIZE)+4,inpNeuron,weight)
            connectors = connectors + newConn
        if (col < (INPSIZE-5)):
            newConn = addNewConn(inpNeuron-(3*INPSIZE)+5,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron-(2*INPSIZE)+5,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron-INPSIZE+5,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+5,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+INPSIZE+5,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(2*INPSIZE)+5,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(3*INPSIZE)+5,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(4*INPSIZE)+5,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(5*INPSIZE)+5,inpNeuron,weight)
            connectors = connectors + newConn
    #print len(connectors)
    #print connectors
    return connectors

def get9x9OffInhib():
    weight = -1.0
    connectors = []
    for inpNeuron in range (0,neuronsPerSubnet):
        col = inpNeuron % INPSIZE
        newConn = addNewConn(inpNeuron,inpNeuron,weight)
        connectors = connectors + newConn
        newConn = addNewConn(inpNeuron+INPSIZE,inpNeuron,weight)
        connectors = connectors + newConn
        newConn = addNewConn(inpNeuron+(2*INPSIZE),inpNeuron,weight)
        connectors = connectors + newConn
        if (col < (INPSIZE-1)):
            newConn = addNewConn(inpNeuron+1,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+INPSIZE+1,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(2*INPSIZE)+1,inpNeuron,weight)
            connectors = connectors + newConn
        if (col < (INPSIZE-2)):
            newConn = addNewConn(inpNeuron+2,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+INPSIZE+2,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(2*INPSIZE)+2,inpNeuron,weight)
            connectors = connectors + newConn

    #print connectors
    return connectors

def get9x9OffExcite():
    weight = 0.2
    connectors = []

    for inpNeuron in range (0,neuronsPerSubnet):
        col = inpNeuron % INPSIZE
        newConn = addNewConn(inpNeuron-(3*INPSIZE),inpNeuron,weight)
        connectors = connectors + newConn
        newConn = addNewConn(inpNeuron-(2*INPSIZE),inpNeuron,weight)
        connectors = connectors + newConn
        newConn = addNewConn(inpNeuron-INPSIZE,inpNeuron,weight)
        connectors = connectors + newConn
        newConn = addNewConn(inpNeuron+(3*INPSIZE),inpNeuron,weight)
        connectors = connectors + newConn
        newConn = addNewConn(inpNeuron+(4*INPSIZE),inpNeuron,weight)
        connectors = connectors + newConn
        newConn = addNewConn(inpNeuron+(5*INPSIZE),inpNeuron,weight)
        connectors = connectors + newConn
        if (col > 2):
            newConn = addNewConn(inpNeuron-(3*INPSIZE)-3,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron-(2*INPSIZE)-3,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron-INPSIZE-3,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron-3,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+INPSIZE-3,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(2*INPSIZE)-3,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(3*INPSIZE)-3,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(4*INPSIZE)-3,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(5*INPSIZE)-3,inpNeuron,weight)
            connectors = connectors + newConn
        if (col > 1):
            newConn = addNewConn(inpNeuron-(3*INPSIZE)-2,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron-(2*INPSIZE)-2,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron-INPSIZE-2,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron-2,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+INPSIZE-2,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(2*INPSIZE)-2,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(3*INPSIZE)-2,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(4*INPSIZE)-2,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(5*INPSIZE)-2,inpNeuron,weight)
            connectors = connectors + newConn
        if (col > 0):
            newConn = addNewConn(inpNeuron-(3*INPSIZE)-1,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron-(2*INPSIZE)-1,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron-INPSIZE-1,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron-1,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+INPSIZE-1,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(2*INPSIZE)-1,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(3*INPSIZE)-1,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(4*INPSIZE)-1,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(5*INPSIZE)-1,inpNeuron,weight)
            connectors = connectors + newConn
        if (col < (INPSIZE-1)): 
            newConn = addNewConn(inpNeuron-(3*INPSIZE)+1,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron-(2*INPSIZE)+1,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron-INPSIZE+1,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(3*INPSIZE)+1,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(4*INPSIZE)+1,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(5*INPSIZE)+1,inpNeuron,weight)
            connectors = connectors + newConn
        if (col < (INPSIZE-2)): 
            newConn = addNewConn(inpNeuron-(3*INPSIZE)+2,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron-(2*INPSIZE)+2,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron-INPSIZE+2,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(3*INPSIZE)+2,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(4*INPSIZE)+2,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(5*INPSIZE)+2,inpNeuron,weight)
            connectors = connectors + newConn
        if (col < (INPSIZE-3)):
            newConn = addNewConn(inpNeuron-(3*INPSIZE)+3,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron-(2*INPSIZE)+3,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron-INPSIZE+3,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+3,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+INPSIZE+3,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(2*INPSIZE)+3,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(3*INPSIZE)+3,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(4*INPSIZE)+3,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(5*INPSIZE)+3,inpNeuron,weight)
            connectors = connectors + newConn
        if (col < (INPSIZE-4)):
            newConn = addNewConn(inpNeuron-(3*INPSIZE)+4,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron-(2*INPSIZE)+4,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron-INPSIZE+4,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+4,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+INPSIZE+4,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(2*INPSIZE)+4,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(3*INPSIZE)+4,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(4*INPSIZE)+4,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(5*INPSIZE)+4,inpNeuron,weight)
            connectors = connectors + newConn
        if (col < (INPSIZE-5)):
            newConn = addNewConn(inpNeuron-(3*INPSIZE)+5,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron-(2*INPSIZE)+5,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron-INPSIZE+5,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+5,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+INPSIZE+5,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(2*INPSIZE)+5,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(3*INPSIZE)+5,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(4*INPSIZE)+5,inpNeuron,weight)
            connectors = connectors + newConn
            newConn = addNewConn(inpNeuron+(5*INPSIZE)+5,inpNeuron,weight)
            connectors = connectors + newConn
    #print len(connectors)
    #print connectors
    return connectors




