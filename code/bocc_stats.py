import csv
import requests
import json

data = []
with open("boccdata.csv") as csvfile:
    reader = csv.reader(csvfile) # change contents to floats
    for row in reader: # each row is a list
        data.append(row)

canadian_banks = ["RBC", "TD", "Scotiabank", "Bank of Montreal", "CIBC"]

banks = dict()
companies = dict()

# bank-centric data 
for row in data[1:]:
    bank = str(row[0].strip())
    company = str(row[2].strip())

    loans2022 = float(row[9].replace(",","").replace(" ", "").replace("-", "").replace("#", "").replace("$", "") or 0)
    

    if bank not in banks:
        banks[bank] = {}
    if company not in banks[bank]:
        banks[bank][company] = 0
    banks[bank][company] += loans2022

def keep_cad(pair):
    key, value = pair
    if key in canadian_banks:
        return True  # keep pair in the filtered dictionary
    else:
        return False  # filter pair out of the dictionary
    
filtered_banks = dict(filter(keep_cad, banks.items()))

ry_top25 = sorted([(k, v) for k, v in filtered_banks["RBC"].items()],
    key=lambda x: x[1]
)[::-1][:25]
ry_top25_companies = list(zip(*ry_top25))[0]

td_top25 = sorted([(k, v) for k, v in filtered_banks["TD"].items()],
    key=lambda x: x[1]
)[::-1][:25]
td_top25_companies = list(zip(*ry_top25))[0]

bns_top25 = sorted([(k, v) for k, v in filtered_banks["Scotiabank"].items()],
    key=lambda x: x[1]
)[::-1][:25]
bns_top25_companies = list(zip(*ry_top25))[0]

bmo_top25 = sorted([(k, v) for k, v in filtered_banks["Bank of Montreal"].items()],
    key=lambda x: x[1]
)[::-1][:25]
bmo_top25_companies = list(zip(*ry_top25))[0]

cm_top25 = sorted([(k, v) for k, v in filtered_banks["CIBC"].items()], 
    key=lambda x: x[1]
)[::-1][:25]
cm_top25_companies = list(zip(*ry_top25))[0]

print(ry_top25_companies)