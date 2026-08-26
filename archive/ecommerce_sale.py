import pandas as pd
import numpy as np
import os

file_path = os.path.join(
    os.path.dirname(__file__),
    "ecommerce_sales.csv"
)

print("Reading:", file_path)

df = pd.read_csv(file_path)

print(df.head())
print("Shape:", df.shape)

print("\nData Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nBasic Statistics:")
print(df.describe())

df = df.drop_duplicates()

print("\nShape after removing duplicates:")
print(df.shape)

df["order_date"] = pd.to_datetime(
    df["order_date"],
    errors="coerce"
)

print("\nDate column after conversion:")
print(df["order_date"].dtype)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nInvalid Values:")

print("Quantity <= 0:",
      (df["quantity"] <= 0).sum())

print("Unit Price <= 0:",
      (df["unit_price"] <= 0).sum())

print("Revenue < 0:",
      (df["revenue"] < 0).sum())

print("Discount < 0:",
      (df["discount"] < 0).sum())

print("Discount > 1:",
      (df["discount"] > 1).sum())

print("Rating below 1:",
      (df["customer_rating"] < 1).sum())

print("Rating above 5:",
      (df["customer_rating"] > 5).sum())

df = df[
    (df["quantity"] > 0) &
    (df["unit_price"] > 0) &
    (df["revenue"] >= 0) &
    (df["discount"] >= 0) &
    (df["discount"] <= 1) &
    (df["customer_rating"] >= 1) &
    (df["customer_rating"] <= 5)
].copy()

print("\nShape after removing invalid rows:")
print(df.shape)

df["year"] = df["order_date"].dt.year

df["month"] = df["order_date"].dt.month

df["month_name"] = df["order_date"].dt.month_name()

df["quarter"] = df["order_date"].dt.quarter

df["day_name"] = df["order_date"].dt.day_name()


df["gross_sales"] = (
    df["quantity"] * df["unit_price"]
)

df["discount_amount"] = (
    df["gross_sales"] * df["discount"]
)

df["net_sales"] = (
    df["gross_sales"] - df["discount_amount"]
)


print("\nNew Columns Created:")
print(df.columns)


df["delivery_category"] = np.select(
    [
        df["delivery_days"] <= 3,
        df["delivery_days"] <= 7,
        df["delivery_days"] > 7
    ],
    [
        "Fast",
        "Standard",
        "Slow"
    ],
    default="Unknown"
)


df["rating_category"] = np.select(
    [
        df["customer_rating"] >= 4,
        df["customer_rating"] >= 3
    ],
    [
        "Good",
        "Average"
    ],
    default="Poor"
)

print("\nDelivery Categories:")
print(df["delivery_category"].value_counts())

print("\nRating Categories:")
print(df["rating_category"].value_counts())

df = df.sort_values("order_date")
df = df.reset_index(drop=True)

df.to_csv(
    "ecommerce_sales_cleaned.csv",
    index=False
)

print("\nCleaned data saved successfully!")
print("File: ecommerce_sales_cleaned.csv")
print("Final Shape:", df.shape)
print("\n==============================")
print("FINAL DATASET CHECK")
print("==============================")

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nFirst 5 Rows:")
print(df.head())