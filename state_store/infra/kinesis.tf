resource "aws_kinesis_stream" "TestDataStream" {
  name             = "TestDataStream"
  shard_count      = 2
  retention_period = 48
  encryption_type = "NONE"

  shard_level_metrics = [
    "IncomingBytes",
    "OutgoingBytes",
    "IncomingRecords", 
  ]
}

output "kinesis_stream_name" {
  value = "${aws_kinesis_stream.TestDataStream.name}"
}