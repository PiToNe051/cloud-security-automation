# EC2 Automation

This directory contains resources for automating Amazon Elastic Compute Cloud (EC2) instance management and related infrastructure. It utilizes both Python with Boto3 for scripting and Terraform for Infrastructure as Code.

## Structure

-   **`boto3/`**: Contains Python scripts for EC2-related tasks:
    -   `EC2_launchers/`: Scripts for launching EC2 instances.
    -   `Key_Pair/`: Scripts for managing EC2 key pairs.
    -   `Security_Groups/`: Scripts for creating and managing security groups.
    -   `README.md`: Details on Boto3 EC2 scripts.
-   **`terraform/`**: Contains Terraform HCL configurations for defining EC2 infrastructure declaratively.
    -   `main.tf`: Core Terraform configuration, likely including provider setup.
    -   `variables.tf`: Input variables for Terraform modules.
    -   `terraform.tfstate` / `terraform.tfstate.backup`: Terraform state files (should generally not be committed directly, but may exist here for local development/testing).
    -   `terraform.tfvars`: Variable values for a specific environment.

## Purpose

This section provides tools to:
*   Programmatically launch, configure, and manage EC2 instances.
*   Automate the creation and management of security groups and key pairs.
*   Define EC2 infrastructure as code using Terraform for reproducible deployments.