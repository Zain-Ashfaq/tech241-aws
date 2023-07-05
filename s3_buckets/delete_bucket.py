# Import boto3 library
import boto3

# Set up an S3 connection
s3 = boto3.resource('s3')

# Specify the bucket name
bucket_name = 'tech241-zain-python-bucket'

# Create a bucket resource
bucket = s3.Bucket(bucket_name)

# Delete all objects in the bucket
bucket.objects.all().delete()

# Delete the bucket
bucket.delete()

print(f'Bucket {bucket_name} has been deleted')
