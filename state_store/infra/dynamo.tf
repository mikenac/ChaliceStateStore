resource "aws_dynamodb_table" "basic-dynamodb-table" {
  name           = "User-StateStore"
  billing_mode   = "PAY_PER_REQUEST"
  read_capacity  = 5
  write_capacity = 5
  hash_key       = "userID"
  range_key      = "createdTimestamp"

  attribute {
    name = "userID"
    type = "S"
  }
  attribute {
    name = "createdTimestamp"
    type = "S"
  }
}



