import cv2

# Task parameters
SURNAME = "kushchevskyi"
TYPES_OF_CLOTHES = 3
BACKGROUND_TYPES = [
    "monotonous",
    "big_objects",
    "bad_lighting"
]
PHOTO_PER_BACKGROUND = 120
SHOT_INTERVAL_SEC = 0.5

# Window parameters
CAMERA_NUM = 0
WINDOW_NAME = "WebCam"
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

# Area parameters
AREA_WIDTH = 170
AREA_HEIGHT = 190
AREA_THIKNESS = 2
AREA_COLOR_BGR = (0, 0, 255)

# Text parameters
TEXT_X = 0
TEXT_Y = 0
TEXT_THICKNESS = 2
TEXT_FONT = cv2.FONT_HERSHEY_SIMPLEX
TEXT_FONT_SCALE = 0.6
TEXT_COLOR_BGR = (135, 0, 0)

# Buttons
SHOT_BLOCK_BUTTON = 32
