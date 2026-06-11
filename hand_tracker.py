import cv2
import mediapipe as mp
import socket
import math

# --- Configuration ---
UDP_IP = "127.0.0.1"
UDP_PORT = 8765

# Smoothing factor (Lower = smoother)
SMOOTHING_FACTOR = 0.15 
PINCH_THRESHOLD = 0.05 

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

prev_x, prev_y = 0.5, 0.5
WINDOW_NAME = "Pro Gesture Mouse"

def scale_coord(val, min_val=0.15, max_val=0.85):
    scaled = (val - min_val) / (max_val - min_val)
    return max(0.0, min(1.0, scaled))

print(f"Starting Tracker... Tracking Pinky Knuckle (Landmark 17). Sending to {UDP_IP}:{UDP_PORT}")

# Fix 1: Initialize window so we can track its properties for the close button
cv2.namedWindow(WINDOW_NAME)

while cap.isOpened():
    # Fix 2: Check if the Red 'X' was clicked (If closed, property returns -1)
    if cv2.getWindowProperty(WINDOW_NAME, cv2.WND_PROP_VISIBLE) < 1:
        break

    success, img = cap.read()
    if not success: break

    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get necessary landmarks
            thumb = hand_landmarks.landmark[4]      # Thumb tip
            index = hand_landmarks.landmark[8]      # Index tip
            
            # Fix 3: Track exactly the knuckle shown in your photo (Landmark 17)
            pinky_knuckle = hand_landmarks.landmark[17] 

            # Cursor Position based on Pinky Knuckle
            raw_x = scale_coord(pinky_knuckle.x)
            raw_y = scale_coord(pinky_knuckle.y)
            curr_x = (SMOOTHING_FACTOR * raw_x) + ((1 - SMOOTHING_FACTOR) * prev_x)
            curr_y = (SMOOTHING_FACTOR * raw_y) + ((1 - SMOOTHING_FACTOR) * prev_y)
            prev_x, prev_y = curr_x, curr_y

            # Pure Click & Drag Logic (Thumb + Index)
            distance = math.hypot(index.x - thumb.x, index.y - thumb.y)
            is_pinching = "true" if distance < PINCH_THRESHOLD else "false"

            # Send Format: "X,Y,isPinching"
            message = f"{curr_x:.4f},{curr_y:.4f},{is_pinching}"
            sock.sendto(message.encode(), (UDP_IP, UDP_PORT))

    cv2.imshow(WINDOW_NAME, img)
    
    # Check for the ESC key
    if cv2.waitKey(1) & 0xFF == 27: 
        break

cap.release()
cv2.destroyAllWindows()
print("Camera safely shut down.")
# completed