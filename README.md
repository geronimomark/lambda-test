# install dependencies
pip install boto3 -t ./

# zip
zip -r ../lambda.zip .

# copy to s3
aws s3 cp ../lambda.zip s3://markgeronimo.net/lambda.zip

## Create dynamodb table
- create users table
- add id as primary key

## SETUP lambda
- create lambda function
- upload file from S3 (ex. s3://markgeronimo.net/lambda.zip)
- create lambda role to access dynamodb

## SETUP API Gateway
- create api gateway
- create POST resource
- point to lambda function
- check lambda proxy
- test
- deploy api