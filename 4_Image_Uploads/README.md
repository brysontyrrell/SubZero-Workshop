# SubZero Workshop

## Image Uploads

Lambda functions associated with the API Gateway endpoints will now process uploaded images and return data about those uploaded images.

Each Lambda function servers a specific purpose. `Upload` accepts an image file and writes it to an S3 bucket. The `List` function returns a JSON array of all the uploaded files.

### AWS Services / Features

- S3
- IAM

### Module Challenge

The `GET /api/images` endpoint is not functioning. Compare the `List` Lambda function resource to the `Upload` functionn and add the missing elements required to grant S3 read permissions.

Reference the [SAM Policy Templates](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-policy-templates.html) documentation to find the appropriate role.

As an additional challenge make use of SAM's `Globals` feature.

### Next Module: [Image Processing](../5_Image_Processing/)

Once instructed, move on to the next module and update your repository with the provided files (overwrite existing files and your changes).
