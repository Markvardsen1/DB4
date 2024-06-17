import uos


class OfflineClient:
    
    def __init__(self):
        
        self.PATH_TO_DATAFILE_FOLDER = PATH_TO_DATAFILE_FOLDER
        self.DATAFILE = DATAFILE
        self.filePath = self.PATH_TO_DATAFILE_FOLDER + "\\" +  self.DATAFILE
        
        if not self.doesDataExist(self.filePath):
            with open(self.filePath, 'w') as f:
                uos.mkdir(self.PATH_TO_DATAFILE_FOLDER)

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




        
            


