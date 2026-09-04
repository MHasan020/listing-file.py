import pandas as pd
import numpy as np

df = pd.read_csv("listings.csv")

df = df.drop_duplicates()

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

columns = [
    "id",
    "listing_url",
    "name",
    "host_id",
    "host_name",
    "host_since",
    "neighbourhood_cleansed",
    "property_type",
    "room_type",
    "accommodates",
    "bathrooms",
    "bedrooms",
    "beds",
    "price",
    "weekly_price",
    "monthly_price",
    "security_deposit",
    "cleaning_fee",
    "guests_included",
    "minimum_nights",
    "maximum_nights",
    "number_of_reviews",
    "review_scores_rating",
    "review_scores_accuracy",
    "review_scores_cleanliness",
    "review_scores_checkin",
    "review_scores_communication",
    "review_scores_location",
    "review_scores_value",
    "availability_365",
    "calculated_host_listings_count",
    "host_is_superhost"
]

columns = [column for column in columns if column in df.columns]

df = df[columns].copy()

df["id"] = pd.to_numeric(
    df["id"],
    errors="coerce"
)

df = df.dropna(subset=["id"])

df["id"] = df["id"].astype(int)

numeric_columns = [
    "host_id",
    "accommodates",
    "bathrooms",
    "bedrooms",
    "beds",
    "guests_included",
    "minimum_nights",
    "maximum_nights",
    "number_of_reviews",
    "review_scores_rating",
    "review_scores_accuracy",
    "review_scores_cleanliness",
    "review_scores_checkin",
    "review_scores_communication",
    "review_scores_location",
    "review_scores_value",
    "availability_365",
    "calculated_host_listings_count"
]

for column in numeric_columns:
    if column in df.columns:
        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )

price_columns = [
    "price",
    "weekly_price",
    "monthly_price",
    "security_deposit",
    "cleaning_fee"
]

for column in price_columns:
    if column in df.columns:
        df[column] = (
            df[column]
            .astype(str)
            .str.replace("$", "", regex=False)
            .str.replace(",", "", regex=False)
            .replace("nan", np.nan)
        )

        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )

date_columns = [
    "host_since"
]

for column in date_columns:
    if column in df.columns:
        df[column] = pd.to_datetime(
            df[column],
            errors="coerce"
        )

if "price" in df.columns:
    df.loc[df["price"] <= 0, "price"] = np.nan

    df["price_status"] = np.where(
        df["price"].isna(),
        "Unknown",
        "Available"
    )

    df["price_category"] = pd.cut(
        df["price"],
        bins=[-np.inf, 75, 150, 250, np.inf],
        labels=[
            "Budget",
            "Standard",
            "Premium",
            "Luxury"
        ]
    )

if "review_scores_rating" in df.columns:
    df.loc[
        (df["review_scores_rating"] < 0) |
        (df["review_scores_rating"] > 100),
        "review_scores_rating"
    ] = np.nan

    df["rating_category"] = pd.cut(
        df["review_scores_rating"],
        bins=[-np.inf, 60, 80, 90, 100],
        labels=[
            "Low",
            "Good",
            "Very Good",
            "Excellent"
        ]
    )

if "availability_365" in df.columns:
    df.loc[
        (df["availability_365"] < 0) |
        (df["availability_365"] > 365),
        "availability_365"
    ] = np.nan

    df["availability_category"] = pd.cut(
        df["availability_365"],
        bins=[-1, 30, 90, 180, 365],
        labels=[
            "Low Availability",
            "Moderate Availability",
            "High Availability",
            "Very High Availability"
        ]
    )

if "host_is_superhost" in df.columns:
    df["host_is_superhost"] = (
        df["host_is_superhost"]
        .astype(str)
        .str.lower()
        .str.strip()
    )

    df["superhost_status"] = np.where(
        df["host_is_superhost"] == "t",
        "Superhost",
        "Not Superhost"
    )

text_columns = df.select_dtypes(
    include=["object"]
).columns

for column in text_columns:
    df[column] = (
        df[column]
        .astype(str)
        .str.replace("\n", " ", regex=False)
        .str.replace("\r", " ", regex=False)
        .str.strip()
    )

df = df.drop_duplicates()

df = df.reset_index(drop=True)

df.to_csv(
    "listings_tableau_cleaned.csv",
    index=False,
    encoding="utf-8-sig"
)

print("Rows:", len(df))

print("Columns:", len(df.columns))

print("Duplicate Rows:", df.duplicated().sum())

print("Average Price:", round(df["price"].mean(), 2))

print("Minimum Price:", df["price"].min())

print("Maximum Price:", df["price"].max())

print("Cleaning completed successfully")

print("File saved as listings_tableau_cleaned.csv")