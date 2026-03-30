import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

engine = create_engine("sqlite:///sales.db")

query = """
SELECT product,
SUM(total) as total_sales
FROM sales
GROUP BY product
"""

data = pd.read_sql(query, engine)

plt.bar(data["product"], data["total_sales"])

plt.title("Sales per product")

plt.show()