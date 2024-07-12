import boto3

# Create an S3 client using boto3
client = boto3.client('s3')

# Delete an S3 bucket (the bucket must be empty before deletion)
# Parameters:
#   Bucket='mybucket' - the name of the S3 bucket to delete
client.delete_bucket(Bucket='mybucket')

# Print a confirmation message once the bucket is deleted
print("S3 bucket is deleted...")
