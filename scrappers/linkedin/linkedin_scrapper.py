from bs4 import BeautifulSoup
import requests
import webbrowser

def set_search_item(user_job, user_location):
    # create the global item to search for
    global search_item
    # update the item to search for with user provided data
    search_item = f"https://www.linkedin.com/jobs/search?keywords={user_job}&location={user_location}&position=1&pageNum=0"

    # make a request to linkedin.com
    req  = requests.get(search_item)
    # make the request a BeautifulSoup element
    soup = BeautifulSoup(req.content, "html.parser")

    # print the website were we scrapped the results from
    print("Website: linkedin", end = "")
    # next operation in line is to print the number of jobs on the website
    number_of_jobs(soup)

def number_of_jobs(soup):
    # print the number of jobs on the website
    print("\tNumber of jobs:", soup.find("span", class_="results-context-header__job-count").get_text())
    print("\n")

def visit():
    print("Opening: ", search_item)
    print("\n")
    # open the website you want to visit in the webbrowser
    webbrowser.open(search_item)