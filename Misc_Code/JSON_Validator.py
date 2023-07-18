# import json

# try:
#     with open("posts_Year_2022_02.json") as file:
#         json_data = json.load(file)
#     # If the JSON is valid, you can proceed with further processing
# except json.JSONDecodeError as e:
#     print(f"Invalid JSON: {e}")


import pandas as pd

# Read the CSV file into a pandas DataFrame
df = pd.read_csv("posts_Year_2022_01.csv")

# Drop duplicate rows based on the 'name' column, keeping only the first occurrence
df.drop_duplicates(subset="name", keep="first", inplace=True)

# Save the updated DataFrame to a new CSV file
df.to_csv("posts_Year_2022_01_updated.csv", index=False)

print("New CSV file saved successfully.")
