#============================IMPORTS================================
import cv2
import numpy as np
import math 
import os
from sys import exit
import tkinter as tk
from tkinter import filedialog as fd 
from tkinter import messagebox
types = [("Image files", "*.png *.jpg *.jpeg *.bmp")]

#============================FUNCTIONS==============================
# Notify user why the app closes
def outputMsg(msg, info=False):
  print(msg)
  if info:
    messagebox.showinfo("Image Scanner", msg)
  else:
    messagebox.showerror("Image Scanner", msg)  
  exit() 

# Get paths
def getFilenames():
  path_input_img = fd.askopenfilename(title="Select your image", filetypes=types)
  if path_input_img is None or path_input_img is "":
    outputMsg("Image selection cancelled.",True) 
  filename = os.path.basename(path_input_img).split('.', 1)[0] + '_scanned.png'
  path_output_img = fd.asksaveasfilename(title="Save image as", filetypes=types, defaultextension=types, initialfile=filename)
  if path_output_img is None or path_output_img is "": 
    outputMsg("Invaling export path.")
  return (path_input_img,path_output_img)  

#===================================================================
# Read image and check valid path
def getImg(path_input_img):
  # using "if" instead or "try-except" because cv2.imread doesn't throw exception
  img = cv2.imread(path_input_img, cv2.IMREAD_COLOR)
  if img is None:
    outputMsg("Couldn't find an image in path: "+path_input_img+".")
  return (img)  

#===================================================================
# Realign image       
def processImg(img):
  # Binarization
  img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  img_gray = cv2.GaussianBlur(img_gray, (99, 99), 0)
  (_, img_bin) = cv2.threshold(img_gray, 90, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

  # Find biggest contour
  (cnts, _) = cv2.findContours(img_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  cnt = max(cnts, key=cv2.contourArea)

  # Finding corners
  epsilon = 0.1*cv2.arcLength(cnt, True)
  approx = cv2.approxPolyDP(cnt, epsilon, True)
  p1 = approx[0][0]
  p2 = approx[1][0]
  p3 = approx[2][0]
  p4 = approx[3][0]
  
  # Finding height and width 
  edge1 = math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))
  edge2 = math.sqrt(((p2[0] - p3[0]) ** 2) + ((p2[1] - p3[1]) ** 2))
  edge3 = math.sqrt(((p3[0] - p4[0]) ** 2) + ((p3[1] - p4[1]) ** 2))
  edge4 = math.sqrt(((p4[0] - p1[0]) ** 2) + ((p4[1] - p1[1]) ** 2))
  side1 = round(min(edge1, edge3))
  side2 = round(min(edge2, edge4))
  if side1 > side2:
    height = side1
    width = side2
    corners=[p1,p4,p2,p3]
  else:
    height = side2
    width = side1
    corners=[p2,p1,p3,p4]

  # Transformation matrix
  pts1 = np.float32(corners)
  pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
  M = cv2.getPerspectiveTransform(pts1,pts2)

  # Transform
  img_output = cv2.warpPerspective(img,M,(width,height))
  return img_output

#===================================================================
# Try to save
def saveImg(path_output_img,img_output):
  try:
    saved = cv2.imwrite(path_output_img,img_output)
    if saved:
      outputMsg("Saved to "+path_output_img,True)
    outputMsg("Couldn't save the image in path: "+path_output_img+".")
  except Exception as error:
    print(error)
    outputMsg("Couldn't save the image in path: "+path_output_img+".")
  
#==============================MAIN=================================
def main():
  # File dialogs
  path_input_img,path_output_img = getFilenames()

  # Read image
  img = getImg(path_input_img)

  # Align paper
  try:
    img_output = processImg(img)
  except Exception as error:
    print(error)
    outputMsg("Couldn't process image.")
   
  # Save image
  saveImg(path_output_img,img_output)

#===================================================================  
if __name__ == "__main__":  
  root = tk.Tk()
  root.withdraw()
  root.iconbitmap("scanner.ico") #Remove if not using an icon
  main()