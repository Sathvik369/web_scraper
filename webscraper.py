# import requests
from bs4 import BeautifulSoup
import csv

with open("amazon.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

    # url = 'https://www.amazon.in/your/product/page/url'

    # response = requests.get(url)

    # #for successful response
    # if response.status_code == 200:
    #     soup = BeautifulSoup(response.content, 'html.parser')

    products = []

    all_divs = soup.find_all(
        "div",
        class_="puis-card-container s-card-container s-overflow-hidden aok-relative puis-expand-height puis-include-content-margin puis puis-v1ptg7iq6f5f4u2smovb1ai55ug s-latency-cf-section puis-card-border",
    )

    for div in all_divs:
        product_name = ""
        price = ""
        ratings = ""

        try:
            product_name_element = div.find(
                "span", class_="a-size-base-plus a-color-base a-text-normal"
            )
            if product_name_element:
                product_name = product_name_element.text.strip()
        except AttributeError:
            pass

        try:
            price_element = div.find("span", class_="a-price-whole")
            if price_element:
                price = price_element.text.strip()
        except AttributeError:
            pass

        try:
            ratings_element = div.find("span", class_="a-icon-alt")
            if ratings_element:
                ratings = ratings_element.text.strip()
        except AttributeError:
            pass

        products.append(
            {"product_name": product_name, "price": price, "ratings": ratings}
        )

    with open("amazon_products.csv", "w", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(
            csvfile, fieldnames=["product_name", "price", "ratings"]
        )
        writer.writeheader()
        writer.writerows(products)

    print("Product data extracted and saved to 'amazon_products.csv'")

# else:
#   print(f"Error: Request failed with status code: {response.status_code}")
