#  Health Check: EC2 Status Checks

## Overview
I created a monitoring script with Python that checks the status of EC2 instances every 5 minutes using Python and AWS Boto3. The infrastructure is managed through Terraform, ensuring consistent and reproducible deployments.

![diagram](https://github.com/Princeton45/ec2-health-check/blob/main/images/diagram.png)

## How It Works
1. Infrastructure is deployed via Terraform
   - EC2 instances are created and configured through IaC

2. Python script fetches instance statuses using AWS API
   - Boto3 connects to AWS
   - Retrieves EC2 instance status information
   - Collects system and instance status checks

3. Results are displayed in a formatted console output
   - Status information is processed
   - Formatted results show instance health

4. Monitoring continues at set intervals until stopped
   - Script runs in a loop with defined intervals
   - Continuous status updates
   - Keeps running until manually terminated

## Infrastructure Setup
I used Terraform to provision the following AWS resources:
- 3 EC2 instances
- VPC & Subnets
- Security Groups

![ec2](https://github.com/Princeton45/ec2-health-check/blob/main/images/ec2-instances.png)

![vpc](https://github.com/Princeton45/ec2-health-check/blob/main/images/vpc.png)


## Python Monitoring Script
Created a Python script that:
- Connects to AWS using Boto3
- Retrieves EC2 instance statuses
- Displays results in the console
- Runs continuous monitoring every 5 minutes

```python
# Import required libraries
import boto3
import schedule

# Initialize AWS EC2 client and resource with specified region
# Client is used for making API calls, Resource provides a higher-level object-oriented interface
ec2_client = boto3.client('ec2', region_name="us-east-1")
ec2_resource = boto3.resource('ec2', region_name="us-east-1")

def check_instance_status():
    # Get status of all EC2 instances
    statuses = ec2_client.describe_instance_status(
        IncludeAllInstances = True
    )
    
    # Display status information for each instance
    for status in statuses['InstanceStatuses']:
        instance_status = status['InstanceStatus']['Status']
        system_status = status['SystemStatus']['Status']
        state = status['InstanceState']['Name']
        print(f"Instance {status['InstanceId']} is {state} with instance status {instance_status} and system status is {system_status} ")
    
    print("########################\n")

# Run status check every 5 seconds
schedule.every(5).seconds.do(check_instance_status)

# Keep the script running
while True:
    schedule.run_pending()
```

![output](https://github.com/Princeton45/ec2-health-check/blob/main/images/output.png)
