import os
import csv
import json

from scrape_pages import scrape_all_pages
from scrape_books import scrape_books


def scrape():
    book_urls = scrape_all_pages()

    print("Total book links:", len(book_urls))

    books = scrape_books(book_urls)

    return books


def write_books_to_csv(books, path):
    fieldnames = [
        "upc",
        "title",
        "category",
        "description",
        "price_gbp",
        "stock"
    ]

    with open(path, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        for book in books:
            writer.writerow(book)


def write_books_to_jsonl(books, path):
    with open(path, "w", encoding="utf-8") as file:
        for book in books:
            line = json.dumps(book, ensure_ascii=False)

            file.write(line)
            file.write("\n")


if __name__ == "__main__":
    base_dir = "artifacts"

    os.makedirs(base_dir, exist_ok=True)

    csv_path = os.path.join(base_dir, "results.csv")
    jsonl_path = os.path.join(base_dir, "results.jsonl")

    books = scrape()

    print("Total books:", len(books))

    assert len(books) == 1000

    write_books_to_csv(books, csv_path)
    print("CSV saved:", csv_path)

    write_books_to_jsonl(books, jsonl_path)
    print("JSONL saved:", jsonl_path)

    print("Scraping completed!")
