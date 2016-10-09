import requests
from datetime import date, timedelta


def get_trending_repositories(top_size):
    date_week_ago = date.today() - timedelta(days=7)
    date_week_ago_to_str = date_week_ago.strftime("%Y-%m-%dT%H:%M:%S")
    payload = {
            'q': 'created:>='+date_week_ago_to_str,
            'sort': 'star',
            'order': 'desc',
            'per_page': top_size
    }
    url = "https://api.github.com/search/repositories"
    response = requests.get(url, params=payload)
    return response.json()['items']


def pretty_print(repositories):
    print(repositories)
    for repo in repositories:
        print("\nName: {0}".format(repo['name']))
        print("Url: {0}".format(repo['html_url']))
        print("Count of issues {0} issues {1}".format(
            repo['owner']['login'], repo['open_issues_count']))


if __name__ == '__main__':
    NUM_OF_TRENDS = 10
    trends_rep = get_trending_repositories(NUM_OF_TRENDS)
    pretty_print(trends_rep)
