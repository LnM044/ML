import numpy as np
import pandas as pd
import cv2
from google.colab.patches import cv2_imshow # for image display
from skimage import io
from PIL import Image
import matplotlib.pylab as plt
img = cv2.imread("/https://upload.wikimedia.org/wikipedia/commons/f/f3/Nazarbayev_University.jpg")
cv2_imshow(img)
