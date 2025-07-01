import pandas as pd
import hashlib
from sqlalchemy import create_engine

def anonymize_customer_id(customer_id):
    """
    Convert a CustomerID to a SHA-256 hashed string to anonymize it.
    """
    return hashlib.sha256(str(customer_id).encode()).hexdigest()

def main():
    # Step 1: Load the raw dataset
    try:
        df = pd.read_csv("data/telecom_churn.csv")
        print("CSV file loaded.")
    except FileNotFoundError:
        print(" telecom_churn.csv not found in /data folder.")
        return

    # Step 2: Anonymize CustomerID
    df['CustomerID'] = df['CustomerID'].apply(anonymize_customer_id)
    print("🔐 CustomerID anonymized.")

    # Step 3: Handle missing values
    df['TechSupport'].fillna('No', inplace=True)
    df['TotalCharges'].fillna(0, inplace=True)
    print(" Missing values handled.")

    # Step 4: Save to SQLite
    engine = create_engine("sqlite:///processed_telecom_churn.db")
    df.to_sql("processed_churn", engine, if_exists="replace", index=False)
    print("💾 Data saved to SQLite database: processed_telecom_churn.db")

    # Step 5: Export to Excel
    df.to_excel("processed_churn_report.xlsx", index=False)
    print(" Excel report saved as: processed_churn_report.xlsx")

    print(" ETL process completed successfully.")

if __name__ == "__main__":
    main()
