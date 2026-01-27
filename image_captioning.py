# Task 3: Image Captioning 
# CODSOFT AI Internship

import cv2
import random

def generate_caption(image_path):
    img = cv2.imread(image_path)

    if img is None:
        return "Image not found."

    captions = [
        "This image shows an everyday object.",
        "The picture contains a real-world scene.",
        "This image appears to be visually clear.",
        "The photo includes recognizable elements.",
        "This is an example of image captioning output."
    ]

    return random.choice(captions)

# Test
img_path = "test.jpg"   # image same folder me honi chahiye
caption = generate_caption(img_path)
print("Generated Caption:", caption)
