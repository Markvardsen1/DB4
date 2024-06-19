import os  # TODO CHANGE THIS


class OfflineClient:
    
    def __init__(self):
        
        from Systems.constants import DATAFILE, PATH_TO_DATAFILE_FOLDER
        
        self.PATH_TO_DATAFILE_FOLDER = PATH_TO_DATAFILE_FOLDER
        self.DATAFILE = DATAFILE
        self.filePath = self.PATH_TO_DATAFILE_FOLDER + "\\" +  self.DATAFILE
        
        if not self.doesDataExist(self.filePath):
            with open(self.filePath, 'w') as f:
                os.mkdir(self.PATH_TO_DATAFILE_FOLDER)

    def doesDataExist(self):
        try:
            os.stat(self.filePath)
            return True
        except OSError:
            return False
    
    def deleteFile(self):
        if self.doesDataExist(self.filePath):
            try:
                os.remove(self.filePath)
                print(f"{self.filePath} has been removed.")
            except Exception:
                pass




        
            


