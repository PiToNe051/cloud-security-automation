# --- IAM Role Creation ---
resource "aws_iam_role" "evidence_writer_role" {
  name = var.role_name
  path = "/"
  description = "Allows EC2 instances to write forensic evidence to S3" # Corrected typo here

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          Service = "ec2.amazonaws.com"
        }
        Action = "sts:AssumeRole"
      }
    ]
  })

    tags = {
    "ManagedBy" = "Terraform"
    "Purpose"   = "Forensic Evidence Writing"
  }
}

# --- IAM Policy Attachment ---
locals {
  s3_put_object_policy_document = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "s3:PutObject",
          "s3:PutObjectAcl",
          "s3:GetBucketLocation"
        ]
        Resource = [
          "arn:aws:s3:::${var.s3_bucket_name}",
          "arn:aws:s3:::${var.s3_bucket_name}/*"
        ]
      }
    ]
  })
}
resource "aws_iam_role_policy" "s3_access_policy" {
  name   = "${var.role_name}-Policy"
  role   = aws_iam_role.evidence_writer_role.name
  policy = local.s3_put_object_policy_document
}

# --- Instance Profile Creation ---
resource "aws_iam_instance_profile" "evidence_writer_profile" {
  name = "${var.role_name}-Profile"
  path = "/"
  role = aws_iam_role.evidence_writer_role.name
}

# --- Outputs ---
output "iam_role_name" {
  description = "The name of the created IAM role."
  value       = aws_iam_role.evidence_writer_role.name
}

output "iam_instance_profile_name" {
  description = "The name of the created IAM instance profile."
  value       = aws_iam_instance_profile.evidence_writer_profile.name
}
