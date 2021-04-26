# Using client itself to display all the buckets in s3
import boto3
client = boto3.client('s3')
response = client.list_buckets()
for bucket in response['Buckets']:
    print(f'{bucket["Name"]}')
          
# Using resource to display all the buckets in s3
import boto3
client = boto3.resource('s3')
for buckets in client.buckets.all():
    print(buckets.name)
          
# Using client to display the object names in a bucket in s3
import boto3
client = boto3.client('s3')
response = client.list_objects_v2(Bucket = 'bucket-name')
for object in response['Contents']:
    print(f'{object["Key"]}')

# Using resource to display the object names in a bucket in s3
import boto3
client = boto3.resource('s3')
bucket = client.Bucket('bucket-name')
for objects in bucket.objects.all():
    print(objects.key)

# Using client to display the contents inside a particular file in s3 (recommend to use resource if not sure of exact filename)
import boto3
client = boto3.client('s3')
target = client.get_object(Bucket = 'bucket-name',Key= 'object name')
contents = target['Body'].read().decode(encoding = "utf-8", errors = "ignore")
for line in contents.splitlines():
    print(line)

# Using resource to display the contents inside a particular file in s3 (so filter it according to the target object name) 
import boto3
client = boto3.resource('s3')
bucket = client.Bucket('bucket-name')
for object in bucket.objects.filter(Prefix = 'starting of target object name'):
    contents = object.get()['Body'].read().decode(encoding = "utf-8", errors = "ignore")
for line in contents.splitlines():
    print(line)
