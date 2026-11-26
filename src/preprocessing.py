
import cv2
import numpy as np

def preprocess_image(image_path):
    image = cv2.imread(image_path)

    if image is None:
        raise ValueError("Image not found")

    image = cv2.cvtColor(
        image, cv2.COLOR_BGR2RGB
    )

    image = cv2.resize(image, (256, 256))

    image = image.astype("float32") / 255.0

    return image

if __name__ == "__main__":
    print("Image preprocessing module ready!")
