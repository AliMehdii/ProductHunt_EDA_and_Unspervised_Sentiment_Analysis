# JSON Review to CSV Converter

This script converts JSON data containing product reviews into a CSV file for easier analysis and manipulation. The script reads the input JSON file, extracts relevant information from the data, handles character encoding, and writes the extracted data into a CSV file.

## Prerequisites

- Python 3.x
- Required Python packages: `json`, `csv`

## Usage

1. Place the input JSON file (`posts_Year_2022_Coments_03.2_Cleaned.json`) in the same directory as the script.
2. Run the script using the following command:

3. After the script execution, a CSV file (`posts_Year_2022_Coments_03.2_Cleaned.csv`) will be created in the same directory.

## File Descriptions

- `JSON_Review_to_CSV.py`: The main Python script that performs the JSON to CSV conversion.
- `posts_Year_2022_Coments_03.2_Cleaned.json`: Input JSON file containing product review data.
- `posts_Year_2022_Coments_03.2_Cleaned.csv`: Output CSV file where the extracted data will be stored.

## Customization

If you need to modify the code to fit your specific JSON structure, you can make the following changes:

- Adjust the file paths:
- Modify the input JSON file path in the `open()` function in line 7.
- Modify the output CSV file path in the `open()` function in line 12.

- Adjust the column names in the CSV file:
- Modify the list passed to `csv_writer.writerow()` in line 15 to change the column names.

- Customize the data extraction:
- Modify the data extraction logic in the nested `for` loop starting from line 19 to fit your JSON structure.

## Notes

- The script uses the `cp1252` encoding to handle character encoding issues. You can modify the encoding scheme in the `handle_encoding()` function if needed.

- If you encounter any issues or errors, please feel free to contact the script author at [your-email@example.com](mailto:your-email@example.com).

