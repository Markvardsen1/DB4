import time

import network


class WifiConnecter:
    
    def __init__(self):
        from Systems.constants import WIFI_PASSWORD, WIFI_SSID
        self.WIFI_SSID = WIFI_SSID
        self.WIFI_PASSWORD = WIFI_PASSWORD
        
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
        print("attempting to connect to wifi")
        while not wifi.isconnected() and attempt_count < MAX_ATTEMPTS:
            print("attempting to connect...")
            attempt_count += 1
            time.sleep(0.5)

        if attempt_count == MAX_ATTEMPTS:
            print("no connection")
            raise ZeroDivisionError
        
        print("connected :DDD")
        
    def testWifiConnecter(self):
        
        print("Running wifi test")
        try:
            print("Trying to connect to wifi...")
            self.connectToWifi()
            print("Connected :DDD")
            
        except ZeroDivisionError:
            print("couldnt connect")
        
        
        
