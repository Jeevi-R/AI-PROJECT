eye_closed_frames = 0

def update_eye_status(eyes_detected):
    global eye_closed_frames

    if not eyes_detected:
        eye_closed_frames += 1
    else:
        eye_closed_frames = 0

    return eye_closed_frames