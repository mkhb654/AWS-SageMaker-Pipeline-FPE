import sagemaker
from sagemaker.sklearn.estimator import SKLearn

def train_model(s3_input_data):
    sagemaker_session = sagemaker.Session()
    role = sagemaker.get_execution_role()
    
    estimator = SKLearn(
        entry_point='train.py',
        framework_version='0.23-1',
        instance_type='ml.m5.xlarge',
        instance_count=1,
        role=role,
        sagemaker_session=sagemaker_session
    )
    
    estimator.fit({'train': s3_input_data})
    model_artifacts = estimator.model_data
    print("Model artifacts saved to:", model_artifacts)
    return model_artifacts
