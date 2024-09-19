import xlsxwriter
import os
import datetime

header = [
    "TICKER + FINANCIAL YEAR", "GHG SCOPE 1", "GHG SCOPE 2 LOCATION BASED", "GHG SCOPE 3",
    "SCOPE 3-1 PURCHASED GOODS AND SERVICES", "SCOPE 3-2 CAPITAL GOODS", "SCOPE 3-3 FUEL AND ENERGY RELATED ACTIVITIES",
    "SCOPE 3-4 UPSTREAM TRANS DIST", "SCOPE 3-5 WASTE GENERATED IN OPERATIONS", "SCOPE 3-6 BUSINESS TRAVEL EMISSIONS",
    "SCOPE 3-7 EMPLOYEE COMMUTING", "SCOPE 3-8 UPSTREAM LEASED ASSETS", "SCOPE 3-9 DOWNSTRM TRANSPORATION AND DISTRIBUTION",
    "SCOPE 3-10 PROCESSING OF SOLD PRODUCTS", "SCOPE 3-11 USE OF SOLD PRODUCTS", "SCOPE 3-12 END-OF-LIFE TREATMENT OF SOLD PRODUCTS",
    "SCOPE 3-13 DOWNSTRM LEASED ASSETS", "SCOPE 3-14 FRANCHISES", "SCOPE 3-15 INVESTMENTS", "SCOPE 3 EMISSIONS OTHER",
    "ENTERPRISE VALUE INCLUDING CASH", "ANNUAL REVENUE", "HISTORICAL MARKET CAP", "NAME", "SHARES OUTSTANDING",
    "ANNUAL CLOSING STOCK PRICE", "SHORT AND LONG TERM DEBT", "CASH AND MARKETABLE SECURITIES", "TOTAL COMPANY ASSETS"
]

print("\nWelcome to the GHG Emissions DataGen Tool!\nThis can be used to generate .xlsx files that when accessed through a Microsoft Excel session with a Bloomberg Terminal plugin, will output the company's most recent GHG emissions data.\n")
tickers = input("Enter the ticker, then an underscore, then the Bloomberg exchange country code for your desired company. For example for Microsoft you would enter MSFT_US. If you want to generate the template sheets for multiple companies use a '+' to separate them like this: XOM_US+CNQ_CN+SU_CN.\n\n")
tickers = tickers.upper().replace("_", " ").split("+")

directory = str(int(datetime.datetime.now().timestamp()))

if not os.path.exists(directory):
    os.makedirs(directory)

for ticker in tickers:
    try:
        workbook = xlsxwriter.Workbook(directory + '/GHG_Emissions_' + ticker.replace("/","-") + '.xlsx')
        worksheet = workbook.add_worksheet()

        for idx, col_name in enumerate(header):
            worksheet.write(0, idx, col_name)

        worksheet.write('A2', ticker + " 2022")
        worksheet.write('B2', '=BDH("' + ticker + ' Equity", "GHG_SCOPE_1", "FY 2022")')
        worksheet.write('C2', '=BDH("' + ticker + ' Equity", "GHG_SCOPE_2_LOCATION_BASED", "FY 2022")')
        worksheet.write('D2', '=BDH("' + ticker + ' Equity", "GHG_SCOPE_3", "FY 2022")')
        worksheet.write('E2', '=BDH("' + ticker + ' Equity", "SCOPE_3_PURCH_GOODS_SRVCS", "FY 2022")')
        worksheet.write('F2', '=BDH("' + ticker + ' Equity", "SCOPE_3_CAPITAL_GOODS", "FY 2022")')
        worksheet.write('G2', '=BDH("' + ticker + ' Equity", "SCOPE_3_FUEL_ENRG_RELATD_ACT", "FY 2022")')
        worksheet.write('H2', '=BDH("' + ticker + ' Equity", "SCOPE_3_UPSTREAM_TRANS_DIST", "FY 2022")')
        worksheet.write('I2', '=BDH("' + ticker + ' Equity", "SCOPE_3_WASTE_GENRTD_IN_OP", "FY 2022")')
        worksheet.write('J2', '=BDH("' + ticker + ' Equity", "SCOPE_3_BUSINESS_TRVL_EMISSIONS", "FY 2022")')
        worksheet.write('K2', '=BDH("' + ticker + ' Equity", "SCOPE_3_EMPLOYEE_COMMUTING", "FY 2022")')
        worksheet.write('L2', '=BDH("' + ticker + ' Equity", "SCOPE_3_UPSTREAM_LEASED_ASSETS", "FY 2022")')
        worksheet.write('M2', '=BDH("' + ticker + ' Equity", "SCOPE_3_DWNSTRM_TRANS_DIST", "FY 2022")')
        worksheet.write('N2', '=BDH("' + ticker + ' Equity", "SCOPE_3_PRCSS_OF_SOLD_PRODS", "FY 2022")')
        worksheet.write('O2', '=BDH("' + ticker + ' Equity", "SCOPE_3_USE_SOLD_PRODUCTS", "FY 2022")')
        worksheet.write('P2', '=BDH("' + ticker + ' Equity", "SCOPE_3_EOL_TRTMNT_PRODS", "FY 2022")')
        worksheet.write('Q2', '=BDH("' + ticker + ' Equity", "SCOPE_3_DWNSTRM_LEASE_ASSTS", "FY 2022")')
        worksheet.write('R2', '=BDH("' + ticker + ' Equity", "SCOPE_3_FRANCHISES", "FY 2022")')
        worksheet.write('S2', '=BDH("' + ticker + ' Equity", "SCOPE_3_INVESTMENTS", "FY 2022")')
        worksheet.write('T2', '=BDH("' + ticker + ' Equity", "SCOPE_3_EMISSIONS_OTHER", "FY 2022")')
        worksheet.write('U2', '=BDH("' + ticker + ' Equity", "ENTERPRISE_VALUE", "FY 2022")')
        worksheet.write('V2', '=BDH("' + ticker + ' Equity", "IS_COMP_SALES", "FY 2022")')
        worksheet.write('W2', '=BDH("' + ticker + ' Equity", "HISTORICAL_MARKET_CAP", "FY 2022")')
        worksheet.write('X2', '=BDP("' + ticker + ' Equity", "NAME")')
        worksheet.write('Y2', '=BDH("' + ticker + ' Equity", "IS_AVG_NUM_SH_FOR_EPS", "FY 2022")')
        worksheet.write('Z2', '=BDH("' + ticker + ' Equity", "PX_LAST", "FY 2022")')
        worksheet.write('AA2', '=BDH("' + ticker + ' Equity", "SHORT_AND_LONG_TERM_DEBT", "FY 2022")')
        worksheet.write('AB2', '=BDH("' + ticker + ' Equity", "CASH_AND_MARKETABLE_SECURITIES", "FY 2022")')
        worksheet.write('AC2', '=BDH("' + ticker + ' Equity", "BS_TOT_ASSET", "FY 2022")')

        print('\nA new .xlsx file containing the Bloomberg plugin functions for your desired company (' + ticker + ') for 2022 has been successfully created!')

        workbook.close()
    except:
        print('\nProcess failed for ' + ticker + '!')


print("\nTask fully completed!!\n\n")