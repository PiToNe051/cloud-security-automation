import boto3
import sys
from botocore.exceptions import ClientError

def create_evidence_locker(bucket_name, region=None):
    """Creates a secure S3 bucket for forensic evidence."""
    try:
        if region is None or region == "us-east-1":
            s3_client = boto3.client('s3', region_name='us-east-1')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)
        
        print(f"✅ Bucket '{bucket_name}' created successfully.")
        
        # Apply Security Layers
        set_public_access_block(bucket_name, s3_client)
        enable_encryption(bucket_name, s3_client)
        enable_versioning(bucket_name, s3_client)
        
    except ClientError as e:
        print(f"❌ Error: {e}")
        return False
    return True

def set_public_access_block(bucket_name, s3_client):
    """Blocks all public access to the bucket."""
    try:
        s3_client.put_public_access_block(
            Bucket=bucket_name,
            PublicAccessBlockConfiguration={
                'BlockPublicAcls': True,
                'IgnorePublicAcls': True,
                'BlockPublicPolicy': True,
                'RestrictPublicBuckets': True
            }
        )
        print(f"🔒 Public access blocked for '{bucket_name}'.")
    except ClientError as e:
        print(f"❌ Error setting public access block: {e}")

def enable_encryption(bucket_name, s3_client):
    """Enforces Server-Side Encryption (AES-256) on the bucket."""
    try:
        s3_client.put_bucket_encryption(
            Bucket=bucket_name,
            ServerSideEncryptionConfiguration={
                'Rules': [{'ApplyServerSideEncryptionByDefault': {'SSEAlgorithm': 'AES256'}}]
            }
        )
        print(f"🔑 Encryption (AES-256) enabled for '{bucket_name}'.")
    except ClientError as e:
        print(f"❌ Error enabling encryption: {e}")

def enable_versioning(bucket_name, s3_client):
    """Enables versioning to preserve file history."""
    try:
        s3_client.put_bucket_versioning(
            Bucket=bucket_name,
            VersioningConfiguration={'Status': 'Enabled'}
        )
        print(f"📜 Versioning enabled for '{bucket_name}'.")
    except ClientError as e:
        print(f"❌ Error enabling versioning: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        bucket_name = sys.argv[1]
        region = sys.argv[2] if len(sys.argv) > 2 else "us-east-1"
        create_evidence_locker(bucket_name, region)
    else:
        print("Usage: python3 s3_locker_creator.py <bucket_name> [region]")
