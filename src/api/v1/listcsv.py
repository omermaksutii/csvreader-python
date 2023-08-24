import os
import json

UPLOADS_DIR = 'uploads'

def lambda_handler(event, context):
    try:
        query_parameters = event.get('queryStringParameters')
        if not query_parameters:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Missing query parameters'})
            }

        topic = query_parameters.get('topic')
        if topic is None:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Missing or invalid topic parameter'})
            }

        uploaded_files = []
        for filename in os.listdir(os.path.join('/tmp', UPLOADS_DIR)):
            if filename.startswith(topic + '-') and filename.endswith('.csv'):
                uploaded_files.append(filename)

        if not uploaded_files:
            response_body = {'message': f'No files found with the topic: {topic}'}
        else:
            response_body = {'uploaded_files': uploaded_files}

        return {
            'statusCode': 200,
            'body': json.dumps(response_body)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
