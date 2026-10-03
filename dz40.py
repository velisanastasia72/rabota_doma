import requests
from bs4 import BeautifulSoup
import csv
import time


class Book:

    def __init__(self, title, price, stock_status):
        self.title = title
        self.price = price
        self.stock_status = stock_status

    def to_dict(self):
        return {
            'title': self.title,
            'price': self.price,
            'stock': self.stock_status
        }

    def __str__(self):
        return f"{self.title} | {self.price}"


class Scraper:


    def __init__(self, base_url):
        self.base_url = base_url
        self.all_books = []
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

    def get_page(self, url):
        print(f"Загрузка страницы: {url}")
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Ошибка загрузки: {e}")
            return None

    def parse_page(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        articles = soup.find_all('article', class_='product_pod')
        page_books = []

        for article in articles:
            title = article.find('h3').find('a')['title']


            price = article.find('p', class_='price_color').text.replace('Â£', '')


            stock = article.find('p', class_='instock availability').text.strip()


            book = Book(title, price, stock)
            page_books.append(book)

        return page_books

    def get_next_page_url(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        next_btn = soup.find('li', class_='next')

        if next_btn:
            relative_url = next_btn.find('a')['href']
            base = self.base_url.replace('index.html', '')
            return f"{base}{relative_url}"
        return None

    def run(self, max_pages=3):
        current_url = self.base_url
        page_count = 1

        while current_url and page_count <= max_pages:
            print(f"\n--- Обработка страницы {page_count} ---")

            html = self.get_page(current_url)
            if not html:
                break

            books = self.parse_page(html)
            self.all_books.extend(books)
            print(f"Найдено книг на странице: {len(books)}")


            current_url = self.get_next_page_url(html)
            page_count += 1

            time.sleep(1)

        print(f"\nПарсинг завершен. Всего собрано книг: {len(self.all_books)}")

    def save_to_csv(self, filename='books_result.csv'):
        if not self.all_books:
            print("Нет данных для сохранения.")
            return

        with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
            writer = csv.DictWriter(f, fieldnames=['title', 'price', 'stock'], delimiter=';')
            writer.writeheader()

            for book in self.all_books:
                writer.writerow(book.to_dict())

        print(f"Данные сохранены в файл: {filename}")


if __name__ == '__main__':
    scraper = Scraper("https://books.toscrape.com/index.html")

    scraper.run(max_pages=3)

    scraper.save_to_csv()