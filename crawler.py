import requests
from bs4 import BeautifulSoup
import json
import time

def mycrawler():
    """ 
    this function is the crawler which parses throuhh the coventry university school of economic,finance and accounting websites and retrives 
    details about publications on the website. 
    """ 
    url = "https://pureportal.coventry.ac.uk/en/organisations/school-of-economics-finance-and-accounting/publications/?page="
    html = requests.get(url)
    soup = BeautifulSoup(html.text, "html.parser")
    page_tag = soup.find('nav',{'class':'pages'}) 
    number_of_pages = len(page_tag.findAll('li')) # get the total number of pages to control the while loop.
    crawled_data = [] #stores the list of dictionaries which contain details about each publication.
    count = 0
    while (count < number_of_pages): 
        new_url = url + str(count)
        count +=1
        print("fetching: ", new_url)
        html = requests.get(new_url)
        soup = BeautifulSoup(html.text, "html.parser")
        publications = soup.findAll("h3",{"class":"title"})
        for p in publications:
            publication_details = {} # disctionary of each publication with name of item as key and the details as values
            publication_title = p.get_text()
            publication_link = p.a.get("href")
            new_url = publication_link
            html = requests.get(new_url)
            time.sleep(1)
            soup = BeautifulSoup(html.text, "html.parser")
            authors = soup.find("p",{"class":"relations persons"}).get_text()  
            get_abstract = soup.find("div",{"class":"textblock"})
            date = soup.find("span", {"class":"date"}).get_text() 
            author_link = soup.findAll("a",{"class":"link person"})   
            author_links = []  
            for link in author_link:
                authlink = link.get("href")
                author_links.append(authlink)
            if get_abstract is None:
                abstract = " "
            else: 
                abstract = get_abstract.get_text()
            publication_details.update([                                
                                ("publication title", publication_title),
                                ("abstract",abstract),
                                ("authors", authors),
                                ("publication link", publication_link),
                                ("authors link", author_links),
                                ("publication date", date)
                                ])
            crawled_data.append(publication_details)
            with open("data/database.json", "w") as jsonfile: #storing the crawled_data list as a json file
                json.dump(crawled_data, jsonfile, indent=4)
    else:
        print(f"Crawling Completed with {count} number of pages")