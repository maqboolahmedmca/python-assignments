import requests
import bs4
books_scrape_url = "http://books.toscrape.com/catalogue/page-{}.html"
page=1

print("fetching all 2 star books from the books.toscrape.com")

# you can increase the page till 50 below as there are 50 pages in the website
while page <= 5:
    books_res = requests.get(books_scrape_url.format(page))
    soup = bs4.BeautifulSoup(books_res.text, "lxml")
    elements = soup.select('.star-rating.Two')
    if (len(elements) == 0):
        break
    for elem in elements:
        title = elem.find_next_sibling().select('a')[0]['title']
        print(title)
        
    page+=1