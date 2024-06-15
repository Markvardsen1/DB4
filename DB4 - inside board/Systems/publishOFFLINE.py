
import os


def publishFileToAdafruitIO(filePathToData, dataFileName):
    filePathToData = os.path.join(filePathToData, dataFileName)

    # Open the text file and read its contents
    file = open(filePathToData, 'r')
    lines = file.readlines()
    file.close()  # Close the file after reading
    
    # Iterate through each line in the text file
    for line in lines:
        # Parse the line into a dictionary
        row = dict(item.split(":") for item in line.strip().split(","))
        
        try:
            # Publish the temperature and od values to Adafruit IO
            # web.publish(row["temp"], adafruit_username, "tempTracker", client_offline)
            # web.publish(row["od"], adafruit_username, "odTracker", client_offline)
            print(f"Publishing temp: {row['temp']} and od: {row['od']}")
            pass
        except Exception:
            pass
            #TODO go back to run the offline version
        
    deleteFile(filePathToData)

def deleteFile(filePathToData):
    # Remove the text file after publishing
    if os.path.exists(filePathToData):
        try:
            os.remove(filePathToData)
            print(f"{filePathToData} has been removed.")
        except Exception as e:
            print(e)
            #TODO go back to run the offline version

def writeToFile(data: dict, filePathToData):
    # Define the data filePathToData and file path
    dataFile = os.path.join(filePathToData, 'output.txt')

    # Create the data directory if it doesn't exist
    if not os.path.exists(filePathToData):
        os.makedirs(filePathToData)

    # Append the data to the text file
    file = open(dataFile, 'a')
    # Write the key-value pairs in a single line separated by commas
    line = ",".join([f"{key}:{value}" for key, value in data.items()])
    file.write(line + "\n")
    file.close()  # Close the file after writing
    print(f"Written to file: {line}")

