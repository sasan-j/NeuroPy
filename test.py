from NeuroPy import NeuroPy
import logging

#object1=NeuroPy("COM6") #If port not given 57600 is automatically assumed
object1=NeuroPy("/dev/tty.BrainBandXL-SPPDev")
logging.basicConfig(level=logging.INFO)


def asic_eeg_callback(asic_eeg):
    "this function will be called everytime NeuroPy has a new value for attention"
    for x in asic_eeg:
        print (x, ' : ', asic_eeg[x])
    #do other stuff (fire a rocket), based on the obtained value of attention_value
    #do some more stuff
    return None

def attention_callback(attention_value):
    "this function will be called everytime NeuroPy has a new value for attention"
    logging.info("Value of attention is: %d",attention_value)
    #do other stuff (fire a rocket), based on the obtained value of attention_value
    #do some more stuff
    return None

def meditation_callback(meditation_value):
    "this function will be called everytime NeuroPy has a new value for attention"
    logging.info("Value of meditation is: %d",meditation_value)
    #do other stuff (fire a rocket), based on the obtained value of attention_value
    #do some more stuff
    return None

def lowBeta_callback(lowBeta_value):
    "this function will be called everytime NeuroPy has a new value for attention"
    logging.info("Value of lowBeta is: %d",lowBeta_value)
    #do other stuff (fire a rocket), based on the obtained value of attention_value
    #do some more stuff
    return None

def lowGamma_callback(lowGamma_value):
    "this function will be called everytime NeuroPy has a new value for attention"
    logging.info("Value of lowGamma is: %d",lowGamma_value)
    #do other stuff (fire a rocket), based on the obtained value of attention_value
    #do some more stuff
    return None

def rawValue_callback(rawValue_value):
    "this function will be called everytime NeuroPy has a new value for attention"
    logging.info("Value of rawValue is: %d",rawValue_value)
    #do other stuff (fire a rocket), based on the obtained value of attention_value
    #do some more stuff
    return None

def poorSignal_callback(poorSignal_value):
    "this function will be called everytime NeuroPy has a new value for attention"
    logging.info("Value of poorSignal is: %d",poorSignal_value)
    #do other stuff (fire a rocket), based on the obtained value of attention_value
    #do some more stuff
    return None

#set call back:
object1.setCallBack("attention",attention_callback)
object1.setCallBack("meditation",meditation_callback)

#set call back:
#object1.setCallBack("lowBeta",lowBeta_callback)

#set call back:
object1.setCallBack("lowGamma",lowGamma_callback)

#set call back:
object1.setCallBack("poorSignal",poorSignal_callback)
#object1.setCallBack("rawValue",rawValue_callback)


object1.setCallBack("asic_eeg", asic_eeg_callback)
#set call back:
#object1.setCallBack("blinkStrength",blinkStrength_callback)


object1.start()

while True:
    True
