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