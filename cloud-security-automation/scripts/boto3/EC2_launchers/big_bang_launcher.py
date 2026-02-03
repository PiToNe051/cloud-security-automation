import boto3

ec2 = boto3.resource('ec2', region_name='us-east-1')

# -- CONFIGURATION 
AMI_ID = 'ami-0b6c6ebed2801a5cb' # Find The AMI
INSTANCE_TYPE = 't2.micro' # Free Tier
KEY_NAME = 'Sentinel-Project-Key' 
SG_ID = 'sg-0e5ba34f03df0425b' # SG-created previously

def launch_sentinel():
    try:
        print(f"[*] Launching Sentinel Instance with Key: {KEY_NAME}...")

        instances = ec2.create_instances(
            ImageId=AMI_ID,
            MinCount=1,
            MaxCount=1,
            InstanceType=INSTANCE_TYPE,
            SecurityGroupIds=[SG_ID],
            TagSpecifications=[
                {
                    'ResourceType': 'instance',
                    'Tags': [
                        {'Key': 'Name', 'Value': 'Sentinel-Node-01'},
                        {'Key': 'Project', 'Value': 'CloudForensics'}
                    ]
                }
            ]
        )

        instance = instances[0]
        print(f"[*] Success! Instance created. ID {instance.id}")

        # Wait for it to exist so we can grab the public IP
        print("[*] Waiting for instance to initialize...")
        instance.wait_until_running()
        instance.reload() # Refresh the object data

        print("[!!!] DEPLOYMENT COMPLETE")
        print(f"IP Address: {instance.public_ip_address}")
        print(f"SSH Command: ssh -i {KEY_NAME}.pem ec2-user@{instance.public_ip_address}")

    except Exception as e:
        print(f"[!] Deployment Failed: {e}")

if __name__ == "__main__":
    launch_sentinel()
