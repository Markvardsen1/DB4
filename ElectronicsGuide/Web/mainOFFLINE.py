import csv
import os

from mainNEW import *


def run():

    iter = 0
    while True:
            
        temperature = tempSensor.getTemperature()
        OD = ODSensor.getOD()
        
        #PID controllers #TODO

        if iter == 200: #TODO Make iter large enough, so that it wont break the ping limit.
            
            #publishing data
            data = {
                "temp": temperature,
                "od": OD
                }
            
            writeToFile(data)
                        
            #displaying stuff on OLED
            #TODO make some nice OLED if time.
            #algaeConcentration = calculateAlageConcentration(OD, dimensionsOfTube) #TODO talk to others how this can be calculated. 
            #foodFlow = calculateFoodFlow(pumpFrequency, pumpDutyCyle, algaeConcentration) #TODO this would be nice to have
            
            try:
                web.connectToWifi(WIFI_SSID, WIFI_PASSWORD)
                client_OFFLINE = web.connectToServer(ADAFRUIT_USERNAME, ADAFRUIT_IO_KEY)
                publishFileToAdafruitIO(client_OFFLINE)
                mainONLINE.run(client_OFFLINE)
    
            except ZeroDivisionError:
                mainOFFLINE.run()

        iter+=1
        

def publishFileToAdafruitIO(client_OFFLINE):
    # Open the CSV file and read its contents
    with open(filePathToData, 'r', newline='') as file:
        reader = csv.DictReader(file)
        
        # Iterate through each row in the CSV file
        for row in reader:
            
            row = row
            # Publish the temperature and od values to Adafruit IO
            web.publish(row["temp"], ADAFRUIT_USERNAME, "tempTracker", client_OFFLINE)
            web.publish(row["od"], ADAFRUIT_USERNAME, "odTracker", client_OFFLINE)
    

def writeToFile(data: map):
    # Define the data folder and file path
    folder = filePathToData
    dataFile = os.path.join(folder, 'output.csv')

    # Create the data folder if it doesn't exist
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Check if the file exists and if it has a header
    file_exists = os.path.exists(dataFile)
    header_exists = False

    if file_exists:
        with open(dataFile, 'r', newline='') as file:
            reader = csv.reader(file)
            header = next(reader, None)
            if header == list(data.keys()):
                header_exists = True

    # Append the data to the CSV file
    with open(dataFile, 'a', newline='') as file:
        writer = csv.writer(file)
        
        if not header_exists:
            # Write the header which are the keys of the map
            header = data.keys()
            writer.writerow(header)
            
        # Write the values of the map
        values = data.values()
        writer.writerow(values)