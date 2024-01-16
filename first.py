import requests
import urllib.request 
from PIL import Image 

response = requests.get('https://randomuser.me/api')
#print(response.json())


gith = response.json()['results'][0]



title = gith['name']['title']
first_name=gith['name']['first']
last_name = gith['name']['last']

gender = gith['gender']

address_val = gith['location']

street_add=address_val['street']
street_num=address_val['street']['number']
street_name=address_val['street']['name']
city_name = address_val['city']
state_name=address_val['state']
country_name=address_val['country']

email_id=gith['email']

dob=gith['dob']['date']

phone=gith['phone']

image=gith['picture']['large']

print(f'{title}. {first_name} {last_name}')
print(gender)
print(dob)
print(f'Street:{street_num} {street_name}, {city_name}, {country_name}')
print(email_id)
print(phone)

urllib.request.urlretrieve(image,"photo.jpg")
img=Image.open("photo.jpg")  
img.show()
