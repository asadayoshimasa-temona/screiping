# yahooショッピングから営業リストを作成する
test2を実行することで
https://store.shopping.yahoo.co.jp
から始まるリンクをlist.txtに出力
それ以外をlist_ex.txtに出力

test1を実行することでlist.txtに出力したリンクを元に営業リストを作成。
respons.csvに格納。


## 構築~実行
```sh
docker build -t yahoo-screiping-py ./yahoo_py
# Dockerfileからyahoo-screiping-pyという名前でイメージ作成
docker run -it -v $(pwd)/rakuten:/app screiping /bin/bash
# 上で作成したyahoo-screiping-pyのイメージからコンテナを作成し、そのコンテ内に入る
python python create_shop_info_url_list.py
# ショップのurlリスト作成
python create_sales_list.py
# ショップのurlリストから営業リストを作成
```
