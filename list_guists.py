import requests

user = 'nestoralonsovina'
token = 'YOUR TOKEN'

def run_query(query):
    """
    query -> GraphQL query
    simple function to use request.posts to make the API call.
    """
    request = requests.post('https://api.github.com/graphql', json={'query': query}, auth=(user, token))

    if request.status_code == 200:
        return request.json()
    else:
        raise Exception(f"Query faild to run by returning code of {request.status_code}. {query}")

query = """
{
  viewer {
    gists(last: 30) {
      nodes {
        name
        description
        files {
          name
          text
        }
      }
    }

  }
}
"""


result = run_query(query)
print(result)
