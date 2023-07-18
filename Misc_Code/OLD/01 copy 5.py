import requests
import json

access_token = "TOKEN"

query = """
query ($afterDate: DateTime!, $cursor: String) {
  posts(postedAfter: $afterDate, after: $cursor) {
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
        reviewsRating
        reviewsCount
        commentsCount
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
after_date = "2023-07-10"

# Pass the date as a variable to the GraphQL query
variables = {"afterDate": after_date, "cursor": None}

all_posts = []

while True:
    response = send_graphql_request(query, access_token, variables)
    print(response)  # Print the response for analysis

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
    else:
        break

# Step 3: Open the file in write mode
print("Saved!")
with open("posts_After_2023-07-12.json", "w") as file:
    # Step 4: Write the dictionary as JSON data into the file
    json.dump(all_posts, file)
