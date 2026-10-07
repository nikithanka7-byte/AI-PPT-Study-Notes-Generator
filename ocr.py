import io
import cv2
import numpy as np
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

def extract_text_from_image(
    image_bytes
):

    image = Image.open(
        io.BytesIO(image_bytes)
    ).convert("RGB")

    image_array = np.array(
        image
    )

    gray = cv2.cvtColor(
        image_array,
        cv2.COLOR_RGB2GRAY
    )

    gray = cv2.resize(
        gray,
        None,
        fx=2,
        fy=2,
        interpolation=cv2.INTER_CUBIC
    )

    gray = cv2.GaussianBlur(
        gray,
        (3, 3),
        0
    )

    processed = cv2.threshold(
        gray,
        0,
        255,
        cv2.THRESH_BINARY
        + cv2.THRESH_OTSU
    )[1]

    text = pytesseract.image_to_string(
        processed,
        config="--psm 6"
    )

    return text