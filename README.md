# Bay-St-Climate-Calculations: README

## Overview

This repository contains the data and scripts necessary to replicate the results of the "Bay-St-Climate-Calculations" study, which investigates the financed emissions of key financial institutions in the oil and gas sector. The study focuses on six major Canadian banks and their involvement in financing the fossil fuel industry through loans, asset management, and equity holdings.

Below are step-by-step instructions on how to replicate the study results, including data collection, transformation, and the final calculations of financed emissions.

  -

## Step-by-Step Instructions

### 1. Data Collection

#### a. Download Data from [Banking on Climate Chaos (BOCC)](https://www.bankingonclimatechaos.org/)

The primary data source for this study is from the **Banking on Climate Chaos** website. Specifically, the 2022 report data is used, which can be downloaded using the following archived link:

- [BOCC 2022 Fossil Fuel Financing Data (Excel)](https://web.archive.org/web/20240210093432/https://www.bankingonclimatechaos.org/wp-content/themes/bocc-2021/inc/bcc-data-2023/GROUP-Fossil_Fuel_Financing_by_Company_Banking_on_Climate_Chaos_2023.xlsx)

#### b. Consult Investment Rankings Based from [Investing in Climate Chaos (IICC)](https://investinginclimatechaos.org/)

Although no archived listing of investment activities by Toronto-based for 2022 is available. The table below provides a sanpshot of the exact rankings we used:

| Financial Institution                     | Investee Energy Companies (based on IICC 2023) |                                       |                         |                                   |                              |                                     |                           |                                     |                            |                                     |                                     |                                |                                     |                                     |                                     |                            |                                     |                                  |                                |                                   |
|                                           |                                                |                                       |                         |                                   |                              |                                     |                           |                                     |                            |                                     |                                     |                                |                                     |                                     |                                     |                            |                                     |                                  |                                |                                   |
| Name                                      | No. 1                                          | No. 2                                 | No. 3                   | No. 4                             | No. 5                        | No. 6                               | No. 7                     | No. 8                               | No. 9                      | No. 10                              | No. 11                              | No. 12                         | No. 13                              | No. 14                              | No. 15                              | No. 16                     | No. 17                              | No. 18                           | No. 19                         | No. 20                            |
| Royal Bank of Canada                      | Canadian Natural Resources Ltd (CNRL)          | Suncor Energy Inc                     | Chevron Corporation     | Fortis Inc                        | Exxon Mobil Corporation      | Equinor ASA                         | Duke Energy Corp          | Cenovus Energy Inc                  | Teck Resources Ltd         | Dominion Energy Inc                 | The Williams Companies Inc          | ConocoPhillips                 | Xcel Energy Inc                     | EOG Resources Inc                   | Imperial Oil Ltd                    | TotalEnergies SE           | American Electric Power Company Inc | TransAtla Corp                   | ARC Resources Ltd              | Emera Inc                         |
| Bank of Montreal                          | Canadian Natural Resources Ltd (CNRL)          | Suncor Energy Inc                     | Fortis Inc              | Exxon Mobil Corporation           | Chevron Corporation          | Cenovus Energy Inc                  | Pioneer Natural Resources | Emera Inc                           | ConocoPhillips             | Shell plc                           | Air Products and Chemicals Inc      | BP plc                         | Teck Resources Ltd                  | Imperial Oil Ltd                    | Occidental Petroleum Corporation    | FirstEnergy Corp           | Southern Co                         | EOG Resources Inc                | Duke Energy Corp               | Devon Energy Corporation          |
| Toronto-Dominion (TD)                     | Canadian Natural Resources Ltd (CNRL)          | Suncor Energy Inc                     | Fortis Inc              | Chevron Corporation               | Cenovus Energy Inc           | Exxon Mobil Corporation             | TotalEnergies SE          | ConocoPhillips                      | Tourmaline Oil Corp        | ITOCHU Corporation                  | ARC Resources Ltd                   | Air Products and Chemicals Inc | Emera Inc                           | American Electric Power Company Inc | Equinor ASA                         | Schlumberger Ltd           | Imperial Oil Ltd                    | Enel SpA                         | Ameren Corp                    | Pioneer Natural Resources Company |
| Bank of Nova Scotia (Scotiabank)          | Canadian Natural Resources Ltd (CNRL)          | Suncor Energy Inc                     | Fortis Inc              | Cenovus Energy Inc                | Exxon Mobil Corporation      | Chevron Corporation                 | Teck Resources Ltd        | The Williams Companies Ltd          | Tourmaline Oil Corp        | Xcel Energy Inc                     | WEC Energy Group Inc                | ConocoPhillips                 | Dominion Energy Inc                 | Imperial Oil Ltd                    | American Electric Power Comapny Inc | Shell plc                  | Schlumberger Ltd                    | Equinor ASA                      | FirstEnergy Corp               | CMS Energy Corp                   |
| Canadian Imperial Bank of Commerce (CIBC) | Canadian Natural Resources Ltd (CNRL)          | Suncor Energy Inc                     | Cenovus Energy Inc      | Pioneer Natural Resources Company | Chevron Corporation          | Fortis Inc                          | Teck Resources Ltd        | Tourmaline Oil Corp                 | ConocoPhillips             | Exxon Mobil Corporation             | Shell plc                           | TransAtla Corp                 | ARC Resources Ltd                   | EOG Resources Inc                   | Xcel Energy Inc                     | Imperial Oil Ltd           | Dominion Energy Inc                 | Devon Energy Corporation         | TotalEnergies SE               | The Williams Companies Inc        |
| National Bank of Canada                   | Canadian Natural Resources Ltd (CNRL)          | Suncor Energy Inc                     | Cenovus Energy Inc      | Fortis Inc                        | Teck Resources Ltd           | Petroleo Brasileiro SA - Petrobras  | The Carlyle Group Inc     | Imperial Oil Ltd                    | EOG Resources Ltd          | Exxon Mobil Corporation             | BP plc                              | Chevron Corporation            | Marathon Oil Corporation            | Pioneer Natural Resources Company   | Vermilion Energy Inc                | TransAtla Corp             | Duke Energy Corp                    | Crescent Point Energy Corp       | Air Products and Chemicals Inc | ConocoPhilips                     |
| Sun Life Financial                        | ConocoPhilips                                  | Southern Co                           | Duke Energy Corp        | Pioneer Natural Resources Company | Dominion Energy Inc          | TotalEnergies SE                    | Glencore PLC              | EOG Resources Inc                   | Hess Corporation           | American Electric Power Company Inc | Eni SpA                             | Woodside Petroleum Ltd         | Xcel Energy Inc                     | Galp Energia SGPS SA                | Suncor Energy Inc                   | Shell plc                  | Diamondback Energy Inc              | AES Corp                         | CenterPoint Energy Inc         | RWE AG                            |
| Power Corporation of Canada               | Exxon Mobil Corporation                        | Canadian Natural Resources Ltd (CNRL) | Shell plc               | ConocoPhillips                    | Suncor Energy Inc            | American Electric Power Comapny Inc | Chevron Corporation       | NRG Energy Inc                      | ARC Resources Ltd          | Southern Co                         | Cenovus Energy Inc                  | Duke Energy Corp               | Glencore PLC                        | Fortis Inc                          | Tourmaline Oil Corp                 | The Williams Companies Inc | Schlumberger Ltd                    | EOG Resources Inc                | TotalEnergies SE               | Ameren Corp                       |
| Manulife Financial                        | Suncor Energy Inc                              | Canadian Natural Resources Ltd (CNRL) | Exxon Mobil Corporation | Duke Energy Corp                  | Cenovus Energy Inc           | Occidental Petroleum Corporation    | Shell plc                 | Xcel Energy Inc                     | The Williams Companies Inc | Chevron Corporation                 | Fortis Inc                          | FirstEnergy Corp               | American Electric Power Company Inc | ConocoPhillips                      | TotalEnergies SE                    | Alliant Energy Corp        | Continental Resources Inc           | OGE Energy Corp                  | Southern Co                    | WEC Energy Group Inc              |
| Brookfield Asset Management               | Chesapeake Energy                              | Vistra Corp                           | TransAtla Corp          | CenterPoint Energy Inc            | Dominion Energy Inc          | Xcel Energy Inc                     | FirstEnergy Corp          | American Electric Power Company Inc | Ameren Corp                | The Williams Companies Inc          | Petreoleo Brasileiro SA - Petrobras | Civitas Resources Inc          | Berry Corporation (bry)             | Aluminum Corporation of China       | Battalion Oil Corporation           | Vista Energy SAB de CV     | Pampa Energia SA                    | Occidental Petroleum Corporation | RWE AG                         | Southern Co                       |
| Fairfax Financial                         | BP plc                                         | Occidental Petroleum Corporation      | Chevron Corporation     | DTE Energy Co                     | Berkshire Hathaway Energy Co | American Electric Power Comapny Inc | Diamondback Energy Inc    | Duke Energy Co                      | Devon Energy Corporation   | Pioneer Natural Resources Company   | EOG Resources Inc                   | The Williams Companies Inc     | TotalEnergies SE                    |                                     |                                     |                            |                                     |                                  |                                |                                   |
| Intact Financial                          | Suncor Energy Inc                              | Canadian Natural Resources Ltd (CNRL) | TransAtla Corp          | Cenovus Energy Inc                | Fortis Inc                   | Crescent Point Energy Corp          | Imperial Oil Ltd          | Chevron Corporation                 | Southern Co                | Vermilion Energy Inc                | Pioneer Natural Resources Company   | Dominion Energy Inc            | Air Products and Chemicals Inc      | AES Corp                            | EOG Resources Inc                   | Teck Resources Ltd         | Exxon Mobil Corporation             | Obsidian Energy Ltd              | The Williams Companies Inc     |                                   |

#### c. Bloomberg Financed Emissions (Global Investments)

For Bloomberg-related data, you can use the pre-made table in the repository, or create one by pulling the **enterprise value including cash (EVIC)**, **market closing price as of December 31, 2022**, and **carbon emissions data (Scope 1, 2, and 3)** directly from the Bloomberg Terminal.

#### d. Use Python Helper Scripts

The python scripts provided in the `code/` directory help to automate the process of gathering and consolidating the necessary data from the Bloomberg Terminal. You can read more in the directory's README, as well as in-line documentation.

#### e. Optional: Download Consolidated Excel Data

Alternatively, download the **ConsolidatedCompanyData.xlsx** file, which contains all the required data across multiple sheets. Refer to the "Overview" sheet for instructions, including the scaling factors for GHG emissions (10^3) and EVIC (10^6). Cells B, C, and D contain the total Scope 1, 2, and 3 emissions for each company.

> **Note:** Some companies may have missing data due to unavailability on Bloomberg at the time of collection.

#### f. Shareholding Data

For banks and asset managers, the shareholding data in oil and gas companies was manually extracted from Bloomberg. Instructions on how to replicate this search are provided below (coming soon). Alternatively, refer to the pre-downloaded data in:

- **Public Equity: Shares Held, 2018-2023 (Banks and Asset Managers)**

For pension funds, use **Form 13F-HR** filings from the SEC's **EDGAR** database. Links are provided in the "Overview" sheet of the consolidated data file:

- **Public Equity: Shares Held, 2018-2023 (Pension Funds)**

  -

### 2. Data Transformation

#### a. Filter Canadian Banks

From the BOCC data, filter the data to focus on the five major Canadian banks: TD, RBC, CIBC, BMO, and ScotiaBank. Aggregate the loan amounts at the parent company level for each bank, and sort the companies in descending order. Use the top 25 companies for financed emissions calculations.

#### b. Filter Financial Institutions

Similarly, filter the data for the top 20 investee companies for the chosen banks, asset managers, and pension funds. After removing duplicates, you should have a final list of approximately 135 oil and gas companies.

#### c. Extract EVIC, Market Prices, and Emissions

Using the Bloomberg data and EDGAR filings, extract the necessary EVIC, market prices, and Scope 1-3 GHG emissions for the final list of oil and gas companies.

  -

### 3. Final Calculations

#### a. Apply the Financed Emissions Formula

With all required data collected, apply the formula provided in the "Methodology" section of the final report. Calculate the attributable emissions for each financial institution by summing the emissions for all relevant oil and gas companies.

#### b. Currency Conversion

For loaned amounts, ensure that the EVIC data is converted to USD using the exchange rate on December 31, 2022. Currency conversion is not required for equity calculations, as the ratio of closing market price to EVIC will be used directly.

Use historical exchange rates available at:

- [Historical Exchange Rates (December 31, 2022)](https://www.x-rates.com/historical/?from=USD&amount=1&date=2022-12-31#google_vignette)

  -

## Files in the Repository

- **Python Helper Scripts:** Automate data collection and transformation processes.
- **ConsolidatedCompanyData.xlsx:** Pre-downloaded data with multiple sheets containing GHG emissions, EVIC, and shareholding details.
- **BOCC 2022 Data:** Downloadable link to fossil fuel financing data.
- **Final Report:** A copy of the methodology and calculations for reference.

  -

## Contact Information

For any issues or questions, feel free to reach out via the issues section of this repository. Happy replicating!
