import rasterio
# Abrir o arquivo TIFF

#
    # Obter os limites (bounding box)
    # bounds = dataset.bounds
    # print("Limites do raster:")
    # print(f"Min X (Longitude): {bounds.left}")
    # print(f"Max X (Longitude): {bounds.right}")
    # print(f"Min Y (Latitude): {bounds.bottom}")
    # print(f"Max Y (Latitude): {bounds.top}")
    # print("Sistema de referência espacial (CRS):", dataset.crs)

    

def botao_converte(lat, long):
    # with rasterio.open("C:\\Users\\betsabenogueira\\Downloads\\sentinel2_rio_25_2.tif") as dataset:
    with rasterio.open("C:\\Users\\betsabenogueira\Documents\Visualizador de tiff\\Projeto-Taludes\\betsabe\\Corte_RJ.tif") as dataset:
        print(f"CRS do dataset: {dataset.crs!r}")
        if dataset.crs is None:
            print("⚠️ O TIFF não tem CRS! Entrando no if...") # Se NÃO houver Sistema de referência espacial (CRS)
            lat_inicial = -22.77
            lon_inicial = -43.5

            lat_final = -23
            lon_final = -43.15

            latitude = int(lat)
            longitude = int(long)
            
            if (latitude > lat_inicial and latitude < lat_final) or latitude == lat_inicial or latitude == lat_final: 
                if (longitude > lon_final and longitude < lon_inicial) or longitude == lon_inicial or longitude == lon_final:
                    resto = latitude - lat_inicial
                    print("resto lat:",resto) 
                    qt_celulay = resto/0.00028

                    resto2 = longitude - lon_inicial
                    print("resto long:",abs(resto2)) 
                    qt_celulax = resto2/0.00028

                    print(dataset.shape)
                    print(f"Célula: {abs(qt_celulay):.0f}, {abs(qt_celulax):.0f}")
        else:
            print("✅ O TIFF tem CRS:", dataset.crs)
            resolucao_x, resolucao_y = dataset.res[0], dataset.res[1] # Tamanho do pixel em graus (lon/lat)
            bounds = dataset.bounds # Obter os limites (bounding box)

            lat_inicial = bounds.bottom # Min Y (Latitude)
            lon_inicial = bounds.left # Min X (Longitude)

            lat_final = bounds.top # Max Y (Latitude)
            lon_final = bounds.right # Max X (Longitude)

            print(f"Coordenadas iniciais: {bounds.bottom},{bounds.left}/Coordenadas finais: {bounds.top},{bounds.right}")
            
            if (latitude > lat_inicial and latitude < lat_final) or latitude == lat_inicial or latitude == lat_final: 
                print("latitude",latitude)
                if (longitude > lon_final and longitude < lon_inicial) or longitude == lon_inicial or longitude == lon_final:
                    print("longitude")
                    resto = latitude - lat_inicial
                    print("resto lat:",resto) 
                    qt_celulax = resto/resolucao_x

                    resto2 = longitude - lon_inicial
                    print("resto long:",abs(resto2)) 
                    qt_celulay = resto2/resolucao_y

                    banda1 = dataset.read(1)
                    print(banda1.shape)
                    print(f"Célula: {abs(qt_celulax):.0f}, {abs(qt_celulay):.0f}")
                    

        

# botao_converte(-22.499878342520628, -42.99988228377017)
botao_converte(-23, -43.15)