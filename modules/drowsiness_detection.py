from utils.config import THRESHOLD

def check_drowsiness(eye_closed_frames):
    return eye_closed_frames > THRESHOLD