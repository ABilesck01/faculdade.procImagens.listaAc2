import cv2
import numpy as np
from matplotlib import pyplot as plt

imagem = cv2.imread("figs/objetos.png")

imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)

red = imagem[:, :, 0]
green = imagem[:, :, 1]
blue = imagem[:, :, 2]

cv2.imwrite("figsResultado/ex3_objetosVermelhos.png", red)
cv2.imwrite("figsResultado/ex3_objetosVerdes.png", green)
cv2.imwrite("figsResultado/ex3_objetosAzuis.png", blue)

