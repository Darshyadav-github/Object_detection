# YOLO Real-Time Object Detection

This repository contains two Python scripts for live object detection using Ultralytics’ YOLO models and OpenCV:

- **`yolvo10.py`** – Real-time detection with YOLOv10 (any variant) and video saving.  
- **`yolo11.py`** – Simple webcam demo using YOLO11-medium.

---

## 📋 Table of Contents

- [Requirements](#requirements)  
- [Installation](#installation)  
- [Usage](#usage)  
  - [`yolvo10.py`](#yolvo10py)  
  - [`yolo11.py`](#yolo11py)  
- [Custom Models](#custom-models)  
- [Contributing](#contributing)  
- [License](#license)  

---

## Requirements

- Python 3.8+  
- [Ultralytics YOLO](https://pypi.org/project/ultralytics/)  
- OpenCV (`opencv-python`)  
- NumPy  
- (Optional) a webcam or video-stream URL  

---

## Installation

1. Clone this repo:
   ```bash
   git clone https://github.com/yourusername/yolo-realtime.git
   cd yolo-realtime
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # Linux/macOS
   venv\Scripts\activate      # Windows
   ```

3. Install dependencies:
   ```bash
   pip install ultralytics opencv-python numpy
   ```

---

## Usage

### `yolvo10.py`

Real-time detection with YOLOv10 models. Annotated video frames are displayed live and saved to an output file.

```bash
python yolvo10.py   --model yolov10l.pt   --camera 0   --output output.avi
```

**Arguments**  
- `--model`  Path to your YOLOv10 `.pt` weights (default: `yolov10l.pt`).  
- `--camera` Camera index (`0`, `1`, …) or video stream URL (e.g., `rtsp://…`).  
- `--output` Path to save the annotated video (default: `output.avi`).

---

### `yolo11.py`

Webcam-only live detection demo using YOLO11-medium. Displays annotated frames in a window.

```bash
python yolo11.py
```

**Key Details**  
- Loads `yolo11m.pt` (ensure this file is in the same folder).  
- Opens your default webcam (`device 0`).  
- Press **Q** in the display window to quit.

---

## Custom Models

To use your own YOLO weights:

1. Download or train your `.pt` file (e.g., `yolov10-custom.pt` or `yolo11m-custom.pt`).  
2. Pass its path via `--model` (for `yolvo10.py`) or replace the default filename in `yolo11.py`.

---

## Contributing

1. Fork the repository  
2. Create a feature branch (`git checkout -b feature/YourFeature`)  
3. Commit your changes (`git commit -m "Add feature"`)  
4. Push to your branch (`git push origin feature/YourFeature`)  
5. Open a Pull Request

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
