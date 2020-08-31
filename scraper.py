import requests
from bs4 import BeautifulSoup

class Scraper:


    def scrape(url, html_elm, id_or_class, tag): 
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        job_elems = 0
        if(tag == 'id'):
            job_elems = soup.find(id=id_or_class)
        else if(tag == 'class'):
            job_elems = soup.find(html_elm, class_=id_or_class)



        print(job_elems.prettify())
        return job_elems
    # for testing
    URL = 'https://lyrics.fandom.com/wiki/Bob_Dylan:The_Times_They_Are_A-Changin\''
    scrape(URL, "div", "lyricbox", 'class')