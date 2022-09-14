import boto3
import json


s3 = boto3.resource('s3')
bucket = s3.Bucket('ritikbucket102')
response = bucket.create(
    ACL='private',

    CreateBucketConfiguration={
        'LocationConstraint': 'us-east-2'
    }
)
# with open('/Users/consultadd/Desktop/codes/AWS/files/boto.json','rb') as f:
#     data=f.read()
# # data1=data.decode('utf-8')
# # data2=json.loads(data1)
# # print(data2)
# # # with open('/Users/consultadd/Desktop/codes/AWS/files/boto.json','r') as f:
# # #     data1=json.loads(str(f.read()))
# # # print(data1['thumbnail']['url'])
object = bucket.put_object(
    ACL='private',
    Body=data,
    
    Key='boto.json'
)