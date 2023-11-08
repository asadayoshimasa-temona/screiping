import requests
from bs4 import BeautifulSoup
import pandas as pd

# URLを指定
url = 'https://store.shopping.yahoo.co.jp/lorelife/info'

# URLからページの内容を取得
response = requests.get(url)

# BeautifulSoupオブジェクトを作成し、パーサーを指定
soup = BeautifulSoup(response.text, 'html.parser')

# elRowContent クラスを持つすべての要素を取得
elements = soup.find_all(class_='elRowContent')

# 各要素のテキストコンテンツを取得し、リストに格納
lines = [element.get_text(separator=',', strip=True) for element in elements]
df = ','.join(lines)
# print(df)
with open('response.csv', 'w', encoding='utf-8') as file:
    file.write(df)
# リストをDataFrameに変換
# df = pd.DataFrame(lines)

# DataFrameをCSVファイルに書き出し
# df.to_csv('response.csv', index=False, header=False)

print('response.csv にデータが保存されました。')

