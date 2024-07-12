import boto3

# Create an S3 client using boto3
client = boto3.client('s3')

# Download a file from an S3 bucket
# Parameters:
#   'mybucket' - the name of the S3 bucket from which to download the file
#   'remote_file.txt' - the key (filename) of the file to be downloaded from the bucket
#   'local_downloaded_file.txt' - the local path where the downloaded file will be saved
client.download_file('mybucket', 'remote_file.txt', 'local_downloaded_file.txt')

# Print a confirmation message once the file is downloaded
print("File downloaded from S3 bucket...")
