import requests
import json
import csv
from operator import itemgetter

access_token = "YmY_hVX5X-e9zKMBPCowCVlvIOpmdkq9wP8H4MEJptE"

query = """
query {
  posts(first: 5) {
    edges {
      node {
        id
        name
        description
        votesCount
        reviewsRating
        reviewsCount
        commentsCount
        createdAt
        topics
      }
    }
  }
}
"""


def send_graphql_request(query, access_token):
    url = "https://api.producthunt.com/v2/api/graphql"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}",
    }
    data = {"query": query}

    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()


response = send_graphql_request(query, access_token)

if "data" in response:
    posts = response["data"]["posts"]["edges"]

    # Sort posts based on creation date in descending order
    sorted_posts = sorted(posts, key=lambda x: x["node"]["createdAt"], reverse=True)

    # Open a CSV file for writing
    with open("products.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Name", "Description", "Votes", "Comments"])

        for post in sorted_posts:
            post_info = post["node"]
            name = post_info["name"]
            description = post_info["description"]
            votes = post_info["votesCount"]
            comments = post_info["commentsCount"]

            writer.writerow([name, description, votes, comments])

    print("CSV file saved successfully.")
else:
    print("Error:", response.get("errors"))
