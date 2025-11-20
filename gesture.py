import cv2
import mediapipe as mp


mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5)
mp_draw = mp.solutions.drawing_utils

def get_gesture(landmarks):
    
    try:
        
        thumb_tip_y = landmarks[mp_hands.HandLandmark.THUMB_TIP].y
        index_tip_y = landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
        middle_tip_y = landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y
        ring_tip_y = landmarks[mp_hands.HandLandmark.RING_FINGER_TIP].y
        pinky_tip_y = landmarks[mp_hands.HandLandmark.PINKY_TIP].y

        
        thumb_ip_y = landmarks[mp_hands.HandLandmark.THUMB_IP].y
        index_pip_y = landmarks[mp_hands.HandLandmark.INDEX_FINGER_PIP].y
        middle_pip_y = landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y
        ring_pip_y = landmarks[mp_hands.HandLandmark.RING_FINGER_PIP].y
        pinky_pip_y = landmarks[mp_hands.HandLandmark.PINKY_PIP].y

    except:
        
        return "Where is your hand?"

    if (thumb_tip_y < thumb_ip_y and
        index_tip_y < index_pip_y and
        middle_tip_y < middle_pip_y and
        ring_tip_y < ring_pip_y and
        pinky_tip_y < pinky_pip_y):
        return "OPEN HAND"


    if (thumb_tip_y > thumb_ip_y and
        index_tip_y > index_pip_y and
        middle_tip_y > middle_pip_y and
        ring_tip_y > ring_pip_y and
        pinky_tip_y > pinky_pip_y):
        return "FIST"
    
    if (index_tip_y > index_pip_y and
        middle_tip_y < middle_pip_y and
        ring_tip_y > ring_pip_y and
        pinky_tip_y > pinky_pip_y):
        return "DUCK SIGN"

    if (index_tip_y < index_pip_y and
        middle_tip_y < middle_pip_y and
        ring_tip_y > ring_pip_y and
        pinky_tip_y > pinky_pip_y):
        return "PEACE SIGN"
    
    
    if (thumb_tip_y < thumb_ip_y and 
        index_tip_y > index_pip_y and
        middle_tip_y > middle_pip_y and
        ring_tip_y > ring_pip_y and
        pinky_tip_y > pinky_pip_y):
        return "THUMB UP"

    return "detecting..."


cap = cv2.VideoCapture(0) 

if not cap.isOpened():
    print("Error: Cannot open webcam.")
    exit()

print("Webcam opened. Press 'q' to quit.")

while cap.isOpened():
    
    success, image = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue

    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)

    image.flags.writeable = False
    
    results = hands.process(image)

    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    gesture_name = "" 

    if results.multi_hand_landmarks:
        
        for hand_landmarks in results.multi_hand_landmarks:
            
            mp_draw.draw_landmarks(
                image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            landmarks_list = hand_landmarks.landmark
            
            gesture_name = get_gesture(landmarks_list)
    
    cv2.putText(
        image, 
        gesture_name, 
        (10, 50), 
        cv2.FONT_HERSHEY_SIMPLEX, 
        1, # Font scale
        (255, 0, 255), 
        3, 
        cv2.LINE_AA
    )

    cv2.imshow('Real-Time Gesture Recognition', image)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

print("Closing webcam.")
cap.release()
cv2.destroyAllWindows()