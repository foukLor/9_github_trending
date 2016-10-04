import requests
from datetime import date, timedelta


def get_trending_repositories(top_size):
    date_week_ago = date.today() - timedelta(days=7)
    url = "https://api.github.com/search/repositories?"\
        "q=+created:>={0}&sort=stars&order=desc".format(date_week_ago)
    response = requests.get(url)
    return response.json()['items'][:top_size]


def get_open_issues_amount(repo_owner, repo_name):
    url = 'https://api.github.com/repos/{0}/{1}/issues'\
        .format(repo_owner, repo_name)
    response = requests.get(url)
    return len(response.json())


def pretty_print(repositories):
    for repo in repositories:
        print("\nName: {0}".format(repo['name']))
        print("Url: {0}".format(repo['html_url']))
        print("Count of issues {0}".format(
            get_open_issues_amount(repo['owner']['login'], repo['name'])))


if __name__ == '__main__':
    trends_rep = get_trending_repositories(10)
    pretty_print(trends_rep)
