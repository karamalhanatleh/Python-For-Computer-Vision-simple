import cv2
import pytesseract

# Path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\DELL\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# Load the image
img = cv2.imread("Extract Text ocr\\txt.png")

# Check if the image was loaded successfully
if img is None:
    print("Error: Unable to load image.")
else:
    # Convert to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply adaptive thresholding
    binary_img = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    
    # Perform OCR
    text = pytesseract.image_to_string(binary_img)
    
    # Print the extracted text
    print("Extracted Text:")
    print(text)
    
    # Display the original and processed images (optional)
    cv2.imshow('Grayscale Image', gray_img)
    cv2.imshow('Binary Image', binary_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
