class DataPublisher:
    
    def __init__(self, adafruitIOClient, offlineClient):
        
        self.adafruitIOClient = adafruitIOClient
        self.offlineClient = offlineClient


    def publishOnline(self, data:dict): #TODO what happens if feedName is misspelled
        
        
        def publishOnline_helper(self, data, feedName): #TODO what happens if feedName is misspelled
        
            mqtt_feedname = self.adafruitIOClient.getMQQTFeed(feedName)
        
            try:
                    self.adafruitIOClient.client.publish(mqtt_feedname,
                            bytes(data, 'utf-8'),
                            qos=0)
                
            except Exception:
                    raise ConnectionError
                
        for feedName in self.adafruitIOClient.LIST_OF_FEEDS:
                
                try:
                    self.publishOnline(data[feedName], feedName)
                
                except Exception:
                    pass
                    #TODO go back to run the offline version



    def publishOffline(self, data: dict):
    
        # Append the data to the text file
        file = open(self.offlineClient.client.DATAFILE, 'a')
        
        
        # Write the key-value pairs in a single line separated by commas
        line = ",".join([f"{key}:{value}" for key, value in data.items()])
        file.write(line + "\n")
        file.close()  # Close the file after writing
        print(f"Written to file: {line}")
            
            
    
    def importOfflineDataToOnline(self):
        
        # Open the text file and read its contents
        file = open(self.offlineClient.client.DATAFILE, 'r')
        lines = file.readlines()
        file.close()  # Close the file after reading
        
        # Iterate through each line in the text file
        for line in lines:
            
            
            # Parse the line into a dictionary
            data = dict(item.split(":") for item in line.strip().split(","))
            self.publishOnline(data)
            
            
        self.offlineClient.deleteFile()
        



