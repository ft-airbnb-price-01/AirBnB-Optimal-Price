"""Handles loading of model and predicting user input"""

import tensorflow as tf


def make_prediction(input_arr):
    """
    Takes in 2D numpy array of user input
    Loads pretrained model and predicts based on user input
    Returns predicted price per night of listing.
    """
    nn_model = tf.keras.models.load_model('brute_force_grid_search_model/')
    prediction = nn_model.predict(input_arr)
    return prediction[0]
