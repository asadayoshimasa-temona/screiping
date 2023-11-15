from requests import Session
url = "https://ck.storematch.jp/rd?v=4.2&c=p&campaign_id=9y9&cat=cHr&code=mobile-p_wa-30days&date=elugCP&debug=0&ecsite_id=1&frequency_control_group=-&ope=3&page=6&pos=5&qid=17w&rid=ZVMkCwAGpc-3T_uTCoMglgqDAWRsrQ&rqcat=cpN&search_keyword=&sig=vepqYMSUNfWX/jnPE0M8Y+5FzS9kYJYYf09z7pCnCbU=&site_browser_id=dc345a1bdcd00155b9b859fd7c7c2570a0aad673856dce251ce29f9d25400c2c&site_user_id=&uid=9y9&url_type=2"
# セッションを作成
session = Session()

# リダイレクトの上限を設定
session.max_redirects = 50

# リクエストを送信し、リダイレクトを許可
response = session.get(url, allow_redirects=True)
print(response)
final_url = response.url

print(final_url)
# アクセスするURL
