
import uos


class OfflineClient:
    
    def __init__(self, pathToDataFileFolder, dataFile):
        
        self.pathToDataFileFolder = pathToDataFileFolder
        self.dataFile = dataFile
        self.filePath = self.pathToDataFileFolder + "\\" +  self.dataFile
        
        if not self.doesDataExist(self.filePath):
            with open(self.filePath, 'w') as f:
                uos.mkdir(self.pathToDataFileFolder)

    def doesDataExist(self):
        try:
            uos.stat(self.filePath)
            return True
        except OSError:
            return False
    
    def deleteFile(self):
        if self.doesDataExist(self.filePath):
            try:
                uos.remove(self.filePath)
                print(f"{self.filePath} has been removed.")
            except Exception:
                pass




        
            


