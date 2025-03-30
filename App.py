import customtkinter as ctk
import os
from Text import image_to_latex


font = ("", 30)

chosen_file_path = ""

def selectfile():
    file_path = ctk.filedialog.askopenfilename()
    valid = isFileValid(file_path)
    global chosen_file_path
    if not valid:
        label.configure(text="Invalid file!")
        chosen_file_path = ""
        return

    file_name = os.path.split(file_path)[1]
    label.configure(text=file_name)
    chosen_file_path = file_path

def isFileValid(file_path):
    # Check if the path returned is a string
    if type(file_path) is not str:
        return False
    
    # Check if the file is an image type
    if (
        not file_path.endswith("png")
        and not file_path.endswith("webp")
        and not file_path.endswith("jpg")
        and not file_path.endswith("jpeg")
    ):
        return False
    
    # Check if the file exists
    return os.path.isfile(file_path)

def convert():
    print(chosen_file_path)

    if not len(chosen_file_path) > 0:
        return
    
    image_to_latex(chosen_file_path, "document.tex")

# Set up the app
app = ctk.CTk()
app.title("DigiNotes")
app.geometry("640x640")


# app.grid_columnconfigure(0, weight=1)

button = ctk.CTkButton(app, 300, 125, text="Select a file",font=font, command=selectfile)
button.grid(row=0, column=0, padx=10, pady=10)

label = ctk.CTkLabel(app, 300, 25, text="Selected File: None", font=font)
label.grid(row=0, column=1, padx=10, pady=10)

button2 = ctk.CTkButton(app, 300, 125, text="Convert!", font=font, command=convert)
button2.grid(row=2, column=0, padx=10, pady=10)

app.mainloop()
