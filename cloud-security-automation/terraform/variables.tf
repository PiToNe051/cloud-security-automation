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

variable "size" {
  description = "The size of the EBS volume in GiB."
  type        = number
  default     = 8
}