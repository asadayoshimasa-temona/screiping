const axios = require('axios');
const cheerio = require('cheerio');

const url = 'https://shopping.yahoo.co.jp/category/2496/list?p=&area=13&astk=&first=1&ss_first=1&ts=1699412102&mcr=b80fa60dde8057ac1d85b8b4167e0ffc&tab_ex=commerce&sretry=1&sc_i=shp_pc_search_searchBox_2&sretry=1';

axios.get(url)
  .then(response => {
    const html = response.data;
    const $ = cheerio.load(html);
    const hrefs = [];

    // SearchResultItemStore_SearchResultItemStore__rXVLG クラスを持つ要素の href を取得
    $('.SearchResultItemStore_SearchResultItemStore__rXVLG').each((i, elem) => {
      const href = $(elem).attr('href');
      hrefs.push(href);
    });

    // 結果をコンソールに表示
    console.log(hrefs);
  })
  .catch(error => {
    console.error('スクレイピング中にエラーが発生しました:', error);
  });




// const puppeteer = require('puppeteer');

// (async () => {
//   const url = 'https://shopping.yahoo.co.jp/category/2496/list?p=&area=13&astk=&first=1&ss_first=1&ts=1699412102&mcr=b80fa60dde8057ac1d85b8b4167e0ffc&tab_ex=commerce&sretry=1&sc_i=shp_pc_search_searchBox_2&sretry=1';
//   const browser = await puppeteer.launch({ headless: true });
//   const page = await browser.newPage();
//   await page.goto(url, { waitUntil: 'networkidle2' });

//   let hrefs = [];
//   try {
//     // スクロールをシミュレートする
//     let previousHeight;
//     for (let i = 0; i < 10; i++) {
//       previousHeight = await page.evaluate('document.body.scrollHeight');
//       await page.evaluate('window.scrollTo(0, document.body.scrollHeight)');
//       await page.waitForFunction(`document.body.scrollHeight > ${previousHeight}`);
//       await page.waitForTimeout(1000); // スクロール後のコンテンツがロードされるのを待つ
//     }

//     // スクレイピングする
//     hrefs = await page.$$eval('a', anchors => anchors.map(anchor => anchor.href));
//   } catch (e) {
//     console.error(e);
//   }

//   console.log(hrefs);
//   await browser.close();
// })();