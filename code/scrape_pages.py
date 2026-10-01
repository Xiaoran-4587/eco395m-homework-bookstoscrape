from common import get_soup
from urllib.parse import urljoin


def scrape_page(num):
   
    page_number = str(num)
    page_url = "http://books.toscrape.com/catalogue/page-" + page_number + ".html"

    soup = get_soup(page_url)

    books = soup.find_all("article", class_="product_pod")

    book_urls = []

    for book in books:
        heading = book.find("h3")
        link = heading.find("a")
        relative_url = link["href"]

        full_url = urljoin(page_url, relative_url)
        book_urls.append(full_url)

    return book_urls


def scrape_all_pages():
    all_book_urls = []
    page_number = 1

    while True:
        book_urls = scrape_page(page_number)

        if len(book_urls) == 0:
            break

        for book_url in book_urls:
            all_book_urls.append(book_url)

        print("Finished page:", page_number)

        page_number = page_number + 1

    return all_book_urls


if __name__ == "__main__":

    page_3_actual_book_urls = [
        "http://books.toscrape.com/catalogue/slow-states-of-collapse-poems_960/index.html",
        "http://books.toscrape.com/catalogue/reasons-to-stay-alive_959/index.html",
        "http://books.toscrape.com/catalogue/private-paris-private-10_958/index.html",
        "http://books.toscrape.com/catalogue/higherselfie-wake-up-your-life-free-your-soul-find-your-tribe_957/index.html",
        "http://books.toscrape.com/catalogue/without-borders-wanderlove-1_956/index.html",
        "http://books.toscrape.com/catalogue/when-we-collided_955/index.html",
        "http://books.toscrape.com/catalogue/we-love-you-charlie-freeman_954/index.html",
        "http://books.toscrape.com/catalogue/untitled-collection-sabbath-poems-2014_953/index.html",
        "http://books.toscrape.com/catalogue/unseen-city-the-majesty-of-pigeons-the-discreet-charm-of-snails-other-wonders-of-the-urban-wilderness_952/index.html",
        "http://books.toscrape.com/catalogue/unicorn-tracks_951/index.html",
        "http://books.toscrape.com/catalogue/unbound-how-eight-technologies-made-us-human-transformed-society-and-brought-our-world-to-the-brink_950/index.html",
        "http://books.toscrape.com/catalogue/tsubasa-world-chronicle-2-tsubasa-world-chronicle-2_949/index.html",
        "http://books.toscrape.com/catalogue/throwing-rocks-at-the-google-bus-how-growth-became-the-enemy-of-prosperity_948/index.html",
        "http://books.toscrape.com/catalogue/this-one-summer_947/index.html",
        "http://books.toscrape.com/catalogue/thirst_946/index.html",
        "http://books.toscrape.com/catalogue/the-torch-is-passed-a-harding-family-story_945/index.html",
        "http://books.toscrape.com/catalogue/the-secret-of-dreadwillow-carse_944/index.html",
        "http://books.toscrape.com/catalogue/the-pioneer-woman-cooks-dinnertime-comfort-classics-freezer-food-16-minute-meals-and-other-delicious-ways-to-solve-supper_943/index.html",
        "http://books.toscrape.com/catalogue/the-past-never-ends_942/index.html",
        "http://books.toscrape.com/catalogue/the-natural-history-of-us-the-fine-art-of-pretending-2_941/index.html",
    ]

    page_3_book_urls = scrape_page(3)

    assert set(page_3_book_urls) == set(page_3_actual_book_urls)
  
    print(page_3_book_urls)
    print("Number of books:", len(page_3_book_urls))

    all_book_urls = scrape_all_pages()

    print("Total books:", len(all_book_urls))

    assert len(all_book_urls) == 1000
    assert len(set(all_book_urls)) == 1000

    print("All pages test passed!")