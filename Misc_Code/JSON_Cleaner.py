# import json

# # Load the JSON data from a file
# with open("posts_Year_2022_Coments_03.2.json") as f:
#     data = json.load(f)

# # Convert the data to a string
# json_string = json.dumps(data)

# # Replace '][' with ','
# json_string = json_string.replace("][", ",")

# # Convert the modified string back to JSON
# updated_data = json.loads(json_string)

# # Save the updated data to a new file
# with open("posts_Year_2022_Coments_03.2_Cleaned.json", "w") as f:
#     json.dump(updated_data, f)

# print("Updated JSON data saved to 'updated_file.json'.")

import json

# Open the original file for reading
with open("Posts_2022_Rate_Fix_01.json", "r") as f:
    lines = f.readlines()

# Process each line
updated_lines = []
for line in lines:
    # Replace '][' with ','
    updated_line = line.replace("][", ",")
    updated_lines.append(updated_line)

# Save the updated lines to a new file
with open("Posts_2022_Rate_Fix_01_Cleaned.json", "w") as f:
    f.writelines(updated_lines)

print("Updated JSON data saved to 'updated_file.json'.")
