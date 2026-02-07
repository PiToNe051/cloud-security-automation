variable "s3_bucket_name" {
    description = "The name of the S3 bucket for forensic evidence."
    type = string 
    default = "forensic-evidence-2026-alpha"
}

variable "role_name" {
    description = "The name of the IAM role."
    type = string
    default = "Sentinel-Evidence-Writer-Role"
}
