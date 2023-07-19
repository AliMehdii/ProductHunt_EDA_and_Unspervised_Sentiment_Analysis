import json
import csv

with open("Posts_2022_Rate_Fix_01_Cleaned.json") as json_file:
    data = json.load(json_file)


with open("Posts_2022_Rate_Fix_01_Cleaned.csv", "w", newline="") as csv_file:
    writer = csv.writer(csv_file)

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

    for post in data:
        posts = data["node"]

        topics = ", ".join([topic["node"]["name"] for topic in post["topics"]["edges"]])

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
                topics,
            ]
        )
