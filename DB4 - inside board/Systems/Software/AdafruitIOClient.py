import os

from main import *
from Systems.CommandHandler import handleCommand
from umqtt.robust import MQTTClient


class AdafruitIOClient: #TODO consider remaking this class, the structure is kinda weird

    def __init__(self):
        
            self.ADAFRUIT_USERNAME = ADAFRUIT_USERNAME
            self.ADAFRUIT_IO_KEY = ADAFRUIT_IO_KEY
            self.client = self.createClient()
            
            self.listOfFeeds = listOfFeeds
            self.commandFeed = commandFeed

    def checkCommand(self):
            
        mqtt_feedname = bytes('{:s}/feeds/{:s}'.format(self.ADAFRUIT_USERNAME, self.commandFeed), 'utf-8')
        
        self.client.set_callback(self.cb)
        self.client.subscribe(mqtt_feedname)

        mqtt_feedname_get = bytes('{:s}/get'.format(mqtt_feedname), 'utf-8')
        self.client.publish(mqtt_feedname_get, '\0')
            
            
        try:
                self.client.check_msg() #TODO: maybe we have to do wait.msg instead... also code is different when using "check" vs "wait"
        
        except Exception:
                raise ConnectionError
            
            
    def cb(self, topic, msg):
            msg = msg.lower()
            handleCommand(msg)


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


