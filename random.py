'''
dummy file
'''

<<<<<<< HEAD
import pandas as p
=======
import pandas as pand
>>>>>>> 8c5cd5a4e685e2beac5881635b14fe8b5c9f3914


list_file = open("List", "wb")
dataframe_file = open("dataframe", "wb")

<<<<<<< HEAD
dataframe = p.DataFrame()
=======
dataframe = pand.DataFrame()
>>>>>>> 8c5cd5a4e685e2beac5881635b14fe8b5c9f3914

list_values = [1,2,3]

pickle.dump(dataframe, dataframe_file)

