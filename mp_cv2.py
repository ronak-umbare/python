import cv2
import mediapipe as mp

# Open video file
cap = cv2.VideoCapture(0)
mpHand = mp.solutions.hands
hands = mpHand.Hands(max_num_hands=2)
drawingUtils = mp.solutions.drawing_utils

# Create window and set its properties
cv2.namedWindow("Hands", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Hands", 640, 360)

while cap.isOpened():
    s, img = cap.read()
    if not s:
        break
    
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    
    if results.multi_hand_landmarks:
        for h in results.multi_hand_landmarks:
            h, w, c = img.shape
            X, Y = h[4].x*w, h[4].
            drawingUtils.draw_landmarks(img, h, mpHand.HAND_CONNECTIONS)
    
    # Display the resulting frame
    cv2.imshow("Hands", img)
    
    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# Release the video capture object
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
