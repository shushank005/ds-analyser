import pandas as pd
data={'Name':['Shushank','Nitish','Rahul'],
      'Age':[21,25,32]}
df=pd.DataFrame(data)
print("Analysis script is running!")
print(df)
final_df=df.drop_duplicates()
print(final_df)