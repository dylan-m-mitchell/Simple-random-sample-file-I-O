import random
import pandas as pd 

df = pd.read_excel('tariff_database_202405.xlsx', sheet_name="trade_tariff_database_202405") #create file reader

df = df.dropna(subset=["col2_ad_val_rate"]) # drop nan values

values_to_exclude = [0.0, 9999.99, 9999.9999999] #drop outlier values so that we can gather real data to mess around with
df = df[~df['col2_ad_val_rate'].isin(values_to_exclude)]

mylist = df['col2_ad_val_rate'].tolist() # add data to a list


# for i in mylist:
#     print(i)
#     print(" ")
    
    
print(random.sample(mylist, k=25))