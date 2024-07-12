import boto3

# Create an S3 client using boto3
client = boto3.client('s3')

# Enable versioning on a specific S3 bucket
# Parameters:
#   Bucket='mybucket' - the name of the S3 bucket on which to enable versioning
#   VersioningConfiguration={'Status': 'Enabled'} - configuration dictionary specifying 'Enabled' status
client.put_bucket_versioning(
    Bucket='mybucket',
    VersioningConfiguration={
        'Status': 'Enabled'
    }
)

# Print a confirmation message once versioning is enabled
print("Bucket versioning enabled...")
