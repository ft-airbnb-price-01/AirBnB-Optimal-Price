"""Handles loading of model and predicting user input"""

import tensorflow as tf



def make_prediction(input_arr):
    nn_model = tf.keras.models.load_model('brute_force_grid_search_model/')
    prediction = nn_model.predict(input_arr)
    return prediction[0]


