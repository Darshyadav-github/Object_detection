#!/usr/bin/env python3
"""
Live object detection with YOLO11-medium and OpenCV.
"""

import cv2
from ultralytics import YOLO

# Patch OpenCV if any threading call is missing (shouldn't be now)
if not hasattr(cv2, "setNumThreads"):
    cv2.setNumThreads = lambda n: None

def main():
    # Load the YOLO11-medium weights
    model = YOLO("yolo11m.pt")  # make sure you have the .pt in this folder

    # Open the webcam (device 0)
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("❌ Cannot open webcam")
        return

    print("▶️  Running YOLO11-medium live. Press 'Q' to quit.")
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Run inference
        results = model(frame, stream=False)

        # Draw boxes on the frame
        annotated = results[0].plot()

        # Show it
        cv2.imshow("YOLO11-Medium Live", annotated)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
