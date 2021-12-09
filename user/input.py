import scrappers.linkedin.linkedin_scrapper as linkedin_scrapper

def start():
    # get user wanted job
    user_job = "software developer"#input("job: ")
    # get user wanted location
    user_location = "cluj"#input("location: ")

    # start the demo run on the linkedin scrapper
    linkedin_scrapper.set_search_item(user_job, user_location)

    open_website()

def open_website():
    # get the website the user wants to visit
    wanted_website = input("Enter the name of the website you wish to visit(type quit to exit): ")
    print("\n")

    # check for certain website and open it
    if wanted_website.lower() == "linkedin": linkedin_scrapper.visit()

    if wanted_website.lower() == "quit": return

    # if the user entered an invalid value check again
    print("Enter a valid name!")
    print("\n")
    open_website()