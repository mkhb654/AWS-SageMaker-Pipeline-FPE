import json
import boto3

def lambda_handler(event, context):
    runtime = boto3.client('sagemaker-runtime')
    endpoint_name = 'your-endpoint-name'  # Replace with the actual endpoint name

    image_data = event['body'].get('image_data')

    response = runtime.invoke_endpoint(
        EndpointName=endpoint_name,
        ContentType='application/x-image',
        Body=bytearray(image_data, encoding='utf-8')
    )

    result = json.loads(response['Body'].read().decode())
    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }
