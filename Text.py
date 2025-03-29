import PIL.Image
import cv2
import matplotlib.pyplot as plt
import os

from google.genai import types
from google import genai
from dotenv import load_dotenv

load_dotenv(override=True)

API_KEY = os.getenv("API_KEY")

client = genai.Client(api_key=API_KEY)

options = {
    "seed": 42,
    "temperature": 0.7
}

img = cv2.imread("Something.webp") # Read the image

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Convert the image to grayscale

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8)) # Create a CLAHE object (you can adjust clipLimit and tileGridSize as needed)

enhanced = clahe.apply(gray)

blurred = cv2.GaussianBlur(enhanced, (3, 3), 0)

prompt = "Given the image, convert the image into latex code. Be sure to use math formating when needed"

threshold_value = 155
ret, binary = cv2.threshold(enhanced, threshold_value, 255, cv2.THRESH_BINARY)

cv2.imwrite("Enhanced.jpg", binary) # Save the processed image

organ = PIL.Image.open("Enhanced.jpg")

response = client.models.generate_content(
    model="gemini-2.0-flash", contents=[prompt, organ], config=types.GenerateContentConfig(temperature=0, seed=5)
)

print(response.text)