# SubZero Workshop

## Pipeline Update

Update your pipeline using [pipeline-template.yaml](pipeline-template.yaml) before continuing.

## Image Processing

A Step Function on the backend will not take uploaded image files and process them. This will include de-duplicating images, creating additional resized versions, and linking the uploaded user to the file in a DynamoDB table.

The `List` Lambda function now queries the DynamoDB table only for files associated to the authenticated client instead of scanning the S3 bucket.

### AWS Services / Features

- DynamoDB
- Global DynamoDB Tables
- SQS
- Step Functions

### Module Challenge

Add additional states to the `StateMachine` JSON definition for the following image sizes: 512 and 256. Use the 1024 state as a baseline and modify as needed.

### Next Module: [Monitoring](../6_Monitoring/)

Once instructed, move on to the next module and update your repository with the provided files (overwrite existing files and your changes).
