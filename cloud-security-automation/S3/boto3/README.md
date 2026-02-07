# S3 Evidence Locker Creator 🔒

This tool creates a **secure, forensic-ready S3 bucket** for storing sensitive logs and evidence.

## Features
*   **Automatic Creation:** Handles region constraints (including `us-east-1` quirks).
*   **Block Public Access:** Enforces AWS "Block Public Access" on the bucket level.
*   **Encryption:** Enables AES-256 Server-Side Encryption (SSE-S3) by default.
*   **Versioning:** Protects against accidental deletion or tampering (Chain of Custody).

## Usage

```bash
# Create a bucket in us-east-1 (default)
python3 s3_locker_creator.py my-forensic-bucket-2026

# Create a bucket in a specific region
python3 s3_locker_creator.py my-forensic-bucket-eu eu-west-1
```

## Requirements
*   Python 3
*   `boto3` library (`pip install boto3`)
*   AWS Credentials configured (`aws configure`)
