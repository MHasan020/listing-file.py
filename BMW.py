import pandas as pd

# 1. BMW CSV file read karein
df = pd.read_csv("BMW_Car.csv")

# 2. Duplicate rows remove karein
df = df.drop_duplicates()

# 3. Empty spaces remove karein
df.columns = df.columns.str.strip()

# 4. Price ko numeric banayein
df["Price (PKR)"] = pd.to_numeric(df["Price (PKR)"], errors="coerce")

# 5. Auction Rating ko numeric banayein
df["Auction Rating"] = pd.to_numeric(df["Auction Rating"], errors="coerce")

# 6. Model Year ko numeric banayein
df["Model Year"] = pd.to_numeric(df["Model Year"], errors="coerce")

# 7. Mileage ko numeric banayein
df["Mileage"] = pd.to_numeric(df["Mileage"], errors="coerce")

# 8. Engine Capacity ko numeric banayein
df["Engine Capacity"] = pd.to_numeric(df["Engine Capacity"], errors="coerce")

# 9. Price missing ho to un rows ko remove karein
df = df.dropna(subset=["Price (PKR)"])

# 10. Car Name se extra spaces remove karein
df["Car Name"] = df["Car Name"].astype(str).str.strip()

# 11. Fuel Type ko clean karein
df["Fuel Type"] = df["Fuel Type"].astype(str).str.strip()

# 12. Transmission ko clean karein
df["Transmission"] = df["Transmission"].astype(str).str.strip()

# 13. Engine Unit ko clean karein
df["Engine Unit"] = df["Engine Unit"].astype(str).str.strip()

# 14. Price ko normal integer format mein karein
df["Price (PKR)"] = df["Price (PKR)"].round(0).astype("int64")

# 15. Cleaned file save karein
df.to_csv("BMW_Car_Cleaned.csv", index=False)

print("Data cleaning complete!")
print("Original rows:", len(pd.read_csv("BMW_Car.csv")))
print("Cleaned rows:", len(df))
print("Cleaned file: BMW_Car_Cleaned.csv")