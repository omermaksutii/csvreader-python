import json
import os

TEMP_DIR = '/tmp'
UPLOADS_DIR = 'uploads'  # Specify the uploads folder
if os.environ.get('IS_LOCAL'):
    import requests  # Include the requests module

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        csv_url = body['csv_url']
        topic = body['topic']

        if os.environ.get('IS_LOCAL'):
            response = requests.get(csv_url)
            response.raise_for_status()
        else:
            # Use AWS Lambda's HTTP client or other methods to fetch the CSV
            pass  # Placeholder, replace with your actual code

        csv_filename = csv_url.split('/')[-1]
        full_csvname = topic + '-' +csv_filename
        local_csv_path = os.path.join(TEMP_DIR, UPLOADS_DIR, full_csvname)

        # Create the uploads folder if it doesn't exist
        os.makedirs(os.path.join(TEMP_DIR, UPLOADS_DIR), exist_ok=True)

        with open(local_csv_path, 'wb') as f:
            if os.environ.get('IS_LOCAL'):
                f.write(response.content)
            else:
                # Write your logic for AWS Lambda environment here
                pass  # Placeholder, replace with your actual code

        return {
            'statusCode': 200,
            'body': json.dumps({'message': f'CSV file "{csv_filename}" downloaded successfully.'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
