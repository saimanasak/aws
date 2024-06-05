# Import boto3 that is the AWS SDK for Python, which allows to interact with AWS services
import boto3

# Define the lambda_handler function
def lambda_handler(event, context):
    
    # Initialize EC2 and SNS clients using boto3
    ec2 = boto3.client('ec2')
    sns = boto3.client('sns')

    # Describe all instances
    response = ec2.describe_instances()

    # Create an empty list to store stopped or terminated instances
    stopped_or_terminated_instances = []

    # Iterate over all reservations and instances
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            instance_state = instance['State']['Name']

            # Check if the instance is stopped or terminated and add it to the list
            if instance_state == 'stopped' or instance_state == 'terminated':
                stopped_or_terminated_instances.append((instance_id, instance_state))

    # Send notification for each stopped or terminated instance
    for instance_id, state in stopped_or_terminated_instances:
        message = f'Instance {instance_id} is {state}'
        sns.publish(
            TopicArn='arn:aws:sns:<AWS-Region>:<AWS-Account-ID>:<SNS-Topic-Name>',  
            Message=message,
            Subject='EC2 Instance Status Alert'
        )

    # Return a response indicating the success of the Lambda function execution
    # statusCode: 200 indicates a successful execution
    # body: Provide a message detailing the number of reservations checked and the number of alerts sent

    return {
        'statusCode': 200,
        'body': f'Checked {len(response["Reservations"])} reservations. Alerts sent for {len(stopped_or_terminated_instances)} instances.'
    }