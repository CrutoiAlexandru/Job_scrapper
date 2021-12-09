from bs4 import BeautifulSoup
import requests
import webbrowser

def set_search_item(user_job, user_location):
    # create the global item to search for
    global search_item
    # update the location of the user with a valid city from romania
    user_location = check_for_city(user_location)
    # update the item to search for with user provided data
    search_item = f"https://www.ejobs.ro/locuri-de-munca/{user_location}/{user_job}"

    # make a request to ejobs.ro
    req  = requests.get(search_item)
    # make the request a BeautifulSoup element
    soup = BeautifulSoup(req.content, "html.parser")

    # print the website were we scrapped the results from
    print("Website: ejobs", end = "")
    # next operation in line is to print the number of jobs on the website
    number_of_jobs(soup)

def number_of_jobs(soup):
    # print the number of jobs on the website
    print("\t\tNumber of jobs:", soup.find("h1", class_="SearchInfo").find("span").get_text().replace("\n", "").replace(" ", ""))
    print("\n")

def visit():
    print("Opening: ", search_item)
    print("\n")
    # open the website you want to visit in the webbrowser
    webbrowser.open(search_item)

# ejobs needs an exact name of the city you are looking for so we are going to check the user input against a list of Romania cities
# the list we are going to gather from https://ro.wikipedia.org/wiki/Lista_orașelor_din_România
def check_for_city(user_location):
    # make a request to the ^ link
    req  = requests.get("https://ro.wikipedia.org/wiki/Lista_orașelor_din_România")
    # make the request a BeautifulSoup element
    soup = BeautifulSoup(req.content, "html.parser")

    # retrieve the cities as a list
    city_list = soup.find("div", class_="div-col columns column-width").find_all("a")

    # iterate through the list in order to find a match
    for index in range(len(city_list)):
        # strip the list into single string 
        actual_city = city_list[index].get_text()
        actual_city = actual_city.lower()
        #strip romanian characters from both string in order to avoid accidents
        actual_city   = actual_city.replace("ă", "a").replace("â", "a").replace("î", "i").replace("ș", "s").replace("ț", "t")
        user_location = user_location.replace("ă", "a").replace("â", "a").replace("î", "i").replace("ș", "s").replace("ț", "t")
        # if the strings match return the actual name of the city
        if user_location in actual_city: return actual_city
    
    # unless the user_location matches an actual city from Romania return an empty string
    # this way the search will not take in consideration any specific location and will give results country wide
    return "" 
