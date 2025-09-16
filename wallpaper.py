import ctypes
import os
import time
import itertools

def change_wallpaper(img_path):
    img_path = os.path.abspath(img_path)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, img_path, 3)

wallpapers = [
    r"D:\python\images\image1.jpg",
    r"D:\python\images\image2.jpg",
    r"D:\python\images\image3.jpg",
    r"D:\python\images\image4.jpg"
]

for image in itertools.cycle(wallpapers):
    change_wallpaper(image)
    print(f"Wallpaper changed to: {image}")
    time.sleep(10)

