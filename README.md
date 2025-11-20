# Real-Time Hand Gesture Recognition

This project uses **OpenCV** and **MediaPipe** to detect a hand from your webcam and classify simple gestures like:

- OPEN HAND  
- FIST  
- DUCK SIGN  
- PEACE SIGN  
- THUMB UP  

The gesture name is displayed live on the video feed.

---

## 🧠 How It Works

- Uses **MediaPipe Hands** to detect hand landmarks from the webcam.
- Extracts landmark positions for each finger (tip and joint).
- Applies simple rules based on landmark positions (tip vs joint) to classify:
  - All fingers up → `OPEN HAND`
  - All fingers down → `FIST`

- Displays the video stream with:
  - Hand landmarks drawn.
  - The detected gesture name shown on the frame.

---

## 📦 Requirements

Install dependencies using:

pip install -r requirements.txt
The main libraries are:

opencv-python

mediapipe

▶️ How to Run
Make sure a webcam is connected.

Run the Python script:

python gesture.py

A window will open showing the webcam feed.

Try different hand gestures in front of the camera.

Press q to quit.

📁 Project Structure (example)
text
Copy code
hand-gesture-recognition/
├─ gesture.py
├─ requirements.txt
└─ README.md
❗ Notes
If the webcam cannot be opened, the program will print an error message and exit.

If no hand is detected, it shows: detecting....

If landmark extraction fails, it returns: Where is your hand?.