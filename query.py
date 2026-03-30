from sqlalchemy import create_engine
import pandas as pd

# Connect to database
engine = create_engine("sqlite:///sales.db")

# SQL query
query = """
SELECT product, SUM(total) AS total_sales
FROM sales
GROUP BY product
"""

# Run query
data = pd.read_sql(query, engine)

print("Total sales per product:")
print(data)