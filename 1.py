import pandas as pd
df=pd.read_csv("BMW_Car.csv",on_bad_lines="skip")
print(df.columns.tolist())