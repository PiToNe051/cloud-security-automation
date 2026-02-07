variable "bucket_prefix" {
    description = "The prefix of the S3 bucket, ensures a unique name."
    type = string
    default = "forensic-evidence-"
}

variable "s3_tag_name" {
    description = "The name of the S3 bucket tag"
    type = string
    default = "Forensic Evidence Locker"
}

variable "s3_environment" {
    description = "The name of the S3 Environment."
    type = string
    default = "Security-Lab"
}

