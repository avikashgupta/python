import requests

import bs4

base_url = "https://books.toscrape.com/catalogue/page-{}.html"

three_star_titles = []

for n in range(1,51):
    scrape_url = base_url.format(n)
    result = requests.get(scrape_url)
    soup = bs4.BeautifulSoup(result.text,"lxml")
    books = soup.select(".product_pod")
    
    for i in books:
        if len(i.select(".star-rating.Three")) != 0:
        #if "star-rating Three" in str(books):
            book_title = i.select("a")[1]["title"]
            three_star_titles.append(book_title)

print(three_star_titles)
