import folium 
import pandas
import geopandas as gpd

data=pandas.read_csv('veri.csv',encoding="ansi")

LAT=list(data['LAT'])
LON=list(data['LON'])
name=list(data['NAME'])
capacity=list(data['capacity'])
website=list(data['website'])
picture=list(data['picture'])



fg=folium.FeatureGroup('my map')
fg.add_child(folium.GeoJson(data=(open('tr.json','r',encoding='utf-8').read())))


 
for lt,ln,nm,cp,ws,pic in zip(LAT,LON,name,capacity,website,picture):
 	fg.add_child(folium.Marker(location=[lt,ln],popup="<b>City name  : </b>"+nm+ "<br> <b>Population-density : </b> "+str(cp)+"<br><b>wikipeda link: </b><a href="+ws+">click here</a>"+"<br> <img src="+pic+" height=142 width=290>",icon=folium.Icon(color='green')))

#height=142 width=290
map=folium.Map(location=[38.963745,35.243320],zoom_start=5)


map.add_child(fg)
map.save('interactive_map.html')



