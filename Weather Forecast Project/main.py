import requests
from bs4 import BeautifulSoup


def get_weather_report(city: str):
    weather_url = f"https://www.google.com/search?q=weather+{city}"
    html = requests.get(weather_url).content

    # Create soup from HTML data
    soup = BeautifulSoup(html, 'html.parser')
    temperature = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    current_data = soup.find(
        'div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

    time = current_data.split('\n')[0]
    sky =  current_data.split('\n')[1]
    

    print(----------------------------------------------------------------------)
    print()
    print("Current Time is: "+time)
    print("Current Temperature in "+ city + " is: " + temperature)
    print("Sky condition in " + city + " is: " + sky)


if __name__ == '__main__':
    city = input("Enter city name: ")
    get_weather_report(city)

