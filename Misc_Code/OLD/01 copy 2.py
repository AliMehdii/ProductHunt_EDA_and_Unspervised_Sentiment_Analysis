import requests
import json
import csv

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
        topics(first:3){
          edges {
            node {
              name
              description
              followersCount  
              postsCount
            }
          }
        }
        comments(first: 3) {
          edges {
            node {
              body
              votesCount 
            }
          }
        }
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

    # Open a CSV file for writing
    with open("products_03.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(
            [
                "Name",
                "Description",
                "Votes",
                "Comment 1",
                "Upvotes 1",
                "Comment 2",
                "Upvotes 2",
                "Comment 3",
                "Upvotes 3",
            ]
        )

        for post in posts:
            post_info = post["node"]
            name = post_info["name"]
            description = post_info["description"]
            votes = post_info["votesCount"]
            comments = post_info["comments"]["edges"]

            comment1 = comments[0]["node"]["body"] if len(comments) > 0 else ""
            upvotes1 = comments[0]["node"]["votesCount"] if len(comments) > 0 else 0
            comment2 = comments[1]["node"]["body"] if len(comments) > 1 else ""
            upvotes2 = comments[1]["node"]["votesCount"] if len(comments) > 1 else 0
            comment3 = comments[2]["node"]["body"] if len(comments) > 2 else ""
            upvotes3 = comments[2]["node"]["votesCount"] if len(comments) > 2 else 0

            writer.writerow(
                [
                    name,
                    description,
                    votes,
                    comment1,
                    upvotes1,
                    comment2,
                    upvotes2,
                    comment3,
                    upvotes3,
                ]
            )

    print("CSV file saved successfully.")
else:
    print("Error:", response.get("errors"))
