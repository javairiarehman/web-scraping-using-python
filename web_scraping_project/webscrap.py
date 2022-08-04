import requests
from bs4 import BeautifulSoup


city = str(input("Enter city name= "))

url = "https://www.google.com/search?q="+"weather"+city

html = requests.get(url).content

soup = BeautifulSoup(html, 'html.parser')
#print(soup)
temp = soup.find('div',attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text

time_skyDescription = soup.find('div',attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

data = time_skyDescription.split('\n')
time =data[0]
sky = data[1]

print("Temperature is ", temp)
print("Time:", time)
print("Sky Description:", sky)
