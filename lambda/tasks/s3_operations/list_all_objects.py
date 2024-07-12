import boto3

# Create an S3 client using boto3
client = boto3.client('s3')

# List objects in a specific S3 bucket
# Parameters:
#   Bucket='mybucket' - the name of the S3 bucket from which to list objects
response = client.list_objects_v2(Bucket='mybucket')

# Iterate over each object (file) in the bucket and print its key (filename)
for obj in response.get('Contents', []):
    print(obj['Key'])

# Print a confirmation message once all objects are listed
print("Listed all objects in the bucket...")
