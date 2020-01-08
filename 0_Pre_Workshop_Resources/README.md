# SubZero Workshop

## Pre-Workshop Resources

These are resources that were created in the AWS account prior to the start of the workshop. The templates are provided to you here for your reference and are not meant to be deployed again.

### StackSet Roles

The [StackSet Roles](stackset-roles-template.yaml) template creates two IAM roles that are required when using StackSets: a feature to create CloudFormation stacks across multiple accounts and regions.

### Artifact Buckets

In single-region deployments a pipeline template can create its own S3 bucket to use for artifacts. In multi-region deployments it easier to handle the replication of build artifacts to those regions if the buckets follow a naming convention.

The [Artifact Buckets](artifact-buckets.yaml) template creates a S3 bucket in a region using the following patter:

```text
subzero-workshop-${AWS::Region}-${AWS::AccountId}
```

S3 bucket names must be globally unique across all regions and all AWS accounts in existence. Appending the region name and the account ID ensures uniqueness and is easily replicated in other CloudFormation stacks.

### Shared Cognito User Pool

During this workshop you will secure your API Gateways using AWS Cognito. There is a per region limit of 5 Cognito User Pools. To avoid this there will be a single [Shared Cognito User Pool](shared-cognito-pool-template.yaml) for the workshop configured for the domain.

### Parameters

There are some values that need to be available to CloudFormation stacks across all regions supported in the workshop. These values have been populated into SSM Parameter Store using a StackSet (just as the artifact buckets).

> The `RegionalCertificateArnParameter` is populated by an inline Lambda function that executes as a part of the CloudFormation stack. StackSets do not support transforms (like `AWS::Serverless-2016-10-31`) so the Lambda function and its IAM role are standard CloudFormation resources.
