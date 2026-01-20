import json
import math

import boto3
from time import gmtime, strftime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('PowerOfMathTable')

now = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

# the handler function that the Lambda service will use an entry point
def lambda_handler(event, context):

# extract the two numbers from the Lambda service's event object
    mathResult = math.pow(int(event['base']), int(event['exponent']))

# write result and time to the DynamoDB table using the object we instantiated and save response in a variable
    response = table.put_item(
        Item={
            'ID': str(mathResult),
            'LatestGreetingTime':now
            })

# returning the ebj
    return {
    'statusCode': 200,
    'body': json.dumps('Your result is ' + str(mathResult))
    }

