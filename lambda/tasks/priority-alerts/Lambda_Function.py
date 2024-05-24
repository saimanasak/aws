# Import json module that is used for parsing and manipulating JSON data 
import json

# Import boto3 that is the AWS SDK for Python, which allows to interact with AWS services
import boto3

# Create an SNS client
sns = boto3.client('sns')

# ARN of the SNS topic to which notifications will be sent
TOPIC_ARN = 'arn:aws:sns:<aws-region-name>:<aws-account-ID>:<SNS-topic-name>'

# 'Event' contains the data passed to the function, and 'Context' contains runtime information
def lambda_handler(event, context):
    try:
        # Parse the JIRA webhook event body from the incoming request
        message = json.loads(event['body'])
        
        # Check if the ticket priority is 'Highest' 
        if message['issue']['fields']['priority']['name'] == 'Highest':
            
            # Construct the message to be sent to the SNS topic
            sns_message = (
                f"Highest Priority Ticket Created: {message['issue']['key']}\n"
                f"Summary: {message['issue']['fields']['summary']}\n"
                f"Description: {message['issue']['fields']['description']}"
            )

            # Publish the message to SNS topic
            sns.publish(
                Message=sns_message,
                Subject='High Priority Ticket Alert',
                TopicArn=TOPIC_ARN
            )
            
            # Return a successful response
            return {
                'statusCode': 200,
                'body': json.dumps({'message': 'Notification Sent Successfully...!!!'})
            }
            
        else:
            
            # Return a response indicating that the ticket is not a priority ticket
            return {
                'statusCode': 200,
                'body': json.dumps({'message': 'Not a priority ticket'})
            }
    
     # Log the exception and return an error response
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Failed to process the request', 'details': str(e)})
        }
