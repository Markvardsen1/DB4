import sys
import os

sensorValue : float = temp[-1]
referenceValue : int = 18
error : float = referenceValue - sensorValue


pgainValue = 1
igainValue = 1
dgainValue = 1

pidData = {
    'PGain' : pgainValue, # Should be inputs from adafruot IO
    'IGain' : igainValue,
    'DGain' : dgainValue,
}

actuatorValue : float = PIDUpdate(pidData, sensorValue : float, referenceValue : float)

errorsum : float = 0.0

def PIDUpdate(pidData : dict, sensorValue : float, referenceValue : float) -> float:
    (Pterm, Iterm, Dterm) : float = 0.0, 0.0, 0.0
    error : float = referenceValue - sensorValue
    
    Pterm = pidData['PGain'] * error
    
    errorsum = errorsum + error
    Iterm = pidData['IGain'] * errorsum
    
    difference : float = newestValue - previousValue
    Dterm = pidData['DGain'] * difference
    
    return (Pterm + Iterm + Dterm)


    
