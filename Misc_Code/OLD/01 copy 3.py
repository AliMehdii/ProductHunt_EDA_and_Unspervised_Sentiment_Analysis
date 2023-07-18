import requests
import json
import csv
import pandas as pd


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
        collections {
          totalCount
        }
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
# print("response: ", response)
print(type(response))
print(len(response))

# Extract the necessary data from the response
posts = response["data"]["posts"]["edges"]
# print(posts[4])
# print(type(posts[0]))
# print(len(posts[0]))


# Step 3: Open the file in write mode
print("Saved!")
with open("posts_02.json", "w") as file:
    # Step 4: Write the dictionary as JSON data into the file
    json.dump(posts, file)

# Step 5: Close the file


# df = pd.DataFrame(posts)
# df.to_csv("posts.csv", index=False, header=True)


# data_rows = []


# for post in posts:
#     node = post["node"]
#     row = [
#         node["id"],
#         node["name"],
#         node["description"],
#         node["votesCount"],
#         node["reviewsRating"],
#         node["reviewsCount"],
#         node["commentsCount"],
#         node["createdAt"],
#     ]

#     topics = node["topics"]["edges"]
#     topic_names = [topic["node"]["name"] for topic in topics]
#     topic_descriptions = [topic["node"]["description"] for topic in topics]
#     topic_followers_count = [topic["node"]["followersCount"] for topic in topics]
#     topic_posts_count = [topic["node"]["postsCount"] for topic in topics]

#     row.extend(topic_names)
#     row.extend(topic_descriptions)
#     row.extend(topic_followers_count)
#     row.extend(topic_posts_count)

#     comments = node["comments"]["edges"]
#     comment_bodies = [comment["node"]["body"] for comment in comments]
#     comment_votes_count = [comment["node"]["votesCount"] for comment in comments]

#     row.extend(comment_bodies)
#     row.extend(comment_votes_count)

#     data_rows.append(row)

# print(type(data_rows[0]))
# print(len(data_rows[0]))
# # Save the data to a CSV file
# csv_filename = "producthunt_data_02.csv"

# with open(csv_filename, "w", newline="", encoding="utf-8") as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(
#         [
#             "ID",
#             "Name",
#             "Description",
#             "Votes Count",
#             "Reviews Rating",
#             "Reviews Count",
#             "Comments Count",
#             "Created At",
#             "Topic 1 Name",
#             "Topic 2 Name",
#             "Topic 3 Name",
#             "Topic 1 Description",
#             "Topic 2 Description",
#             "Topic 3 Description",
#             "Topic 1 Followers Count",
#             "Topic 2 Followers Count",
#             "Topic 3 Followers Count",
#             "Topic 1 Posts Count",
#             "Topic 2 Posts Count",
#             "Topic 3 Posts Count",
#             "Comment 1 Body",
#             "Comment 2 Body",
#             "Comment 3 Body",
#             "Comment 1 Votes Count",
#             "Comment 2 Votes Count",
#             "Comment 3 Votes Count",
#         ]
#     )
#     writer.writerows(data_rows)

# print(f"Data saved to {csv_filename}")
