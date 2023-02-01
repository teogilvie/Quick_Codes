# update incorrectly named columns 

import pandas as pd 

#read csv file
df = pd.read_csv("Lunas_Smoke_Shop_Catalogue_Items.csv")

n = 1

for x in range(1, len(df.loc[:, 'Name'])):
    if df.loc[x, 'Name'] == df.loc[(x-1), 'Name']:
        df.loc[x, 'fieldType'] = 'Variant'
    elif df.loc[x, 'Name'] != df.loc[(x-1), 'Name']:
        df.loc[x, 'fieldType'] = 'Product'
    
for x in range(1, len(df.loc[:, 'Name'])):
    if df.loc[x, 'fieldType'] == 'Product':
        n = n + 1
        df.loc[x, 'HandleId'] = f'Product_{n}'
    elif df.loc[x, 'fieldType'] == 'Variant':
        df.loc[x, 'HandleId'] = df.loc[x-1, 'HandleId']

#write to csv
df.to_csv("Lunas_Smoke_Shop_Catalogue_Items.csv", index=False)