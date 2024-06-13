import csv
import os

from mainNEW import *


def run():

    iter = 0
    while True:
        
        print(iter)
        
        temperature = temperatureSensor.getTemperature()
        OD = odSensor.getOD()
        #voltageLED = led.getVoltage #TODO
        
        #PID controllers #TODO

        if iter == 200: #TODO Make iter large enough, so that it wont break the ping limit.
            
            #publishing data
            
            data = {
                "temp": temperature
                #"od": OD
                #TODO add voltage of LED
                }
            
            writeToFile(data)
                        
            #displaying stuff on OLED
            oledScreen.display(data)
            
            
            try:
                web.connectToWifi(WIFI_SSID, WIFI_PASSWORD)
                client_OFFLINE = web.connectToServer(ADAFRUIT_USERNAME, ADAFRUIT_IO_KEY)
                publishFileToAdafruitIO(client_OFFLINE) #TODO this one does not work, "file is being used elsewhere"
                mainONLINE.run(client_OFFLINE)
    
            except ConnectionError:
                mainOFFLINE.run()

        iter+=1

def publishFileToAdafruitIO(filePathToData, dataFileName):
    
    filePathToData = os.path.join(filePathToData, dataFileName)

    # Open the CSV file and read its contents
    with open(filePathToData, 'r', newline='') as file:
        reader = csv.DictReader(file)
        
        # Iterate through each row in the CSV file
        for row in reader:
            
            try:
                # Publish the temperature and od values to Adafruit IO
                # web.publish(row["temp"], adafruit_username, "tempTracker", client_offline)
                # web.publish(row["od"], adafruit_username, "odTracker", client_offline)
                pass
            except Exception:
                pass
                #TODO go back to run the offline version
        
        deleteFile(filePathToData)
    


def deleteFile(filePathToData):
    # Remove the output.csv file after publishing
    
    print ("asdjfasdjflkasdfjsad")
    print( filePathToData)
    print(os.path.exists(filePathToData))
    
    if os.path.exists(filePathToData):
        try:
            os.remove(filePathToData)
            print(f"{filePathToData} has been removed.")
        
        except Exception as e:
            print(e)
                #TODO go back to run the offline version
                
    
    
def writeToFile(data: map, filePathToData):
    # Define the data filePathToData and file path
    dataFile = os.path.join(filePathToData, 'output.csv')

    # Create the data filePathToData if it doesn't exist
    if not os.path.exists(filePathToData):
        os.makedirs(filePathToData)

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



filePathToData = r'C:\Users\User\Desktop\pythonHyg'
dataFileName = "output.csv"

map = { "temp":5,"od":10}

#writeToFile(map, filePathToData)
publishFileToAdafruitIO(filePathToData, dataFileName)



