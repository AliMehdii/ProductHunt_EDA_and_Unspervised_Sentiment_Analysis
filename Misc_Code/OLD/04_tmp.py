import requests
import json
import time

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
        description
        votesCount
        commentsCount
        reviews {
        rating
        count  
        }
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
              description
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
    return response.json()


# Specify the desired date in the format "YYYY-MM-DD"
after_date = "2022-07-16"
before_date = "2023-07-17"

# Pass the date as a variable to the GraphQL query
variables = {"afterDate": after_date, "beforeDate": before_date, "cursor": None}

all_posts = []


file_path = "/content/drive/My Drive/CS_Projects/2023/posts_After_2022-01-01.json"

while True:
    response = send_graphql_request(query, access_token, variables)
    print(response)

    # Check if the response contains the expected data structure
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

        # Add sleep for 1 second
        time.sleep(4)
    else:
        break

    print("Saved!")
    with open("posts_Test.json", "a") as file:
        # Step 4: Write the dictionary as JSON data into the file
        json.dump(all_posts, file)
