from tensorflow import keras
import tensorflow as tf
import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import os
os.makedirs("logs", exist_ok-True)

print(f"load minst dataset")

(X_train, Y_Train),(x_test,y_test) = keras.datasets.mnist.load_data()

# Normalizing of the data
X_train = X_train.astype("float32")/255.0
x_test = x_test.astype("float32")/255.0

#reshaping of the data to cnn

X_train = X_train.reshape(-1,28,28,3)
x_test = x_test.reshape(-1,28,28,3)