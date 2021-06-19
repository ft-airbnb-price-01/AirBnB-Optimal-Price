'''
dummy file
'''

import pandas as pand


list_file = open("List", "wb")
dataframe_file = open("dataframe", "wb")

dataframe = pand.DataFrame()

list_values = [1,2,3]

pickle.dump(dataframe, dataframe_file)

