### README for `code/`

#### Overview

This directory contains Python scripts designed to help streamline the data processing workflow for the project, particularly around the handling and analysis of financial and environmental data sourced from BOCC and Bloomberg Terminal datasets.

#### Files

1. **`bocc_stats.py`**
   - **Description**: This script is used to analyze the large BOCC dataset (downloaded via the Banking on Climate Chaos archive). It provides tools to filter and summarize specific financial and emissions data relevant to the study.
   - **Usage**: Run the script to perform various operations, such as aggregation and filtering, on the BOCC dataset.
2. **`convert_csv_directory_to_xlsx.py`**

   - **Description**: A utility to convert all CSV files in a specified directory into a single consolidated XLSX file. This is helpful when dealing with multiple CSV files generated from Bloomberg Terminal data.
   - **Usage**: Specify the directory containing CSV files, and the script will output a single Excel workbook.

3. **`convert_xlsx_to_csv_directory.py`**

   - **Description**: This script converts each sheet in a specified XLSX file into individual CSV files. It’s the reverse of the previous script and allows easy manipulation of data from Excel into smaller CSV formats.
   - **Usage**: Point the script to an XLSX file, and it will generate corresponding CSV files for each sheet.

4. **`generate_bloomberg_templates.py`**

   - **Description**: This script generates preformatted Excel templates that can be used with a Bloomberg Terminal plugin. When accessed through Excel (connected to Bloomberg), these templates will pull the most recent GHG emissions data for the companies listed.
   - **Usage**: After running the script, open the generated XLSX files in Excel on a machine with a Bloomberg Terminal plugin, and the emissions data will be retrieved.

5. **`process_csv_files.py`**
   - **Description**: This script processes CSV files in a specified directory by reading each file, cleaning the data, and writing it to a new directory. It ensures that the files have at least two rows and removes occurrences of #N/A N/A, replacing them with empty strings.
   - **Usage**: Usage: Run the script, input the source directory containing the CSV files, and specify an output directory. The script will process the files and save them to the specified location.

#### How to Use

1. **Run the scripts**: Make sure you have Python installed. Navigate to this directory and run the desired script using the command:
   ```
   python script_name.py
   ```
2. **Modify for your needs**: The scripts can be easily adapted to other datasets by changing the file paths or filtering criteria.
