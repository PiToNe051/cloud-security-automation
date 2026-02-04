import boto3
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Creates A Security Group with flexible configuration.')
    
    parser.add_argument('--vpc', type=str, default= 'vpc-0aec7117b29d0fcd7', help='VPC ID where the Security Group is created.')
    parser.add_argument('--name', type=str, default='WebAccess-SG', help='The name of the Security Group (default: WebAccess-SG)')
    parser.add_argument('--region', type=str, default='us-east-1', help='The AWS region the Security Group is created (default: us-east-1)')
    parser.add_argument('--port', type=int, default=2222 , help='The Port Number for the SSH service (default: 2222)')
    parser.add_argument('--cidr', type=str, default='0.0.0.0/0', help='The Source IP range (default: 0.0.0.0/0)')

    return parser.parse_args()



def create_sg(vpc_id, sg_name, aws_region, ssh_port, source_cidr):

    ec2 = boto3.resource('ec2', region_name=aws_region)

    try:
        security_group = ec2.create_security_group(
            GroupName=sg_name,
            Description='Allow HTTP and Custom SSH',
            VpcId=vpc_id
        )

        security_group.authorize_ingress(
            IpPermissions=[
                {
                    'IpProtocol': 'tcp',
                    'FromPort': 80,
                    'ToPort': 80,
                    'IpRanges': [{'CidrIp': source_cidr}]
                },
                {
                    'IpProtocol': 'tcp',
                    'FromPort': ssh_port,
                    'ToPort': ssh_port,
                    'IpRanges': [{'CidrIp': source_cidr}]
            
                }

            ]
        )   

        print(f"Successfully created SG: {security_group.id}")
    
    except Exception as e:
        print(f"[!] ERROR: Failed to create Security Group : {e}")

if __name__ == "__main__":
    args = parse_arguments()
    create_sg(
        args.vpc,
        args.name,
        args.region,
        args.port,
        args.cidr
    )
