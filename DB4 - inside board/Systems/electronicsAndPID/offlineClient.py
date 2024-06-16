
import os


class OfflineClient:
    
    def __init__(self, filePathToFolder, dataFile):
        
        self.filePathToFolder = filePathToFolder
        self.dataFile = os.path.join(self.filePathToFolder, dataFile)

        # Create the data directory if it doesn't exist
        if not os.path.exists(self.filePathToFolder):
            os.makedirs(self.filePathToFolder)

    def deleteFile(self): #TODO this should only delete file no?
        # Remove the text file after publishing
        if os.path.exists(self.filePathToFolder):
            try:
                os.remove(self.filePathToFolder)
                print(f"{self.filePathToFolder} has been removed.")
            except Exception as e:
                print(e)
                #TODO go back to run the offline version




        
            


