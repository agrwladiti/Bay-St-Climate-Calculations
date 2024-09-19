import pandas as pd
import os

filename = input("Enter the name of the excel file (without the .xlsx extension) you want to split into individual .csv files:\n")

excel_file = filename + ".xlsx"
all_sheets = pd.read_excel(excel_file, sheet_name=None)
sheets = all_sheets.keys()

if not os.path.exists(filename):
    os.makedirs(filename)

for sheet_name in sheets:
    sheet = pd.read_excel(excel_file, sheet_name=sheet_name)
    sheet.to_csv(filename + "/" + sheet_name + ".csv")
    print(sheet_name+".csv successfully extracted...")

print("\nProcess successfully completed! You can find your new .csv files in the new /" + filename + " folder.\n")