# EC2 Health Check Monitor

## Overview
I created a monitoring system that checks the status of EC2 instances using Python and AWS Boto3. The infrastructure is managed through Terraform, ensuring consistent and reproducible deployments.

![diagram](https://github.com/Princeton45ec2-health-check/blob/main/images/diagram.png)

## Prerequisites
- AWS Account  
- Python 3.x
- Terraform
- AWS CLI configured
- Required Python packages (listed in requirements.txt)

## Infrastructure Setup
I used Terraform to provision the following AWS resources:
- Multiple EC2 instances with different configurations
- Required IAM roles and policies  
- Security Groups

![AWS Console](images/instances.png)

## Python Monitoring Script
Created a Python script that:
- Connects to AWS using Boto3
- Retrieves EC2 instance statuses
- Displays results in the console
- Runs continuous monitoring at specified intervals

![Script Output](images/monitoring.png)

## How It Works
1. Infrastructure is deployed via Terraform
2. Python script fetches instance statuses using AWS API
3. Results are displayed in a formatted console output
4. Monitoring continues at set intervals until stopped

## Results
Successfully implemented automated health checking for:
- System Status Checks
- Instance Status Checks
- Overall Instance State

![Monitoring Results](images/results.png)

## Future Improvements
- Add email notifications
- Implement dashboard visualization
- Include CloudWatch metrics
- Add automated recovery actions
