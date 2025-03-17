import time

from Systems import constants


class DataPublisher:
    
    def __init__(self, adafruitIOClient, offlineClient):
        
        self.adafruitIOClient = adafruitIOClient
        self.offlineClient = offlineClient

    
    def publishOnline(self, data : dict):
                
                def publishOnline_helper(key: str, data):
                        
                        key_bytes = key.encode('utf-8')
                        adafruitUsername = b"" + key_bytes
                        
                        mqtt_feedname = bytes('{:s}/feeds/{:s}'.format(self.adafruitIOClient.ADAFRUIT_USERNAME, adafruitUsername ), 'utf-8')
                        
                        
                        self.adafruitIOClient.client.publish(
                                        mqtt_feedname,
                                        bytes(str(data), 'utf-8'),
                                        qos=0)
                        
                        print("data published to" + key)
                

                for key in data:
                        
                        try:
                                print(key, data[key])
                                print(type(key), type(data[key]))
                                publishOnline_helper(key, data[key])
                        
                        except Exception as e:
                                print("cock")
                                print(e)

    def publishOffline(self, data: dict):
        
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
            if not (type(line) == type(None)):
                data = dict(item.split(":") for item in line.strip().split(","))
                
                print("this is data:")
                print(data)
                print(type(data))
                self.publishOnline(data)
            
        self.offlineClient.deleteFile()
        
    
