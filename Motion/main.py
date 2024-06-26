#Import paskages
import cv2

# Load the video file
video = cv2.VideoCapture("Motion/people.mp4")

# Create background subtractor objects
subtractor_knn = cv2.createBackgroundSubtractorKNN(history=500, dist2Threshold=400.0, detectShadows=True)
subtractor_mog2 = cv2.createBackgroundSubtractorMOG2(history=20, varThreshold=50, detectShadows=True)

# Process the video frames
while True:
    ret, frame = video.read()
    if not ret:
        break
    
    # Apply the KNN background subtractor
    mask_knn = subtractor_knn.apply(frame)
    
    # Apply the MOG2 background subtractor
    mask_mog2 = subtractor_mog2.apply(frame)
    
    # Display the resulting masks for KNN and MOG2 side by side
    cv2.imshow("KNN Mask", mask_knn)
    cv2.imshow("MOG2 Mask", mask_mog2)
    
    # Wait for a short period (5 milliseconds)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

# Cleanup: close all OpenCV windows and release the video capture object
cv2.destroyAllWindows()
video.release()
