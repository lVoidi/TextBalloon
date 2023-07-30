"""
This file can be imported. Just run text_balloon_on(path_of_your_image, above=True/False)
"""

from PIL import Image
from typing import List
import os
import sys

text_balloon = Image.open("tb.png")
def text_balloon_on(path: str, index: int = 0) -> Image.Image:
    global text_balloon
    image = Image.open(path)
    text_balloon = text_balloon.resize((image.width, image.height//2))
    image.paste(text_balloon, (0, 0), text_balloon)
    image.save(f"output/new_file_{index}.png")
    return image

if __name__ == "__main__":
    print("Lol text balloon")
    args = sys.argv[1:]
    for arg_index, arg_name in enumerate(args):
        if os.path.isdir(arg_name):
            images = (text_balloon_on(image, index=index) for index, image in enumerate(os.listdir(arg_name)) if image.endswith(("jpg", "png", "webp")))
        else:
            text_balloon_on(arg_name, index=arg_index)
    
    if not args: 
        print("please, put an image or a directory as argument")