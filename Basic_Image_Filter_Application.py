import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image
img = cv2.imread("C:\\Users\\Acer\\Desktop\\Project 18\\elon.jpg")

# Check if the image was loaded successfully
if img is None:
  print("Unable to load image.")
  
else:
  # Convert image to RGB
  img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  
  # Sharpening using filter
  sharpened_img = cv2.filter2D(img, -1, np.array([[0, -1, 0],
                                                  [-1, 5, -1],
                                                  [0, -1, 0]]))
  
  # Embossing using filter
  embossed_img = cv2.filter2D(img, -1, np.array([[-2, -1, 0],
                                                 [-1, 1, 1],
                                                 [0, 1, 2]]))
  
  # For display 
  plt.figure(figsize=(10, 5))
  
  # For original image
  plt.subplot(1, 3, 1)
  plt.title("Original Image")
  plt.imshow(img_rgb)
  plt.axis('off')
  
  # For sharpened image
  plt.subplot(1, 3, 2)
  plt.title("Sharpened Image")
  plt.imshow(cv2.cvtColor(sharpened_img, cv2.COLOR_BGR2RGB))
  plt.axis('off')
  
  # For embossed image
  plt.subplot(1, 3, 3)
  plt.title("Embossed Image")
  plt.imshow(cv2.cvtColor(embossed_img, cv2.COLOR_BGR2RGB))
  plt.axis('off')
  
  # To display all images
  plt.show()