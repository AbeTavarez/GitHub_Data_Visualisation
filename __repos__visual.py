import requests
from plotly.graph_objs import Bar
from plotly import offline


# * Make  API call and store responce

# * Make API call
url = "https://api.github.com/search/repositories?q=language:python&sort=starts"
headers = {"Accept": "application/vnd.github.v3+json"}
# GET Request
req = requests.get(url, headers=headers)
# Print status code from request
print(f"Status code: {req.status_code}")

# * Process results
# Creates a dictionary with the json data from request
res_dict = req.json()
# Grabs the items list which contains all repos (list of dictionaries)
repo_dicts = res_dict["items"]
repo_names, starts = [], []
for repo in repo_dicts:
    repo_names.append(repo['name'])
    starts.append(repo['stargazers_count'])

# * Make Visualization
data = [{
    "type": "bar",
    "x": repo_names,
    "y": starts,
}]

layout = {
    "title": "Most-Starred Python Projects in Github",
    "xaxis": {'title': 'Repository'},
    "yaxis": {'title': 'Stars'},
}

fig = {"data": data, "layout": layout}
offline.plot(fig, filename='python_repos.html')

# * LOGS
# Print the total of repositories
print(f"Total repositories: {res_dict['total_count']}")
print(res_dict.keys())
# * Explore information about the repositories
# Total number of repos (which checks the size of the items array)
print(f"Repositories returned: {len(repo_dicts)}")
