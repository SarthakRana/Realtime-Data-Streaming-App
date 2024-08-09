import json
import boto3

s3_client = boto3.client('s3')
kinesis_client = boto3.client('kinesis')

def lambda_handler(event, context):
    
    try:
        # get buket name and key name from event
        bucket_name = event['Records'][0]['s3']['bucket']['name']
        key_name = event['Records'][0]['s3']['object']['key']
        
        # get the object from S3 bucket
        response = s3_client.get_object(Bucket=bucket_name, Key=key_name)
        content = response['Body'].read()
        decoded_content = content.decode('utf-8')
        
        # send data to kinesis strema 
        kinesis_response = kinesis_client.put_record(
            StreamName='stream-system-datastream',
            Data=json.dumps(decoded_content),
            PartitionKey=key_name
        )
        print(f'Successfully sent data to Kinesis: {kinesis_response}')
    
    except Exception as e:
        print(f"Exception : {e}")