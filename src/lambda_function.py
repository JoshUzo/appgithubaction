import json
import boto3
import pandas as pd

def lambda_handler(event, context):
    print("Extracting data from Salesforce...")

    # Mock Extract step
    data = [
        {"id": 1, "name": "Alice", "amount": 200, "date": "2025-02-28"},
        {"id": 2, "name": "Bob", "amount": 350, "date": "2025-02-27"}
    ]

    # Transform
    df = pd.DataFrame(data)
    df["date"] = pd.to_datetime(df["date"])
    df = df[df["amount"] > 200]

    # Load
    s3 = boto3.client("s3")
    bucket_name = "my-etl-bucket848"
    filename = "transformed_data.json"
    s3.put_object(Bucket=bucket_name, Key=filename, Body=df.to_json(orient="records"))

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Data processed successfully"})
    }
