import pandas as pd
import boto3
from sqlalchemy import create_engine

def fetch_and_prepare_data(station_id):
    # Database credentials and details
    db_username = 'your_username'
    db_password = 'your_password'
    db_name = 'your_database_name'
    db_host = 'your_rds_host'
    

    engine = create_engine(f'postgresql://{db_username}:{db_password}@{db_host}/{db_name}')
    

    query = f"SELECT * FROM metadata WHERE station_id = {station_id}"
    metadata = pd.read_sql(query, engine)
    

    s3 = boto3.client('s3')
    bucket_name = metadata['s3_bucket_name'].values[0]
    image_path = metadata['image_path'].values[0]
    response = s3.get_object(Bucket=bucket_name, Key=image_path)
    

    data = pd.read_csv(response['Body'])
    normalized_data = (data - data.mean()) / data.std()
    

    output_path = f'processed_data/station_{station_id}.csv'
    normalized_data.to_csv(f's3://{bucket_name}/{output_path}', index=False)

    return f's3://{bucket_name}/{output_path}'
