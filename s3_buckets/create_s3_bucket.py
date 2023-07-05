# first thing is to import boto3 library

import boto3

# set up an s3 connection
s3 = boto3.client('s3')

# create a bucket, in the eu-west-1 region
bucket_name = s3.create_bucket(Bucket="tech241-zain-python-bucket", CreateBucketConfiguration={"LocationConstraint":"eu-west-1"})
# print bucket name to confirm working script
print(bucket_name)