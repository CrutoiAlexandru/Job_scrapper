# Job_scrapper
An application made to ease your online job searching expanding one search across multiple popular job websites.

## Web scraping project
This project is mainly an experiment to see learn a bit about web scrapping. It mainly uses python requests and beautifulsoup.

## How it works
The program takes in input about a job and a location and outputs the number of jobs on one of the implemented websites. The number of supported websites can easily change.

More user input can be made so that it can have job filters.

The way it works is it searches the websites for those certain parameters and scrapes the number of jobs given on the page.

For some pages it needs to also find out which country you are in with the help of the ip address.

Some pages like ejobs also need an exact location, like the exact name of a countries city. For that it gets data from wikipedia where there is a list of the cities and matches the input of the user with a specific city.
