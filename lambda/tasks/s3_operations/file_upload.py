import boto3

# Create an S3 client using boto3
client = boto3.client('s3')

# Upload a file to the specified S3 bucket
# Parameters:
#   'local_file.txt' - the local file to be uploaded
#   'mybucket' - the target S3 bucket name
#   'remote_file.txt' - the name to be given to the file in the S3 bucket
client.upload_file('local_file.txt', 'mybucket', 'remote_file.txt')

# Print a confirmation message once the file is uploaded
print("File uploaded to S3 bucket...")
