import schedule
import time
import os
import subprocess

def run_etl():
    print("⏳ Starting ETL job...")
    
    subprocess.call(["python", "scripts/transform_and_load.py"])

schedule.every(1).hours.do(run_etl)

print(" ETL orchestrator started. Job will run every hour.")
run_etl()  

while True:
    schedule.run_pending()
    time.sleep(60)
