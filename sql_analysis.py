import pandas as pd
import sqlite3

df = pd.read_csv("sales_data.csv")

conn = sqlite3.connect("sales.db")

df.to_sql(
    "sales",
    conn,
    if_exists="replace",
    index=False
)

query = """
SELECT Product,
SUM(Sales) AS Revenue
FROM sales
GROUP BY Product
ORDER BY Revenue DESC;
"""

result = pd.read_sql_query(
    query,
    conn
)

print(result)

conn.close()