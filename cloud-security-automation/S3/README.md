# S3 Automation

This directory houses scripts and Terraform configurations for automating the setup and management of AWS S3 buckets, with a focus on security and operational best practices.

## Structure

-   **`boto3/`**: Contains Python scripts for S3 bucket management.
    -   `s3_locker_creator.py`: Scripts likely for creating secure S3 buckets (e.g., implementing public access blocks, encryption, versioning).
    -   `README.md`: Details on Boto3 S3 scripts.
-   **`terraform/`**: Contains Terraform HCL configurations for defining S3 buckets and their settings declaratively.
    -   `main.tf`: Core Terraform configuration, including provider setup.
    -   `s3_locker.tf`: Terraform resources for S3 bucket configurations (e.g., Public Access Block, Encryption, Versioning, Lifecycle policies).
    -   `variables.tf`: Input variables for S3 configurations.

## Purpose

This section provides tools to:
*   Programmatically create and configure S3 buckets with security best practices using Python/Boto3.
*   Define S3 bucket configurations as Infrastructure as Code using Terraform, ensuring consistent and secure deployments.