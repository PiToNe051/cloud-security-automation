import boto3
from botocore.exceptions import ClientError
import argparse

def parse_arguments():
    """Parses command-line arguments for an Isolation Security Group creation."""
    parser = argparse.ArgumentParser(description='Creates an Isolation Security Group with flexible configuration.')

    parser.add_argument('--vpc', type=str, default='vpc-0aec7117b29d0fcd7', help='The VPC ID where the SG is created')
    parser.add_argument('--name', type=str, default='ISOLATION-TEST-ZONE', help='The name of the Security Group (default: ISOLATION-TEST-ZONE)')
    parser.add_argument('--region', type=str, default='us-east-1', help='The AWS region where the SG is created (default: us-east-1)')
    parser.add_argument('--description', type=str, default='FORENSIC ISOLATION - NO TRAFFIC', help='The description of the Security Group (default: FORENSIC ISOLATION - NO TRAFFIC)')
    parser.add_argument('--cidr', type=str, default='0.0.0.0/0', help='The Source IP range (default: 0.0.0.0/0)')



def create_empty_isolation_sg(vpc_id, sg_name, aws_region, sg_description, source_cidr):
    """Creates a empty isolation Security Group with no Inbound or Outbound traffic allowed."""
    ec2 = boto3.client('ec2', region_name=aws_region)
    group_name = sg_name
    try:
        # 1. Create The Group
        print(f"Creating {group_name}")
        sg = ec2.create_security_group(
            GroupName=group_name,
            Description=sg_description,
            VpcId=vpc_id
        )
        sg_id = sg['GroupId']

        # 2. Strip The Default Outbound Rule
        # AWS adds 'Allow ALL' to every new SG. We must rovoke it.
        print(f"[*] Purging default outbound rules from {sg_id}")
        ec2.revoke_security_group_egress(
            GroupId=sg_id,
            IpPermissions=[{
                'IpProtocol': '-1',
                'IpRanges': [{'CidrIp': source_cidr}] # All destinations
            }]
        )
    # NOTE: We do NOT need to revoke Inbound rules. 
        # New SGs are created with ZERO Inbound rules by default.
    
        print(f"[+] Success {sg_id} is now an empty Black Hole.")
        return sg_id
    
    except ClientError as e:
        if 'InvalidGroup.Duplicate' in str(e):
            print("[!] Group already exists. Use Audit script to verify it's empty.")
        else:
            raise e
        
if __name__ == "__main__":
    args = parse_arguments()
    create_empty_isolation_sg(
        args.vpc,
        args.name,
        args.region,
        args.description,
        args.cidr
    )
