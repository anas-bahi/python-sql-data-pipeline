import pandas as pd

def clean_data():
    # Read CSV (UTF-8 first, fallback to Latin1)
    try:
        data = pd.read_csv("data.csv", encoding="utf-8")
    except UnicodeDecodeError:
        data = pd.read_csv("data.csv", encoding="latin1")
    
    # Check required columns
    if not all(col in data.columns for col in ["product", "price", "quantity"]):
        raise ValueError("CSV must have columns: product, price, quantity")
    
    # Calculate total sales
    data["total"] = data["price"] * data["quantity"]
    
    # Save clean CSV
    data.to_csv("clean_data.csv", index=False, encoding="utf-8")
    print("Clean CSV saved as clean_data.csv")

if __name__ == "__main__":
    clean_data()