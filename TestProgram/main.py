# Importing the OpenCV library
from time import sleep, perf_counter
from threading import Thread
from Imagen import Imagen 
import random
import cv2

threadList = []
objectList = []

def createObjects(total):
    for num in range(total):
        # Reading the image using imread() function
        image = cv2.imread('cat_dog.jpg')
        #Create the object
        img1 = Imagen('cat_dog.jpg',image)
        #filter(img1)
        objectList.append(img1)

def filter(imagen):
    imagen.resize(random.randint(100,400),random.randint(200,600))
    imagen.rotate(random.randint(-90,90))
    
def applyFilter(imagenList):    
    for img in imagenList:
        filter(img)

total = 2000
createObjects(total)

step = int(total/10)
#print(f"Step {step}")

# Inicial el conteo del tiempo
start_time = perf_counter()

bottomLimit = 0
topLimit = step

## ------- Creacion de 10 hilos -------
for val in range(10):
    #print(f"Bottom: {bottomLimit} | top {topLimit}")
    #print(random.randint(-10,10))
    t = Thread(target=applyFilter, args=(objectList[bottomLimit:topLimit],))
    bottomLimit = topLimit
    topLimit = topLimit + step
    threadList.append(t)
    t.start()

for thread in threadList:
    thread.join()

end_time = perf_counter()
# FInaiza el conteo del tiempo
print(f'It took {end_time- start_time: 0.2f} second(s) to complete.')
