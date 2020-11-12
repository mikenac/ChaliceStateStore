import os
import json
import boto3
from chalice import Chalice

app = Chalice(app_name='state-store')
app.debug = True


@app.on_kinesis_record(stream=os.environ["KINESIS_STREAM_NAME"])
def handle_kinesis_message(event):
    """ Handle batch of events from Kinesis topic """
    
    for record in event:
        # The .data attribute is automatically base64 decoded for you.
        app.log.debug("Received message with contents: %s", record.data)
        result = add_thing(record.data)
        app.log.debug("Response from persist: %s", result)

def get_db():
    """ get the Dynamo table """
    return boto3.resource('dynamodb').Table(
            os.environ['TABLE_NAME'])

def add_thing(thing):
    """ store the latest thing in the data store, in real life, store all version of thing """
    thing_def = get_thing_def(thing)
    return get_db().put_item(
            Item=thing_def
        )

# abstract type method, defines what our thing is. This is the only 
# "specific" method required.
def get_thing_def(thing):
    """ Define the mapping of our JSON to dynamo table """

    json_thing = json.loads(thing)
    return {
        'userID': json_thing["userID"],
        'createdTimestamp': json_thing["createdTimestamp"],
        'user': json_thing
    }