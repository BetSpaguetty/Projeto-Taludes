import rasterio
import math
file_path = "C:\\Users\\betsabenogueira\\Documents\\Visualizador de tiff\\Projeto-Taludes\\betsabe\\rj_recortes\\RJ_20.tif"
# file_path = "C:\\Users\\betsabenogueira\\Downloads\\srtm_rio (1).tif"
# file_path = "c:\\Users\\betsabenogueira\\Downloads\\sentinel2_rio_25_2.tif"
# file_path = "C:\\Users\\betsabenogueira\\Downloads\\aleatorio_30.tif"
# file_path = "C:\\Users\\betsabenogueira\\Downloads\\exportando_25.tif"
# file_path = "c:\\Users\\betsabenogueira\\Downloads\\exportando_30_rj.tif"
# file_path = "C:\\Users\\betsabenogueira\\Downloads\\srtm_rj_35.tif"

# with rasterio.open(file_path) as src:
#     # Obtém os limites (bounding box)
#     bounds = src.bounds

#     # Calcula centro (em coordenadas geográficas)
#     center_x = (bounds.left + bounds.right) / 2
#     center_y = (bounds.top + bounds.bottom) / 2

#     print(f"Centro do raster: lon = {center_x}, lat = {center_y}")


# with rasterio.open(file_path) as dataset:
#     if dataset.crs is None:
#         print(f"informações nulas")
#         metros = 25
#         print("metros:", metros)
#     else:
#         print("informações obtidas")
#         transform = dataset.transform
#         pixel_width = transform.a      # tamanho do pixel no eixo X
#         pixel_height = -transform.e    # tamanho do pixel no eixo Y (negativo, por convenção)

#         print(f"Resolução: {pixel_width} x {pixel_height} metros/pixel")

#         # lat_rad = math.radians(center_y)

#         # Aproximação do tamanho de 1 grau em metros
#         meters_per_deg_lat = 111320 
#         meters_per_deg_lon = 111320 #* math.cos(lat_rad)

#         # Converte resolução de graus/pixel para metros/pixel
#         res_x_m = pixel_width * meters_per_deg_lon
#         res_y_m = pixel_height * meters_per_deg_lat

#         print(f"Resolução aproximada: {res_x_m:.2f} x {res_y_m:.2f} metros/pixel")

# -------------------------------------------------------------
def calcula_distancia_lat():
    c = 2 * math.pi * 6371000
    return c/360

def meters_per_pixel(file_path):
    with rasterio.open(file_path) as dataset:
        if dataset.crs is None:
            print(f"informações nulas")
            largura = dataset.width      # número de colunas (pixels no eixo X)
            altura = dataset.height      # número de linhas (pixels no eixo Y)

            res_x_m = (1.5/largura) * (111320 * math.cos(math.radians(largura)))
            res_y_m = (1/altura) * 111320 
            return(res_x_m,res_y_m)
        else:
            print("informações obtidas")
            transform = dataset.transform
            pixel_width = transform.a      # tamanho do pixel no eixo X
            pixel_height = -transform.e    # tamanho do pixel no eixo Y (negativo, por convenção)

            res_x_m = pixel_width * calcula_distancia_lat() * math.cos(math.radians(pixel_width)) # (lon) -> meia luas
            res_y_m = pixel_height * calcula_distancia_lat()                                      # (lat) -> paralelos
            print(pixel_width,pixel_height)

            return (round(res_x_m),round(res_y_m))
        

# def meters_per_pixel(file_path):
#         with rasterio.open(file_path) as dataset:
#             if dataset.crs is None:
#                 print(f"informações nulas")
#                 return(25,25)
#             else:
#                 print("informações obtidas")
#                 transform = dataset.transform
#                 pixel_width = transform.a      # tamanho do pixel no eixo X (lon)
#                 pixel_height = -transform.e    # tamanho do pixel no eixo Y (lat)(negativo, por convenção)
#                 print(pixel_height,pixel_width)
#                 res_x_m = pixel_width * 111.320 
#                 res_y_m = pixel_height * 111.320 
#                 print(round(res_x_m),round(res_y_m))
#                 return (round(res_x_m),round(res_y_m))

print(meters_per_pixel(file_path))
# print(calcula_distancia_lat())