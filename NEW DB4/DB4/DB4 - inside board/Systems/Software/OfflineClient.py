import uos  # TODO CHANGE THIS


class OfflineClient:
    
    def __init__(self):
        
        from Systems.constants import DATAFILE, PATH_TO_DATAFILE_FOLDER
        
        self.PATH_TO_DATAFILE_FOLDER = PATH_TO_DATAFILE_FOLDER
        self.DATAFILE = DATAFILE
        self.filePath = self.PATH_TO_DATAFILE_FOLDER
        
        if not self.doesDataExist():
            with open(self.filePath, 'w') as f:
                uos.mkdir(self.PATH_TO_DATAFILE_FOLDER)

    def doesDataExist(self):
        try:
            uos.stat(self.filePath)
            return True
        except OSError:
            return False
    
    def deleteFile(self):
        if self.doesDataExist():
            try:
                uos.remove(self.filePath + "\\" + self.DATAFILE)
                print(f"{self.filePath} has been removed.")
<<<<<<< HEAD
            except Exception as e:
                print(e)
=======
            except Exception:
                pass
>>>>>>> ba198947ef0e347ee4d5b5b01c7c07ce979e0164
                print("failed to remove data file")




        
            


