#using CoinGeckoAPI
#Donation ETH/Erc20 address: 0x172aa811d2F81b71D7c774a96295A9001242F815


from pycoingecko import CoinGeckoAPI
import time
from datetime import datetime

cg = CoinGeckoAPI()

holding = int(input("How much Statera tokens do you own: "))
delay = int(input('Choose update delay (in seconds, recomended 60): '))
print('------')

while True:
	price = cg.get_price(ids='statera', vs_currencies='usd')
	value = list((list(price.values())[0]).values())[0]
	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")
	print('STA Price: $',value)
	print('Your STA is valued at: $',value*holding)
	print("Last Updated =", current_time)
	print('------')
	time.sleep(delay)
