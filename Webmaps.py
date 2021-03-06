#importing folium library
import folium

#importing pandas to read and use .txt file
import pandas

#making map object.
#Here, in location we passed latitude and longitude. The bigger the zoom_start value, the closer in you get.
map = folium.Map(location=[38.58,-98.09],zoom_start=6)

#read data
data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
elev = list(data["ELEV"])

#function to return color based on valcanoes's elevation
def color_producer(elevation):
    if elevation<1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

#feature group. group of features like marker
fgv = folium.FeatureGroup(name="Valcanoes")

#add marker
for lt,ln,nm,el in zip(lat,lon,name,elev):
    fgv.add_child(folium.Marker(location=[lt,ln],popup=nm+" "+str(el)+" m",icon=folium.Icon(color=color_producer(el))))

#feature group for polygon layer
fgp = folium.FeatureGroup(name="Population")

#It's polygon layer which is best suitable to show areas on map.
#Here, we are showing world population data by countries using polygon layer on the map.
fgp.add_child(folium.GeoJson(data=open("world.json",'r',encoding='utf-8-sig').read(),
                            style_function=lambda x: {'fillColor':'yellow'}))

#adding feature groups to the map
map.add_child(fgv)
map.add_child(fgp)

#adding layer control
map.add_child(folium.LayerControl())

#save map object in html file.
map.save("map.html")