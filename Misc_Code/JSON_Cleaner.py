path = "C:/Users/alime/Dropbox/PC/Documents/Coding/2023/ProductHunt_EDA_and_Unspervised_Sentiment_Analysis/Data/Stats/JSON/"
# Open the original file for reading
with open(
    path + "Posts_Feb_2023.json",
    "r",
) as f:
    lines = f.readlines()

# Process each line
updated_lines = []
for line in lines:
    # Replace '][' with ','
    updated_line = line.replace("][", ",")
    updated_lines.append(updated_line)

# Save the updated lines to a new file
with open(path + "Posts_Feb_2023_Cleaned.json", "w") as f:
    f.writelines(updated_lines)

print("Updated JSON data saved.")
