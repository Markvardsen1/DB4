
import csv
import os


def _(data: map):
    # Define the data folder and file path
    folder = r'C:\Users\User\Desktop\DB4\DB4\ElectronicsGuide\Web\data'
    dataFile = os.path.join(folder, 'output.csv')

    # Create the data folder if it doesn't exist
    os.makedirs(folder, exist_ok=True)


    # Append the data to the CSV file
    with open(dataFile, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())

        # Write the data to the CSV file
        writer.writerow(data)


