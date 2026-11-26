
import cv2
import numpy as np

def localize_defect(image, normal_reference):
    image = cv2.resize(image, (256, 256))
    normal_reference = cv2.resize(
        normal_reference, (256, 256)
    )

    difference = cv2.absdiff(
        image, normal_reference
    )

    gray = cv2.cvtColor(
        difference, cv2.COLOR_BGR2GRAY
    )

    blurred = cv2.GaussianBlur(
        gray, (5, 5), 0
    )

    _, mask = cv2.threshold(
        blurred, 30, 255, cv2.THRESH_BINARY
    )

    contours, _ = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    result = image.copy()
    locations = []

    for contour in contours:
        if cv2.contourArea(contour) > 20:
            x, y, w, h = cv2.boundingRect(contour)

            cv2.rectangle(
                result,
                (x, y),
                (x + w, y + h),
                (0, 0, 255),
                2
            )

            locations.append((x, y, w, h))

    return result, mask, locations
