import json
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

# Define the GraphQL query
query = gql(
    """
    query {
        posts {
            edges {
                node {
                    id
                    name
                    description
                    votesCount
                    reviewsRating
                    reviewsCount
                    commentsCount
                }
            }
        }
    }
"""
)

# Create a transport to make the HTTP request
transport = RequestsHTTPTransport(
    url="https://api.producthunt.com/v2/api/graphql",
    headers={
        "Authorization": "Bearer YmY_hVX5X-e9zKMBPCowCVlvIOpmdkq9wP8H4MEJptE",
        "Content-type": "application/json",
    },
    use_json=True,
)

# Create a GraphQL client using the transport
client = Client(transport=transport, fetch_schema_from_transport=True)

# Execute the query
result = client.execute(query)

# Extract the required fields from the response
posts = result["posts"]["edges"]
extracted_data = []

for post in posts:
    node = post["node"]
    extracted_data.append(
        {
            "id": node["id"],
            "name": node["name"],
            "description": node["description"],
            "votesCount": node["votesCount"],
            "reviewsRating": node["reviewsRating"],
            "reviewsCount": node["reviewsCount"],
            "commentsCount": node["commentsCount"],
        }
    )

# Save the extracted data to a JSON file
with open("extracted_data.json", "w") as file:
    json.dump(extracted_data, file, indent=4)

print("Data extraction and saving complete.")
