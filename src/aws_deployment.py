import boto3
import os

def upload_model_to_s3(model_path, bucket_name, object_name=None):
    s3 = boto3.client('s3')
    if object_name is None:
        object_name = os.path.basename(model_path)
    s3.upload_file(model_path, bucket_name, object_name)

if __name__ == "__main__":
    upload_model_to_s3("recommender_model.pth", "my-ml-model-bucket")
    upload_model_to_s3("campaign_model.pkl", "my-ml-model-bucket")