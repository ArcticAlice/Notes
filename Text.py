import PIL.Image
import cv2
import matplotlib.pyplot as plt
import os
import subprocess

from google.genai import types
from google import genai
from dotenv import load_dotenv
from pylatex import Document, Section

def read_image(path):
    # Read the image
    img = cv2.imread(path)

    # Process the image...

    # Grayscale 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Clip
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8)) 
    enhanced = clahe.apply(gray)
    # Contrast
    threshold_value = 115
    ret, binary = cv2.threshold(enhanced, threshold_value, 255, cv2.THRESH_BINARY)

    final_image = PIL.Image.fromarray(binary)

    return final_image

def get_latex(img):
    # Load the .env file and get the api key
    load_dotenv(override=True)
    API_KEY = os.getenv("API_KEY")

    # Give the api key to gemini ai
    client = genai.Client(api_key=API_KEY)

    prompt = "Given the image, convert the image into latex code. Be sure to use math formating when needed"
    
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=[prompt, img], config=types.GenerateContentConfig(temperature=0, seed=5)
    )

    latex = response.text
    lines = latex.split("\n")
    latex = "\n".join(lines[1:-1])

    return latex

def save_latex(path, latex):
    with open(f"{path}", "w") as f:
        f.write(latex)

def compile_latex_to_pdf(path):
    try:
        subprocess.run(['pdflatex', path], check=True)
        print(f"{path} compiled successfully into PDF.")
    except subprocess.CalledProcessError:
        print(f"Error compiling {path}. Make sure pdflatex is installed.")

def main():
    image_path = "Good/d.jpg"
    latex_path = "document.tex"
    image = read_image(image_path)
    latex = get_latex(image)
    save_latex(latex_path, latex)
    compile_latex_to_pdf(latex_path)

if __name__ == "__main__":
    main()