import time

import uos
from Systems.Software.CommandHandler import handleCommand
from umqtt.robust import MQTTClient


class AdafruitIOClient:

        def __init__(self):
                from Systems.constants import (ADAFRUIT_IO_KEY,
                                               ADAFRUIT_USERNAME, commandFeed,
                                               listOfDataFeeds)
                
                print("command feed is called:" + commandFeed)
                self.ADAFRUIT_USERNAME = ADAFRUIT_USERNAME
                self.ADAFRUIT_IO_KEY = ADAFRUIT_IO_KEY
                
                
                self.client = self.createClient()
                self.listOfDataFeeds = listOfDataFeeds
                
                commandFeed = commandFeed.encode('utf-8')
                self.commandFeed = b"" + commandFeed
                self.mqtt_feedname = bytes('{:s}/feeds/{:s}'.format(self.ADAFRUIT_USERNAME, self.commandFeed), 'utf-8')

        def createClient(self):
        
                print("creating adafruit client")
                # create a random MQTT clientID
                random_num = int.from_bytes(uos.urandom(3), 'little')
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
                        raise ZeroDivisionError

        def checkCommand(self): #TODO FIX THIS ONE

        
                self.client.set_callback(self.cb)
                self.client.subscribe(self.mqtt_feedname)

                mqtt_feedname_get = bytes('{:s}/get'.format(self.mqtt_feedname), 'utf-8') 
                self.client.publish(mqtt_feedname_get, '\0')
                
                try:
                        while True:
                                print("checking....")
                                self.client.check_msg()
                                

                except Exception:
                        raise ZeroDivisionError


        def cb(self, topic, command):
                
                command = command.lower()
                handleCommand(command)
