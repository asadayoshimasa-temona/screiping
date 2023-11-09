from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time


# ChromeOptionsを設定（必要に応じて）
options = Options()
options.add_argument('--headless')  # ヘッドレスモードで実行。
options.add_argument('--no-sandbox')  # OSのセキュリティモデルをバイパス。
options.add_argument('--disable-dev-shm-usage')
# options.add_argument('--headless')  # ヘッドレスモードで実行する場合など

# WebDriverのServiceオブジェクトを作成
# 実際のchromedriverのパスに置き換えてください
service = Service(executable_path='/usr/bin/chromedriver')

# WebDriverを起動
driver = webdriver.Chrome(service=service, options=options)

# URLを開く
url = 'https://shopping.yahoo.co.jp/category/2496/list?p=&area=13&astk=&first=1&ss_first=1&ts=1699412102&mcr=b80fa60dde8057ac1d85b8b4167e0ffc&tab_ex=commerce&sretry=1&sc_i=shp_pc_search_searchBox_2&sretry=1'
driver.get(url)


response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
search_results_count = soup.find(class_='SearchResultsDisplayOptions_SearchResultsDisplayOptions__count__WBsPf')
# print(search_results_count.get_text().replace(",", "").replace("件", ""))


wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'SearchBox__optionTrigger--filtered')))

# クラス名が'SearchBox__optionTrigger--filtered'の要素をクリックしてモーダルを開く
element.click()

# モーダルが表示されるのを待つ
modal = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'SearchBox__filterPulldown')))

# selectボックスの値を取得
select_values = [option.get_attribute('value') for option in modal.find_elements(By.TAG_NAME, 'option')]


numeric_select_values = []
for value in select_values:
    try:
        # 整数に変換を試みる
        numeric_value = int(value)
        numeric_select_values.append(numeric_value)
    except ValueError:
        # 変換できない場合は無視するか、適切な処理を行う
        print(f"Value '{value}' cannot be converted to an integer.")

url_template = 'https://shopping.yahoo.co.jp/category/{}/list/'
category_urls = [url_template.format(value) for value in numeric_select_values]
print(category_urls)

with open('shop_category_index_url.txt', 'w') as file:
    for category_url in category_urls:
        file.write(category_url + "\n")

driver.quit()