import os
import cv2
import mediapipe as mp
import math
import pyautogui
import pygetwindow as gw
import time
import threading

# Variables to track if the video is liked or not
is_liked = False
last_action_time = 0
gesture_delay = 1

# Path to the gestures folder where images will be saved
gestures_folder = r"C:\Users\Hari krishan\Pictures\python\Hand gesture machine\Gestures"

# Create the 'gestures' folder if it doesn't exist
if not os.path.exists(gestures_folder):
    os.makedirs(gestures_folder)

# Initialize MediaPipe and drawing utilities
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_draw = mp.solutions.drawing_utils

# Video Capture with reduced resolution
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Track video playback state
is_paused = False

# Function to focus YouTube window
def focus_youtube_window():
    try:
        youtube_window = gw.getWindowsWithTitle("YouTube")[0]
        if youtube_window:
            youtube_window.activate()
    except IndexError:
        print("No YouTube window found.")

# Function to calculate angle between three points
def calculate_angle(p1, p2, p3):
    angle = math.degrees(math.atan2(p3.y - p2.y, p3.x - p2.x) - math.atan2(p1.y - p2.y, p1.x - p2.x))
    if angle < 0:
        angle += 360
    return angle

# Gesture recognition functions
def is_thumbs_up(landmarks):
    return landmarks[4].y < landmarks[3].y < landmarks[2].y and all(landmarks[i].y > landmarks[i - 2].y for i in [8, 12, 16, 20])

def is_thumbs_down(landmarks):
    return landmarks[4].y > landmarks[3].y > landmarks[2].y and all(landmarks[i].y < landmarks[i - 2].y for i in [8, 12, 16, 20])

def are_all_fingers_open(landmarks):
    return all(landmarks[i].y < landmarks[i - 2].y for i in [8, 12, 16, 20])

def are_all_fingers_closed(landmarks):
    return all(landmarks[i].y > landmarks[i - 2].y for i in [8, 12, 16, 20])

def is_victory_sign(landmarks):
    return landmarks[8].y < landmarks[6].y and landmarks[12].y < landmarks[10].y and all(landmarks[i].y > landmarks[i - 2].y for i in [16, 20])

# Threaded function for video processing
def process_video():
    global is_paused, is_liked, last_action_time

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                landmarks = hand_landmarks.landmark

                # Play/Pause toggle
                if are_all_fingers_open(landmarks) and not is_paused:
                    focus_youtube_window()
                    pyautogui.press('space')
                    is_paused = True

                elif are_all_fingers_closed(landmarks) and is_paused:
                    focus_youtube_window()
                    pyautogui.press('space')
                    is_paused = False

                # Thumbs Up to Like Video
                current_time = time.time()
                if is_thumbs_up(landmarks) and current_time - last_action_time > gesture_delay:
                    if not is_liked:
                        pyautogui.press('l')
                        is_liked = True
                        last_action_time = current_time

                # Thumbs Down to Unlike Video
                if is_thumbs_down(landmarks) and current_time - last_action_time > gesture_delay:
                    if is_liked:
                        pyautogui.press('l')
                        is_liked = False
                        last_action_time = current_time

                # Detect Victory Sign and Save Image
                if is_victory_sign(landmarks):
                    image_filename = os.path.join(gestures_folder, "victory_sign_picture.jpg")
                    success = cv2.imwrite(image_filename, frame)
                    if success:
                        print(f"Victory sign picture saved: {image_filename}")

        # Show the frame
        cv2.imshow("Hand Gesture Recognition", frame)

        # Stop the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Run the process_video function in a thread
capture_thread = threading.Thread(target=process_video)
capture_thread.start()

# Wait for the thread to complete
capture_thread.join()

# Release resources
cap.release()
cv2.destroyAllWindows()
hands.close()
