import pandas as pd
import numpy as np 
from datetime import datetime, timedelta
np.random.seed(42)
num_rows=400
cities=["Lahore", "Karachi", "Islamabad", "Faisalabad", "Multan", "Peshawar", "Sargodha", "Rawalpindi"]
categories=["Electronics", "Clothing", "Groceries", "Cosmetics", "Footwear", "Home Application"]
start_data= datetime(2024, 1, 1)
end_date= datetime(2024, 12, 31)
date_range=(end_date-start_data).days
date= {
    "Date": [start_data + timedelta(days=np.random.randint(0, date_range)) for _ in range(num_rows)],
    "City": np.random.choice(cities, num_rows),
    "Product Category": np.random.choice(categories, num_rows),
    "Units Sold": np.random.randint(1, 50, num_rows),
}
df = pd.DataFrame(date)
price_per_unit=np.random.randint(200, 500, num_rows)
df["Revenue"] = df["Units Sold"] * price_per_unit
df["Profit"] = (df["Revenue"] * np.random.uniform(0.10, 0.30, num_rows)).round(0)
df = df.sort_values("Date").reset_index(drop=True)
df.to_csv("pakistan_retail_sales.csv", index=False)
print(df.head())
print(df.info())
print(df.isnull().sum())
print(df.duplicated().sum())
print(df.shape)