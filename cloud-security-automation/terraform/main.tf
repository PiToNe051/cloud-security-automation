terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

# Configure the AWS Provider (It uses your existing ~/.aws/credentials)
provider "aws" {
  region = "us-east-1"
}

# Define SG

resource "aws_security_group" "forensic_isolation" {
  name        = "FORENSIC-ISOLATION-ZONE"
  description = "Total lockdown group - No Inbound or Outbout"
  vpc_id      = "vpc-0aec7117b29d0fcd7"
}


resource "aws_instance" "sentile_twin" {
  ami           = "ami-0b6c6ebed2801a5cb"
  instance_type = "t2.micro"
  key_name      = "Sentinel-Project-Key"
 

  vpc_security_group_ids = [aws_security_group.forensic_isolation.id]

  tags = {
  Name = "Sentinel-Forensic-Twin"
  }  
} 

# Provisioning Isolated Workstation for Disk Analysis

resource "aws_instance" "forensic_workstation" {
  ami               = "ami-0b6c6ebed2801a5cb"
  instance_type     = "t2.micro"
  availability_zone = "us-east-1a" 
  key_name          = "Sentinel-Project-Key"


  # Attach to existing lockdown group
  vpc_security_group_ids = [aws_security_group.forensic_isolation.id]

  tags = {
    Name = "Forensic-Analyst-Workstation"
  }
}

# 1. Create a physical disk from the forensic snapshot
resource "aws_ebs_volume" "evidence_disk" {
  availability_zone = "us-east-1a" 
  snapshot_id       = "snap-081ac51b83cdf41c2"
  size              = 8

  tags = {
    Name = "Evidence-Disk-Case-Alpha"
  }
}

# Plug In the disk to the Workstation
resource "aws_volume_attachment" "ebs_att" {
  device_name = "/dev/sdh"
  volume_id   = aws_ebs_volume.evidence_disk.id
  instance_id = aws_instance.forensic_workstation.id
}
