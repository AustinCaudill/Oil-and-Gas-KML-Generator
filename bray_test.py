import pandas as pd

# Load the well data from the Excel file
well_data_path = 'DLP Well Master.xlsx'  # Update with the correct path if necessary
well_data = pd.read_excel(well_data_path)

# Define the log file path
log_file_path = 'divestment_debug_log.txt'

# Filter the data for wells in the "BRAY" engineering group
bray_wells = well_data[well_data['EngGroup'] == 'BRAY']

# Open the log file to write the debug information
with open(log_file_path, 'w') as log_file:
    # Loop through each well in the "BRAY" group
    for index, row in bray_wells.iterrows():
        # Check divestment status
        is_divested = pd.notna(row['DIV_CLOSE_DATE'])
        
        # Log the well's information to the log file
        log_file.write(f"Processing well {row['WellName']}: DIV_CLOSE_DATE = {row['DIV_CLOSE_DATE']}, is_divested = {is_divested}\n")

print(f"Debugging information saved to {log_file_path}")
