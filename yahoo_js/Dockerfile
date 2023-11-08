# 安定版のNode.jsイメージを使用
# FROM node:latest
# FROM node:buster
FROM --platform=linux/arm64/v8 node:16

# アプリケーションディレクトリを作成
WORKDIR /app

# アプリケーションの依存関係をインストール
# パッケージ.jsonとパッケージ.lock.jsonをコピー
COPY package*.json ./

RUN npm install
RUN npm install axios cheerio
RUN npm install fs
RUN npm install puppeteer
# いるかこれ

# Install Puppeteer dependencies
RUN apt-get update && apt-get install -y \
    wget \
    ca-certificates \
    apt-transport-https \
    gnupg \
    hicolor-icon-theme \
    fontconfig \
    fonts-noto-color-emoji \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdrm2 \
    libdbus-1-3 \
    libexpat1 \
    libfontconfig1 \
    libgbm1 \
    libgtk-3-0 \
    libnspr4 \
    libnss3 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxkbcommon0 \
    libxrandr2 \
    xdg-utils \
    libu2f-udev \
    libvulkan1 \
    libxcb-dri3-0 \
    libxshmfence1 \
    libegl1 \
    libx11-xcb1 \
    libgles2 \
    libgl1 \
    libpci3 \
    libasound2 \
    && rm -rf /var/lib/apt/lists/*


# アプリケーションのソースをバンドル
COPY . .

# アプリケーションを実行
# CMD [ "node", "your-script.js" ]