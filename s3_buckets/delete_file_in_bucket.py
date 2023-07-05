# Import boto3 library
import boto3

# Set up an S3 connection
s3 = boto3.client('s3')

# Specify the bucket name and the file name
bucket_name = 'tech241-zain-python-bucket'
file_name = 'test-file-from-script.text'

# Delete the file from the bucket
s3.delete_object(Bucket=bucket_name, Key=file_name)

print(f'File {file_name} deleted successfully from bucket {bucket_name}.')
