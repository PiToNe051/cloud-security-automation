import boto3

ec2 = boto3.resource('ec2')
VPC_ID = 'vpc-0aec7117b29d0fcd7'

security_group = ec2.create_security_group(
    GroupName='WebAccess-SG',
    Description='Allow HTTP and Custom SSH',
    VpcId=VPC_ID
)

security_group.authorize_ingress(
    IpPermissions=[
        {
            'IpProtocol': 'tcp',
            'FromPort': 80,
            'ToPort': 80,
            'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
        },
        {
            'IpProtocol': 'tcp',
            'FromPort': 2222,
            'ToPort': 2222,
            'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
            
        }

    ]
)

print(f"Successfully created SG: {security_group.id}")
