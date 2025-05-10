#!/usr/bin/env python3
import argparse
import os
import cv2
from ultralytics import YOLO

def real_time_detection(model_path: str, camera_source: str, output_file: str):
    """
    Perform real-time object detection using YOLOv10 and save output to a video file.
    camera_source can be:
      - an integer index (e.g. '0', '1') for local webcams
      - a string URL (rtsp://... or http://...) for network cameras
    """
    print(f"Loading model from `{model_path}`…")
    model = YOLO(model_path)

    # Determine if camera_source is an int index or a URL/path
    try:
        cam_idx = int(camera_source)
        cap = cv2.VideoCapture(cam_idx)
    except ValueError:
        cap = cv2.VideoCapture(camera_source)

    if not cap.isOpened():
        print(f"Error: Could not open camera/source `{camera_source}`.")
        return

    # Video writer setup
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps    = cap.get(cv2.CAP_PROP_FPS) or 30  # fallback to 30 fps

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out    = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

    print("Streaming… Press 'q' to quit.")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ Failed to read frame; exiting.")
            break

        # Run detection & annotate
        results = model(frame)
        annotated = results[0].plot()

        # Write & display
        out.write(annotated)
        cv2.imshow("YOLO Real-Time (q to quit)", annotated)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print(f"▶️ Video saved to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="YOLOv10 Real-Time Detection on any camera/source")
    parser.add_argument('--model',  type=str, default='yolov10l.pt',
                        help='path to your YOLOv10 model')
    parser.add_argument('--camera', type=str, default='0',
                        help="camera index (e.g. '0' or '1') or video stream URL")
    parser.add_argument('--output', type=str, default='output.avi',
                        help='where to save the annotated video')
    args = parser.parse_args()

    real_time_detection(args.model, args.camera, args.output)
