from tensorflow.keras.applications import MObileNetV2
from tensorflow.keras.applications.MObileNetV2 import decode_prediction
import numpy as np


class MObileNetClassifier:
    def _init_(self):
        print("Loading of the model.....")
        self.model = MObileNetV2(weight = 'imagenet')
        print("Model Ready!")

        def predict(self, frames):
            if len(frames.shape) == 3:
                frames = np.expand_dims(frames, axis=0)

                preds = self.model.predict(frames,verbose = 1)
                
                results = []

                for pred in preds:
                    decode = decode_prediction(np.expand_dims(pred,0), top = 5[0])
                    results.append([(name, float(prob)) for _, name, prob in decode])
                    return results
                    