# S3 Security Module 🪣

This module focuses on secure storage automation, specifically for forensic data handling.

## 📂 Components

### 1. Evidence Locker (`s3-locker/`)
*   **`s3_locker_creator.py`**: A tool to provision **secure-by-default** S3 buckets.
    *   **Encryption:** Enforces AES-256 (SSE-S3).
    *   **Access:** Blocks **ALL** public access (Bucket Policy & ACLs).
    *   **Integrity:** Enables **Versioning** to prevent data tampering or accidental deletion.
    *   **Compatibility:** Auto-handles `us-east-1` location constraint quirks.

## 🚀 Usage

**Create a new forensic locker:**
```bash
cd s3-locker
python3 s3_locker_creator.py evidence-case-2026-alpha
```

**Verify Security:**
Check the AWS Console > S3. The bucket should show:
*   "Access: Bucket and objects not public"
*   "Default encryption: Enabled"
*   "Bucket Versioning: Enabled"
