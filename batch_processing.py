
import boto3
import requests
import datetime
import time
import io

# AWS CONFIG
BUCKET_NAME="rawcrimedata"
S3_PREFIX="raw/crimes_data"
REGION="eu-north-1"

#API CONFIGURATION
BASE_URL = "https://data.cityofchicago.org/resource/ijzp-q8t2.csv"
ROWS_PER_REQUEST = 500000
MAX_RECORDS = 2000000
APP_TOKEN = ""

# AWS CLIENT
s3 = boto3.client('s3', region_name=REGION)

def fetch_data(offset):
    """fetching chunks of data from api this is were we do this"""
    params = {
        "$limit": ROWS_PER_REQUEST,
        "$offset": offset,
    }
    headers = {"x-App-Token": APP_TOKEN} if APP_TOKEN else {}
    print(f"fetching rows {offset} to {offset + ROWS_PER_REQUEST}")
    response = requests.get(BASE_URL, params=params, headers=headers)
    if response.status_code == 200:
        return response.content
    else:
        print(f"Error {response.status_code}")
        return None

def upload_to_s3(content,part):
    key = f"{S3_PREFIX}crimes_part_{part}.csv"
    s3.upload_fileobj(io.BytesIO(content), BUCKET_NAME, key)
    print(f"Uploaded to {key}")

def main():
    offset = 0
    part = 1
    while offset < MAX_RECORDS:
        data = fetch_data(offset)
        if not data:
            break
        upload_to_s3(data,part)
        part += 1
        offset += ROWS_PER_REQUEST
        time.sleep(2)

if __name__ == "__main__":
    main()

