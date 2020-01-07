# SubZero Workshop

## Pipeline

Create a pipeline that will continuously build and deploy the application from your GitHub repository.

Use the [pipeline-template.yaml](pipeline-template.yaml) file to create a CloudFormation stack using the AWS console or the AWS CLI.

#### AWS CLI example:
```shell script
aws cloudformation deploy \
    --profile ${AWS_PROFILE_NAME} \
    --region ${AWS_REGION} \
    --template-file pipeline-template.yaml \
    --stack-name ${STACK_NAME} \
    --capabilities CAPABILITY_IAM \
    --parameter-overrides \
        RepositoryOwner=${GITHUB_ACCOUNT_NAME} \
        RepositoryName=${GITHUB_REPOSITORY_NAME} \
        GitHubToken=${GITHUB_TOKEN} \
        AppName=${APP_NAME} \
        DeploymentRegion1=${AWS_REGION}
```

Once the stack has been created CodePipeline will automatically run and create an empty CloudFormation stack for the application.

A webhook will be automatically registered with your GitHub repository. All commits to your `master` branch going forward will trigger your pipeline.

### AWS Services / Features

- CloudFormation
- CodePipeline
- CodeBuild

### Module Challenge

Update your pipeline to deploy to a second region in the US. Target the secondary AWS region assigned to you. You will need to make the following modifications to the template before updating the CloudFormation stack:

- `DeploymentRegion2` Parameter with the following allowed values:
  - us-east-2
  - us-west-1
  - us-west-2
- Add the `DeploymentRegion2` parameter to the `TARGET_REGIONS` environment variable of the `BuildProject`.
- Add an `ArtifactStore` for the new region to the `Pipeline`.
- Add a `Deployment` action for the new region.