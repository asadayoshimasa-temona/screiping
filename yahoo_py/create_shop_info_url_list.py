from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time
import requests
import random

# ChromeOptionsを設定（必要に応じて）
options = Options()
options.add_argument('--headless')  # ヘッドレスモードで実行。
options.add_argument('--no-sandbox')  # OSのセキュリティモデルをバイパス。
options.add_argument('--disable-dev-shm-usage')

# WebDriverのServiceオブジェクトを作成
service = Service(executable_path='/usr/bin/chromedriver')

# WebDriverを起動
driver = webdriver.Chrome(service=service, options=options)

with open('shop_category_index_url.txt', 'r') as file:
    urls = [line.strip() for line in file]

for url in urls:
    driver.get(url)

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    search_results_count = soup.find(class_='SearchResultsDisplayOptions_SearchResultsDisplayOptions__count__WBsPf')
    search_results_category = soup.find(class_='SearchResultHeader_SearchResultHeader__link__Gu9dB')
    time.sleep(1)

    # print(search_results_count.get_text().replace(",", "").replace("件", ""))
    # 件数を取得し、数値型に変換
    # 10回スクロールさせるところをこの数/30に変更すれば自動化いけるか
    scroll_num = 30 if url in ['https://shopping.yahoo.co.jp/category/2498/list/', 'https://shopping.yahoo.co.jp/category/2499/list/', 'https://shopping.yahoo.co.jp/category/2500/list/', 'https://shopping.yahoo.co.jp/category/2501/list/', 'https://shopping.yahoo.co.jp/category/2509/list/'] else 10
    sleep_time = 3

    for _ in range(scroll_num):
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        time.sleep(sleep_time)  # ページがロードされるのを待つ

    # BeautifulSoupを使用してページの内容を解析
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # 対象の要素を選択
    elements = soup.select('.SearchResultItemStore_SearchResultItemStore__rXVLG')
    print(len(elements))
    # 条件にマッチする href をリストに格納
    shop_hrefs = []
    for elem in elements:
        href = elem.get('href')

        # urlがhttps://store.shopping.yahoo.co.jp/で始まるものはそのまま書き込み、そうでないものはリダイレクト先のurlを書き込み
        if href and href.startswith('https://store.shopping.yahoo.co.jp/'):
            shop_hrefs.append(href)
            with open('shop_info_url_list_all.txt', 'a') as file:
                file.write(href + "info.html" + "\n")
        else:
            random_number = random.randint(1, 5)
            time.sleep(random_number)
            driver.get(href)
            shop_hrefs.append(driver.current_url)
            with open('shop_info_url_list_all.txt', 'a') as file:
                file.write(driver.current_url + "info.html" + "\n")

    unique_urls = list(set(shop_hrefs))
    # yahooの店舗詳細ページ持ってたらURLをshop_info_url_list.txtに格納
    with open('shop_info_url_list.txt', 'a') as file:
        for href in unique_urls:
            file.write(search_results_category.get_text() + ',' + href + "info.html" + "\n")

# ブラウザを閉じる
driver.quit()