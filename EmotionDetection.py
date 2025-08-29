import cv2
from deepface import DeepFace
import sys

try:
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise IOError("Cannot open webcam")
except Exception as e:
    print(f"Error: {e}")
    print("Please make sure you have a webcam connected and that it is not being used by another application.")
    sys.exit()

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

print("Webcam started. Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    try:
        results = DeepFace.analyze(
            img_path=frame,
            actions=['emotion'],
            enforce_detection=False,
            detector_backend='opencv'
        )

        if isinstance(results, list) and len(results) > 0:
            for result in results:
                x = result['region']['x']
                y = result['region']['y']
                w = result['region']['w']
                h = result['region']['h']

                emotion = result['dominant_emotion']
                
                confidence = result['emotion'][emotion]
                text = f"{emotion} ({confidence:.2f}%)"

                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                font = cv2.FONT_HERSHEY_SIMPLEX
                font_scale = 1
                font_color = (255, 255, 255)
                line_type = 2
                text_size, _ = cv2.getTextSize(text, font, font_scale, line_type)
                
                cv2.rectangle(frame, (x, y - text_size[1] - 10), (x + text_size[0] + 10, y), (0, 255, 0), -1)
                
                cv2.putText(frame, text, (x + 5, y - 5), font, font_scale, font_color, line_type)

    except Exception as e:
        pass

    cv2.imshow('Emotion Recognition', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("Webcam stopped and resources released.")
