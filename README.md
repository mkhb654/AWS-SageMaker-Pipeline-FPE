# AWS SageMaker Pipeline for Real-Time Inference

This repository contains all the code and instructions needed to deploy a machine learning model using AWS SageMaker, from initial training to setting up real-time inference endpoints.

## Project Structure

Below is the layout of the project directory, explaining where each part of the application is stored and how it is organized:

```text
AWS-SageMaker-Pipeline-FPE/
├── README.md               # Project overview and setup instructions
├── requirements.txt        # List of dependencies
├── setup_aws.md            # Instructions to setup AWS services
├── data_preprocessing/
│   └── data_preprocessing.py  # Script for data cleaning and preparation
├── model_training/
│   └── train.py               # Script for model training
├── pipeline/
│   └── pipeline.py            # Defines and sets up the SageMaker pipeline
├── real_time_inference/
│   ├── create_sagemaker_model.py  # Script to create and deploy SageMaker model
│   └── lambda_inference.py        # Lambda function for real-time inference
```

## Getting Started

### Prerequisites

Ensure you have the following installed:
- Python 3.x
- AWS CLI
- An AWS account with appropriate permissions to SageMaker, S3, RDS, and Lambda

### Installation

1. Clone the repository
2. Navigate to the cloned directory and install the required Python packages:
```bash
pip install -r requirements.txt
```

### AWS Setup

For detailed instructions on setting up the required AWS services, refer to [setup_aws.md](./setup_aws.md). Make sure to adjust the placeholders in the code with your specific configurations after setup.

## Usage

### Data Preprocessing

Navigate to the data_preprocessing directory and execute:
```bash
python data_preprocessing.py
```

### Model Training

Navigate to the model_training directory and execute:
```bash
python train.py
```

### Deploying the Model

Navigate to the real_time_inference directory:

- To create and deploy the model to a SageMaker endpoint, run:
```bash
python create_sagemaker_model.py
```

- To invoke the endpoint using a Lambda function, refer to the script:
```bash
lambda_inference.py
```