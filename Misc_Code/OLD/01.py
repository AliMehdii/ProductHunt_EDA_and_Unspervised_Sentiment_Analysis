import requests
import json
import csv

url = "https://api.producthunt.com/v2/api/graphql"

headers = {"Authorization": "Bearer YmY_hVX5X-e9zKMBPCowCVlvIOpmdkq9wP8H4MEJptE"}

query = """
{
  posts(first: 5, orderBy: {direction: DESC, field: CREATED_AT}) {
    edges {
      node {
        name
        tagline
        description
        reviews {
          totalCount 
        }
        followers {
          totalCount
        }
        stats {
          stars
        }
      }
    }
  }
}
"""

data = {"query": query}
print("data: ", data)
print("--------------------------------\n")

response = requests.post(url, json=data, headers=headers)
print("response: ", response)
print("--------------------------------\n")

results = json.loads(response.text)
print("results: ", results)

# with open("products.csv", "w", newline="", encoding="utf-8") as f:
#     writer = csv.writer(f)
#     writer.writerow(["Name", "Tagline", "Description", "Reviews", "Followers", "Stars"])

#     for post in results["data"]["posts"]["edges"]:
#         name = post["node"]["name"]
#         tagline = post["node"]["tagline"]
#         description = post["node"]["description"]
#         reviews = post["node"]["reviews"]["totalCount"]
#         followers = post["node"]["followers"]["totalCount"]
#         stars = post["node"]["stats"]["stars"]

#         writer.writerow([name, tagline, description, reviews, followers, stars])
