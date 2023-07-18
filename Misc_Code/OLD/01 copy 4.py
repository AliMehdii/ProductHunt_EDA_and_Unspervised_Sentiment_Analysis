import requests
import json

access_token = "TOKEN"

query = """
query ($afterDate: DateTime!, $cursor: String) {
  posts(first 4, postedAfter: $afterDate, after: $cursor) {
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
with open("posts_After_2023-07-10_.json", "w") as file:
    # Step 4: Write the dictionary as JSON data into the file
    json.dump(all_posts, file)


# import requests
# import json

# access_token = "YmY_hVX5X-e9zKMBPCowCVlvIOpmdkq9wP8H4MEJptE"

# query = """
# query ($afterDate: DateTime!) {
#   posts(postedAfter: $afterDate) {
#     edges {
#       node {
#         id
#         name
#         description
#         votesCount
#         reviewsRating
#         reviewsCount
#         commentsCount
#         createdAt
#         collections {
#           totalCount
#         }
#         topics(first:3) {
#           edges {
#             node {
#               name
#               description
#               followersCount
#               postsCount
#             }
#           }
#         }
#         comments(first: 3) {
#           edges {
#             node {
#               body
#               votesCount
#             }
#           }
#         }
#       }
#     }
#   }
# }
# """


# def send_graphql_request(query, access_token, variables=None):
#     url = "https://api.producthunt.com/v2/api/graphql"
#     headers = {
#         "Content-Type": "application/json",
#         "Authorization": f"Bearer {access_token}",
#     }
#     data = {"query": query, "variables": variables}

#     response = requests.post(url, headers=headers, data=json.dumps(data))
#     return response.json()


# # Specify the desired date in the format "YYYY-MM-DD"
# after_date = "2023-07-10"

# # Pass the date as a variable to the GraphQL query
# variables = {"afterDate": after_date}

# response = send_graphql_request(query, access_token, variables)

# # Extract the necessary data from the response
# posts = response["data"]["posts"]["edges"]

# # Step 3: Open the file in write mode
# print("Saved!")
# with open("posts_After_2023-07-10.json", "w") as file:
#     # Step 4: Write the dictionary as JSON data into the file
#     json.dump(posts, file)

# import requests
# import json
# import csv
# from datetime import datetime

# access_token = "YOUR_ACCESS_TOKEN"

# # Specify the date from which you want to retrieve the posts
# target_date = "2023-07-12"

# # Convert the target date string to a datetime object
# target_datetime = datetime.strptime(target_date, "%Y-%m-%d")

# query = """
# query ($cursor: String){
#   posts( after: $cursor) {
#     edges {
#       node {
#         id
#         name
#         description
#         votesCount
#         reviewsRating
#         reviewsCount
#         commentsCount
#         createdAt
#         collections {
#           totalCount
#         }
#         topics(first:3){
#           edges {
#             node {
#               name
#               description
#               followersCount
#               postsCount
#             }
#           }
#         }
#         comments(first: 3) {
#           edges {
#             node {
#               body
#               votesCount
#             }
#           }
#         }
#       }
#     }
#   }
# }
# """


# def send_graphql_request(query, access_token, variables):
#     url = "https://api.producthunt.com/v2/api/graphql"
#     headers = {
#         "Content-Type": "application/json",
#         "Authorization": f"Bearer {access_token}",
#     }
#     data = {"query": query, "variables": variables}

#     response = requests.post(url, headers=headers, data=json.dumps(data))
#     return response.json()


# posts = []

# # Fetch posts recursively until reaching the target date
# while True:
#     variables = {"cursor": None} if not posts else {"cursor": posts[-1]["cursor"]}
#     response = send_graphql_request(query, access_token, variables)

#     if "data" in response:
#         edges = response["data"]["posts"]["edges"]

#         # Filter posts based on the target date
#         filtered_posts = [
#             edge
#             for edge in edges
#             if datetime.strptime(edge["node"]["createdAt"], "%Y-%m-%dT%H:%M:%S.%fZ")
#             > target_datetime
#         ]

#         posts.extend(filtered_posts)

#         # Break the loop if there are no more posts or the last post is before the target date
#         if (
#             not filtered_posts
#             or datetime.strptime(
#                 filtered_posts[-1]["node"]["createdAt"], "%Y-%m-%dT%H:%M:%S.%fZ"
#             )
#             <= target_datetime
#         ):
#             break

#     else:
#         print("Error:", response.get("errors"))
#         break

# # Step 3: Open the file in write mode
# print("Saved!")
# with open("posts_After_2023-07-12.json", "w") as file:
#     # Step 4: Write the dictionary as JSON data into the file
#     json.dump(posts, file)

# # # Open a CSV file for writing
# # with open("products.csv", "w", newline="", encoding="utf-8") as csvfile:
# #     writer = csv.writer(csvfile)
# #     writer.writerow(
# #         [
# #             "Name",
# #             "Description",
# #             "Votes",
# #             "Comment 1",
# #             "Upvotes 1",
# #             "Comment 2",
# #             "Upvotes 2",
# #             "Comment 3",
# #             "Upvotes 3",
# #         ]
# #     )

# #     for post in posts:
# #         post_info = post["node"]
# #         name = post_info["name"]
# #         description = post_info["description"]
# #         votes = post_info["votesCount"]
# #         comments = post_info["comments"]["edges"]

# #         comment1 = comments[0]["node"]["body"] if len(comments) > 0 else ""
# #         upvotes1 = comments[0]["node"]["upvotesCount"] if len(comments) > 0 else 0
# #         comment2 = comments[1]["node"]["body"] if len(comments) > 1 else ""
# #         upvotes2 = comments[1]["node"]["upvotesCount"] if len(comments) > 1 else 0
# #         comment3 = comments[2]["node"]["body"] if len(comments) > 2 else ""
# #         upvotes3 = comments[2]["node"]["upvotesCount"] if len(comments) > 2 else 0

# #         writer.writerow(
# #             [
# #                 name,
# #                 description,
# #                 votes,
# #                 comment1,
# #                 upvotes1,
# #                 comment2,
# #                 upvotes2,
# #                 comment3,
# #                 upvotes3,
# #             ]
# #         )

# # print("CSV file saved successfully.")
