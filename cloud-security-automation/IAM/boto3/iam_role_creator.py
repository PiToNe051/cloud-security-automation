import boto3
import json
import argparse
from botocore.exceptions import ClientError

def parse_arguments():
    parser = argparse.ArgumentParser(description='Creates a IAM Role with dynamic name')

    parser.add_argument('--name', type=str, default='Sentinel-Evidence-Writer-Role', help='The Name of the IAM role (default: Sentinel-Evidence-Writer-Role)')
    parser.add_argument('--bucket', type=str, default="forensic-evidence-2026-alpha", help='The name of the S3 Bucket you want to use (default: forensic-evidence-2026-alpha)')
    
    return parser.parse_args()

def create_iam_role(role_name):
    """Creates an IAM Role with an EC2 Trust Policy."""
    iam = boto3.client('iam')

    # 1. Define Trust Policy (Who can assume this role?)
    trust_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {"Service": "ec2.amazonaws.com"},
                "Action": "sts:AssumeRole"
            }
        ]
    }

    try:
        # 2. Create the Role
        iam.create_role(
            RoleName=role_name,
            AssumeRolePolicyDocument=json.dumps(trust_policy),
            Description="Allows EC2 instances to write forensic evidence to S3"
        )
        print(f"[+] Role '{role_name}' created successfully.")
        return True
    
    except ClientError as e:
        if e.response['Error']['Code'] == 'EntityAlreadyExists':
            print(f"[!] Role '{role_name}' already exists. Skipping creation.")
            return False
        else:
            print(f"[!] Error creating role {e}")

def attach_custom_policy(role_name, bucket_name):
    """Creates and attaches a Least Priviledge policy for S3 access."""
    iam = boto3.client('iam')
    policy_name = f"{role_name}-Policy"

    # 1. Define Permissions (What can it do?)
    my_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "s3:PutObject",
                    "s3:PutObjectAcl",
                    "s3:GetBucketLocation"
                ],
                "Resource": [
                    f"arn:aws:s3:::{bucket_name}",
                    f"arn:aws:s3:::{bucket_name}/*"
                ]
            }
        ]
    }

    try:
        # 2. Put the Policy inline (directly on the role)
        iam.put_role_policy(
            RoleName=role_name,
            PolicyName=policy_name,
            PolicyDocument=json.dumps(my_policy)
        )
        print(f"[+] Policy '{policy_name}' attached to the role, Allowed access to '{bucket_name}'.")
    
    except ClientError as e:
        print(f"[!] Error attaching policy: {e}")

def create_instance_profile(role_name):
    """Creates an Instance Profile and adds the role to it."""
    iam = boto3.client('iam')
    profile_name = role_name + "-Profile"

    try:
        # 1. Create Profile
        iam.create_instance_profile(InstanceProfileName=profile_name)
        print(f"[+] Instance Profile '{profile_name}' created.")
    except ClientError as e:
        if e.response['Error']['Code'] == 'EntityAlreadyExists':
            print(f"[!] Profile '{profile_name}' already exists.")
        else:
            print(f"[!] Error creating profile: {e}")
            return 
        
    # 2 Add Role to Profile
    try:
        iam.add_role_to_instance_profile(
            InstanceProfileName=profile_name,
            RoleName=role_name
        )
        print(f"[+] Role '{role_name}' added to Profile.")
    
    except ClientError as e:
        if e.response['Error']['Code'] == "LimitExceeded":
            print(f"[!] Role already added to profile.")
        else:
            print(f"[!] Error adding role to profile: {e}")

# Test Run
if __name__ == "__main__":
    args = parse_arguments()
    create_iam_role(args.name)
    attach_custom_policy(
        args.name,
        args.bucket
    )
    create_instance_profile(args.name)
