# Importing the OpenCV library
import cv2

class Imagen:
    def __init__(self, nombre, imagen):
        self.nombre = nombre
        self.imagen = imagen
        self.height = self.getHeight()
        self.width = self.getWidth()
        self.rotatedImage = None
        self.resizedImage = None

    def __str__(self):
        return f"Nombre imagen: {self.nombre}. Altura: {self.height} y Ancho {self.width}"        

    def getHeight(self):
        return self.imagen.shape[0]

    def getWidth(self):
        return self.imagen.shape[1]

    def rotate(self,degres):
        # Calculating the center of the image
        center = (self.getWidth() // 2, self.getHeight() // 2)

        # Generating a rotation matrix
        matrix = cv2.getRotationMatrix2D(center, degres, 1.0) 

        # Performing the affine transformation
        self.rotatedImage  = cv2.warpAffine(self.imagen, matrix, (self.width, self.height))

    def resize(self,height,width):
        self.resizedImage = cv2.resize(self.imagen, (height, width))
