import requests

search_query = 'solar'
number_of_results = 5
url = 'https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/hu.wikipedia/all-access/all-agents/Csokol%C3%A1d%C3%A9/monthly/2022010100/2022123100'
headers = {'User-Agent': 'MediaWiki REST API docs examples/0.1 (https://www.mediawiki.org/wiki/API_talk:REST_API)'}

response = requests.get(url, headers=headers, params={'q': search_query, 'limit': number_of_results})
data = response.json()

print(data)

aggregated_views_string = ""

for index, value in enumerate(data["items"]):
    aggregated_views_string += str(index+1) + ";" + str(value["views"]) + "\n"

print(aggregated_views_string)

file1 = open("page_views_per_year.xls", "w")

file1.write(aggregated_views_string)
file1.close()
