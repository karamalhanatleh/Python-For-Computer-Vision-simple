#import paskages
import cv2
import numpy as np

# Open the default camera 
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()
    
    # Display the original frame
    cv2.imshow('frame', frame)
    
    # Apply Laplacian edge detection to the frame
    laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    
    # Convert the Laplacian result to the uint8 data type (8-bit image)
    laplacian = np.uint8(laplacian)
    
    # Display the Laplacian result
    cv2.imshow('laplacian', laplacian)

    # Apply Canny edge detection to the frame
    edges = cv2.Canny(frame, 50, 50)
    
    # Display the Canny edge detection result
    cv2.imshow("Canny", edges)
    
    # Check for user input to quit the loop (press 'q' to exit)
    if cv2.waitKey(10) == ord("q"):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
