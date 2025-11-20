import os
import sys
import config
from models import MObileNetClassifier
from units import video_processor, preprocessing, visualisation


def classify_video(video_path):
    if os.path.exists(video_path):
        print(" The video path not exist")
        return


        #Extraction of frames
        frames, _=extract_frames(video_path, num_frames = NUM_FRAMES)

        #classify the object
        classifier = MobileNetClassifier()
        preprocessing = preprocess_batch(
    frames,
    target_size=config.INPUT_SIZE
)
        prediction = classifier.predict(preprocessing)

        #results
        print("result summary")
        print_results_summary(prediction,  len(frames))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("python inference")
        sys.exit(1)

    classify_video(sys.argv[1])