import requests


# * Make  API call and store responce

# * Make API call
url = "https://api.github.com/search/repositories?q=language:python&sort=starts"
headers = {"Accept": "application/vnd.github.v3+json"}
# GET Request
req = requests.get(url, headers=headers)
# Print status code from request
print(f"Status code: {req.status_code}")


# * Store API responce
# Creates a dictionary with the json data from request
res_dict = req.json()
# Print the total of repositories
print(f"Total repositories: {res_dict['total_count']}")


# * Process results
print(res_dict.keys())

# * Explore information about the repositories
# Grabs the items list which contains all repos (list of dictionaries)
repo_dicts = res_dict["items"]
# Total number of repos (which checks the size of the items array)
print(f"Repositories returned: {len(repo_dicts)}")


# * Examine the first repository
# Grabs the first element of the list of repos
repo_dict = repo_dicts[0]
# Print the total of keys in the first dictionaries
print(f"\nKeys: {len(repo_dict)}")
# Iterates on the first dictionary of the items list and print all keys sorted()
for key in sorted(repo_dict.keys()):
    print(key)

for repo in repo_dicts[:10]:
    print("\nSelected information about first repository: ")
    print(f"Repo Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Starts: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
