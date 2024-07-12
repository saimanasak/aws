import boto3

# Create an S3 client using boto3
client = boto3.client('s3')

# List all S3 buckets associated with the AWS account
response = client.list_buckets()

# Iterate over each bucket in the response and print its name
for bucket in response['Buckets']:
    print(bucket['Name'])

# Print a confirmation message once all buckets are listed
print("Listed all buckets...")
