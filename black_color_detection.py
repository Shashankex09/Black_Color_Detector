import cv2
import numpy as np

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Better FPS control
cap.set(3, 640)
cap.set(4, 480)

if not cap.isOpened():
    print("❌ Camera not detected")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)

    # Blur for noise reduction
    blurred = cv2.GaussianBlur(frame, (7, 7), 0)

    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    # 🔥 IMPROVED BLACK RANGE (wider but controlled)
    lower_black = np.array([0, 0, 0])
    upper_black = np.array([180, 255, 80])  # increased range

    mask = cv2.inRange(hsv, lower_black, upper_black)

    # ================= ADVANCED FILTERING =================

    kernel = np.ones((5, 5), np.uint8)

    # Remove small noise
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    # Fill gaps
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # Smooth edges
    mask = cv2.GaussianBlur(mask, (5, 5), 0)

    # ================= CONTOUR DETECTION =================

    contours = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

    if len(contours) > 0:
        # Only largest contour (important 🔥)
        cnt = max(contours, key=cv2.contourArea)

        area = cv2.contourArea(cnt)

        if area > 1500:  # increased threshold for accuracy
            x, y, w, h = cv2.boundingRect(cnt)

            # Draw bounding box
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 0), 2)

            cx = x + w // 2
            cy = y + h // 2

            # Draw center
            cv2.circle(frame, (cx, cy), 6, (0, 255, 0), -1)

            cv2.putText(frame, f"BLACK ({cx},{cy})",
                        (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6,
                        (255, 255, 255),
                        2)

    # ================= DISPLAY =================

    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)

    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()