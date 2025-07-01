# 📊 Telecom Customer Churn – Python ELT Pipeline

This project implements a complete ELT (Extract, Load, Transform) pipeline using **pure Python** for processing and analyzing telecom customer churn data. It includes data ingestion, cleaning, anonymization, storage, scheduling, and reporting via Excel and a Streamlit dashboard.

---

## 📂 Folder Structure

telecom-churn-python-pipeline/
├── data/
│ └── telecom_churn.csv # Raw dataset
├── scripts/
│ ├── transform_and_load.py # Main ETL logic
│ ├── orchestrator.py # Runs ETL every hour using schedule
│ └── reporting_app.py # Streamlit dashboard app
├── processed_telecom_churn.db # Output SQLite DB
├── processed_churn_report.xlsx # Excel report
├── requirements.txt # Python package dependencies
└── README.md


---

## ✅ Features

-  Loads customer data from CSV
-  Anonymizes sensitive PII (CustomerID)
-  Cleans missing values in key fields
-  Loads processed data to SQLite DB
-  Exports cleaned data to Excel
-  Generates an interactive dashboard with Streamlit
-  Schedules the ETL to run hourly using `schedule`

---

## 🛠️ Tech Stack

- Python (pandas, sqlalchemy, openpyxl)
- SQLite (lightweight local database)
- Streamlit (for dashboard)
- schedule (for hourly orchestration)
- Excel (for offline report)

---

## 🚀 How to Run This Project

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/telecom-churn-python-pipeline.git
cd telecom-churn-python-pipeline

### 2. Install Python Dependencies
pip install -r requirements.txt

### 3. Run ETL Pipeline

python scripts/transform_and_load.py
 Output:

processed_telecom_churn.db – cleaned data in SQLite

processed_churn_report.xlsx – Excel file for offline analysis

4. View the Dashboard 
streamlit run scripts/reporting_app.py
Open http://localhost:8501 in your browser.

5. Run ETL Every Hour (Simulated Orchestration)
  
python scripts/orchestrator.py
This runs transform_and_load.py once immediately and then every hour using the schedule library.

