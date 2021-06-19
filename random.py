'''
dummy file
'''

import pandas as pd


list_file = open("List", "wb")
dataframe_file = open("dataframe", "wb")

dataframe = pd.DataFrame()

list_values = [1,2,3]

pickle.dump(dataframe, dataframe_file)

