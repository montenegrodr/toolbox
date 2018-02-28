import requests
from letmecrawl import letmecrawl

for proxy in letmecrawl.letmecrawl():
    response = requests.get(
        url='http://ifconfig.co/json',
        proxies={'http': str(proxy)}
    )
    print response.content
