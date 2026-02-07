# Cloud Security Automation

This repository contains a collection of scripts and Terraform configurations designed to automate common cloud security tasks across AWS services like EC2, IAM, and S3. The goal is to provide robust, repeatable, and secure infrastructure management.

The automation is implemented using two primary approaches:
*   **Python with Boto3 SDK:** For programmatic interaction with AWS services, enabling dynamic and complex task execution.
*   **Terraform:** For Infrastructure as Code (IaC), allowing declarative definition, versioning, and repeatable deployment of cloud resources.

## Project Structure

The repository is organized into top-level directories representing major AWS services or functional areas:

-   **`boto3/`**: Contains Python scripts that leverage the Boto3 SDK for AWS interactions.
    -   `cloud_forensics/`: Scripts specifically for cloud forensic analysis and evidence protection.
    -   `EC2/`, `IAM/`, `S3/`: Boto3 scripts related to their respective AWS services.
-   **`EC2/`**: Scripts and Terraform modules for automating EC2 instance management, security groups, key pairs, etc.
-   **`IAM/`**: Scripts and Terraform modules for managing AWS Identity and Access Management (IAM) resources like roles, policies, and instance profiles.
-   **`S3/`**: Scripts and Terraform modules for managing AWS S3 buckets, including configurations for security and lifecycle management.

Each subdirectory may contain its own README.md for more specific details.