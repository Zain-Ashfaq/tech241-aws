# Import boto3
import boto3

# set the s3 connection
s3 = boto3.client("s3")

# download the file
download_file = s3.download_file("tech241-zain-python-bucket", "test-file-from-script5.txt", "hasitworked.txt")

print(s3.download_file)