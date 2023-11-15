import requests
import random
import time
from bs4 import BeautifulSoup

# list.txt ファイルからURLを読み込む
with open('shop_info_url_list.txt', 'r', encoding='utf-8') as file:
    urls = file.read().splitlines()

# 出力ファイルを開く
with open('sales_list.txt', 'w', encoding='utf-8') as output_file:
    # 各URLに対してリクエストを送信し、データを取得
    for url in urls:
        random_number = random.randint(1, 5)
        time.sleep(random_number)
        # 人間がやってるふうに見せる

        category, shop_url = url.split(',')

        response = requests.get(shop_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # elRowContent クラスを持つすべての要素を取得
        elements = soup.find_all(class_='elRowContent')

        # 各要素のテキストコンテンツを取得し、リストに格納
        lines = [element.get_text(separator=',', strip=True) for element in elements]
        lines.insert(0, shop_url)
        new_lines = [element.replace("\n", "") for element in lines]
        if len(new_lines) > 9:
        # infoページがない場合の処理もっといい書き方あると思う

            if new_lines[9].startswith('〒'):
                new_lines.insert(8, "")

            print(new_lines)
            if "@" in new_lines[13]:
                new_lines.insert(13, "")

            df = ';'.join(new_lines)
            # print(df)
            
            # ファイルに書き込む
            output_file.write(category + ';' + df + '\n')