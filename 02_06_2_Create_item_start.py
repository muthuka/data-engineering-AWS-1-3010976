import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('Employees')

# Create item with Name: Mark Wilbur and Email: markwilbur@dataengineer.cloud

response = table.put_item(
    Item={
        'Name': 'Mark Wilbur',
        'Email': 'markwilbur@dataengineer.cloud',
        'Department': 'IT'
    }
)
print(response)
