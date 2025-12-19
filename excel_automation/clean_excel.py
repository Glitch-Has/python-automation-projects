import pandas as pd

input_file = "input.xlsx"
output_file = "cleaned_output.xlsx"

try:
    df = pd.read_excel(input_file)

    df.dropna(how="all", inplace=True)
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    df.to_excel(output_file, index=False)
    print("Excel file cleaned and saved successfully!")

except FileNotFoundError:
    print("Error: input.xlsx file not found.")
except Exception as e:
    print(f"Unexpected error: {e}")

