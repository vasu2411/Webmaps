#importing folium library
import folium

#making map object.
#Here, in location we passed latitude and longitude. The bigger the zoom_start value, the closer in you get.
map = folium.Map(location=[42.31,-83.03],zoom_start=6)

#feature group. group of features like marker
fg = folium.FeatureGroup(name="MyMap")

#add marker
fg.add_child(folium.Marker(location=[42.28,-83.02],popup="I am marker",icon=folium.Icon(color="red")))
map.add_child(fg)

#save map object in html file.
map.save("map.html")