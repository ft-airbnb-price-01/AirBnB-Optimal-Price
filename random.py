'''
dummy file
'''

import pandas as p


list_file = open("List", "wb")
dataframe_file = open("dataframe", "wb")

dataframe = p.DataFrame()

list_values = [1,2,3]

pickle.dump(dataframe, dataframe_file)

