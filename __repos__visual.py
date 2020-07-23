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
# Store data for initial chart/ for repo name and starts for height of bars
repo_names, starts = [], []
for repo in repo_dicts:
    repo_names.append(repo['name'])
    starts.append(repo['stargazers_count'])

# * Make Visualization
# provides data for x and y values /x repo names / y starts
data = [{
    "type": "bar",
    "x": repo_names,
    "y": starts,
    "marker": {
        "color": "rgb(60,100,150)",
        "line": {"width": 1.5, "color": "rgb(25,25,25)"}
    },
    "opacity": 0.6,
}]

layout = {
    "title": "Most-Starred Python Projects on Github",
    "titlefont": {"size": 28},
    "xaxis": {'title': 'Repository',
              "titlefont": {"size": 24},
              "tickfont": {"size": 14}},
    "yaxis": {'title': 'Stars',
              "titlefont": {"size": 24},
              "tickfont": {"size": 14}},
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
