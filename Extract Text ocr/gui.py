import cv2
import pytesseract
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk

# Path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\DELL\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

def select_image():
    global panelA, panelB, img_path

    # Open a file dialog and select an image file
    img_path = filedialog.askopenfilename()

    # Check if an image path was selected
    if len(img_path) > 0:
        # Load the image
        image = cv2.imread(img_path)
        
        if image is None:
            messagebox.showerror("Error", "Unable to load image.")
            return
        
        # Convert to RGB (OpenCV uses BGR)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # Convert to PIL format
        image_pil = Image.fromarray(image_rgb)
        
        # Convert to ImageTk format
        image_tk = ImageTk.PhotoImage(image_pil)
        
        # If the panels are None, initialize them
        if panelA is None or panelB is None:
            panelA = tk.Label(image=image_tk)
            panelA.image = image_tk
            panelA.pack(side="left", padx=10, pady=10)

            panelB = tk.Label(text="")
            panelB.pack(side="right", padx=10, pady=10)
        # Otherwise, update the image panels
        else:
            panelA.configure(image=image_tk)
            panelA.image = image_tk
            panelB.config(text="")
            text_box.delete("1.0", tk.END)

def perform_ocr():
    global panelB, img_path

    if img_path is None:
        messagebox.showerror("Error", "Please select an image first.")
        return

    # Load the image
    image = cv2.imread(img_path)

    if image is None:
        messagebox.showerror("Error", "Unable to load image.")
        return

    # Convert to grayscale
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply adaptive thresholding
    binary_img = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    
    # Perform OCR
    text = pytesseract.image_to_string(binary_img)

    # Update the text panel
    panelB.config(text="Extracted Text:")
    text_box.insert(tk.END, text)

# Initialize the window toolkit and window
root = tk.Tk()
root.title("OCR Image Uploader")

# Initialize panels
panelA = None
panelB = None
img_path = None

# Create a button to select an image
btn = tk.Button(root, text="Select an image", command=select_image)
btn.pack(side="top", padx=10, pady=10)

# Create a button to perform OCR
btn2 = tk.Button(root, text="Perform OCR", command=perform_ocr)
btn2.pack(side="top", padx=10, pady=10)

# Text box to display OCR results
text_box = tk.Text(root, wrap="word", width=50, height=15)
text_box.pack(side="bottom", padx=10, pady=10)

# Start the GUI loop
root.mainloop()
