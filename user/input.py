import scrappers.linkedin.linkedin_scrapper as linkedin_scrapper
import scrappers.ejobs.ejobs_scrapper as ejobs_scrapper
import scrappers.indeed.indeed_scrapper as indeed_scrapper
import scrappers.jooble.jooble_scrapper as jooble_scrapper

def start():
    # get user wanted job
    user_job = "software developer"#input("job: ")
    # get user wanted location
    user_location = "bucuresti"#input("location: ")

    # start scrapping linkedin data
    linkedin_scrapper.set_search_item(user_job, user_location)
    # start scrapping ejobs data
    ejobs_scrapper.set_search_item(user_job, user_location)
    # start scrapping indeed data
    indeed_scrapper.set_search_item(user_job, user_location)
    # start scrapping indeed data
    jooble_scrapper.set_search_item(user_job, user_location)

    open_website()

def open_website():
    # get the website the user wants to visit
    wanted_website = input("Enter the name of the website you wish to visit(type q to exit): ")
    print("\n")

    # check for certain website and open it
    if wanted_website.lower() == "linkedin": linkedin_scrapper.visit()

    if wanted_website.lower() == "ejobs": ejobs_scrapper.visit()

    if wanted_website.lower() == "indeed": indeed_scrapper.visit()

    if wanted_website.lower() == "jooble": jooble_scrapper.visit()

    if wanted_website.lower() == "q": return

    # check again until user quits
    return # right now quit on first run
    open_website()