import boto3
import argparse

def parse_arguments():
    """Parses command-line arguments for EC2 configuration."""
    parser = argparse.ArgumentParser(description="Launches a Sentinel EC2 instance with flexibile configuration")

    parser.add_argument('--ami', type=str, default='ami-0b6c6ebed2801a5cb', help='The AMI ID for the instance')
    parser.add_argument('--type', type=str, default='t2.micro', help='The EC2 instance type (default: t2.micro)')
    parser.add_argument('--key', type=str, default='Sentinel-Project-Key', help='The name of the EC2 Key Pair (default: Sentinel-Project-Key)')
    parser.add_argument('--sg', type=str, default='sg-0e5ba34f03df0425b', help='The ID of the Security Group to attach')
    parser.add_argument('--region', type=str, default='us-east-1', help='The AWS regiorn to launch the instance in (default: us-east-1)')
    parser.add_argument('--name', type=str, default='Sentinel-Node-01', help='The Name tag for the EC2 instance (default: Sentinel-Node-01)')

    return parser.parse_args()



def launch_sentinel(ami_id, instance_type, key_name, sg_id, aws_region, name_tag):
    """Launches an EC2 instance with configuration passed as arguments, 
       waits for it to be running, and printrs its public IP and SSH command.

    """
    
    try:
        ec2 = boto3.resource('ec2', region_name=aws_region)

        print("[*] Launching Sentinel Instance")
        print(f"    > Region: {aws_region}")
        print(f"    > Key: {key_name}")

        instances = ec2.create_instances(
            ImageId=ami_id,
            MinCount=1,
            MaxCount=1,
            InstanceType=instance_type,
            SecurityGroupIds=[sg_id],
            TagSpecifications=[
                {
                    'ResourceType': 'instance',
                    'Tags': [
                        {'Key': 'Name', 'Value': name_tag},
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
        print(f"SSH Command: ssh -i {key_name}.pem ec2-user@{instance.public_ip_address}")

    except Exception as e:
        print(f"[!] Deployment Failed: {e}")

if __name__ == "__main__":
    args = parse_arguments()
    launch_sentinel(
        args.ami,
        args.type,
        args.key,
        args.sg,
        args.region,
        args.name
    )
