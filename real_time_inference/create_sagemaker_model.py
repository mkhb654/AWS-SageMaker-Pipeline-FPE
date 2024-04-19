import boto3
import sagemaker
from sagemaker import get_execution_role
from sagemaker.model import Model

def create_sagemaker_model(model_data, instance_type):
    role = get_execution_role()
    sagemaker_session = sagemaker.Session()

    sage_model = Model(
        image_uri=sagemaker.image_uris.retrieve('xgboost', sagemaker_session.boto_region_name, '1.0-1'),  # Adjust depending on your model requirements
        model_data=model_data,  # S3 path to the model artifacts
        role=role,
        sagemaker_session=sagemaker_session
    )

    predictor = sage_model.deploy(
        initial_instance_count=1,
        instance_type=instance_type
    )

    return predictor.endpoint_name

# Please put the right model_artifact_url here
model_artifact_url = "s3://your-bucket/path-to-model-artifacts/model.tar.gz"
endpoint_name = create_sagemaker_model(model_artifact_url, 'ml.m5.large')
print(f"Model deployed at endpoint: {endpoint_name}")
