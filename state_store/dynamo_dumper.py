import boto3
import json
from boto3.dynamodb.conditions import Key

class DynamoDumper:

    def __init__(self, table):
        self.table = table
        self.client = boto3.resource("dynamodb")

    def get(self, expression):

        resp = self.client.Table(self.table).query(
            TableName=self.table,
            KeyConditionExpression=Key(expression['key']).eq(expression['value'])
            )
        return resp

    def get_latest(self, expression):

        resp = self.client.Table(self.table).query(
            TableName=self.table,
            KeyConditionExpression=Key(expression['key']).eq(expression['value']),
            ScanIndexForward=False,
            Limit=1
            )
        return resp


if __name__ == '__main__':

    expression = {"key": "userID", "value": "1"}

    dumper = DynamoDumper('User-StateStore')
    
    
    print("\nHere are all of the states\n==========================\n")
    resp = dumper.get(expression)
    if 'Items' in resp.keys():
        for item in resp['Items']:
            print(item['user'])
    else:
        print("You cannot haz cheezeburger yet. Please wait.")

    print("\nHere is the latest state\n==========================\n")
    resp = dumper.get_latest(expression)
    if 'Items' in resp.keys():
        for item in resp['Items']:
            print(item['user'])
    else:
        print("You cannot haz cheezeburger yet. Please wait.")
