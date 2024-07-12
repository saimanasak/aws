# Import json module that is used for parsing and manipulating JSON data 
import boto3

# Create an S3 client
client = boto3.client('s3')

# Create a new S3 bucket with specified configurations
response = client.create_bucket(
    ACL='private',  # Set the Access Control List to 'private' (only the owner has full control)
    Bucket='mybucket',  # The name of the bucket to create (must be globally unique)
    CreateBucketConfiguration={
        'LocationConstraint': 'us-west-1'  # AWS region where the bucket will be created
    }
)

# Print a confirmation message
print("S3 bucket is created...")
