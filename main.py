

from pyVinted import Vinted
import requests
bot_token = "5712231465:AAFUrOfBV6WPyY5Tl0hDLBvlV8aFu6EQIq0"
chat_id = "5063650572"
send_message_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
vinted = Vinted()
#https://www.vinted.co.uk/vetements?brand_id[]=73306&order=newest_first
items = vinted.items.search("https://www.vinted.co.uk/vetements?brand_id[]=73306&order=newest_first",10,1)
for item in items:
    print(item.price)
