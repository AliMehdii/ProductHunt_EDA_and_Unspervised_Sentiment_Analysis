import json
import csv


def handle_encoding(text):
    # Replace or skip problematic characters
    if isinstance(text, str):
        return text.encode("cp1252", errors="replace").decode("cp1252")
    return text


with open("posts_Year_2022_Coments_03.2_Cleaned.json", encoding="utf-8") as json_file:
    data = json.load(json_file)

csv_file = open(
    "posts_Year_2022_Coments_03.2_Cleaned.csv", "w", encoding="utf-8", newline=""
)
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Comments Body", "votesCount", "Creation Date", "Product Name"])

for product in data:
    product_name = product["node"]["name"]
    for comment in product["node"]["comments"]["edges"]:
        body = handle_encoding(comment["node"]["body"])
        votesCount = comment["node"]["votesCount"]
        created_at = handle_encoding(comment["node"]["createdAt"])
        csv_writer.writerow([body, votesCount, created_at, product_name])

csv_file.close()
