FROM python:3.8

WORKDIR app

RUN apt-get update
RUN apt-get install -y chromium-driver

RUN pip install requests beautifulsoup4 pandas
RUN pip install selenium


# COPY ./chromedriver /usr/local/bin/chromedriver

# ローカルマシンのファイルをコンテナにコピー
COPY . .

# コンテナが起動したときに実行されるコマンド
# CMD [ "python", "./hello.py" ]