import cv2
import numpy as np

manequim = cv2.imread('figs/manequim.png', 0)

kernel = np.ones((5,5),np.uint8)
manequim_open = cv2.morphologyEx(manequim, cv2.MORPH_OPEN, kernel)

cv2.imwrite('figsResultado/ex05_manequim.png', manequim_open)

tabuleiro = cv2.imread('figs/tabuleiro.jpg', 0)

tabuleiro_open = cv2.morphologyEx(tabuleiro, cv2.MORPH_OPEN, kernel)

cv2.imwrite('figsResultado/ex05_tabuleiro.png', tabuleiro_open)

circulos = cv2.imread('figs/circulos.tif', 0)

kernel = np.ones((15,15),np.uint8)

circulos_closed = cv2.morphologyEx(circulos, cv2.MORPH_CLOSE, kernel)

circulos_open = cv2.morphologyEx(circulos_closed, cv2.MORPH_OPEN, kernel)

cv2.imwrite('figsResultado/ex05_circulos.png', circulos_open)
