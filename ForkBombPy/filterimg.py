import PIL.Image
import threading
import numpy as np
import sys
import time
import os 
class Image:
    def __init__(self):
        self.path = "lena.jpg"
        self.image = PIL.Image.open(self.path)
        self.image = np.asarray(self.image).astype('uint8')

    def filter(self): ## Aplica filtro equalizacion de histograma
        h = np.histogram(self.image, bins=256, range=(0,255))[0] # Cálculo de histograma
        m, n = self.image.shape;
        ac = np.zeros(256)
        ac[0] = h[0]
        for i in range(1,255):
            ac[i] = ac[i-1] + h[i]

        ac /= m*n

        # Obtener nueva imagen aplicando técnica de ecualización
        B = np.zeros((m, n))

        for x in range(0, m):
            for y in range(0,n):
                B[x,y] = round(ac[self.image[x,y]]*255)
        B = np.uint8(B)
        self.image = B

    def run(self):
        t1 = threading.Thread(target=self.filter)
        t1.start()
        t1.join()



def ejecutar():
    numberElements = 500
    start_time = time.time()
    objects = []
    for i in range(int(numberElements/100)):
        objects.extend([Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image(),Image()])
    i = 0
    while i < numberElements:
        objects[i].run()
        objects[i+1].run()
        objects[i+2].run()
        objects[i+3].run()
        objects[i+4].run()
        objects[i+5].run()
        objects[i+6].run()
        objects[i+7].run()
        objects[i+8].run()
        objects[i+9].run()
        i =+ numberElements
    print("--- %s seconds ---" % (time.time() - start_time))

