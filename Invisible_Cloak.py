import cv2
import numpy as np
import time

# Start the webcam
cap = cv2.VideoCapture(0)
time.sleep(2)  # Allow the camera to warm up

# Capture the background
print("Capturing background. Please stay out of the frame...")
for i in range(60):
    ret, background = cap.read()
background = np.flip(background, axis=1)  # Mirror the background

print("Background captured. Now you can wear the black cloak!")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = np.flip(frame, axis=1)

    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define range for black color (you can fine-tune these values)
    lower_black = np.array([0, 0, 0])
    upper_black = np.array([180, 255, 50])

    # Create a mask for black color
    mask = cv2.inRange(hsv, lower_black, upper_black)

    # Refine the mask
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))
    mask = cv2.dilate(mask, np.ones((3,3), np.uint8), iterations=1)

    # Inverse the mask to get parts that are not black
    mask_inv = cv2.bitwise_not(mask)

    # Segment out the cloak (black area)
    cloak_area = cv2.bitwise_and(background, background, mask=mask)

    # Segment out everything else
    non_cloak_area = cv2.bitwise_and(frame, frame, mask=mask_inv)

    # Combine both
    final_output = cv2.addWeighted(cloak_area, 1, non_cloak_area, 1, 0)

    cv2.imshow('Invisible Cloak (Black)', final_output)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
