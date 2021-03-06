# Using client itself to display all the buckets in s3:
import boto3
client = boto3.client('s3')
response = client.list_buckets()
for bucket in response['Buckets']:
    print(f'{bucket["Name"]}')
          
# Using resource to display all the buckets in s3:
import boto3
client = boto3.resource('s3')
for buckets in client.buckets.all():
    print(buckets.name)
          
# Using client to display the object names in a bucket in s3:
import boto3
client = boto3.client('s3')
response = client.list_objects_v2(Bucket = 'bucket-name')
for object in response['Contents']:
    print(f'{object["Key"]}')

# Using resource to display the object names in a bucket in s3:
import boto3
client = boto3.resource('s3')
bucket = client.Bucket('bucket-name')
for obj in bucket.objects.all():
    print(obj.key)

# Using client to display the contents inside a particular file in s3 (recommend to use resource if not sure of exact filename):
import boto3
client = boto3.client('s3')
target = client.get_object(Bucket = 'bucket-name',Key= 'object name')
contents = target['Body'].read().decode(encoding = "utf-8", errors = "ignore")
for line in contents.splitlines():
    print(line)

# Using resource to display the contents inside a particular file in s3 (so filter it according to the target object name):
import boto3
client = boto3.resource('s3')
bucket = client.Bucket('bucket-name')
for object in bucket.objects.filter(Prefix = 'starting of target object name'):
    contents = object.get()['Body'].read().decode(encoding = "utf-8", errors = "ignore")
for line in contents.splitlines():
    print(line)
          
# Download objects from s3 using client only:
import boto3 
objectlist = []
client = boto3.client('s3')
files = client.list_objects_v2(Bucket = 'bucket-name')
for objects in files['Contents']:
    res = objects['Key']
    objectlist.append(res)
for i in objectlist:
    client.download_file(Bucket = 'bucket-name',Key = i,Filename = i)
          
# Download objects from s3 using client and resource combo:
import boto3
s3 = boto3.resource('s3')
client = boto3.client('s3')
bucket = s3.Bucket('bucket-name')
files = bucket.objects.all()
for file in files:
    client.download_file('bucket-name',file.key,file.key)
          
# Upload objects to s3 from local directory using client:
import glob 
files = glob.glob('images/*')
import boto3
client = boto3.client('s3')
def upload_new_files(file_name,bucket,object_name= None,args= None):
    if object_name == None:
            object_name = file_name
    Args = {'ACL':'public-read'}
    client.upload_file(file_name,bucket,object_name, ExtraArgs= Args) 
for file in files:
    upload_new_files(file,'bucket-name')
    print('uploaded',file)
