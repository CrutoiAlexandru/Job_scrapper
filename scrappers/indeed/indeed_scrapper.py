from bs4 import BeautifulSoup
import requests
import webbrowser

# retrieve the country of the user by ip
# the country is needed for indeed in order to know which indeed website to access
def get():
    # get user public ip address
    IP_addres = requests.get('https://api.ipify.org').text
    # this website return the country you are in based on your public ip address
    req = requests.get(f'https://ipinfo.io/{IP_addres}/json', verify = True)

    return req.json()['country']

def set_search_item(user_job, user_location):
    # retrieve the country of the ip address
    my_country = get()
    # create the global item to search for
    global search_item
    # update the item to search for with user provided data
    search_item = f"https://{my_country}.indeed.com/{user_job}-jobs-in-{user_location}"

    # make a request to linkedin.com
    try: req  = requests.get(search_item)
    except Exception: print("Could not make the indeed.com request. Please check that indeed supports your country!")
    # make the request a BeautifulSoup element
    soup = BeautifulSoup(req.content, "html.parser")

    # print the website were we scrapped the results from
    print("Website: indeed", end = "")
    # next operation in line is to print the number of jobs on the website
    number_of_jobs(soup)

# function to isolate the number of jobs out of a string like: page 1 of <<200>> jobs
def isolate_number(soup):
    # isolate the div containing the number of jobs
    soup = soup.find("div", id="searchCountPages").get_text()
    # split the soup element in a list of strings
    soup_list = soup.split(" ")

    # the number of jobs is for sure a digit so we will retain only digits and for sure last because it is the last number of the string list
    # so we retain the last number in the string
    for index in range(len(soup_list)):
        if soup_list[index].isdigit():  number_of_jobs = soup_list[index]

    return number_of_jobs

def number_of_jobs(soup):
    # print the number of jobs on the website
    try: print("\t\tNumber of jobs:", isolate_number(soup))
    except Exception: print("\t\tNumber of jobs: missing data")
    print("\n")

def visit():
    print("Opening: ", search_item)
    print("\n")
    # open the website you want to visit in the webbrowser
    webbrowser.open(search_item)