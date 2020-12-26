from screeninfo import get_monitors
from config import *
import platform
import copy
import time
import cv2
import os

# Task parameters
BLOCK_SIZE = int(PHOTO_PER_BACKGROUND / TYPES_OF_CLOTHES)
if not BLOCK_SIZE * TYPES_OF_CLOTHES == PHOTO_PER_BACKGROUND:
    print("ERROR: PHOTO_PER_BACKGROUND / TYPES_OF_CLOTHES NEEDS TO BE INTEGER")
    exit(1)

# Screen parameters
SCREEN_WIDTH = get_monitors()[0].width
SCREEN_HEIGHT = get_monitors()[0].height

# Area parameters
AREA_LEFT_X = int(WINDOW_WIDTH / 2 - AREA_WIDTH / 2)
AREA_LEFT_Y = int(WINDOW_HEIGHT / 2 - AREA_HEIGHT / 2)
AREA_RIGHT_X = int(WINDOW_WIDTH / 2 + AREA_WIDTH / 2)
AREA_RIGHT_Y = int(WINDOW_HEIGHT / 2 + AREA_HEIGHT / 2)
AREA_LEFT = (AREA_LEFT_X, AREA_LEFT_Y)
AREA_RIGHT = (AREA_RIGHT_X, AREA_RIGHT_Y)

# Text parameters
TEXT_HEIGHT = int(TEXT_FONT_SCALE * 33)

# Buttons
EXIT_BUTTON = 27


def init_cam():
    cv2.namedWindow(WINDOW_NAME)
    cv2.resizeWindow(WINDOW_NAME, WINDOW_WIDTH, WINDOW_HEIGHT)
    cv2.moveWindow(
        WINDOW_NAME,
        int(SCREEN_WIDTH / 2 - WINDOW_WIDTH / 2),
        int(SCREEN_HEIGHT / 2 - WINDOW_HEIGHT / 2)
    )

    camera = cv2.VideoCapture(CAMERA_NUM)
    if camera.isOpened():
        return camera
    else:
        return None


def get_frame(app_data):
    rval, frame = app_data["camera"].read()
    real_frame = copy.deepcopy(frame)
    showed_frame = cv2.rectangle(
        frame,
        AREA_LEFT,
        AREA_RIGHT,
        AREA_COLOR_BGR,
        AREA_THIKNESS
    )
    now_ppb = app_data["current_photo"] % PHOTO_PER_BACKGROUND
    now_bt = BACKGROUND_TYPES[
        int(app_data["current_photo"] / PHOTO_PER_BACKGROUND)
    ]
    log_text = [
        f'Photos Shoot for background: {now_ppb}',
        f'Background Type: {now_bt}',
        f'Photos Shoot: {app_data["current_photo"]}',
        f'Saving Mode: {str(app_data["saving_mode"])}'
    ]
    for i in range(len(log_text)):
        showed_frame = cv2.putText(
            showed_frame, log_text[i],
            (TEXT_X, TEXT_Y + (i + 1) * TEXT_HEIGHT),
            TEXT_FONT, TEXT_FONT_SCALE,
            TEXT_COLOR_BGR, TEXT_THICKNESS,
            bottomLeftOrigin=False
        )

    return rval, real_frame, showed_frame


def save_frame(app_data, frame):
    bg_id = int(app_data["current_photo"] / PHOTO_PER_BACKGROUND)
    shot_id = app_data["current_photo"] % (PHOTO_PER_BACKGROUND)
    background = BACKGROUND_TYPES[bg_id]
    if platform.system() == "Windows":
        path = f"{SURNAME}\{background}\{SURNAME}_{bg_id + 1}_{shot_id + 1}.bmp"
    else:
        path = f"{SURNAME}/{background}/{SURNAME}_{bg_id + 1}_{shot_id + 1}.bmp"
    print(path)
    cv2.imwrite(path, frame)
    app_data["current_photo"] += 1

    bg_amount = len(BACKGROUND_TYPES)
    if int(app_data["current_photo"] / PHOTO_PER_BACKGROUND) == bg_amount:
        print("Success")
        return 0
    return 1


def main_loop(app_data):
    old_time = time.time()
    rval, frame, showed_frame = get_frame(app_data)
    while cv2.getWindowProperty(
            WINDOW_NAME, cv2.WND_PROP_VISIBLE) > 0 and rval:
        cv2.imshow(WINDOW_NAME, showed_frame)
        rval, frame, showed_frame = get_frame(app_data)

        now_time = time.time()
        dt = now_time - old_time
        if app_data["saving_mode"] and dt >= SHOT_INTERVAL_SEC:
            old_time = now_time
            if save_frame(app_data, frame) == 0:
                break

        if app_data["current_photo"] % BLOCK_SIZE == 0:
            app_data["saving_mode"] = False

        key = cv2.waitKey(20)
        if key == EXIT_BUTTON:
            break
        elif key == SHOT_BLOCK_BUTTON:
            app_data["saving_mode"] = True


def deinit_cam():
    cv2.destroyWindow(WINDOW_NAME)


def prepare_storage():
    if platform.system() == "Windows":
        del_cmd = "RMDIR /S /Q"
        create_cmd = "MKDIR"
    else:
        del_cmd = "rm -rf"
        create_cmd = "mkdir -p"
    os.system(f"{del_cmd} {SURNAME}")
    for dir_name in BACKGROUND_TYPES:
        if platform.system() == "Windows":
            os.system(f"{create_cmd} {SURNAME}\{dir_name}")
        else:
            os.system(f"{create_cmd} {SURNAME}/{dir_name}")


if __name__ == "__main__":
    camera = init_cam()
    if camera is not None:
        app_data = {
            "saving_mode": False,
            "current_photo": 0,
            "camera": camera
        }
        prepare_storage()
        main_loop(app_data)
    deinit_cam()
