import cv2
from utils.config import CAMERA_INDEX

def start_camera():
    print("🔄 Starting camera...")

    cap = cv2.VideoCapture(CAMERA_INDEX)

    # Try alternative index if failed
    if not cap.isOpened():
        print("⚠️ Camera index failed, trying 0...")
        cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("❌ Camera open aagala")
        return None

    print("✅ Camera started successfully")
    return cap