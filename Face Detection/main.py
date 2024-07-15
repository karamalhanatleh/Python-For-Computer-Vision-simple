# Import package
import cv2

# Load the cascade classifier for detecting faces
clf = cv2.CascadeClassifier("Face Detection/haarcascade_frontalface_default.xml")

# Initialize the camera for live stream (use either camera or video)
camera = cv2.VideoCapture(0)  # Use camera index 0 for default camera

# Uncomment below line for video file instead of live stream
camera = cv2.VideoCapture("Face Detection/people.mp4")

while True:
    # Capture frame-by-frame
    ret, frame = camera.read()
    
    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = clf.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    
    # Draw rectangles around the detected faces
    for (x, y, width, height) in faces:
        cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 255, 0), 3)
    
    # Display the frame with the detected faces
    cv2.imshow("Face Detection", frame)
    
    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) == ord("q"):
        break

# Release the camera and close all OpenCV windows
camera.release()
cv2.destroyAllWindows()
