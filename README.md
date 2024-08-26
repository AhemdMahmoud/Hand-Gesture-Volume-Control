# Hand Gesture Volume Control

This project uses computer vision and hand tracking to control the system volume through hand gestures. By detecting the distance between your thumb and index finger, you can adjust the volume level of your computer.

## Demo

[Link to demo video]

## Features

- Real-time hand tracking
- Volume control through hand gestures
- Visual feedback with volume bar and percentage
- FPS display

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7+
- OpenCV
- NumPy
- Mediapipe
- CVZone
- Pycaw

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/AhemdMahmoud/Hand-Gesture-Volume-Control.git
   ```

2. Install the required packages:
   ```
   pip install opencv-python numpy mediapipe cvzone
   ```

3. Install Pycaw:
   ```
   pip install https://github.com/AndreMiras/pycaw/archive/develop.zip
   ```

## Usage

1. Run the script:
   ```
   python hand_gesture_volume_control.py
   ```

2. Place your hand in front of the camera.
3. Adjust the distance between your thumb and index finger to control the volume.
4. Press 'q' to quit the application.

## How it works

1. The script captures video from your default camera.
2. It uses the HandDetector from CVZone to track your hand.
3. The distance between the thumb and index finger is calculated.
4. This distance is mapped to a volume range.
5. The system volume is adjusted accordingly.
6. Visual feedback is provided on the video feed.
