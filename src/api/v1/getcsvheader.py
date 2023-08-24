import json
import os
import csv

UPLOADS_DIR = 'uploads'

def get_csv_header(filename):
    try:
        file_path = os.path.join('/tmp', UPLOADS_DIR, filename)

        if not os.path.isfile(file_path):
            return None  # File not found

        with open(file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            header_line = next(csv_reader)  # Get the first row (header) as a list

        return header_line
    except Exception as e:
        return None  # Error occurred

def lambda_handler(event, context):
    try:
        query_parameters = event.get('queryStringParameters')
        if not query_parameters:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Missing query parameters'})
            }

        filename = query_parameters.get('filename')
        if filename is None:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Missing or invalid filename parameter'})
            }

        header = get_csv_header(filename)
        if header is None:
            response_body = {'message': f'Failed to retrieve header for file: {filename}'}
        else:
            response_body = {'csv_header': header}

        return {
            'statusCode': 200,
            'body': json.dumps(response_body)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
