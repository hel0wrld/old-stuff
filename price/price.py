from bs4 import BeautifulSoup
import requests
import time
n = int(input('1 for btc and 2 for eth\n'))
while True:
	URL = 'https://in.investing.com/crypto/'
	header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36'}
	page = requests.get(URL,headers=header)
	soup = BeautifulSoup(page.content, 'html.parser')
	coins = soup.find_all('tr')
	coin = coins[n]
	name = coin.find('td', class_='left bold elp name cryptoName first js-currency-name').find('a').string
	price = coin.find('td', class_="price js-currency-price").find('a').string
	print(name, end=" ")
	print(price)
	#time.sleep(2)
	#price = coins[n-1].find('td', class_="price js-currency-price").find('a').string
	#print(price)