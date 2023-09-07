# CloudFront Cache Invalidator Lambda function that is triggered by S3 PUT events.
# It will invalidate the CloudFront cache for the object that was just uploaded to S3 after the code is deployed from CodePipeline.
# This lambda function will invalidate cache from two different CloudFront distributions.

import boto3
import os

s3 = boto3.client('s3')
cloudfront = boto3.client('cloudfront')


def lambda_handler(event, context):
    # Get the object from the event
    print("Event: ", event)
    print("Bucket: ", event['Records'][0]['s3']['bucket']['name'])
    
    bucket = event['Records'][0]['s3']['bucket']['name']
    print("The bucket name is: " + bucket)
        
    key = event['Records'][0]['s3']['object']['key']
    print("Key is: " + key)

    # Get the CloudFront distribution IDs from the environment variables
    distributionId1 = os.environ['DISTRIBUTION_ID_1']
    distributionId2 = os.environ['DISTRIBUTION_ID_2']

    # Create the CloudFront invalidation batch
    invalidationBatch = {
        'Paths': {
            'Quantity': 1,
            'Items': [
                '/' + key
            ]
        },
        'CallerReference': 'lambda-' + key
    }
    print("Invalidation batch is: " + str(invalidationBatch))

    # Invalidate the CloudFront cache for the objects that were just uploaded to S3
    cloudfront.create_invalidation(
        DistributionId=distributionId1,
        InvalidationBatch=invalidationBatch
    )
    cloudfront.create_invalidation(
        DistributionId=distributionId2,
        InvalidationBatch=invalidationBatch
    )

    return {
        'statusCode': 200,
        'body': 'Success'
    }