# Setting Up AWS Services for SageMaker Pipeline

This guide provides step-by-step instructions for setting up the required AWS services to run the SageMaker Pipeline and deploy real-time inference endpoints for the FPE model.

## AWS Services Used

- Amazon S3
- Amazon SageMaker
- AWS RDS
- AWS Lambda (optional for Task 2)

## Prerequisites

- AWS Account
- AWS CLI installed and configured
- Basic understanding of AWS services

## Configurations

### Amazon S3

1. **Create an S3 Bucket:**
   - Navigate to the S3 service in the AWS Management Console.
   - Click **Create bucket**.
   - Enter a bucket name and select the region.
   - Keep the default settings and click **Create**.
   - Note: Replace all instances of `your-bucket` in your code with your bucket name.

### Amazon RDS

1. **Set Up an RDS Instance for storing model data and metadata:**
   - Go to the RDS dashboard in the AWS Management Console.
   - Click **Create database**.
   - Choose a database creation method, select your engine options, and specify your DB instance size.
   - Configure settings like instance identifier, credentials, and VPC settings.
   - Enable public accessibility if needed and configure additional security groups.
   - Note: You will need to update the database connection settings in your Python scripts (`data_preprocessing.py` or any other script accessing the RDS).

### Amazon SageMaker

1. **Create a SageMaker Role:**
   - Go to the IAM service in the AWS Management Console.
   - Navigate to Roles and click **Create role**.
   - Select **SageMaker** as the service that will use this role.
   - Attach policies like `AmazonSageMakerFullAccess` and any specific permissions for accessing S3 buckets or RDS.
   - Note: Replace `sagemaker.get_execution_role()` in your code with the actual ARN if running scripts outside of SageMaker notebook instances.

### AWS Lambda (For Task 2)

1. **Create a Lambda Function:**
   - Navigate to Lambda in the AWS Management Console.
   - Click **Create function**.
   - Choose **Author from scratch**.
   - Enter a function name and select Python 3.x for the runtime.
   - Choose or create a new role with permissions to access SageMaker and any other required services.
   - Note: Ensure the Lambda function code (`lambda_inference.py`) has the correct endpoint and configuration settings.

## Important Notes

- Ensure all paths, credentials, and specific AWS resource identifiers like bucket names, database connection strings, and endpoint names are updated in your code where applicable.
- It's essential to manage your AWS credentials securely and not expose them in your code.

## Next Steps

After setting up the AWS services, follow the detailed instructions in the README.md to install dependencies, configure your project, and run the scripts.
