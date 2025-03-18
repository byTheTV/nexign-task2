from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import re
from webdriver_manager.chrome import ChromeDriverManager

def fetch_page_content(url):
    try:
        chrome_options = Options()
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get(url)
        page_content = driver.page_source
        driver.quit()
        return page_content
    except Exception as e:
        print(f"Error fetching URL with Selenium: {e}")
        return None

def count_nexign_mentions(text):
    return len(re.findall(r"Nexign", text, re.IGNORECASE))

def save_to_file(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(data)

if __name__ == "__main__":
    url = "https://nexign.com/ru"
    html_filename = "page_content.html"

    page_content = fetch_page_content(url)

    if page_content:
        save_to_file(html_filename, page_content)
        print(f"Page content saved to {html_filename}")

        soup = BeautifulSoup(page_content, 'html.parser')
        text_content = soup.get_text()

        mentions_count = count_nexign_mentions(text_content)
        print(f'В контенте главной страницы сайта слово "Nexign" упомянуто {mentions_count} раз.')

