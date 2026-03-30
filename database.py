from sqlalchemy import create_engine
import pandas as pd

def save_to_db():
    # Read cleaned CSV
    data = pd.read_csv("clean_data.csv", encoding="utf-8")
    
    # Create SQLite DB
    engine = create_engine("sqlite:///sales.db")
    
    # Save data to table "sales"
    data.to_sql("sales", engine, index=False, if_exists="replace")
    print("Database created and data saved!")

if __name__ == "__main__":
    save_to_db()