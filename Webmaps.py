#importing folium library
import folium

#making map object. Here, in location we passed latitude and longitude.
map = folium.Map(location=[42.31,-83.03],zoom_start=6)

#save map object in html file.
map.save("map.html")