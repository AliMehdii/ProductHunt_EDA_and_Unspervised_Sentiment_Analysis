# -*- coding: utf-8 -*-
"""Copy of ProductHunt_From_2022.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-OWMVhmBn855uXy198ewoHEyCNdkVdiV
"""

import requests
import json
import time

from google.colab import drive
drive.mount('/content/drive')

access_token = "YmY_hVX5X-e9zKMBPCowCVlvIOpmdkq9wP8H4MEJptE"

query = """
query ($afterDate: DateTime!, $beforeDate: DateTime!, $cursor: String) {
  posts(postedAfter: $afterDate, postedBefore: $beforeDate, after: $cursor) {
    pageInfo {
      endCursor
      hasNextPage
    }
    edges {
      node {
        id
        name
        votesCount
        reviewsRating
        reviewsCount
        commentsCount
        votes {
          totalCount
        }
        createdAt
        collections {
          totalCount
        }
        topics(first:3) {
          edges {
            node {
              name
              followersCount
              postsCount
            }
          }
        }
      }
    }
  }
}
"""

def send_graphql_request(query, access_token, variables=None):

  url = "https://api.producthunt.com/v2/api/graphql"

  headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {access_token}",
  }

  data = {"query": query, "variables": variables}

  response = requests.post(url, headers=headers, data=json.dumps(data))

  # Check rate limit headers
  limit = int(response.headers['X-Rate-Limit-Limit'])
  remaining = int(response.headers['X-Rate-Limit-Remaining'])
  reset = int(response.headers['X-Rate-Limit-Reset'])
  # print("limit: ", limit)
  print("remaining: ", remaining)
  print("reset: ", reset)
  if remaining < 100:
    print("Waiting...")
    time.sleep(int(reset)) # l


  return response.json()

# Specify dates
before_date = "2022-12-25"
after_date = "2022-01-01"

# Initial variables
variables = {"afterDate": after_date, "beforeDate": before_date, "cursor": None}

all_posts = []

file_path = "/content/drive/My Drive/CS_Projects/2023/Posts_2021_Fix.json"

while True:

  response = send_graphql_request(query, access_token, variables)
  print("response", response)
  # print("response", type(response))
  # Check response format
  if "data" not in response or "posts" not in response["data"]:
    print("Invalid response format.")
    break

  posts = response["data"]["posts"]["edges"]
  all_posts.extend(posts)

  pageInfo = response["data"]["posts"]["pageInfo"]
  has_next_page = pageInfo["hasNextPage"]

  if has_next_page:
    cursor = pageInfo["endCursor"]
    variables["cursor"] = cursor

  else:
    break

  print("Saved!")

  with open(file_path, "a") as file:
    json.dump(all_posts, file)

# file_path = '/content/drive/My Drive/CS_Projects/2023/posts_After_2022-01-01.json'

# print("Saved!")
# with open(file_path, "w") as file:
#     # Step 4: Write the dictionary as JSON data into the file
#     json.dump(all_posts, file)

