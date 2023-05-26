import folium
from geopy.distance import geodesic
m=folium.Map([31.335432273991238, 75.53764505992153],zoom_start=6,tiles="Mapbox Bright")
m.add_child(folium.Marker(location=[31.333,75.537],popup="First Marker"))
fg=folium.FeatureGroup(name="My map")
fg.add_child(folium.Marker(location=[32.00,75.00],popup="2nd",icon=folium.Icon(color="green")))
m.add_child(fg)
distance_miles = geodesic([31.333,75.537], [32.00,75.00]).miles
distance_km = distance_miles * 1.60934 
folium.Polygon(locations=[[31.333,75.537], [32.00,75.00]],popup=distance_km ,color='blue').add_to(m)
m.save("m1.html")

