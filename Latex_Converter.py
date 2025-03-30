from pylatex import Document, Section
import subprocess

def compile_latex_to_pdf(latex_file):
    try:
        subprocess.run(['pdflatex', latex_file], check=True)
        print(f"{latex_file} compiled successfully into PDF.")
    except subprocess.CalledProcessError:
        print(f"Error compiling {latex_file}. Make sure pdflatex is installed.")

if __name__ == "__main__":
    compile_latex_to_pdf("document.tex")