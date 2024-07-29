import cv2
import pytesseract
import numpy as np
from PIL import Image

ALLOWED_CHARS = ' -qwertyuiopasdfghjklzxcvbnm,.?!1234567890"":;\'éáíóúãõâêîôûç'

def get_bubbles(img: np.ndarray):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_gray = cv2.adaptiveThreshold(img_gray, 255, cv2.THRESH_BINARY,
                                        cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 75, 10)
    img_gray = cv2.bitwise_not(img_gray)

    kernel = np.ones((2,2), np.uint8)
    img_gray = cv2.erode(img_gray, kernel, iterations = 2)
    img_gray = cv2.bitwise_not(img_gray)

    contours, _ = cv2.findContours(img_gray, cv2.RETR_TREE,
                                    cv2.CHAIN_APPROX_SIMPLE)
    pruned_contours = []
    mask = np.zeros_like(img)
    mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
    height, width, _ = img.shape

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 100 and area < ((height / 3) * (width / 3)):
            pruned_contours.append(cnt)

    # find contours for the mask for a second pass after pruning the large and small contours
    cv2.drawContours(mask, pruned_contours, -1, (255,255,255), 1)
    contours2, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL,
                                    cv2.CHAIN_APPROX_NONE)

    cropped_images = []
    for cnt in contours2:
        area = cv2.contourArea(cnt)
        if area > 1000 and area < ((height / 3) * (width / 3)):
            approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)

            y = approx[:, 0, 1].min()
            h = approx[:, 0, 1].max() - y
            x = approx[:, 0, 0].min()
            w = approx[:, 0, 0].max() - x
            cropped_images.append(img[y:y+h, x:x+w])
    return cropped_images

def extract_advanced_text(image: Image) -> list[str]:
    if image is None: return []
    image = np.array(image)

    scripts = list()
    for token in get_bubbles(image):
        token = cv2.resize(token, None, fx=1.7, fy=1.7,
                           interpolation=cv2.INTER_CUBIC)
        token = cv2.cvtColor(token, cv2.COLOR_BGR2GRAY)

        token = cv2.adaptiveThreshold(token, 255, cv2.THRESH_BINARY,
                                      cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 45, 20)
        token = cv2.bitwise_not(token)

        script = pytesseract.image_to_string(token, "por")
        script = script.replace("\n", " ")
        if len(script) == 0 or script.isspace():
            continue

        for char in script:
            if char.lower() not in ALLOWED_CHARS:
                script = script.replace(char, '')
        scripts.append(script.strip())
    return scripts

def extract_text(img: np.ndarray) -> list[str]:
    text = pytesseract.image_to_string(img)
    texts = text.split("\n\n")
    new_texts = []
    for text in texts:
        text = text.replace("\n", " ")
        if text.strip() != "":
            new_texts.append(text.strip())
    return new_texts
