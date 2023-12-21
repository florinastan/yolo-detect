# main.py
from yolo_predictions import YOLO_Pred
from utils import show_image, real_time_object_detection
import cv2

# Create YOLO_Pred instance
yolo = YOLO_Pred('./Model/weights/best.onnx', 'data.yaml')

# Read and display an image
img = cv2.imread('./street_image.jpg')
show_image(img, 'img')

# Get YOLO predictions using the YOLO_Pred class
img_pred = yolo.predictions(img)
show_image(img_pred, 'prediction image')

# Real-time object detection
real_time_object_detection(yolo)
