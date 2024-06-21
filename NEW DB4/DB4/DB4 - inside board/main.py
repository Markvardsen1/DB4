
from Systems.components import adafruitIOClient, wifiConnecter
from Systems.Software.MuscleFarmRunner import MuscleFarmRunner


def main():
    muscleFarmRunner = MuscleFarmRunner()

    try:
        wifiConnecter.connectToWifi()
        adafruitIOClient.connectToAdafruitIO()
        muscleFarmRunner.onlineMode()
        
    except ZeroDivisionError:
        
        muscleFarmRunner.offlineMode()