# pyrefly: ignore[missing-import]
import folium

tempat = {
    "Pantai Panjang": (-3.8167, 102.2667),
    "Benteng Marlborough": (-3.7867, 102.2481),
    "Universitas Bengkulu": (-3.7587, 102.2755),
}
peta = folium.Map(location=(-3.80, 102.26), zoom_start=12, tiles="CartoDB positron")
for nama, (lat, lon) in tempat.items():
    folium.Marker((lat, lon), popup=nama).add_to(peta)
peta.save("peta_bengkulu.html")