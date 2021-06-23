"""Handles loading of model and predicting user input"""

import tensorflow as tf



def make_prediction(input_arr):
    nn_model = tf.keras.models.load_model('./my_model')
    prediction = nn_model.predict(input_arr)
    return prediction


# if __name__ == "__main__":
# model = make_prediction()
# print(model.summary())
