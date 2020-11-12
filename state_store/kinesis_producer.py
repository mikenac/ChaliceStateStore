import boto3
import subprocess
import json
import os
import datetime

class KinesisProducer():

    def __init__(self, stream_name: str):
        self.stream_name = stream_name
        os.environ["KINESIS_STREAM_NAME"] = stream_name

    @classmethod
    def from_tf_state(cls):
        """ NOT REALLY NEEDED,BUT GOOD EXAMPLE - get the identity of the stream from the TF state """
        result = subprocess.run(args=['terraform', 'output', 'kinesis_stream_name'],
                stdout=subprocess.PIPE, cwd="infra/")
        stream_name = (result.stdout.decode('UTF-8')).strip()
        return cls(stream_name)

    def publish(self, partition_key: str, payload: str):
        client = boto3.client('kinesis')
        client.put_record(
            StreamName=self.stream_name,
            Data=payload,
            PartitionKey=str(partition_key))


if __name__ == '__main__':

    now = datetime.datetime.now().isoformat()
   
    users = [
        f"""{{"userID": "1", "createdTimestamp": "{now}", "user": {{ "userID": "1", "userName": "BJenkins", "lastName": "Dole", "firstName": "Bob"}}}}\n"""
    ]

    producer = KinesisProducer.from_tf_state()
    for user in users:
        user_json = json.loads(user)
        producer.publish(user_json["userID"], user)
        print(f"Added: {user_json}")

