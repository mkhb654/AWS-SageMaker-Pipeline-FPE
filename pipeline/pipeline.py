import sagemaker
from sagemaker.workflow.pipeline import Pipeline
from sagemaker.workflow.steps import ProcessingStep, TrainingStep
from sagemaker.processing import ScriptProcessor
from sagemaker.sklearn.estimator import SKLearn

def setup_pipeline():
    sagemaker_session = sagemaker.Session()
    role = sagemaker.get_execution_role()
    
    script_processor = ScriptProcessor(
        image_uri=sagemaker.image_uris.retrieve('sklearn', sagemaker_session.boto_region_name, '0.23-1'),
        command=['python3'],
        instance_type='ml.m5.xlarge',
        instance_count=1,
        base_job_name='data-processing-job',
        role=role,
        sagemaker_session=sagemaker_session
    )
    
    processing_step = ProcessingStep(
        name="DataPreprocessing",
        processor=script_processor,
        inputs=[sagemaker.processing.ProcessingInput(
            source='s3://your-bucket/path_to_station_data',
            destination='/opt/ml/processing/input'
        )],
        outputs=[sagemaker.processing.ProcessingOutput(
            output_name='processed_data',
            destination='/opt/ml/processing/output',
            source='/opt/ml/processing/output'
        )],
        code='data_preprocessing.py'  
    )

    estimator = SKLearn(
        entry_point='train.py',
        role=role,
        instance_count=1,
        instance_type='ml.m5.large',
        framework_version='0.23-1',
        sagemaker_session=sagemaker_session
    )
    
    training_step = TrainingStep(
        name="ModelTraining",
        estimator=estimator,
        inputs={
            'train': sagemaker.inputs.TrainingInput(
                s3_data=processing_step.properties.ProcessingOutputConfig.Outputs['processed_data'].S3Uri,
                content_type='text/csv'
            )
        }
    )

    pipeline = Pipeline(
        name='FPEModelBuildingPipeline',
        steps=[processing_step, training_step],
        sagemaker_session=sagemaker_session
    )

    pipeline.upsert(role_arn=role)
    return pipeline

setup_pipeline()
