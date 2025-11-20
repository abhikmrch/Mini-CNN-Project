import os
Base_DIR = os.path.dirname(os.path.abspath(_file_))
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
os.makedirs(OUTPUT_DIR, exist_ok = True)

NUM_FRAMES = 30
INPUT_SIZE = (224,224)