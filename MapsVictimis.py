#Mapa utilizado para destacar os países que estão numa lista CSV
#Desenvolvi para facilitar a apresentação visual dos países afetados por determinado ataque cibernético
#Version 1, 18 July 2025

import pandas as pd
import geopandas as gpd
import folium

# Leitura dos dados
csv_path = "paises.csv"
shapefile_path = "ne_10m_admin_0_countries.shp"

# Ler CSV
paises_csv = pd.read_csv(csv_path)
lista_paises = [nome.strip().lower() for nome in paises_csv['Country'].dropna()]

# Ler shapefile
world = gpd.read_file(shapefile_path)

# Criar mapa
mapa = folium.Map(location=[0, 0], zoom_start=2, tiles='cartodbpositron')

# Adicionar cada país com a cor correta
for idx, row in world.iterrows():
    # Verificar se o país está na lista
    nome_pais = row['ADMIN'].strip().lower()
    cor = '#c41b32' if nome_pais in lista_paises else '#dde9ed'
    
    # Adicionar ao mapa
    folium.GeoJson(
        row['geometry'],
        style_function=lambda feature, cor=cor: {
            'fillColor': cor,
            'color': 'gray',
            'weight': 0.5,
            'fillOpacity': 0.85
        },
        tooltip=folium.Tooltip(row['ADMIN'])
    ).add_to(mapa)

# Salvar mapa
mapa.save('mapvictimis.html')
print("Mapa criado com sucesso!")
