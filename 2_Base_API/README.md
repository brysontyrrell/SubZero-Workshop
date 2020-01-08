# SubZero Workshop

## Base API

With a pipeline in place, create the base API for the application. Your updates will automatically deploy as you push commits to GitHub.

### AWS Services / Features

- Serverless (SAM) Transform
- API Gateway
- Lambda

### Module Challenge

Add a second `AWS::Serverless::Function` resource to the template to create a `GET /images` endpoint. Use `/src/get_images` for the `CodeUri`. 

As an additional challenge update both Lambda function resources to use SAM's `Globals` feature.
