import cv2

# Load video
cap = cv2.VideoCapture(0)

# Background subtractor
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    
    if not ret:
        break

    # Apply background subtraction
    fgmask = fgbg.apply(frame)

    # Show frames
    cv2.imshow("Original Frame", frame)
    cv2.imshow("Motion Detection", fgmask)

    # Press ESC to exit
    if cv2.waitKey(30) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
