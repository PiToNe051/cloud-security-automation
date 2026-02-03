import os
import boto3

ec2 = boto3.client('ec2', region_name='us-east-1')

key_name = 'Sentinel-Project-Key'
file_name = f"{key_name}.pem"

try:
    print(f"[*] Creating Key Pair: {key_name}")
    
    # Create the key pair
    response = ec2.create_key_pair(KeyName=key_name)

    # Extract the private key material 
    private_key = response['KeyMaterial']

    # Save to a file
    with open(file_name, 'w') as f:
        f.write(private_key)

    # SECURITY: Linux permissions must be set to 400 (Read-only for owner)
    os.chmod(file_name, 0o400)

    print(f"[*] Success! Private key saved as {file_name}")
    print("[!] Remember: AWS does not store this file. If you lose it, it's gone.")

except ec2.exceptions.ClientError as e:
    if 'InvalidKeyPair.Duplicate' in str(e):
        print(f"[!] Error: Key Pair '{key_name}' already exists in AWS.")
    else:
        print(f"[?] Unexpected Error: {e}")
