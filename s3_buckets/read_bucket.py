# Import boto3 library
import boto3

# Set up an S3 connection
s3 = boto3.client('s3')

# List all objects in the bucket
response = s3.list_objects(Bucket='tech241-zain-python-bucket')
for file_name in response['Contents']:
    print(file_name["Key"])
    obj = s3.get_object(Bucket='tech241-zain-python-bucket', Key=file_name["Key"])

    # Read the content of the file
    file_content = obj['Body'].read().decode('utf-8')

    # Print the content of the file
    print(file_content)
