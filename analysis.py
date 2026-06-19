import pandas as pd

df = pd.read_csv("sales_data.csv")

print(df.head())

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())

# Category Analysis
category_sales = df.groupby("Category")["Sales"].sum()

print("\nCategory Sales:")
print(category_sales)

# Product Analysis
product_sales = df.groupby("Product")["Sales"].sum()

print("\nProduct Sales:")
print(product_sales.sort_values(ascending=False))

# Monthly Analysis
df["Date"] = pd.to_datetime(df["Date"])

df["Month"] = df["Date"].dt.month

monthly_sales = df.groupby("Month")["Sales"].sum()

print("\nMonthly Sales:")
print(monthly_sales)