import requests
from bs4 import BeautifulSoup

class Scraper:


        def scrape(url, html_elm, id_or_class, tag): 
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            job_elems
            if(tag == 'id'):
                job_elems = soup.find(id=id_or_class)
            else:
                job_elems = soup.find("div", class_=id_or_class)


    
            print(job_elems.prettify())
            return job_elems  