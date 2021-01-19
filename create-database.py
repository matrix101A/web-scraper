import requests, bs4

def scrape_it(link):
    res = requests.get(link)
    soup = bs4.BeautifulSoup(res.content,'html.parser')

        


links = open("question-links.txt","r")

for link in links:
    scrape_it(link)
    break