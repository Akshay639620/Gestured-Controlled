# 🖐️ Gesture Controlled Mouse

A real-time hand gesture based virtual mouse system that allows users to control the computer cursor without using a physical mouse.  
The project uses computer vision to detect hand movements and converts gestures into mouse actions.

---

## 🚀 Features

- Real-time hand tracking using webcam
- Cursor control using hand movements
- Pinch gesture for mouse click
- Drag and drop functionality
- Smooth cursor movement
- Contactless mouse control

---

## 🛠️ Technologies Used

- Python
- Java
- OpenCV
- MediaPipe
- Socket Programming (UDP)
- Java Robot API

---

## 📂 Project Structure

```
Gesture-Controlled-Mouse/

├── hand_tracker.py       # Detects hand gestures using webcam
├── GestureMouse.java     # Controls mouse actions
└── README.md
```

---

## ⚙️ Working

1. Webcam captures real-time hand movement.
2. Python uses OpenCV and MediaPipe for hand landmark detection.
3. Hand coordinates and gestures are processed.
4. Data is transferred from Python to Java using UDP socket communication.
5. Java Robot API performs mouse movement, click, and drag operations.

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Gesture-Controlled-Mouse.git
```

Move into project folder:

```bash
cd Gesture-Controlled-Mouse
```

Install required Python libraries:

```bash
pip install opencv-python mediapipe
```

Compile Java program:

```bash
javac GestureMouse.java
```

---

## ▶️ How to Run

Start the Java mouse controller:

```bash
java GestureMouse
```

Run the Python hand tracker:

```bash
python hand_tracker.py
```

---

## 🎮 Gesture Controls

| Gesture | Action |
|--------|--------|
| Move Hand | Move Cursor |
| Thumb + Index Pinch | Mouse Click |
| Hold Pinch + Move | Drag & Drop |

---

## 🔮 Future Scope

- Add more gestures such as right click and scrolling.
- Improve gesture recognition accuracy using AI models.
- Create a GUI application for easier user interaction.
- Add customizable gestures based on user preference.

---

## 👨‍💻 Author

Developed by **Your Name**
