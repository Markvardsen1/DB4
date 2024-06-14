
import time

import network


class OnlineConnecter:
    
    def __init__(self, WIFI_SSID, WIFI_PASSWORD, ADAFRUIT_USERNAME: str, ADAFRUIT_IO_KEY: str):

        self.WIFI_SSID = WIFI_SSID
        self.WIFI_PASSWORD = WIFI_PASSWORD
        self.ADAFRUIT_USERNAME = ADAFRUIT_USERNAME
        self.ADAFRUIT_IO_KEY = ADAFRUIT_IO_KEY
        
    def connectToWifi(self):
    
        # turn off the WiFi Access Point
        ap_if = network.WLAN(network.AP_IF)
        ap_if.active(False)

        # connect the device to the WiFi network
        wifi = network.WLAN(network.STA_IF)
        wifi.active(True)
        wifi.connect(self.WIFI_SSID, self.WIFI_PASSWORD)

        # wait until the device is connected to the WiFi network
        MAX_ATTEMPTS = 20
        attempt_count = 0
        while not wifi.isconnected() and attempt_count < MAX_ATTEMPTS:
            attempt_count += 1
            time.sleep(1)

        if attempt_count == MAX_ATTEMPTS:
            raise ConnectionError
        
    def connectToServer(self, ADAFRUIT_USERNAME: str, ADAFRUIT_IO_KEY: str):

        # create a random MQTT clientID
        random_num = int.from_bytes(os.urandom(3), 'little')
        mqtt_client_id = bytes('client_' + str(random_num), 'utf-8')

        # Adafruit IO URL and feed name
        ADAFRUIT_IO_URL = b'io.adafruit.com'
        ADAFRUIT_IO_FEEDNAME = b'freeHeap'

        # Convert parameters to bytes
        ADAFRUIT_USERNAME = bytes(ADAFRUIT_USERNAME, 'utf-8')
        ADAFRUIT_IO_KEY = bytes(ADAFRUIT_IO_KEY, 'utf-8')

        # create an MQTT client instance
        client = MQTTClient(client_id=mqtt_client_id,
                            server=ADAFRUIT_IO_URL,
                            user=ADAFRUIT_USERNAME,
                            password=ADAFRUIT_IO_KEY,
                            ssl=False)
        try:
            client.connect()
        except Exception:
            raise ConnectionError
        
        return client
    
    
    
    
