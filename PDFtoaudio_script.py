import pyttsx3
import PyPDF2
import tkinter as tk
from tkinter import filedialog

# Function to open file explorer and get selected file path
def open_file_dialog():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    return file_path

# Open file dialog to select PDF file
pdf_path = open_file_dialog()

# Ensure file is selected
if pdf_path:
    with open(pdf_path, 'rb') as file:
        # Initialize the PDF reader
        pdf_reader = PyPDF2.PdfReader(file)

        # Initialize the text variable to store extracted text
        text = ''

        # Extract text from each page of the PDF
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

        # Initialize the text-to-speech engine
        speaker = pyttsx3.init()

        # Convert extracted text to audio
        audio_file_name = pdf_path[:-4] + '_audio.mp3'  # Create a new file name for audio
        speaker.save_to_file(text, audio_file_name)
        speaker.runAndWait()

        # Stop the engine
        speaker.stop()
else:
    print("No file selected")
