import time

from Systems import constants


class DataPublisher:
    
    def __init__(self, adafruitIOClient, offlineClient):
        
        self.adafruitIOClient = adafruitIOClient
        self.offlineClient = offlineClient

    
    
            


    def publishOnline(self, data : dict):
        
        def publishOnline_helper(key, data : int):
                    
                mqtt_feedname = bytes('{:s}/feeds/{:s}'.format(self.adafruitIOClient.ADAFRUIT_USERNAME, bytes (key)), 'utf-8')
                
                
                print(mqtt_feedname)
                
                self.adafruitIOClient.client.publish(mqtt_feedname,
                                bytes(data, 'utf-8'),
                                qos=0)
                
                print("data published to" + key)
                                    
        for key in data:
            
                try:
                    publishOnline_helper(key[data],)
                
                except Exception:
                    print("failed to publish data")
                    pass



    def publishOffline(self, data: dict):
        
        self.lastPublish = time.time()
        self.nextPublish = self.lastPublish + constants.secBetweenPublishes + self.publishDelay
        
        # Append the data to the text file
        file = open(self.offlineClient.DATAFILE, 'a')
        
        print("file")
        
        # Write the key-value pairs in a single line separated by commas
        line = ",".join([f"{key}:{value}" for key, value in data.items()])
        file.write(line + "\n")
        file.close()  # Close the file after writing
        print(f"Written to file: {line}")
            
            
    
    def importOfflineDataToOnline(self):
        
        # Open the text file and read its contents
        file = open(self.offlineClient.DATAFILE, 'r')
        lines = file.readlines()
        file.close()  # Close the file after reading
        
        # Iterate through each line in the text file
        for line in lines:
            
            
            # Parse the line into a dictionary
            data = dict(item.split(":") for item in line.strip().split(","))
            self.publishOnline(data)
            
            
        self.offlineClient.deleteFile()
        
    
    def testOfflinePublishData(self):
        data = {
        "Temperature": "N",
        "Humidity": "45%",
        "Pressure": "1013hPa",
        "Altitude": "500m",
        "Wind Speed": "I",
    }
        self.publishOffline(data)
        
    def testOnlinePublishData(self):
        
        data = {
        "temp": 5,
        "od": 6,
    }
        self.publishOnline(data)
