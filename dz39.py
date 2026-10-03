import requests
from bs4 import BeautifulSoup
import csv


URL = "https://books.toscrape.com/"


def parse_books(url):
    print(f"Загрузка данных с {url}...")


    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Ошибка при загрузке страницы: {e}")
        return []


    soup = BeautifulSoup(response.text, 'html.parser')


    books_articles = soup.find_all('article', class_='product_pod')

    books_data = []

    for book in books_articles:
        title_tag = book.find('h3').find('a')
        title = title_tag['title']


        price_tag = book.find('p', class_='price_color')
        price = price_tag.text.replace('Â£', '')


        stock_tag = book.find('p', class_='instock availability')
        stock = stock_tag.text.strip()


        books_data.append({
            'title': title,
            'price': price,
            'stock': stock
        })

    return books_data


def save_to_csv(data, filename='books.csv'):
    if not data:
        print("Нет данных для сохранения.")
        return


    headers = ['title', 'price', 'stock']

    with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=headers, delimiter=';')


        writer.writeheader()


        writer.writerows(data)

    print(f"Данные успешно сохранены в файл '{filename}' ({len(data)} записей).")



if __name__ == '__main__':
    books = parse_books(URL)


    print("\n--- Пример полученных данных ---")
    for b in books[:3]:
        print(f"Книга: {b['title']} | Цена: {b['price']} | Статус: {b['stock']}")
    print("------------------------------\n")


    save_to_csv(books)