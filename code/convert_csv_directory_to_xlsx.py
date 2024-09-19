import pandas as pd
import csv
import os
  
directory = input("\nPlease type in the name of the source directory from which your .csv files are located:\n\n")

files = os.listdir(directory)
numfiles = len(files)

for file in files:
    f = pd.read_csv(directory + "/" + file) 
    f.to_csv(directory + "/" + file, index=False) 


# Path to the directory containing CSV files
csv_directory = directory

# Get a list of all CSV files in the directory
csv_files = [file for file in os.listdir(csv_directory) if file.endswith('.csv')]

# Create a Pandas Excel writer using XlsxWriter as the engine
excel_writer = pd.ExcelWriter(str(directory) + '.xlsx', engine='xlsxwriter')

# Loop through each CSV file and read it into a Pandas DataFrame, then write to Excel
for csv_file in csv_files:
    csv_path = os.path.join(csv_directory, csv_file)
    df = pd.read_csv(csv_path)
    df.to_excel(excel_writer, sheet_name=os.path.splitext(csv_file)[0], index=False)

# Close the Pandas Excel writer to save the Excel file
excel_writer.close()

print("Conversion completed successfully!")