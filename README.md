# Telecom Customer Churn – Python ETL Pipeline

##  About the Dataset

This dataset contains telecom customer data such as age, tenure, internet type, monthly charges, and whether they churned. The goal is to build a lightweight ELT (Extract, Load, Transform) pipeline using Python.

---

## ✅ Features Implemented

- Ingested raw customer data from a CSV file
- Anonymized `CustomerID` using SHA-256
- Cleaned missing values in key columns
- Loaded transformed data into a local SQLite database

---

## ️ Tech Stack

- Python (pandas, sqlalchemy)
- SQLite (for reporting/storage)

---

## 📂 Folder Structure

telecom-churn-python-pipeline/
├── data/ # Raw CSV file
├── scripts/ # Transformation logic
├── processed_telecom_churn.db # Output SQLite DB
├── requirements.txt
└── README.md 

##  Orchestration

- The ETL pipeline is orchestrated using the `schedule` library in Python.
- The script `orchestrator.py` runs `transform_and_load.py` every hour.
- This simulates a real-world workflow schedule without needing external tools like Airflow or Task Scheduler.

```bash
python scripts/orchestrator.py


