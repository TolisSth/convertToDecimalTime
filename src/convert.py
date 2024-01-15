# Author: Apostolos Halis 2024 
from datetime import datetime, timedelta

divideBy = 0.864 # This is the value that represents how many standard seconds is a decimal time second

# in general SIs means SI (Système International) seconds
def getSeconds(SIs): 
    return int(SIs / divideBy)

def getMinutes(SIs): 
    seconds = SIs / divideBy 
    return int(seconds / 100) 

def getHours(SIs): 
    seconds = SIs / divideBy
    minutes = getMinutes(seconds)
    return int(minutes / 100) 

def getTimeNow(): 
    hoursMinsSecs = [] # We return everything in this function

    timeNow = datetime.now() 
    startOfDay = (timeNow - timeNow.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()

    secondsFromMidnight = int(startOfDay) 
    print(secondsFromMidnight)
     
    # Convert & add to returning array
    hours = getHours(secondsFromMidnight) 
    hoursMinsSecs.append(hours) 
 
    minutes = getMinutes(secondsFromMidnight) 
    hoursMinsSecs.append(minutes)

    seconds = getSeconds(secondsFromMidnight) 
    hoursMinsSecs.append(seconds)

    return hoursMinsSecs
