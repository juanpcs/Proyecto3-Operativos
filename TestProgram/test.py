# Importing the OpenCV library
import cv2




# Reading the image using imread() function
image = cv2.imread('cat_dog.jpg')

## Extracting the height and width of an image
#h, w = image.shape[:2]
## Displaying the height and width


print(f"Alto: {image.shape[0]} | Ancho: {image.shape[1]}")

image_resize = cv2.resize(image, (800, 600))


cv2.imshow('sample image',image_resize)
 
cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows() # destroys the window showing image
