import main
from umqtt.robust import MQTTClient


class AdafruitIOClient:

    def __init__(self, ADAFRUIT_USERNAME: str, ADAFRUIT_IO_KEY: str):
        
            self.ADAFRUIT_USERNAME = ADAFRUIT_USERNAME
            self.ADAFRUIT_IO_KEY = ADAFRUIT_IO_KEY
            self.client = self.createClient()
            self.listOfFeeds = main.listOfFeeds
            

    
    def getMQQTFeed(self, feedName):
        
        
        for feed in self.listOfFeeds:
            if feed == feedName:
                
                ADAFRUIT_IO_FEEDNAME = feed
                return bytes('{:s}/feeds/{:s}'.format(self.ADAFRUIT_USERNAME, ADAFRUIT_IO_FEEDNAME), 'utf-8')
            
        return None
        
        
        
    
    def createClient(self):
        # create a random MQTT clientID
        random_num = int.from_bytes(os.urandom(3), 'little')
        mqtt_client_id = bytes('client_' + str(random_num), 'utf-8')

        # Adafruit IO URL
        ADAFRUIT_IO_URL = b'io.adafruit.com'

        # Convert parameters to bytes
        ADAFRUIT_USERNAME = bytes(self.ADAFRUIT_USERNAME, 'utf-8')
        ADAFRUIT_IO_KEY = bytes(self.ADAFRUIT_IO_KEY, 'utf-8')

        # create an MQTT client instance
        client = MQTTClient(client_id=mqtt_client_id,
                            server=ADAFRUIT_IO_URL,
                            user=ADAFRUIT_USERNAME,
                            password=ADAFRUIT_IO_KEY,
                            ssl=False)
        
        return client
    
    def connectToAdafruitIO(self):

            try:
                self.client.connect()
            except Exception:
                raise ConnectionError