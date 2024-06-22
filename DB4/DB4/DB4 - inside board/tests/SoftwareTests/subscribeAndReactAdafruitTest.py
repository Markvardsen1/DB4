from Systems.components import adafruitIOClient, wifiConnecter

wifiConnecter.connectToWifi()
adafruitIOClient.connectToAdafruitIO()

#remember to write a commnad 
adafruitIOClient.checkCommand()