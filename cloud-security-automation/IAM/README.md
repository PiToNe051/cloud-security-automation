# IAM Automation

This directory focuses on automating the management of AWS Identity and Access Management (IAM) resources, particularly roles, policies, and instance profiles. It offers both programmatic and Infrastructure as Code approaches.

## Structure

-   **`boto3/`**: Contains Python scripts for creating IAM resources dynamically.
    -   `iam_role_creator.py`: A script to programmatically create IAM roles with specific trust policies and attach least-privilege policies, suitable for services like EC2 instances needing S3 access.
-   **`terraform/`**: Contains Terraform HCL configurations for declarative IAM resource management.
    -   `main.tf`: Core Terraform configuration, including provider setup.
    -   `iam.tf`: Defines IAM roles, policies, and instance profiles using Terraform resources.
    -   `variables.tf`: Input variables for IAM configurations.

## Purpose

This section provides tools to:
*   Programmatically create IAM roles and attach policies using Python/Boto3.
*   Define and manage IAM roles, policies, and instance profiles as Infrastructure as Code using Terraform, enabling version control and repeatable deployments.