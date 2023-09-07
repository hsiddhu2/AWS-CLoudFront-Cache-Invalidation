import boto3
import json

codePipeline = boto3.client("codepipeline")
cloudFront = boto3.client("cloudfront")
systemManager = boto3.client("ssm")

def lambda_handler(event, context):
    job_id = event["CodePipeline.job"]["id"]
    print("Cache invalidation started for job: " + job_id)
    
    try:
        # {"distributionId": "string", "objectPaths": ["/*"]}
        userParams = event["CodePipeline.job"]["data"]["actionConfiguration"]["configuration"]["UserParameters"]
    
        print("User parameters: " + str(userParams))
        print("Parameter Name: " + userParams["distributionId"])

        # get the distributionId from ssm parameter store
        distributionId = systemManager.get_parameter(Name=userParams["distributionId"], WithDecryption=True)["Parameter"]["Value"]    
    
        # get the objectPaths from the userParamsJson and ssm parameter store
        objectPaths = userParams["objectPaths"]
        
        #invalidate the cache
        cloudFront.create_invalidation(
            DistributionId=distributionId,
            InvalidationBatch={
                'Paths': {
                    'Quantity': len(objectPaths),
                    'Items': objectPaths
                },
                'CallerReference': 'hpythonn.com CodePipeline InvalidateCache'
            }
        )
        print("Cache invalidation completed for job " + job_id)
    except Exception as e:
        print("Error: " + str(e))
        codePipeline.put_job_failure_result(
            jobId=job_id,
            failureDetails={
                'type': 'JobFailed',
                'message': str(e)
            }
        )
        raise e
    
    
    
    
    