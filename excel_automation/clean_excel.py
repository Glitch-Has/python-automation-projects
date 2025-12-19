import pandas as pd

# Load Excel file
input_file = "input.xlsx"
output_file = "cleaned_output.xlsx"

# Read data
df = pd.read_excel(input_file)

# Drop completely empty rows
df.dropna(how="all", inplace=True)

# Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Save cleaned file
df.to_excel(output_file, index=False)

print("Excel file cleaned and saved successfully!")
