from ultralytics import YOLO
import tkinter as tk
from tkinter.filedialog import askopenfilename
tk.Tk().withdraw()

suffixes = ["", "-cls", "-pose", "-seg"]
suffix = suffixes[0]

sizes = "nsmlx"
model_size = sizes[0]

model = YOLO(f"yolov8{model_size}{suffix}.pt")
image_path = askopenfilename()
model.predict(image_path, show=True, save=True, save_txt=True)
input()