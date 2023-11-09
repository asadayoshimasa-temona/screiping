

import requests
from bs4 import BeautifulSoup

# list.txt ファイルからURLを読み込む
with open('list.txt', 'r', encoding='utf-8') as file:
    urls = file.read().splitlines()

# 出力ファイルを開く
with open('respons.csv', 'w', encoding='utf-8') as output_file:
    # 各URLに対してリクエストを送信し、データを取得
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # elRowContent クラスを持つすべての要素を取得
        elements = soup.find_all(class_='elRowContent')

        # 各要素のテキストコンテンツを取得し、リストに格納
        lines = [element.get_text(separator=',', strip=True) for element in elements]
        df = ','.join(lines)
        
        # ファイルに書き込む
        output_file.write(df + '\n')