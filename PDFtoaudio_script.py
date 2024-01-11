import tkinter as tk
from tkinter import filedialog
from tkinter import ttk, messagebox
import pyttsx3
import PyPDF2

# Initialize the global variable to store the selected PDF file path
pdf_path = ''

# Function to open file dialog and store the selected PDF file path
def open_file_dialog():
    global pdf_path
    pdf_path = filedialog.askopenfilename()
    if pdf_path:
        print("Selected file:", pdf_path)
        # Update the text in the text box to display the selected file path
        file_path_text.delete(1.0, tk.END)  # Clear previous text
        file_path_text.insert(tk.END, pdf_path)

# Function to convert selected PDF to audio
def file_select():
    global pdf_path
    if pdf_path:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ''
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()

            speaker = pyttsx3.init()
            audio_file_name = pdf_path[:-4] + '_audio.mp3'
            speaker.save_to_file(text, audio_file_name)
            speaker.runAndWait()
            speaker.stop()

            #message box to show when conversion is complete
            messagebox.showinfo("Succcess", "Conversion is complete!")
    else:
        #show message if no file is selected
        messagebox.showerror("Error", "No file selected!")

# Create the Tkinter window
root = tk.Tk()
root.title("PDF to mp3 converter")

# Set window dimensions
canvas = tk.Canvas(root, height=300, width=700, bg="#2d3139", highlightthickness=0)
canvas.pack()

# Create a button to open the file dialog
button = tk.Button(root, text="Open File Dialog ", command=open_file_dialog, bg="#5a6272", fg="white")
button.place(x=20, y=20)

# Create a button to convert selected PDF to audio
button2 = tk.Button(root, text="Convert to Audio", command=file_select, bg="#5a6272",fg="white")
button2.place(x=20, y=70)

# Create a text box to display the selected file path
file_path_text = tk.Text(root, height=1, width=50, bg="#5a6272", fg="white")
file_path_text.place(x=150, y=20)

# Run the Tkinter main loop
root.mainloop()
