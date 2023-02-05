# Valari Graham 
# Programming Challenge Feb 2023

import os 
import pandas as pd

df = pd.DataFrame()

for file in os.listdir(os.getcwd()):
	if file.endswith(".csv"):
		df_file = pd.read_csv(file)
		# Add column identifier to the file 
		df_file[len(df_file.columns)] = file
		# Add file to the master dataframe 
		df = df.append(df_file)
	else :
		print("This file is not compatible:" + file)

# Add filename to the last column as the identifier 
df = df.set_axis([*df.columns[:-1], 'filename'], axis=1)

# Print first 10 rows to terminal 
print(df.head(10))

# Output combined master dataframe to .csv 
df.to_csv("combined.csv", index = False) 