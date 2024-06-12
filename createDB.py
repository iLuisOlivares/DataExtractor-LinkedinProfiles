#Archivo que crea la Tabla en DynamoDB
import boto3
from dotenv import load_dotenv
import os
load_dotenv()

aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
aws_table_name = os.getenv('AWS_TABLE_NAME')
os.environ['AWS_ACCESS_KEY_ID'] = aws_access_key_id
os.environ['AWS_SECRET_ACCESS_KEY'] = aws_secret_access_key

os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'

dynamodb = boto3.client('dynamodb')


table = dynamodb.create_table(
    TableName=aws_table_name,
    KeySchema=[
        {
            'AttributeName': 'public_id',
            'KeyType': 'HASH' 
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'public_id',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)


dynamodb.get_waiter('table_exists').wait(TableName=aws_table_name)

print("Table created successfully.")