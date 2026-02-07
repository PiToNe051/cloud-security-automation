# Assign values to the variables defined in variables.tf

# REQUIRED VALUES
vpc_id              = "vpc-0aec7117b29d0fcd7"      # Replace with your existing VPC ID
ami_id              = "ami-0b6c6ebed2801a5cb"      # Replace with your desired AMI ID
key_name            = "Sentinel-Project-Key"       # Replace with your EC2 Key Pair name
snapshot_id         = "snap-081ac51b83cdf41c2"     # Replace with your EBS snapshot ID

# OPTIONAL/DEFAULT VALUES (Uncomment and change if you want to override the default)
# aws_region        = "us-east-1"
# instance_type     = "t2.micro"
# availability_zone = "us-east-1a"
# size              = 8
# forensic_sg_name  = "FORENSIC-ISOLATION-ZONE"
# ... and so on for other variables ...