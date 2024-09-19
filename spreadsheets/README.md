### README for `spreadsheets/`

#### Overview

This directory contains CSV and XLSX files that were generated using the Bloomberg Terminal. These files contain hard-coded data (i.e., no dynamic Bloomberg functions), making the data accessible and static for further analysis. There is also a consolidated Excel file that merges all individual CSVs for convenience.

#### Files

1. **CSV files (in AllCompanyData)**

   - These CSV files represent the raw data exported from Bloomberg Terminal. Each file corresponds to a specific company or set of data points such as GHG emissions or financial metrics.
   - **Usage**: You can open and analyze these CSV files in any spreadsheet application like Microsoft Excel, Google Sheets, or Python.

2. **Consolidated XLSX file (AllCompanyData.xlsx)**

   - **Description**: A single Excel workbook consolidating the individual CSV files found in this directory. This file was created using the `convert_csv_directory_to_xlsx.py` script from the `code/` directory.

   This sheet contains pertinent financial and emissions data for all the companies that went into consideration for this assessment. The colums on each company's sheet are consistent with the following headers (from A to AC):

   TICKER + FINANCIAL YEAR: This refers to the ticker symbol along with the financial year to specify the period the data pertains to.
   GHG SCOPE 1: Scope 1 greenhouse gas emissions refer to direct emissions from sources that are owned or controlled by the reporting entity, such as emissions from combustion in owned or controlled boilers, furnaces, vehicles, etc.
   GHG SCOPE 2 LOCATION BASED: Scope 2 greenhouse gas emissions refer to indirect emissions associated with the generation of electricity, heating, cooling, or steam purchased and consumed by the reporting entity. Location-based emissions refer to emissions associated with the average emissions intensity of grid electricity consumed in a particular geographical area.
   GHG SCOPE 3: Scope 3 greenhouse gas emissions refer to all other indirect emissions that occur in the value chain of the reporting entity, including both upstream and downstream emissions from activities such as business travel, employee commuting, supply chain activities, etc.
   SCOPE 3-1 PURCHASED GOODS AND SERVICES: This refers to Scope 3 emissions from purchased goods and services, which includes emissions associated with the production of goods and services purchased by the reporting entity.
   SCOPE 3-2 CAPITAL GOODS: Scope 3 emissions from capital goods refer to emissions associated with the production of goods and services purchased by the reporting entity.
   SCOPE 3-3 FUEL AND ENERGY RELATED ACTIVITIES: These are Scope 3 emissions related to fuel and energy-related activities, such as emissions associated with the extraction, production, and transportation of fuels and energy used by the reporting entity.
   SCOPE 3-4 UPSTREAM TRANS DIST: This refers to upstream transportation and distribution emissions, which are Scope 3 emissions associated with the transportation and distribution of goods and services upstream in the value chain of the reporting entity.
   SCOPE 3-5 WASTE GENERATED IN OPERATIONS: These are Scope 3 emissions related to waste generated during the operations of the reporting entity.
   SCOPE 3-6 BUSINESS TRAVEL EMISSIONS: Scope 3 emissions from business travel refer to emissions associated with travel undertaken for business purposes by employees of the reporting entity.
   SCOPE 3-7 EMPLOYEE COMMUTING: Scope 3 emissions from employee commuting refer to emissions associated with the travel of employees to and from their workplaces.
   SCOPE 3-8 UPSTREAM LEASED ASSETS: These are Scope 3 emissions associated with leased assets used by the reporting entity.
   SCOPE 3-9 DOWNSTRM TRANSPORATION AND DISTRIBUTION: Downstream transportation and distribution emissions are Scope 3 emissions associated with the transportation and distribution of goods and services downstream in the value chain of the reporting entity.
   SCOPE 3-10 PROCESSING OF SOLD PRODUCTS: These are Scope 3 emissions associated with the processing of products sold by the reporting entity.
   SCOPE 3-11 USE OF SOLD PRODUCTS: Scope 3 emissions from the use of sold products refer to emissions associated with the use of products sold by the reporting entity by its customers.
   SCOPE 3-12 END-OF-LIFE TREATMENT OF SOLD PRODUCTS: These are Scope 3 emissions associated with the end-of-life treatment of products sold by the reporting entity, such as recycling, disposal, etc.
   SCOPE 3-13 DOWNSTRM LEASED ASSETS: Downstream leased assets refer to leased assets used by the reporting entity that contribute to Scope 3 emissions downstream in its value chain.
   SCOPE 3-14 FRANCHISES: Scope 3 emissions from franchises refer to emissions associated with the activities of franchises owned or operated by the reporting entity.
   SCOPE 3-15 INVESTMENTS: These are Scope 3 emissions associated with investments made by the reporting entity, such as emissions from the operations of investee companies.
   SCOPE 3 EMISSIONS OTHER: This likely refers to other Scope 3 emissions not covered by the specific categories listed above.
   ENTERPRISE VALUE INCLUDING CASH: Enterprise value represents the total value of a company, including its market capitalization, debt, and cash or cash equivalents.
   ANNUAL REVENUE: Annual revenue is the total income generated by a company from its operations during a specific financial year.
   HISTORICAL MARKET CAP: Historical market capitalization represents the total market value of a company's outstanding shares at a specific point in time.
   NAME: Name refers to the name of the company or entity.
   SHARES OUTSTANDING: Shares outstanding represent the total number of shares issued by a company that are currently owned by investors.
   ANNUAL CLOSING STOCK PRICE: Annual closing stock price refers to the price of a company's stock at the end of each trading day during a specific financial year.
   SHORT AND LONG TERM DEBT: Short and long-term debt represents the total debt obligations of a company, including both short-term debt (due within one year) and long-term debt (due after one year).
   CASH AND MARKETABLE SECURITIES: Cash and marketable securities represent the liquid assets held by a company, including cash on hand and investments that can be easily converted into cash.
   TOTAL COMPANY ASSETS: Total company assets represent the total value of all assets owned by a company, including tangible assets such as property, plant, and equipment, as well as intangible assets such as patents and goodwill.

   NOTE:
   When making calculations for columns B through T, those raw numbers should be multiplied by 1000 as Bloomberg records GHG emissions in mtCO2e, not tCO2e.
   When making calculations for columns U, V, W, Y, AA, AB, and AC, those raw numbers should be multiplied by 1000000 as Bloomberg records financial numbers in millions of dollars (USD) or the company's reported currency (see `bloomberg/` for a breakdown on which country-based companies use what currency).

   - **Usage**: Open this file in Excel to have a single view of all the data in one place. This is useful for performing more advanced pivot tables, summaries, or visualizations.

#### How to Use

1. **CSV files**: Simply open the desired file in your spreadsheet program of choice for analysis.
2. **Consolidated XLSX file**: Use this file if you prefer having all the data in a single workbook for ease of use.
