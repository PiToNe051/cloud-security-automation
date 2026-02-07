# EC2 Automation Module 💻

This module handles the provisioning and security configuration of Elastic Compute Cloud (EC2) resources.

## 📂 Components

### 1. Launchers (`EC2_launchers/`)
*   **`big_bang_launcher.py`**: Automated deployment of the "Sentinel" forensic node.
    *   **Features:** Deploys t2.micro instance, attaches security groups, tags for project tracking.
    *   **Usage:** `python3 big_bang_launcher.py`

### 2. Security Groups (`Security_Groups/`)
*   **`isolation-sg-creator.py`**: Creates a **"Black Hole"** security group (No Inbound/Outbound). Used for isolating malware or compromised instances.
*   **`sg-creator.py`**: Creates standard access groups (HTTP/SSH).

### 3. Key Management (`Key_Pair/`)
*   **`key_maker.py`**: Generates RSA key pairs for EC2 access and saves the `.pem` file locally with secure permissions (`400`).

## 🚀 Quick Start

**Launch a Sentinel Node:**
```bash
export AWS_REGION=us-east-1
cd EC2_launchers
python3 big_bang_launcher.py
```
