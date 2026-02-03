import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2', region_name='us-east-1')

def create_empty_isolation_sg(vpc_id):
    group_name = 'ISOLATION-TEST-ZONE'

    try:
        # 1. Create The Group
        print(f"Creating {group_name}")
        sg = ec2.create_security_group(
            GroupName=group_name,
            Description='FORENSIC ISOLATION - NO TRAFFIC',
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
                'IpRanges': [{'CidrIp': '0.0.0.0/0'}] # All destinations
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
        
create_empty_isolation_sg('vpc-0aec7117b29d0fcd7')
