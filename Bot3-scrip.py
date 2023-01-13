# Author: Ibrehima Keita Devops Engineer US- Silver Spring
# Use boto3 to manage EBS Volune : Create snapshot and Volumes, create key pairs and an IAM user 
# Perequiste: intall pip, bot3 and configure AWS CLI in your local Environment 
from distutils import config

import boto3

client = boto3.client('ec2')
# Loop inside the available volume in your account.
list_collect_vol_ids = []
for Vol in client.describe_volumes()['Volumes']:
    print(Vol['VolumeId'])
# create snaphot 
response = client.create_snapshot(
    Description='This is my root volume snapshot.',
    VolumeId='vol-0a700b4e6ff53844a',
)

print(response")
response = client.create_volume(
    AvailabilityZone='us-east-1a',
    Size=90,
    VolumeType='gp2',
)

print(response)
response = client.create_key_pair(
    KeyName='bkeita-boto3',
)
# Create user
iam = boto3.client('iam')


response = iam.create_user(
    UserName='keit_ibrehima'
)

print(response)
