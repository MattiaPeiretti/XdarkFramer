# This is a little script to acquire dark frames..
# It allows the creation of multiple captures saved in .bmp of .tiff format
# 
# Arguments to launch
#main py (\/ arguments) 
# 1. [device number ] 
# 2. [frames to take(recommended 256)] 
# 3. [Image format 0 for .bmp, 1 for .tiff ]
# 4. [folder to save the frames (path/to/folder/) ] 


import cv2
import sys
import os, os.path
from datetime import datetime
import time

class Xdarkframer():
    def __init__(self, device, frames_amount, image_filetype, path_to_save):
        self.device = device
        self.frames_amount = frames_amount
        self.image_filetype = image_filetype
        self.save_path = path_to_save

    def run(self):
        capture_dev = cv2.VideoCapture(self.device)

        #Capturing the frames

        if not os.path.isdir(self.save_path):
            os.mkdir(self.save_path)


        for index in range(self.frames_amount):
            ret, frame = capture_dev.read()
            if not ret:
                raise RuntimeError(f'Could not capture frame from device {self.device}')
            
            cv2.imwrite(f"{self.save_path}DarkFrame_{index}.{self.image_filetype}", frame)

        print('Dark Frame Created!')



if __name__ == '__main__':
    device = int(sys.argv[1])
    frames_amount = int(sys.argv[2])
    image_filetype = bool(sys.argv[3])
    save_path = sys.argv[4]

    if image_filetype:
        image_filetype = 'tiff'
    else:
        image_filetype = 'bmp'

    main = Xdarkframer(device, frames_amount, image_filetype, save_path)
    print("Starting in 5 seconds, cover your device!")
    for index in range(5):
        time.sleep(1)
        print(f"Starting in: {index - 5} seconds")
    main.run()

