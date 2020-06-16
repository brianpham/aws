import boto3
from pprint import pprint

client = boto3.client('dynamodb')

## Need to pass it a partition key
## Otherwise will fail 
# response = client.get_item(
#     TableName = "bpham-dev-table",
#     Key={
#         'serial_num': {
#             'S': 'bpham0909'
#         }
#     }
# )

# pprint(response)

## Adding item with partition key
## Otherwise fails
response = client.put_item(
    TableName = "bpham-dev-table",
    Item = {
        'serial_num' : {
            'S': 'bpham_sn_001'
        },
        'account_id' : {
            'S': 'bpham_ai_002'
        },
        'firstName' : {
            'S': 'Brian'
        },
        'lastName' : {
            'S': 'Pham'
        }
    }
)

# response = client.delete_item(
#     TableName = "bpham-dev-table",
#     Key = {
#         'serial_num' : {
#             'S': 'bpham0909'
#         }
#     }
# )

# print(response)

# {
#   "account_id": {
#     "S": "bpham00v15"
#   },
#   "serial_num": {
#     "S": "bpham0909"
#   }
# }

# response = client.get_item(
#     TableName = "bpham-dev-table",
#     Key = "serial_num"
# )

# def put_movie(title, year, plot, rating, dynamodb=None):
#     if not dynamodb:
#         dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

#     table = dynamodb.Table('Movies')
#     response = table.put_item(
#        Item={
#             'year': year,
#             'title': title
#         }
#     )
#     return response