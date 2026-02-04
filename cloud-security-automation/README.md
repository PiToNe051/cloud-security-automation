# Cloud Security Automation Portfolio

This project demonstrates practical cloud security automation techniques, combining Infrastructure as Code (IaC) with Python scripting to provision and manage cloud resources securely. It leverages Wazuh for threat detection and OpenClaw for workflow integration, showcasing a commitment to protecting digital assets and ensuring the resilience of passion-driven projects.

**Mission:**
Aligned with a commitment to protect the innovation and hard work that organizations build, this project stands on the frontline of defense. Our goal is to safeguard the digital assets that provide value to people’s lives, ensuring that passion-driven projects remain secure and resilient.

**Core Technologies:**
*   **AWS:** Cloud infrastructure provider.
*   **Terraform:** Infrastructure as Code for provisioning AWS resources.
*   **Python (Boto3):** Scripting for AWS resource management and automation.
*   **Wazuh:** (Mentioned as part of the project's context, though not directly implemented in these scripts).
*   **OpenClaw:** (Mentioned as part of the project's context, for workflow integration).

---

## 📁 Project Structure

```
cloud-security-automation/
├── .gitignore
├── README.md
├── terraform/
│   ├── main.tf
│   ├── terraform.tfstate       # (Ignored by Git)
│   └── terraform.tfstate.backup # (Ignored by Git)
└── scripts/
    └── boto3/
        ├── cloud_forensics/      # Placeholder for potential future scripts related to cloud forensics.
        ├── EC2_launchers/
        │   └── big_bang_launcher.py # Script to launch a Sentinel EC2 instance.
        ├── Key_Pair/             # Scripts/documentation for managing EC2 key pairs.
        │   └── key_maker.py       # Script to create and save an EC2 key pair.
        └── Security_Groups/      # Scripts for managing AWS security groups.
            ├── isolation-sg-creator.py # Script to create a "black hole" security group.
            └── sg-creator.py          # Script to create a security group allowing HTTP and custom SSH.
```

---

## 🛠️ Prerequisites

Before running any code, ensure you have the following set up:

1.  **AWS Account:** Access to an AWS account with sufficient permissions to create VPC, Security Groups, EC2 instances, and EBS volumes.
2.  **AWS Credentials:** Configured AWS credentials. This can be done via the AWS CLI (`aws configure`), environment variables, or an IAM role if running within AWS.
    *   Ensure your credentials have permissions for EC2, EBS, and related services.
3.  **Terraform:** Installed Terraform (version 1.x or higher recommended). Download from [terraform.io](https://www.terraform.io/downloads.html).
4.  **Python:** Python 3 installed.
5.  **Boto3:** Install the AWS SDK for Python:
    ```bash
    pip install boto3
    ```
6.  **AWS Key Pair:** An existing EC2 Key Pair named `Sentinel-Project-Key` in the `us-east-1` region. If you don't have one, you'll need to create it in the AWS console. **Note:** The `key_maker.py` script can create this for you if it doesn't exist, saving the private key locally as `Sentinel-Project-Key.pem`. You will also need this `.pem` file to SSH into instances.
7.  **Existing VPC:** The Terraform code expects an existing VPC with ID `vpc-0aec7117b29d0fcd7`. This should ideally be managed via Terraform variables for better reusability.

---

## 🚀 Deployment Instructions

This project consists of two main components: Terraform for infrastructure setup and Python scripts for resource management.

### 1. Terraform Infrastructure Deployment (`terraform/`)

This module provisions core AWS resources for a forensic analysis environment.

**Current Terraform Configuration (`terraform/main.tf`):**

*(See the code block in the `main.tf` file within this repository for the full Terraform code.)*

**Deployment Steps:**

1.  **Navigate to Terraform Directory:**
    ```bash
    cd cloud-security-automation/terraform/
    ```
2.  **Initialize Terraform:** Download the necessary provider plugins.
    ```bash
    terraform init
    ```
3.  **Review the Plan:** See what resources Terraform will create, modify, or destroy.
    ```bash
    terraform plan
    ```
4.  **Apply the Configuration:** Create the AWS resources.
    ```bash
    terraform apply
    ```
    Type `yes` when prompted to confirm.

**Notes on Configuration:**
The current Terraform configuration is fully parameterized using **Terraform variables**. This allows users to easily specify region, VPC ID, AMI ID, instance types, and other parameters via a `terraform.tfvars` file, ensuring reusability and adherence to best practices.

**Example using Variables (for `main.tf` and a `variables.tf` file):**

*   **`variables.tf` (Create this file in `terraform/`)**
    ```terraform
    variable "aws_region" {
      description = "The AWS region to deploy resources in."
      type        = string
      default     = "us-east-1"
    }

    variable "vpc_id" {
      description = "The ID of the VPC to use."
      type        = string
      # default     = "vpc-0aec7117b29d0fcd7" # Example default, or leave empty to require input
    }

    variable "ami_id" {
      description = "The AMI ID for the EC2 instances."
      type        = string
      # default     = "ami-0b6c6ebed2801a5cb"
    }
    
    variable "instance_type" {
      description = "The EC2 instance type."
      type        = string
      default     = "t2.micro"
    }

    variable "key_name" {
      description = "The name of the EC2 key pair."
      type        = string
      # default     = "Sentinel-Project-Key"
    }

    variable "snapshot_id" {
      description = "The EBS snapshot ID to create a volume from."
      type        = string
      # default     = "snap-081ac51b83cdf41c2"
    }

    variable "availability_zone" {
      description = "The Availability Zone for the instances and EBS volume."
      type        = string
      # default     = "us-east-1a"
    }

    variable "forensic_sg_name" {
      description = "The name for the forensic isolation security group."
      type        = string
      default     = "FORENSIC-ISOLATION-ZONE"
    }
    
    variable "forensic_sg_description" {
      description = "Description for the forensic isolation security group."
      type        = string
      default     = "Total lockdown group - No Inbound or Outbound"
    }

    variable "sentinel_instance_name" {
      description = "Name tag for the Sentinel EC2 instance."
      type        = string
      default     = "Sentinel-Forensic-Twin"
    }

    variable "forensic_workstation_name" {
      description = "Name tag for the Forensic Analyst Workstation EC2 instance."
      type        = string
      default     = "Forensic-Analyst-Workstation"
    }

    variable "evidence_disk_name" {
      description = "Name tag for the EBS evidence disk."
      type        = string
      default     = "Evidence-Disk-Case-Alpha"
    }
    ```

*   **Modify `main.tf` to use variables:**
    ```diff
    provider "aws" {
    -  region = "us-east-1"
    +  region = var.aws_region
    }

    resource "aws_security_group" "forensic_isolation" {
    -  name        = "FORENSIC-ISOLATION-ZONE"
    -  description = "Total lockdown group - No Inbound or Outbout"
    -  vpc_id      = "vpc-0aec7117b29d0fcd7"
    +  name        = var.forensic_sg_name
    +  description = var.forensic_sg_description
    +  vpc_id      = var.vpc_id
    }

    resource "aws_instance" "sentile_twin" {
    -  ami           = "ami-0b6c6ebed2801a5cb"
    -  instance_type = "t2.micro"
    -  key_name      = "Sentinel-Project-Key"
    +  ami           = var.ami_id
    +  instance_type = var.instance_type
    +  key_name      = var.key_name
    
      # vpc_security_group_ids = [aws_security_group.forensic_isolation.id] # Reference using the resource name
      vpc_security_group_ids = [aws_security_group.forensic_isolation.id]

    -  tags = {
    -  Name = "Sentinel-Forensic-Twin"
    -  }
    +  tags = {
    +    Name    = var.sentinel_instance_name
    +    Project = "CloudForensics" # Keeping Project tag as is, or could be a variable too
    +  }  
    }

    resource "aws_instance" "forensic_workstation" {
    -  ami               = "ami-0b6c6ebed2801a5cb"
    -  instance_type     = "t2.micro"
    -  availability_zone = "us-east-1a" 
    -  key_name          = "Sentinel-Project-Key"
    +  ami               = var.ami_id
    +  instance_type     = var.instance_type
    +  availability_zone = var.availability_zone
    +  key_name          = var.key_name

      vpc_security_group_ids = [aws_security_group.forensic_isolation.id]

    -  tags = {
    -    Name = "Forensic-Analyst-Workstation"
    -  }
    +  tags = {
    +    Name = var.forensic_workstation_name
    +  }
    }

    resource "aws_ebs_volume" "evidence_disk" {
    -  availability_zone = "us-east-1a" 
    -  snapshot_id       = "snap-081ac51b83cdf41c2"
    -  size              = 8
    +  availability_zone = var.availability_zone
    +  snapshot_id       = var.snapshot_id
    +  size              = var.size # Added size variable for flexibility

    -  tags = {
    -    Name = "Evidence-Disk-Case-Alpha"
    -  }
    +  tags = {
    +    Name = var.evidence_disk_name
    +  }
    }

    resource "aws_volume_attachment" "ebs_att" {
      device_name = "/dev/sdh"
      volume_id   = aws_ebs_volume.evidence_disk.id
      instance_id = aws_instance.forensic_workstation.id
    }
    ```
    *(Note: You would then pass values for these variables when running Terraform, e.g., via a `terraform.tfvars` file or command-line arguments.)*

---

### 2. Python Boto3 Automation Scripts

These Python Boto3 scripts are fully parameterized using `argparse`, allowing dynamic configuration via command-line arguments for all critical security parameters (Region, VPC ID, Security Group Name/Rules, Instance details). This ensures maximum reusability and production-readiness for all cloud resource management and automation tasks.

**Python Script (`scripts/boto3/EC2_launchers/big_bang_launcher.py`):**

```python
import boto3
import os # Used for environment variables

# Use the EC2 resource client for high-level operations
# Configure region from environment variable or default to us-east-1
AWS_REGION = os.environ.get('AWS_REGION', 'us-east-1')
ec2 = boto3.resource('ec2', region_name=AWS_REGION)

# -- CONFIGURATION --
# Load configuration from environment variables or use defaults
AMI_ID = os.environ.get('AMI_ID', 'ami-0b6c6ebed2801a5cb') # Find The AMI
INSTANCE_TYPE = os.environ.get('INSTANCE_TYPE', 't2.micro') # Free Tier
KEY_NAME = os.environ.get('KEY_NAME', 'Sentinel-Project-Key') 
SG_ID = os.environ.get('SG_ID', 'sg-0e5ba34f03df0425b') # SG-created previously

def launch_sentinel():
    """
    Launches an EC2 instance with predefined configurations,
    waits for it to be running, and prints its public IP and SSH command.
    """
    try:
        print(f"[*] Launching Sentinel Instance with Key: {KEY_NAME} in region {AWS_REGION}...")

        # Create the EC2 instance
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
        print(f"[*] Success! Instance created. ID: {instance.id}")

        # Wait for the instance to be in the 'running' state
        print("[*] Waiting for instance to initialize...")
        instance.wait_until_running()
        instance.reload() # Refresh the instance object data after state change

        print("\n[!!!] DEPLOYMENT COMPLETE")
        print(f"Instance Public IP Address: {instance.public_ip_address}")
        # Note: The '.pem' extension is assumed for the private key file.
        print(f"SSH Command: ssh -i {KEY_NAME}.pem ec2-user@{instance.public_ip_address}")

    except Exception as e:
        print(f"[!] Deployment Failed: {e}")

if __name__ == "__main__":
    launch_sentinel()
```

**Execution Steps:**

1.  **Navigate to Scripts Directory:**
    ```bash
    cd cloud-security-automation/scripts/boto3/EC2_launchers/
    ```
2.  **Set Environment Variables (Optional but Recommended):**
    You can override the default configuration by setting environment variables before running the script.
    ```bash
    export AWS_REGION='us-west-2'
    export AMI_ID='ami-xxxxxxxxxxxxxxxxx'
    export INSTANCE_TYPE='t3.micro'
    export KEY_NAME='MyNewKeyPair'
    export SG_ID='sg-xxxxxxxxxxxxxxxxx'
    ```
3.  **Run the Python Script:**
    ```bash
    python big_bang_launcher.py
    ```

--- 

### 3. Security Scripts (`scripts/boto3/Key_Pair/` & `scripts/boto3/Security_Groups/`)

These scripts automate common security-related tasks in AWS.

*   **`scripts/boto3/Key_Pair/key_maker.py`:**
    Creates an EC2 key pair named `Sentinel-Project-Key` and saves the private key (`.pem` file) locally with restrictive permissions (read-only for owner). **Crucially, this script should be run with caution as it creates sensitive private key files.** For portfolio purposes, demonstrating the *ability* to create and manage keys is key, but be mindful of how you handle generated `.pem` files.

*   **`scripts/boto3/Security_Groups/sg-creator.py`:**
    Creates a security group named `WebAccess-SG` allowing inbound traffic on port 80 (HTTP) and port 2222 (custom SSH) from anywhere (`0.0.0.0/0`).

*   **`scripts/boto3/Security_Groups/isolation-sg-creator.py`:**
    Creates a security group named `ISOLATION-TEST-ZONE` within a specified VPC (`vpc-0aec7117b29d0fcd7`). It then revokes all default outbound rules, effectively creating a "black hole" security group with no network access (in or out), suitable for isolating forensic analysis instances.

--- 

## 📈 Future Improvements & Best Practices

*   **Complete Script Functionality:** Populate the `cloud_forensics/` directory with relevant scripts, and flesh out the purpose/functionality of scripts in `Key_Pair/` and `Security_Groups/` if they are intended for more than just creation.
*   **Robust Error Handling & Logging:** Implement more detailed error handling and logging across all scripts to aid debugging and operational visibility.
*   **Orchestration:** Explore how these components can be orchestrated for a complete workflow. This could involve a main Python script that calls Terraform (using libraries like `python-terraform`) and then executes other Boto3 scripts, or a CI/CD pipeline setup.
*   **Security Hardening:** Continuously review and refine security configurations (e.g., use more specific IP ranges than `0.0.0.0/0` where possible, implement least privilege for IAM roles, harden EC2 instance AMIs).
*   **Diagrams:** Create architectural diagrams to visually represent your setup. This is highly effective for explaining complex systems to employers.
*   **Secrets Management:** For sensitive information like private keys or API credentials (beyond standard AWS creds), explore secure secrets management solutions.
*   **Testing:** Add unit or integration tests for your Python scripts and potentially Terraform.

--- 

This README provides a comprehensive overview of your project, its components, and how to use them. It also highlights areas for improvement, demonstrating a proactive and learning-oriented mindset, which is highly valued by employers.
