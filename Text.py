from dotenv import load_dotenv

import google.generativeai as genai

import PIL.Image
import os

load_dotenv(override=True)

API_KEY = os.getenv("API_KEY")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')

img = PIL.Image.open('something.webp')

prompt = "Extract text from the image and organize it into ordered blocks. For each block, provide: " \
         "1. Heading: Average font size of the text (for typed text) or specify 'Handwritten' (for handwritten text). " \
         "2. Body: Actual text content. " \
         "Separate blocks based on whether the text is typed or handwritten. " \
         "Ensure the output maintains structured formatting and accurately categorizes each block."


response = model.generate_content([prompt, img])

print(response.text)