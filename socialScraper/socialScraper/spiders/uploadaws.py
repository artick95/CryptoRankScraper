import boto3

#Creating Session With Boto3.
session = boto3.Session(
aws_access_key_id='AKIAT3UE4QVW7SOHMLKM',
aws_secret_access_key='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'
)

#Creating S3 Resource From the Session.
s3 = session.resource('s3')

object = s3.Object('cryptorankbucket', 'newsfeedcryptorank.csv')


result = object.put(Body=open('newsfeedcryptorank.csv', 'rb'))

res = result.get('ResponseMetadata')

if res.get('HTTPStatusCode') == 200:
    print('File Uploaded Successfully')
else:
    print('File Not Uploaded')




