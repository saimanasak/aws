import boto3
import json

# Create an S3 client using boto3
client = boto3.client('s3')

# Define a bucket policy in JSON format
bucket_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::mybucket/*"
        }
    ]
}

# Convert the bucket policy dictionary to a JSON string
bucket_policy = json.dumps(bucket_policy)

# Set the bucket policy on the specified S3 bucket
# Parameters:
#   Bucket='mybucket' - the name of the S3 bucket to which the policy applies
#   Policy=bucket_policy - the JSON string containing the bucket policy
client.put_bucket_policy(
    Bucket='mybucket',
    Policy=bucket_policy
)

# Print a confirmation message once the bucket policy is set
print("Bucket policy is set...")
