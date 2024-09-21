import os
import csv

def process_csv_directory(input_dir, output_dir):
    # Create the clone directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Iterate through all CSV files in the directory
    for filename in os.listdir(input_dir):
        if filename.endswith(".csv"):
            input_file = os.path.join(input_dir, filename)
            output_file = os.path.join(output_dir, filename)

            with open(input_file, mode='r', newline='', encoding='utf-8-sig') as infile, open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
                reader = list(csv.reader(infile))
                writer = csv.writer(outfile)

                # Ensure file has at least 2 rows
                if len(reader) < 2:
                    print(f"File {filename} has less than 2 rows, skipping.")
                    continue
                
                # Write the first and third rows, replacing "#N/A N/A" with an empty string
                writer.writerow([cell.replace("#N/A N/A", "") for cell in reader[1]])

    print(f"Processed all files in {input_dir} and saved them to {output_dir}")

# Main execution
if __name__ == "__main__":
    input_directory = input("\nPlease type in the name of the source directory from which your .csv files are located:\n\n")
    output_directory = "AllCompanyData" # Replace with actual output directory path
    
    # Clone the directory and process the CSV files
    process_csv_directory(input_directory, output_directory)
