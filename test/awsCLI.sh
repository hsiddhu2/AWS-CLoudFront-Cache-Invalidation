# Shell script to Invalidate CloudFront Cache using AWS CLI

#!/bin/bash

# Get the distribution ID from CloudFront console
echo "Get the distribution ID from CloudFront console"
distribution_ids=$(aws cloudfront list-distributions --query "DistributionList.Items[].{Id:Id}" --output text)
echo "The current disbributions are: $distribution_ids"

# Loop through the distribution IDs and run the command to invalidate cache without waiting for the command to complete

for distribution_id in $distribution_ids
do 
    aws cloudfront create-invalidation --distribution-id $distribution_id --paths "/*" &
    echo "Completed running Invalidate cache for distribution ID: $distribution_id"
done

