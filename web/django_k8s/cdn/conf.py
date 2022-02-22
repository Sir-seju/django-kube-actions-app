import os

AWS_ACCESS_KEY_ID=os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY=os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME='graystum-django-k8s-test-bucket'
AWS_S3_ENDPOINT_URL="https://s3.eu-north-1.amazonaws.com"
AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=86400",
    "ACL": "public-read"
}
AWS_LOCATION="https://graystum-django-k8s-test-bucket.s3.eu-north-1.amazonaws.com"
DEFAULT_FILE_STORAGE = "django_k8s.cdn.backends.MediaRootS3BotoStorage"
STATICFILES_STORAGE = 'django_k8s.cdn.backends.StaticRootS3BotoStorage'
