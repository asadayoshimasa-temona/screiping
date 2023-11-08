const axios = require('axios');
const cheerio = require('cheerio');
const fs = require('fs');

const url = 'https://store.shopping.yahoo.co.jp/lorelife/info';

axios.get(url)
  .then(response => {
    const html = response.data;
    const $ = cheerio.load(html);

    // mdInformationTable クラスの要素のテキストコンテンツを取得
    const mdInformationTableText = $('.elRowContent').text();

    // 改行で分割して配列に格納
    const lines = mdInformationTableText.split('\n').map(line => line.trim()).filter(line => line);
    console.log(lines);

    // 配列をCSV形式の文字列に変換
    const csv = lines.join(',')

    // CSV文字列をファイルに書き込み
    fs.writeFile('response.csv', csv, (err) => {
      if (err) {
        console.error('ファイル書き込み中にエラーが発生しました:', err);
      } else {
        console.log('response.csv にデータが保存されました。');
      }
    });
  })
  .catch(error => {
    console.error('スクレイピング中にエラーが発生しました:', error);
  });
