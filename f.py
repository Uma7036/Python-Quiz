import pandas as pd

# Create a DataFrame with a single column named 'Name'
data = {'Name': ['John']}
df = pd.DataFrame(data)

# Specify the file path to save the Excel file
file_path = 'output.xlsx'

# Save the DataFrame to Excel
df.to_excel(file_path, index=False)

print("Name saved to Excel file:", file_path)
