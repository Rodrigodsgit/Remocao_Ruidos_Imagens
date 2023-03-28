import cv2
import numpy as np
import os
import glob

# Abre as imagens de um diretório e armazena em um vetor
filelist = glob.glob('Satelite_ruido\\*.png')
imagens = np.array([cv2.imread(fname, 0).astype(np.float32) for fname in filelist])


# Percorre todas as imagens e soma os valores de cada pixel
soma = np.zeros_like(imagens[0], dtype=np.float32)
for imagem in imagens:
    soma += imagem.astype(np.float32)

# Calcula a média dividindo pela quantidade de imagens
media = (soma / len(imagens)).astype(np.uint8)

rows, cols = imagens[0].shape

# Percorre todas as imagens e ordena os valores de cada pixel
valores = np.zeros((len(imagens), rows*cols), dtype=np.float32)
for i, imagem in enumerate(imagens):
    valores[i] = imagem.ravel()

# Calcula a mediana para cada pixel
mediana = np.zeros_like(imagens[0], dtype=np.uint8)
for r in range(rows):
    for c in range(cols):
        pixel = valores[:, r*cols + c]
        pixel_sorted = np.sort(pixel)
        n = len(pixel_sorted)
        if n % 2 == 0:
            mediana[r, c] = (pixel_sorted[n//2 - 1] + pixel_sorted[n//2]) // 2
        else:
            mediana[r, c] = pixel_sorted[n//2]


# Exibe a imagem de média e mediana 

cv2.imshow('Media', media)

cv2.imshow('Mediana', mediana)

cv2.waitKey(0)
cv2.destroyAllWindows()
