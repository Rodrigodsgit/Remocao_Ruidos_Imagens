import cv2
import numpy as np
import os

diretorio = 'Satelite_ruido'
imagens = [os.path.join(diretorio, f) for f in os.listdir(diretorio) if f.startswith('satelite') and f.endswith('.png')]

lista_imagens = []
for imagem in imagens:
    img = cv2.imread(imagem)
    lista_imagens.append(img)

media = np.mean(lista_imagens, axis=0).astype(np.uint8)
mediana = np.median(lista_imagens, axis=0).astype(np.uint8)


cv2.namedWindow('Imagem Media', cv2.WINDOW_GUI_NORMAL)
cv2.imshow('Imagem Media', media)

cv2.namedWindow('Imagem Mediana', cv2.WINDOW_GUI_NORMAL)
cv2.imshow('Imagem Mediana', mediana)

cv2.waitKey(0)
cv2.destroyAllWindows()

