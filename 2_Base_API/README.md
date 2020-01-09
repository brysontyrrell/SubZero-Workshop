# SubZero Workshop

## Pipeline Update

Update your pipeline using [pipeline-template.yaml](pipeline-template.yaml) before continuing.

## Base API

With a pipeline in place, create the base API for the application. Your updates will automatically deploy as you push commits to GitHub.

### AWS Services / Features

- Serverless (SAM) Transform
- API Gateway
- Lambda
- Route 53

### Module Challenge

Add a second `AWS::Serverless::Function` resource to the template to create a `GET /api/images` endpoint. Use `/src/get_images` for the `CodeUri`. 

As an additional challenge update both Lambda function resources to use SAM's `Globals` feature.

### Next Module: [Cognito](../3_Cognito/)

Once instructed, move on to the next module and update your repository with the provided files (overwrite existing files and your changes).
