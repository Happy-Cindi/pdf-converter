import pandas as pd
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def CUT(image_path):
    try:
        img = Image.open(image_path)

        text = pytesseract.image_to_string(img)
        print(text)

        lines = [line.strip() for line in text.split("\n")]

    except Exception as e:
        print(f"Error: {e}")
        return None


# import pytesseract
# from PIL import Image

# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


# def CUT(image_path):
#     try:
#         # Open the image using Pillow
#         img = Image.open(image_path)

#         # Use Tesseract to do OCR on the image
#         text = pytesseract.image_to_string(img)

#         print(text)

#         return text

#     except Exception as e:
#         print(f"Error: {e}")
#         return None


# import pdfplumber
# from PIL import Image
# import pytesseract


# def extract_text_from_image(image_path):
#     image = Image.open(image_path)
#     text = pytesseract.image_to_string(image)
#     return text


# def CUT(pdf_path):
#     with pdfplumber.open(pdf_path) as pdf:
#         for page_number, page in enumerate(pdf.pages):
#             print(f"Page: {page_number + 1}")

#             for image_number, image in enumerate(page.images):
#                 image_path = (
#                     f"temp_image_page{page_number + 1}_image{image_number + 1}.png"
#                 )
#                 image_obj = page.to_image(resolution=150)  # Adjust resolution as needed
#                 image_obj.save(image_path)

#                 text_from_image = extract_text_from_image(image_path)
#                 print(f"Text from Image {image_number + 1}: {text_from_image}")
