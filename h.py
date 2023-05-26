import pandas as p
import folium
m=p.read_csv("map/Volcanoes_USA.txt")
lat=list(m["LAT"])
lon=list(m["LON"])
k=1
fg=folium.FeatureGroup(name="My map")
for i,j in zip(lat,lon):
    fg.add_child(folium.Marker(location=[i,j],popup=str(k)+" marker",icon=folium.Icon(color="blue")))
    k=k+1
b=folium.Map(location=[lat[0],lon[0]])
b.add_child(fg)
b.save("marked_volcanoes.html")