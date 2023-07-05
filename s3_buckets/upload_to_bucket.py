# Import boto3 library
import boto3

# Set up an S3 connection
s3 = boto3.client('s3')

# Specify the file name and path
file_name = "D:/Zain Sparta Global/tech241/cloud/aws/s3_buckets/test-file.txt"

# Upload the file to the bucket
upload_bucket = s3.upload_file(file_name, 'tech241-zain-python-bucket', 'test-file-from-script5.txt')

print(upload_bucket)