import boto3

# Create an S3 client using boto3
client = boto3.client('s3')

# Delete an object (file) from the specified S3 bucket
# Parameters:
#   Bucket='mybucket' - the name of the S3 bucket from which to delete the file
#   Key='remote_file.txt' - the key (filename) of the file to be deleted
client.delete_object(Bucket='mybucket', Key='remote_file.txt')

# Print a confirmation message once the file is deleted
print("File deleted from S3 bucket...")
