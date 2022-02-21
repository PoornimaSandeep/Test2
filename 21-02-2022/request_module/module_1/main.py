# import requests module
import requests

# Making a get request
response = requests.get('https://gita-api.vercel.app/tel/verse/2/2')

# print response
print(response.json())

# print json content
dict=response.json()
print(dict)





