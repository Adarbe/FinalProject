import urllib.request, json
url = urllib.request.urlopen("https://free.currencyconverterapi.com/api/v6/convert?q=USD_ILS&compact=n")
data = json.loads(url.read().decode())
results = data['results']
USD_ILS = results['USD_ILS']
val = USD_ILS['val']
print(val)

url = urllib.request.urlopen("https://free.currencyconverterapi.com/api/v6/convert?q=USD_ILS&compact=n")
data2 = json.loads(url.read().decode())
val2 = USD_ILS['val']
print(val2)


url3 = urllib.request.urlopen("http://country.io/capital.json")
data3 = json.loads(url3.read().decode())
results1 = data3['IL']
print(results1)


