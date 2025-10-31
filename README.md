🏙️ Chicago Crime Data Pipeline (AWS End-to-End)
📘 Overview

This project demonstrates a complete serverless data engineering pipeline built on AWS.
It automates data ingestion, transformation, and analysis of Chicago crime data using Python, AWS S3, Glue, and Athena.
The pipeline is scalable, cost-effective, and ideal for large public datasets.

⚙️ Architecture

Workflow:

Data Ingestion (Python Script)

Fetches crime data from the City of Chicago Open Data API.

Ingests data in chunks and uploads to Amazon S3 in the raw/ folder.

Data Transformation (AWS Glue Notebook)

Reads raw data from S3.

Cleans and transforms columns (e.g., date parsing, null handling, type casting).

Writes the processed data back to S3 under processed/.

Data Analysis (AWS Athena)

Athena queries the processed data directly from S3.

Enables fast, serverless SQL analytics for insights.

🧰 Tools & Technologies

Python (for ingestion)

AWS S3 (data storage)

AWS Glue (ETL transformation)

AWS Athena (query & analysis)

Boto3 (AWS SDK for Python)

Pandas, Requests (data handling)

🚀 Steps to Reproduce

Create an S3 bucket with raw/ and processed/ folders.

Run the Python ingestion script to load raw data into S3.

Use AWS Glue to transform and clean the data.

Create a table in Athena to query processed data.

Visualize and analyze insights.

📊 Sample Insights

Crime trend analysis by year and district.

Distribution of arrest and non-arrest cases.

Location-based crime heat mapping.

🧑‍💻 Author

Harsh — CSE Student | Aspiring Data Engineer
