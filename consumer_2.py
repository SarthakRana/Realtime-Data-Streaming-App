import json
import base64

def lambda_handler(event, context):
    
    try: 
        print(json.dumps(event))
        
        for record in event['Records']:
            # kinesis data is base64 encoded, so decode it
            payload = base64.b64decode(record['kinesis']['data']).decode('utf-8')
            print(f"Decoded payload for consumer #1: {payload}")
            
            # Process the payload as needed
            data = json.loads(payload)
            # Do something with the data
            print(f"Processed data: {data}")
    
    except Exception as e:
        print(f"Exception: {e}")
