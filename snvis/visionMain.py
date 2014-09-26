"""
The stub for  vision.  
"""

#imports for PyNN
from pyNN.utility import get_script_args, normalized_filename
from neo.io import PyNNTextIO

#imports for image reading
from PIL import Image

#NEAL files and functions
from nealParams import *
from visionClass import visionArea


#------Image Stuff
def openImageFile():
    try: 
        #im = Image.open("../data/lStal1.jpg")  
        im = Image.open("../data/rPyr1.jpg")  
        #im = Image.open("../data/rStal1.jpg")  
        #im = Image.open("../data/lPyr1.jpg")  
    except:
        print "fail to open image"

    im = im.crop((0,0,600,600))
    #print im.size

    #shrink it
    size = (INPSIZE,INPSIZE)
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
                pixelOn = (outRow*INPSIZE)+outColumn
                resultImageArray = resultImageArray + [pixelOn]

    return resultImageArray
        
#------------Main Body---------------
simulator_name = get_script_args(1)[0]  
exec("from pyNN.%s import *" % simulator_name)

setup(timestep=DELAY,min_delay=DELAY,max_delay=DELAY,db_name='if_cond.sqlite')

#----------------create neurons
vision = visionArea(simulator_name)
vision.allocateVisionNeurons()
    
#---------setup connections
vision.makeVisionSynapses()

#-------------------setup recording
vision.setVisionRecording()

#open image file
imagePixels = openImageFile()
#print imagePixels

#turn on the inputs
#set up clamped input from image
cell_params = {'tau_refrac' : 3.0, 'v_rest' : -65.0,
               'v_thresh' : -51.0,  'tau_syn_E'  : 2.0, 
               'tau_syn_I': 5.0,    'v_reset'    : -70.0, 
               'i_offset' : 0.1}

spikeTimes = [[i for i in range(7,int(SIM_LENGTH),5)],]
inputSource = Population(1, SpikeSourceArray, {'spike_times': spikeTimes})

#consider   One off won't run twice.
vision.setInput(imagePixels,inputSource)

run(SIM_LENGTH)

#--------------print results

vision.printVisionNets()

end()

