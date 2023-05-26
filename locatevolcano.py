import pandas as p
import folium
m=p.read_csv("map/Volcanoes_USA.txt")
lat=list(m["LAT"])
lon=list(m["LON"])
el=list(m["ELEV"])
def col(e):
    if(e<1000):
     return "green"
    else:
        return "red"
fg=folium.FeatureGroup(name="Volcanoes")
for i,j,e in zip(lat,lon,el):
    fg.add_child(folium.CircleMarker(location=[i,j],radius=6,popup=str(e)+" m",fill=True,fill_color=col(e),color="white",fill_opacity=0.7))
    #fg.add_child(folium.Marker(location=[i,j],popup=str(e)+" m",icon=folium.Icon(color=col(e))))
     
bg=folium.FeatureGroup(name="Population")
b=folium.Map(location=[lat[0],lon[0]])
bg.add_child(folium.GeoJson(data=open("map/world.json","r",encoding="utf-8-sig").read(),style_function=lambda x:{
    "fillColor":"green" if(x["properties"]["POP2005"]<10000000)
    else "orange" if 10000000<=x["properties"]["POP2005"]<20000000 else "red",
    "color": "black",  # Outline color
        "weight": 1,  # Outline width
        "fillOpacity": 0.6  # Opacity of the fill color
}))
b.add_child(fg)
b.add_child(bg)
b.add_child(folium.LayerControl())
b.save("marked_volcanoes.html")