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
# from datetime import datetime

# with open('shop_info_url_list.txt', 'a') as file:
#     current_time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     # 文字列としてファイルに書き込む
#     file.write(current_time_str + "\n")

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
    # print(search_results_count)
    # print(search_results_category.get_text())
    

    print(search_results_count.get_text().replace(",", "").replace("件", ""))
    # 件数を取得し、数値型に変換
    # 10回スクロールさせるところをこの数/30に変更すれば自動化いけるか
    print(url)
    scroll_num = 30 if url in ['https://shopping.yahoo.co.jp/category/2498/list/', 'https://shopping.yahoo.co.jp/category/2499/list/', 'https://shopping.yahoo.co.jp/category/2500/list/', 'https://shopping.yahoo.co.jp/category/2501/list/', 'https://shopping.yahoo.co.jp/category/2509/list/'] else 10
    sleep_time = 3
    print(scroll_num)

    # スクロールする回数を計算（例：全件数 / 1ページあたりの件数）
    for _ in range(scroll_num):
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        time.sleep(sleep_time)  # ページがロードされるのを待つ

    # BeautifulSoupを使用してページの内容を解析
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # 対象のクラスを持つ要素の href を取得
    # matching_hrefs = [elem.get('href') for elem in soup.select('.SearchResultItemStore_SearchResultItemStore__rXVLG') if elem.get('href').startswith('https://store.shopping.yahoo.co.jp/')]
    # non_matching_hrefs = [elem.get('href') for elem in soup.select('.SearchResultItemStore_SearchResultItemStore__rXVLG') if not elem.get('href').startswith('https://store.shopping.yahoo.co.jp/')]
    # 対象の要素を選択
    elements = soup.select('.SearchResultItemStore_SearchResultItemStore__rXVLG')
    print(len(elements))
    # 条件にマッチする href をリストに格納
    matching_hrefs = []
    for elem in elements:
        href = elem.get('href')
        if href and href.startswith('https://store.shopping.yahoo.co.jp/'):
            matching_hrefs.append(href)
            with open('shop_info_url_list_all.txt', 'a') as file:
                file.write(href + "info.html" + "\n")
        else:
            random_number = random.randint(1, 5)
            time.sleep(random_number)
            driver.get(href)
            print(driver.current_url)
            matching_hrefs.append(driver.current_url)
            with open('shop_info_url_list_all.txt', 'a') as file:
                file.write(driver.current_url + "info.html" + "\n")
        


    unique_urls = list(set(matching_hrefs))
    # yahooの店舗詳細ページ持ってたらURLをshop_info_url_list.txtに格納
    with open('shop_info_url_list.txt', 'a') as file:
        for href in unique_urls:
            file.write(search_results_category.get_text() + ',' + href + "info.html" + "\n")

    # yahooの店舗詳細ページ持ってなければURLをexception_shop_info_url_list.txtに格納
    # with open('exception_shop_info_url_list.txt', 'a') as file:
    #     for href in non_matching_hrefs:
    #         driver.get(href)
    #         print(driver.current_url)
    #         file.write(search_results_category.get_text() + ',' + href + "\n")

# ブラウザを閉じる
driver.quit()
# with open('shop_info_url_list.txt', 'a') as file:
#     current_time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     # 文字列としてファイルに書き込む
#     file.write(current_time_str + "\n")