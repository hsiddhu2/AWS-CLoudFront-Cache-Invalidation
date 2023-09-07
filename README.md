
# 4 Different Ways To Invalidate CloudFront Cache

👋 Welcome to the repository for the code related to managing CloudFront cache invalidation. In this README, we'll explore various methods to invalidate the CloudFront cache for your AWS S3-based static website. These methods include using Lambda Actions in CodePipeline, S3 Events triggering AWS Lambda, configuring a buildspec.yml in the CodeBuild stage, and employing a shell script.


## 🙋‍♂️ Introduction

In the static website hosting using CI/CD, we created a CloudFront distribution with caching enabled to deliver content efficiently to users from CloudFront edge locations. As part of our architecture, we integrated a CI/CD pipeline to deploy changes to the S3 bucket (Origin) automatically whenever new changes became available in the version control system (CodeCommit). The default caching policy retained content in the cache for up to 24 hours (TTL).

**Problem to Fix:** We face the challenge of invalidating the CloudFront cache whenever new changes are added to the S3 bucket.

## 🛠️ Overview

This repository provides code and configurations for four different approaches to invalidate the CloudFront cache:

1. **Using Lambda Actions in CodePipeline:** Configure AWS Lambda functions within your CodePipeline to automatically trigger cache invalidation when changes are detected. Use `src\invalidateCache-LambdaActions.py` and add it after the CodeDeploy stage in your CodePipeline.
   

2. **Using S3 Events to Trigger AWS Lambda:** Utilize S3 events to automatically invoke AWS Lambda functions, ensuring that CloudFront cache is invalidated whenever new objects are added or updated in your S3 bucket. This method will allow you to invalidate the object being added to the S3 bucket. Use `src\invalidateCache-S3Events.py` and add it to your AWS Lambda function.

3. **Using buildspec.yml in the CodeBuild Stage:** Incorporate cache invalidation into your CodeBuild process by defining cache invalidation commands in the buildspec.yml file. Use `src\invalidateCache-buildspec.yml` and add it as a CodeBuild stage in your CodePipeline.

4. **Using a Shell Script:** Manually invalidate the CloudFront cache by running a shell script, which communicates with the AWS CLI to trigger cache invalidation. Run `src\invalidateCache.sh` in your terminal to invalidate the CloudFront cache.


Feel free to explore each method according to your requirements and preferences. I hope this repository helps you efficiently manage cache invalidation for your AWS S3-hosted static website served through CloudFront. If you find this repository useful, please give it a star ⭐ and share it with your friends and colleagues. Also, if you find a new method to invalidate the CloudFront cache, please feel free to contribute to this repository.

Happy Coding! 🚀🌐 

**Author:** [Harry Singh](https://www.linkedin.com/in/harpreetsiddhu/)

**Read Full Blog Here:** [4 Different Ways To Invalidate CloudFront Cache](https://www.medium.com/@harrysiddhu) 

**Disclaimer:** This repository is provided for educational purposes, and you should adapt the code and configurations to your specific needs and security requirements.
