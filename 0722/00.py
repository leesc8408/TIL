# import 지정
import requests
# url을 요청  
url = f'https://api.bithumb.com/public/ticker/BTC_KRW'  # url 에 {order_currency}_{payment_currency} 직접 입력
# 응답값 받고
respon = requests.get(url)
# print(respon)해서 확인

# json 양식으로 전환
data = respon.json()
# data에서 전일종가 출력
print(data.get('data').get('prev_closing_price'))
