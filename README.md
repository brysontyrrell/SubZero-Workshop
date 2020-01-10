# SubZero Workshop

In this workshop you will create a continuously delivered serverless application that accepts, processes, and stores images using a variety of AWS services.

![](images/Application-Diagram.png)

## Resources

- [Serverless Application Model Documentation](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html)
- [Serverless Application Model Template Specification](https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md)

## Modules

The workshop is split across 6 modules over the course of the day. Each module will include a brief lecture, guided hands on activity, and challenges. At the start of a module copy the contents of the directory into your working repository as directed by the workshop leads.

All challenges revolve around modifying CloudFormation templates and resources - you are not required to know or write Python as a part of this workshop. If you do complete the challenges it is recommended you copy the files for the next module and overwrite your changes.

### Introduction and Setup (10:00 - 10:15 / 15 min)

Get setup and ready for the workshop.

### [Pipeline](1_Pipeline/) (10:15 - 11:00 / 45 min)

Create a pipeline for building and deploying the serverless application automatically on commits.

### [Base API](2_Base_API/) (11:00 - 11:45 / 45 min)

Update the template to create the base API Gateway and its Lambda functions.

### [Cognito](3_Cognito/) (11:45 - 12:00 / 15 min)

Secure access to the API Gateway using Cognito.

### Lunch (12:00 - 1:00)

### [Image Uploads](4_Image_Uploads/) (1:00 - 2:00 / 1 hr)

Update the API to accept image files and save them to a S3 bucket.

### [Image Processing](5_Image_Processing/) (2:00 - 3:00 / 1 hr)

Process uploaded images and record them to a DynamoDB table.

### [Monitoring](6_Monitoring/) (3:00 - 4:00 / 1 hr)

View metrics and set alerts using X-Ray and CloudWatch.

### Bonus Challenges

Use the remaining workshop time to ask questions and extend the service.

