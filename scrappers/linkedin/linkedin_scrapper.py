from bs4 import BeautifulSoup
import requests

def demo():
    # get user wanted job
    user_job = "software developer"#input("job: ")
    # get user wanted location
    user_location = "cluj"#input("location: ")
    
    # create the item to search for
    search_item = f"https://www.linkedin.com/jobs/search?keywords={user_job}&location={user_location}&position=1&pageNum=0"
    # make a request to linkedin.com
    req  = requests.get(search_item)
    # make the request a BeautifulSoup element
    soup = BeautifulSoup(req.content, "html.parser")

    # make the request readable
    soup = soup.prettify()  

    # print the request
    print(soup)