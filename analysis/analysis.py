import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# create output folder
os.makedirs("output", exist_ok=True)

df = pd.read_csv("data/amazon.csv")

print("--------------- Amazon Product Analysis ----------------")

print(df.head())
print(df.info())
print(df.describe())
print("Shape:", df.shape)

print(df.isnull().sum())

print(df.columns)

# Remove duplicates
df = df.drop_duplicates()


# Rating
df["rating"] = pd.to_numeric(
    df["rating"],
    errors="coerce"
)

# Rating Count
df["rating_count"] = (
    df["rating_count"]
    .astype(str)
    .str.replace(",", "", regex=False)
)

df["rating_count"] = pd.to_numeric(
    df["rating_count"],
    errors="coerce"
)

# Fill missing values
df["rating"] = df["rating"].fillna(
    df["rating"].mean()
)

df["rating_count"] = df["rating_count"].fillna(0)

# Discounted Price
df["discounted_price"] = (
    df["discounted_price"]
    .str.replace("₹", "", regex=False)
    .str.replace(",", "", regex=False)
)

df["discounted_price"] = pd.to_numeric(
    df["discounted_price"],
    errors="coerce"
)

# Actual Price
df["actual_price"] = (
    df["actual_price"]
    .str.replace("₹", "", regex=False)
    .str.replace(",", "", regex=False)
)

df["actual_price"] = pd.to_numeric(
    df["actual_price"],
    errors="coerce"
)

# Discount Percentage
df["discount_percentage"] = (
    df["discount_percentage"]
    .str.replace("%", "", regex=False)
)

df["discount_percentage"] = pd.to_numeric(
    df["discount_percentage"],
    errors="coerce"
)

# Analysis

# Top Categories
top_categories = df["category"].value_counts().head(10)

print("\nTop Categories:")
print(top_categories)

# Average Rating
print("\nAverage Rating:")
print(df["rating"].mean())

# Highest Rated Products
top_rated = df.sort_values(
    by="rating",
    ascending=False
)

print("\nTop 10 Highest Rated Products:")
print(
    top_rated[
        ["product_name", "rating"]
    ].head(10)
)

# Most Reviewed Products
top_reviewed = df.sort_values(
    by="rating_count",
    ascending=False
)

print("\nTop 10 Most Reviewed Products:")
print(
    top_reviewed[
        ["product_name", "rating_count"]
    ].head(10)
)

# Most Expensive Products
expensive = df.sort_values(
    by="actual_price",
    ascending=False
)

print("\nTop 10 Most Expensive Products:")
print(
    expensive[
        ["product_name", "actual_price"]
    ].head(10)
)

# Biggest Discounts
discounted = df.sort_values(
    by="discount_percentage",
    ascending=False
)

print("\nTop 10 Biggest Discounts:")
print(
    discounted[
        ["product_name", "discount_percentage"]
    ].head(10)
)

# Category-wise Ratings
category_rating = (
    df.groupby("category")["rating"]
    .mean()
    .sort_values(ascending=False)
)

print("\nTop Categories by Rating:")
print(category_rating.head(10))

# VISUALIZATIONS

# Top Categories
top_categories.plot(kind="bar")
plt.title("Top 10 Product Categories")
plt.xlabel("Category")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("output/top_categories.png")
plt.close()

# Ratings Distribution
df["rating"].hist()
plt.title("Ratings Distribution")
plt.xlabel("Rating")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("output/ratings_distribution.png")
plt.close()

# Top Rated Products
top_rated_chart = top_rated.head(10)

top_rated_chart.plot(
    x="product_name",
    y="rating",
    kind="bar"
)

plt.title("Top Rated Products")
plt.xlabel("Product")
plt.ylabel("Rating")
plt.tight_layout()
plt.savefig("output/top_rated_products.png")
plt.close()

# Top Discounted Products
top_discount_chart = discounted.head(10)

top_discount_chart.plot(
    x="product_name",
    y="discount_percentage",
    kind="bar"
)

plt.title("Top Discounted Products")
plt.xlabel("Product")
plt.ylabel("Discount %")
plt.tight_layout()
plt.savefig("output/top_discounted_products.png")
plt.close()

# INSIGHTS

with open("output/insights.txt", "w") as f:
    f.write("Amazon Product Analysis\n")
    f.write("=======================\n\n")
    f.write(f"Total Products: {len(df)}\n")
    f.write(f"Average Rating: {df['rating'].mean():.2f}\n")
    f.write(
        f"Most Common Category: {top_categories.index[0]}\n"
    )

print("\nAnalysis Completed Successfully!")
print("Results saved in output folder.")