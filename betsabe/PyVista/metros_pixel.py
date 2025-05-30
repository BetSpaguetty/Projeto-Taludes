import rasterio
# file_path = "C:\\Users\\betsabenogueira\\Documents\\Visualizador de tiff\\Projeto-Taludes\\betsabe\\rj_recortes\\RJ_20.tif"
# file_path = "C:\\Users\\betsabenogueira\\Downloads\\srtm_rio (1).tif"
file_path = "c:\\Users\\betsabenogueira\\Downloads\\sentinel2_rio_25_2.tif"

with rasterio.open(file_path) as dataset:
    if dataset.crs is None:
        print(f"informações nulas")
        metros = 25
        print("metros:", metros)
    else:
        print("informações obtidas")
        transform = dataset.transform
        pixel_width = transform.a      # tamanho do pixel no eixo X
        pixel_height = -transform.e    # tamanho do pixel no eixo Y (negativo, por convenção)

        print(f"Resolução: {pixel_width} x {pixel_height} metros/pixel")
    