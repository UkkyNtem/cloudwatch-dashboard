# AWS CloudWatch Monitoring Dashboard

This is a simple project that helped me understand how to use AWS CloudWatch to monitor services like EC2, S3, and RDS. I used Python and the AWS CLI to create a dashboard that shows CPU usage, storage size, and database connections.

## What This Project Does

The Python script sends a dashboard configuration file to AWS using the AWS CLI. Once it runs, a CloudWatch dashboard is created that shows:

- EC2 instance CPU usage
- S3 bucket size
- RDS database connections

## Tools I Used

- Python 3
- AWS CLI
- AWS CloudWatch
- EC2, S3, and RDS (all AWS services)

## How I Set It Up

1. I created the following AWS resources:
   - An EC2 instance (Amazon Linux, free tier)
   - An S3 bucket (I uploaded one small file)
   - An RDS instance (MySQL, free tier)

2. I created a file called cloudwatch_dashboard.json to define the dashboard layout and metrics.

3. I wrote a simple Python script (create_dashboard.py) that uses subprocess to run the AWS CLI and create the dashboard.

4. I ran the script like this:
   
bash
   python3 create_dashboard.py


5. I checked the dashboard on the AWS Console under CloudWatch > Dashboards.

## Project Files

- create_dashboard.py: Python script to create the dashboard
- cloudwatch_dashboard.json: JSON file with dashboard layout
- README.md: Notes about the project (this file)

## What I Learned

- How to use Python to call AWS CLI commands
- How to structure a CloudWatch dashboard JSON file
- How CloudWatch helps you monitor services in AWS


