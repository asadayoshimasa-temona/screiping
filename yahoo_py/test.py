import requests
from bs4 import BeautifulSoup

url = 'https://ck.storematch.jp/rd?v=4.2&c=1K&campaign_id=4ZE&cat=6cV&code=iloveheaven_3038&date=eluhke&debug=0&ecsite_id=1&frequency_control_group=-&ope=1&page=3&pos=8&qid=17w&rid=ZVMtvgABGHW3T_uOCoMhMwqDALkClQ&rqcat=Ee&search_keyword=&sig=sVg77xIVtIa49Jf24XwFFGt69x/aTamkcb5lSgXvQ64=&site_browser_id=4eafa5a370d0b9ff8d0cd5e803242ddc29eae5959073c2878e98c2cb424c2cda&site_user_id=&uid=4ZE&url_type=2'  # 初期URL
response = requests.get(url)
# soup = BeautifulSoup(response.content, 'html.parser')

# 現在のURLを取得
print(response.url)


