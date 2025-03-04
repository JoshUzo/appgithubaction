import json
import boto3
import pandas as pd
from datetime import datetime

# Mock function to simulate extracting data from Salesforce
def extract_data():
    print("Extracting data from Salesforce...")
    return [
        {"id": 1, "name": "Alice", "amount": 200, "date": "2025-02-28"},
        {"id": 2, "name": "Bob", "amount": 350, "date": "2025-02-27"},
        {"id": 3, "name": "Charlie", "amount": 150, "date": "2025-02-26"}
    ]

# Transformation logic: Filter transactions above 200 and format dates
def transform_data(data):
    print("Transforming data...")
    df = pd.DataFrame(data)
    df["date"] = pd.to_datetime(df["date"])  # Convert string to datetime
    df = df[df["amount"] > 200]  # Filter transactions above 200
    return df

# Load data into an S3 bucket (or local JSON file for testing)
def load_data(df, save_local=True):
    print("Loading data...")
    filename = f"transformed_data_{datetime.now().strftime('%Y%m%d%H%M%S')}.json"
    
    # Convert dataframe to JSON
    json_data = df.to_json(orient="records")
    
    if save_local:
        with open(filename, "w") as f:
            f.write(json_data)
        print(f"Data saved locally: {filename}")
    else:
        # Upload to S3 (Replace with your bucket name)
        s3 = boto3.client("s3")
        bucket_name = "my-etl-bucket"
        s3.put_object(Bucket=bucket_name, Key=filename, Body=json_data)
        print(f"Data uploaded to S3: s3://{bucket_name}/{filename}")

# Run the ETL pipeline
if __name__ == "__main__":
    raw_data = extract_data()
    transformed_data = transform_data(raw_data)
    load_data(transformed_data, save_local=True)  # Set to False to upload to S3
