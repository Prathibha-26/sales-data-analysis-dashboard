import pandas as pd

df = pd.read_csv("sales_data.csv")

print(df.head())

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())


#Top Selling Category
"""category_sales = df.groupby("Category")["Sales"].sum()

print(category_sales)"""

#Top Selling Product
"""product_sales = df.groupby("Product")["Sales"].sum()

print(product_sales.sort_values(ascending=False))
"""


#Monthly Sales Trend
"""df["Date"] = pd.to_datetime(df["Date"])

df["Month"] = df["Date"].dt.month

monthly_sales = df.groupby("Month")["Sales"].sum()

print(monthly_sales)"""


import matplotlib.pyplot as plt

# Category Sales Chart
"""category_sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(8,5))
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("category_sales.png")
plt.show()
"""
#Monthly Sales Trend
"""df["Date"] = pd.to_datetime(df["Date"])

df["Month"] = df["Date"].dt.month

monthly_sales = df.groupby("Month")["Sales"].sum()

plt.figure(figsize=(8,5))
monthly_sales.plot(marker="o")
plt.title("Monthly Sales Trend")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("monthly_sales.png")
plt.show()"""

#Top Products Chart

product_sales = df.groupby("Product")["Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(8,5))
product_sales.plot(kind="bar")
plt.title("Product Wise Sales")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("product_sales.png")
plt.show()