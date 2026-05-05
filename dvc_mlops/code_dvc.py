import pandas as pd
import os
#create a dataframe with columns name
data = {'Name': ['ayan','krish','bill'], 
        'Age': [20,25,30],
        'City':['Chd','wb','hr']}
df = pd.DataFrame(data)
# adding a new row for v2 of data
new_row_loc = {'Name':"Rah","Age":20,"City": "Chd"}
df.loc[len(df.index)] = new_row_loc 
data_dir = 'data'
os.makedirs(data_dir, exist_ok = True)

#Define file path 
file_path = os.path.join(data_dir, 'sample_data2.csv')

#Save the DataFrame to a CSV file, including Column Names
df.to_csv(file_path, index = False)

print(f"CSV file saved to {file_path}")

