import requests

from twilio.rest import Client

account_sid = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
auth_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxx'



api_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"

url = "https://api.openweathermap.org/data/2.5/forecast"
para = {'lat': 39.364285,'lon': -74.422928,'appid':api_key,'cnt':4}
res = requests.get(url=url,params=para)
res.raise_for_status()

wea = res.json()
for hour_data in wea['list']:
    cond_code = hour_data['weather'][0]['id']
    if int(cond_code) <700:
        client = Client(account_sid, auth_token)

        message = client.messages.create(
    body="It's going to rain today. Bring an ☂️",
  from_='+17164543638',
  to='+919444297710'
)
        
        print(message.status)
        break



