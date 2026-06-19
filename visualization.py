import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

# Category Sales Chart

category_sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(8,5))
category_sales.plot(kind="bar")

plt.title("Sales by Category")
plt.ylabel("Sales")

plt.tight_layout()

plt.savefig("category_sales.png")

plt.show()

# Product Sales Chart

product_sales = (
    df.groupby("Product")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

ax = product_sales.plot(
    kind="bar",
    figsize=(10,6)
)

for container in ax.containers:
    ax.bar_label(container)

plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("product_sales.png")

plt.show()

# Pie Chart

category_sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(7,7))

plt.pie(
    category_sales,
    labels=category_sales.index,
    autopct="%1.1f%%"
)

plt.title("Revenue Share by Category")

plt.savefig("revenue_share.png")

plt.show()

# Monthly Trend

df["Date"] = pd.to_datetime(df["Date"])

df["Month"] = df["Date"].dt.month

monthly_sales = df.groupby("Month")["Sales"].sum()

plt.figure(figsize=(8,5))

monthly_sales.plot(marker="o")

plt.title("Monthly Sales Trend")

plt.ylabel("Sales")

plt.tight_layout()

plt.savefig("monthly_sales.png")

plt.show()