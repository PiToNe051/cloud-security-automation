resource "aws_s3_bucket" "forensic_locker" {
    bucket_prefix = var.bucket_prefix
    force_destroy = true 

    tags = {
        Name        = var.s3_tag_name
        Environment = var.s3_environment
    }
}

resource "aws_s3_bucket_versioning" "locker_versioning" {
    bucket = aws_s3_bucket.forensic_locker.id

    versioning_configuration {
        status = "Enabled"
    }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "locker_encryption" {
    bucket = aws_s3_bucket.forensic_locker.id

    rule {
        apply_server_side_encryption_by_default {
            sse_algorithm = "AES256"
        }
    }
}

resource "aws_s3_bucket_public_access_block" "locker_block" {
    bucket = aws_s3_bucket.forensic_locker.id

    block_public_acls       = true
    ignore_public_acls      = true
    block_public_policy     = true
    restrict_public_buckets = true
}
