import requests
response = requests.get('http://randomuser.me/api/?results=5')
print(response.status_code)
#print(response.json())
#print(response.json()['results'][0]['name']['first'])
data= response.json()
for user in data['results']:
    first_name=user['name']['first']
    last_name=user['name']['last']
    email=user['email']
    country=user['location']['country']
    print('first name:',first_name)
    print('last name:',last_name)
    print('email:',email)
    print('country:',country)