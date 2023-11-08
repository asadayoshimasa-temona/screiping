# yahooショッピングから営業リストを作成する
## 構築~実行
```sh
docker build -t yahoo-screiping-py ./yahoo_py
# Dockerfileからyahoo-screiping-pyという名前でイメージ作成
docker run -it -v $(pwd)/rakuten:/app screiping /bin/bash
# 上で作成したyahoo-screiping-pyのイメージからコンテナを作成し、そのコンテ内に入る
python test.py
```
