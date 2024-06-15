import os


class DataPublisher:
    
    def __init__(self, onlineClient, filePathToData):
        self.onlineClient = onlineClient
        self.filePathToData = filePathToData
        

    
    def publishOnline(self, data, feedName): #TODO what happens if feedName is misspelled
        
        
        mqtt_feedname = self.onlineClient.getMQQTFeed(feedName)
    
        try:
                self.onlineClient.client.publish(mqtt_feedname,
                        bytes(data, 'utf-8'),
                        qos=0)
                
        except Exception:
                raise ConnectionError
            
            
    def publishOffline(self, data):
        # Define the data filePathToData and file path
        dataFile = os.path.join(self.filePathToData, 'output.txt')

        # Create the data directory if it doesn't exist
        if not os.path.exists(self.filePathToData):
            os.makedirs(self.filePathToData)

        # Append the data to the text file
        file = open(dataFile, 'a')
        # Write the key-value pairs in a single line separated by commas
        line = ",".join([f"{key}:{value}" for key, value in data.items()])
        file.write(line + "\n")
        file.close()  # Close the file after writing
        print(f"Written to file: {line}")        
            
            
    #TODO KEEP GOING HERE
    def publishFileToAdafruitIO(filePathToData, dataFileName):
        filePathToData = os.path.join(filePathToData, dataFileName)

        # Open the text file and read its contents
        file = open(filePathToData, 'r')
        lines = file.readlines()
        file.close()  # Close the file after reading
        
        # Iterate through each line in the text file
        for line in lines:
            # Parse the line into a dictionary
            row = dict(item.split(":") for item in line.strip().split(","))
            
            try:
                # Publish the temperature and od values to Adafruit IO
                # web.publish(row["temp"], adafruit_username, "tempTracker", client_offline)
                # web.publish(row["od"], adafruit_username, "odTracker", client_offline)
                print(f"Publishing temp: {row['temp']} and od: {row['od']}")
                pass
            except Exception:
                pass
                #TODO go back to run the offline version
            
        deleteFile(filePathToData)

def deleteFile(filePathToData):
    # Remove the text file after publishing
    if os.path.exists(filePathToData):
        try:
            os.remove(filePathToData)
            print(f"{filePathToData} has been removed.")
        except Exception as e:
            print(e)
            #TODO go back to run the offline version

