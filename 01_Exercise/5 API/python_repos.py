import requests
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url)
print("Status code: ", r.status_code)

response_dict = r.json()

# print(response_dict.keys()) dict_keys(['total_count', 'incomplete_results', 'items'])
print("Total repositories: ", response_dict['total_count'])

repo_dicts = response_dict['items']
print("Repository returned: ", len(repo_dicts))
