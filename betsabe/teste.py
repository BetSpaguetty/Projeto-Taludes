import rasterio
import numpy as np
import matplotlib.pyplot as plt

# Abrir o arquivo TIFF
with rasterio.open("C:\\Users\\betsabenogueira\\Downloads\\sentinel2_rio_25.tif") as src:
    # Ler apenas as bandas RGB (B4, B3, B2)
    red = src.read(4)  # Banda 4 (vermelho)
    green = src.read(3)  # Banda 3 (verde)
    blue = src.read(2)  # Banda 2 (azul)

# Empilhar as bandas RGB para exibição
rgb_image = np.dstack((red, green, blue))

# Exibir a imagem
plt.imshow(rgb_image)
plt.show()


        # with rasterio.open(arquivo) as dataset:
        #     print(f"Formato: {dataset.driver}")
        #     print(f"Dimensões: {dataset.width} x {dataset.height}")
        #     print(f"Número de bandas: {dataset.count}")

        #     if dataset.count > 1:
        #         # Ler apenas a primeira banda
        #         banda1 = dataset.read(1)
        #         self.img_array = banda1
        #         y_ratio, x_ratio = self.img_array.shape
        #     else: