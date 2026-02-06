# Cloud Security Automation Portfolio

This project demonstrates practical cloud security automation techniques, combining Infrastructure as Code (IaC) with Python scripting to provision and manage cloud resources securely. It leverages Wazuh for threat detection and OpenClaw for workflow integration, showcasing a commitment to protecting digital assets and ensuring the resilience of passion-driven projects.

**Mission:**
Aligned with a commitment to protect the innovation and hard work that organizations build, this project stands on the frontline of defense. Our goal is to safeguard the digital assets that provide value to people’s lives, ensuring that passion-driven projects remain secure and resilient.

**Core Technologies:**
*   **AWS:** Cloud infrastructure provider.
*   **Terraform:** Infrastructure as Code for provisioning AWS resources.
*   **Python (Boto3):** Scripting for AWS resource management and automation.
*   **Wazuh:** (Mentioned as part of the project's context, though not directly implemented in these scripts).
*   **OpenClaw:** (Mentioned as part of the project's context, for workflow integration).

---

## 📁 Project Structure

```
cloud-security-automation/
├── .gitignore
├── README.md
├── terraform/
│   ├── main.tf
│   ├── terraform.tfstate
│   └── terraform.tfstate.backup
└── scripts/
    └── boto3/
        ├── cloud_forensics/
        ├── s3-locker/           # 🔒 Secure S3 Evidence Locker Tool
        │   ├── s3_locker_creator.py
        │   └── README.md
        ├── EC2_launchers/
        │   └── big_bang_launcher.py
        ├── Key_Pair/
        │   └── key_maker.py
        └── Security_Groups/
            ├── isolation-sg-creator.py
            └── sg-creator.py
```

---

## 🛠️ Tools & Scripts

### 🔒 S3 Evidence Locker (`scripts/boto3/s3-locker/`)
A forensic-ready tool to create secure evidence vaults instantly.
*   **Features:** AES-256 Encryption, Versioning, Block Public Access.
*   **Usage:** `python3 s3_locker_creator.py <bucket-name>`

### 🚀 EC2 Launchers (`scripts/boto3/EC2_launchers/`)
Automated instance provisioning scripts.
*   **`big_bang_launcher.py`:** Launches a Sentinel EC2 instance with predefined security configs.

### 🔑 Key Management (`scripts/boto3/Key_Pair/`)
*   **`key_maker.py`:** Generates and secures EC2 Key Pairs locally.

### 🛡️ Security Groups (`scripts/boto3/Security_Groups/`)
*   **`isolation-sg-creator.py`:** Creates a "Black Hole" security group (No Inbound/Outbound) for malware analysis.
*   **`sg-creator.py`:** Standard web/ssh security group creator.

---

## 🚀 Deployment Instructions

### 1. Terraform Infrastructure
Navigate to `terraform/` and run:
```bash
terraform init
terraform apply
```

### 2. Python Automation
Navigate to the specific script folder and run via Python 3.
Ensure your AWS credentials are configured (`aws configure`).

```bash
cd scripts/boto3/s3-locker
python3 s3_locker_creator.py forensic-evidence-2026
```

---

## 📈 Future Improvements
*   **Automated Instance Termination:** A "Nuclear Option" script for FinOps.
*   **Orchestration:** CI/CD pipeline integration.
*   **Wazuh Integration:** Automated agent deployment via User Data.
