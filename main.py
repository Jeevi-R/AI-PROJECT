import cv2
from modules.video_capture import start_camera
from modules.face_eye_detection import detect_face_eyes
from modules.eye_monitor import update_eye_status
from modules.drowsiness_detection import check_drowsiness
from modules.alert_system import start_alarm, stop_alarm


def main():
    print("🚀 Program started...")

    cap = start_camera()

    # Camera check
    if cap is None:
        print("❌ Camera not working. Exiting...")
        return

    while True:
        ret, frame = cap.read()

        if not ret:
            print("❌ Frame read error")
            break

        # Detect face and eyes
        faces, eyes_detected, frame = detect_face_eyes(frame)

        # Monitor eye closure
        eye_closed_frames = update_eye_status(eyes_detected)

        # Check drowsiness
        is_drowsy = check_drowsiness(eye_closed_frames)

        if is_drowsy:
            cv2.putText(frame, "DROWSY!", (100, 100),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        2, (0, 0, 255), 3)
            start_alarm()
        else:
            stop_alarm()

        # Show output window
        cv2.imshow("Driver Drowsiness Detection", frame)

        # Exit on ESC key
        if cv2.waitKey(1) & 0xFF == 27:
            print("🛑 Exiting program...")
            break

    cap.release()
    cv2.destroyAllWindows()


# 🔥 IMPORTANT
if __name__ == "__main__":
    main()