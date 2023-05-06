import cv2
import numpy as np

logo = cv2.imread("figs/facensLogo.png")
aerea = cv2.imread("figs/facensVistaAerea.webp")

logo = cv2.cvtColor(logo, cv2.COLOR_BGR2RGB)
aerea = cv2.cvtColor(aerea, cv2.COLOR_BGR2RGB)

altura, largura = aerea.shape[:2]
centro = (largura // 2, altura // 2)

angulo = 45

parte1 = aerea[:centro[1], :centro[0]]
parte2 = aerea[:centro[1], centro[0]:]
parte3 = aerea[centro[1]:, :centro[0]]
parte4 = aerea[centro[1]:, centro[0]:]

rot_parte1 = cv2.warpAffine(parte1, cv2.getRotationMatrix2D((centro[0] // 2, centro[1] // 2), angulo, 1.0), (centro[0], centro[1]))
rot_parte2 = cv2.warpAffine(parte2, cv2.getRotationMatrix2D((centro[0] // 2, centro[1] // 2), -angulo, 1.0), (largura - centro[0], centro[1]))
rot_parte3 = cv2.warpAffine(parte3, cv2.getRotationMatrix2D((centro[0] // 2, centro[1] // 2), 315, 1.0), (centro[0], altura - centro[1]))
rot_parte4 = cv2.warpAffine(parte4, cv2.getRotationMatrix2D((centro[0] // 2, centro[1] // 2), -315, 1.0), (largura - centro[0], altura - centro[1]))

imagem_resultante = np.concatenate((np.concatenate((rot_parte1, rot_parte2), axis=1),
                                    np.concatenate((rot_parte3, rot_parte4), axis=1)), axis=0)

lin = 200
col = 500
logo_menor = cv2.resize(logo,
                        dsize=(col, lin),
                        fx=None,
                        fy=None,
                        interpolation=cv2.INTER_CUBIC)

logo_menor = logo_menor.astype(int)

logo_menor[logo_menor >= 250] = 0
logo_menor[logo_menor != 0] = 255

iLin = 180
iCol = 250

img3 = imagem_resultante[iLin:iLin+lin, iCol:iCol+col] + logo_menor

img4 = imagem_resultante.copy()
img4 = img4.astype(int)

img4[iLin:iLin+lin, iCol:iCol+col] = img3

maximo = np.max(img4)
minimo = np.min(img4)
a = 0
b = 255
img4 = (b-a) * ( ( img4 - minimo ) / ( maximo-minimo ) ) + a

maximo = np.max(img3)
minimo = np.min(img3)
a = 0
b = 255
img3 = (b-a) * ( ( img3 - minimo ) / ( maximo-minimo ) ) + a

img4 = img4.astype(np.uint8)
img3 = img3.astype(np.uint8)

cv2.imwrite("figsResultado/ex2.png", img4)
