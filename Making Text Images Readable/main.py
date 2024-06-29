# Import the OpenCV package
import cv2

# Read the image from the specified file path
img = cv2.imread("Making Text Images Readable/book.png")

# Convert the image to grayscale
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# Apply global (simple) binary thresholding
# The second return value (thresholded image) is assigned to 'result'
# The first return value is the threshold used, which is assigned to '_'
_ , result = cv2.threshold(img, 35, 255, cv2.THRESH_BINARY)

# Apply adaptive thresholding using Gaussian method
# Parameters:
# img - source image (grayscale)
# 255 - maximum pixel value for the thresholded image
# cv2.ADAPTIVE_THRESH_GAUSSIAN_C - adaptive method (Gaussian-weighted sum)
# cv2.THRESH_BINARY - threshold type (binary thresholding)
# 181 - block size (size of the neighborhood area, must be odd)
# 10 - constant subtracted from the mean (fine-tuning parameter)
adaptive = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 181, 10)

# Display the original grayscale image
cv2.imshow('Grayscale Image', img)

# Display the adaptive thresholded image
cv2.imshow("Adaptive Result", adaptive)

# Wait indefinitely until a key is pressed
cv2.waitKey(0)

# Cleanup: close all OpenCV windows
cv2.destroyAllWindows()
