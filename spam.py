###kalau mokad change sendiri:)

import json
from urllib import request

print("Masukan nomor dengan format 8xxxx")
no = input("masukan no: ")
url = f"https://python-api-zhirrr.herokuapp.com/api/spamcall?no={no}"
response = request.urlopen(url)
data = json.loads(response.read())
print (data['logs'])
