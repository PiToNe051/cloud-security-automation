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
  region = var.aws_region
}

# Define SG

resource "aws_security_group" "forensic_isolation" {
  name        = var.forensic_sg_name
  description = var.forensic_sg_description
  vpc_id      = var.vpc_id
}


resource "aws_instance" "sentile_twin" {
  ami           = var.ami_id
  instance_type = var.instance_type
  key_name      = var.key_name
 

  vpc_security_group_ids = [aws_security_group.forensic_isolation.id]

  tags = {
  Name = var.sentinel_instance_name
  }  
} 

# Provisioning Isolated Workstation for Disk Analysis

resource "aws_instance" "forensic_workstation" {
  ami               = var.ami_id
  instance_type     = var.instance_type
  availability_zone = var.availability_zone 
  key_name          = var.key_name


  # Attach to existing lockdown group
  vpc_security_group_ids = [aws_security_group.forensic_isolation.id]

  tags = {
    Name = var.forensic_workstation_name
  }
}

# 1. Create a physical disk from the forensic snapshot
resource "aws_ebs_volume" "evidence_disk" {
  availability_zone = var.availability_zone 
  snapshot_id       = var.snapshot_id
  size              = var.size

  tags = {
    Name = var.evidence_disk_name
  }
}

# Plug In the disk to the Workstation
resource "aws_volume_attachment" "ebs_att" {
  device_name = "/dev/sdh"
  volume_id   = aws_ebs_volume.evidence_disk.id
  instance_id = aws_instance.forensic_workstation.id
}
