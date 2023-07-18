import json
import csv

# Load the JSON data
with open(
    "C:/Users/alime/Dropbox/PC/Documents/Coding/2023/ProductHunt_EDA_and_Unspervised_Sentiment_Analysis/Data/Stats/JSON/Stats_Year_2022_Cleaned.json"
) as f:
    data = json.load(f)
print("mhm")
# Open a CSV file for writing
with open("Stats_Year_2022.csv", "w", encoding="utf-8") as csvfile:
    # Create CSV writer
    writer = csv.writer(csvfile)

    # Write column headers
    writer.writerow(
        [
            "id",
            "name",
            "votesCount",
            "reviewsRating",
            "reviewsCount",
            "commentsCount",
            "createdAt",
            "totalCount",
            "topics",
        ]
    )

    # Loop through each post
    for post in data:
        post = post["node"]

        # Get the topics and convert to comma separated string
        topics = [topic["node"]["name"] for topic in post["topics"]["edges"]]
        # print("topics: ", topics)
        topics_str = ", ".join(topics)

        # Write post data as a row
        writer.writerow(
            [
                post["id"],
                post["name"],
                post["votesCount"],
                post["reviewsRating"],
                post["reviewsCount"],
                post["commentsCount"],
                post["createdAt"],
                post["collections"]["totalCount"],
                topics_str,
            ]
        )
