import requests
#import matplotlib.pyplot as plt
#import numpy as np

# If you want to use classes
# class Place:
# would have attributes lat, long, name,
# Would be like a card in blackjack and the place_list would be like a deck

# class WeatherReport
# place, temp, precip

places_list = [
(39.896519, 32.861969, "Cappadocia"),
(-20.269600, 148.720530, "Whitsundays"),
(57.057941, -5.909100, "Isle Of Skye"),
(7.544510, 4.556030, "Osun State"),
(-44.671799, 167.927002, "Milford Sound"),
(13.1631, 72.5450, "Macu Pichu"),
(-14.0858, -75.7580, "Huacachina Oasis"),
(33.9249, -18.4241, "Cape Town")
]

def climate(locations):
    climate_data_packet = {}
    for location in locations:
        url = "https://api.climacell.co/v3/weather/realtime"
        payload = {
        "apikey":"vKSp6RY2GPGxk2nt4x8sRuVFwwEgm1y7",
        "lat":location[0], 
        "lon":location[1],
        "fields": ["temp", "precipitation", "wind_gust"],
        "unit_system":"us",  
        } 

        response = requests.get(url, params=payload).json()

        climate_data_packet[location[2]] = response["temp"] ["value"] 
        
    for city, temp in climate_data_packet.items():

        print(f"Current Temperature is {temp} in {city}.") 

    for city, precipitation in climate_data_packet.items():

        print(f"Current Precipitation is {precipitation} in {city}.")   
        
    return climate_data_packet

climate_data = climate(places_list)
#print(climate_data)
 #expects to see real numbers

#TODO construct a list of places that are tuples lat and long
#(lat, long)
# you can use [] to retrieve items by position, like you can in list
# ex. (lat, long)[0] = lat



def get_weather_data(places_list):
  # get lats and longs from tuples
  # give me temp and precip for a location, given lat and long
  # it will make a request to the 'realtime' url that we used below
  pass

np.random.seed(19680801)


plt.rcdefaults()
fig, ax = plt.subplots()


locations = ('Cappadocia', 'Whitsundays', 'Isle Of Skye', 'Osun State', 'Milford Sound', 'Macu Pichu', 'Huacachina Oasis', 'Cape Town')
y_pos = np.arange(len(locations))
#performance = np.random.rand(len(locations))
error = np.random.rand(len(locations))

ax.barh(y_pos, x_pos, xerr=error, align='center',)
ax.set_yticks(y_pos)
ax.set_yticklabels(locations)
ax.invert_yaxis()  
#ax.set_xlabel('Performance')
ax.set_title('How Is The Weather?')

plt.show()



