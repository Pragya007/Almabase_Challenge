import sys
import re
import requests
import json

class GitHubApi:

    # Initialsing URL's values
    def __init__(self):
        self.github_url = r'https://api.github.com/'
        self.org_url = r'orgs/'
        self.search_repo_url = r'search/repositories'

    # Hitting the API to check whether it is responding or not
    def get_request(self, url):
        return requests.get(url)

    # To check if organization is valid or not and so as the URL
    def is_valid_organization(self, organization):
        url = self.github_url + self.org_url + organization   #Appending the org name to URL
        print("Organization URL: " + url)                     # To display the URL in the textbox(ListWidget in PyQt)
        response = self.get_request(url)
        return (response.status_code == 200)                  # To check the status of the URL

    # To get the most popular repo on the basis of forks and sorting it
    def get_popular_repositories(self, organization, sort_on, repoCount):
        url = self.github_url + self.search_repo_url + r'?q=user:' + organization + r'&sort=' + sort_on 
        print("Search URL: " + url)

        response = self.get_request(url)      #getting the response from the API
        repo_json_response = json.loads(response.text)    #converting to JSON
        results = []
        for repo in repo_json_response['items'][0:repoCount]:      #iterating and filling the result array from JSON
            results.append((repo['id'],repo['name'],repo['forks']))

        # if results size is repoCount then return else handle pagination
        if len(results) == repoCount:
            return results
        else:
            #Handling Paginated results
            next_page, last_page = map(int,re.findall(r'page=(\d+)',response.headers['Link']))
            while next_page <= last_page and len(results) < repoCount:
                remaining_result_count = repoCount - len(results)
                next_url = url + r'&page=' + str(next_page) 
                print("Fetching Results from: " + next_url)
                response = self.get_request(next_url)
                repo_json_response = json.loads(response.text)
                for repo in repo_json_response['items'][0:remaining_result_count]:
                    results.append((repo['id'],repo['name'], repo['forks']))
                next_page+=1
        return results

    # To get the most top committees 
    def get_top_committees(self, org, id, committeeCount):
        url = self.github_url + 'repositories/' + str(id) +'/contributors' 
        print("Contributors URL: " + url)

        response = self.get_request(url)     #getting the response from the API
        contributors_json_response = json.loads(response.text)    # converting to JSON
        results = []
        for contribution in contributors_json_response[0:committeeCount]:      #iterating and filling the result array from JSON
            results.append((contribution['login'], contribution['contributions']))

        # if results size is RepoCount then return else handle pagination
        if len(results) == committeeCount:
            return results
        else:
            # Handling Paginated results
            if 'Link' in response.headers:
                print(response.headers['Link'])
                next_page, last_page = map(int, re.findall(r'page=(\d+)', response.headers['Link']))
                while next_page <= last_page and len(results) < committeeCount:
                    remaining_result_count = committeeCount - len(results)
                    next_url = url + r'?page=' + str(next_page)
                    print("Fetching Results from: " + next_url)
                    response = self.get_request(next_url)
                    contributors_json_response = json.loads(response.text)
                    for contribution in contributors_json_response[0:remaining_result_count]:
                        results.append((contribution['login'], contribution['contributions']))
                    next_page += 1
        return results


if __name__ == '__main__':
    if len(sys.argv)!=4:
        print("Invaild arguments")
        print("Usage: github.py organization n m")
        print("Ex: github.py google 5 6")

    organizationName , RepoCount , CommitteeCount = sys.argv[1:]      # Getting org name, repo count, committee count from text box
    # to fetch repos
    githubApiCall = GitHubApi()
     # if org name is valid then fetch repos
    if githubApiCall.is_valid_organization(organizationName):
        print(organizationName + " is a valid Organization")
        sort_on = 'forks'     #to sort on the basis of forks
        print("Sorting Results on " + sort_on + " count")
        # to fetch popular repos of given org 
        popular_repos_org = githubApiCall.get_popular_repositories(organizationName, sort_on, int(RepoCount))
        print(RepoCount + " most popular Repositories of " + organizationName + " and their fork counts:")
        repoiterate = 1
        # printing popular repos
        for repo in popular_repos_org:
            print("Repository: ", repoiterate)
            repoiterate = repoiterate + 1
            print(repo[0], repo[1] , repo[2])
            # to fetch popular committees in repos respectively
            top_committees = githubApiCall.get_top_committees(organizationName, repo[0], int(CommitteeCount))
            print(CommitteeCount + " most popular Committees and their commit counts:")
            committeeIterate = 1
            # printing top committees
            for committee in top_committees:
                print("Committee: ", committeeIterate)
                committeeIterate = committeeIterate + 1
                print(committee[0], committee[1])
            print("-----------------------------")
    else:
        print("Invalid Organization")
        sys.exit()