from requests.auth import HTTPBasicAuth
import requests
basic = HTTPBasicAuth('123', 'abc')
response=requests.get('https://httpbin.org/basic-auth/123/abc', auth=basic)
print(response)
print(response.text)
print()



