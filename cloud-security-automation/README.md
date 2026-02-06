# Cloud Security Automation Portfolio

This project demonstrates practical cloud security automation techniques, combining Infrastructure as Code (IaC) with Python scripting to provision and manage cloud resources securely.

---

## 📁 Project Structure

```
cloud-security-automation/
├── .gitignore
├── README.md
├── terraform/
└── scripts/
    └── boto3/
        ├── cloud_forensics/
        ├── EC2/                # Compute & Network Automation
        │   ├── EC2_launchers/
        │   ├── Key_Pair/
        │   └── Security_Groups/
        └── S3/                 # Storage Security
            └── s3-locker/
```

---

## 🛠️ Modules

### 💻 EC2 Automation (`scripts/boto3/EC2/`)
Scripts for launching secure instances, managing key pairs, and configuring firewalls.
*   [View EC2 Documentation](scripts/boto3/EC2/README.md)

### 🪣 S3 Security (`scripts/boto3/S3/`)
Tools for creating secure, compliant storage for forensic evidence.
*   [View S3 Documentation](scripts/boto3/S3/README.md)

---

## 🚀 Deployment Instructions

### 1. Terraform Infrastructure
Navigate to `terraform/` and run:
```bash
terraform init
terraform apply
```

### 2. Python Automation
Navigate to the specific module folder.

**Example: Launch a Sentinel Node**
```bash
cd scripts/boto3/EC2/EC2_launchers
python3 big_bang_launcher.py
```

**Example: Create an Evidence Locker**
```bash
cd scripts/boto3/S3/s3-locker
python3 s3_locker_creator.py forensic-case-001
```
