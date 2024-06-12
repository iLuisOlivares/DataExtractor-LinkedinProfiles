# Consulta a la tabla de para imprimir los items (Ejemplo practico)

import boto3
import os

from dotenv import load_dotenv
import os
load_dotenv()

aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
aws_table_name = os.getenv('AWS_TABLE_NAME')

os.environ['AWS_ACCESS_KEY_ID'] = aws_access_key_id
os.environ['AWS_SECRET_ACCESS_KEY'] = aws_secret_access_key
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')


table = dynamodb.Table(aws_table_name)

response = table.scan()

items = response.get('Items', [])

for item in items:
    print(item)
# print(items[0].get('experience', [])[0].get('company', {}).get('companyName', ''))