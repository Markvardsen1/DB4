
from Systems.constants import (adafruitIOClient, dataPublisher, offlineClient,
                               wifiConnecter)
from Systems.Software.MuscleFarmRunner import MuscleFarmRunner


def main():
    muscleFarmRunner = MuscleFarmRunner()

    try:
        wifiConnecter.connectToWifi()
        adafruitIOClient.connectToAdafruitIO()
        
        muscleFarmRunner.onlineMode()
        
        
    except ConnectionError:
        
        muscleFarmRunner.offlineMode()