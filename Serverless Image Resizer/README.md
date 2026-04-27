🚀 Serverless Image Resizer (S3 + Lambda) – 

📌 Project Overview

This project builds a serverless image resizing pipeline using Amazon Web Services where images uploaded to S3 are automatically resized using AWS Lambda and stored back in the same bucket.

🎯 Objective
Automate image resizing on upload
Use event-driven architecture
Avoid server management
Build a scalable cloud solution

⚙️ Step-by-Step Implementation
🧱 Step 1: Create S3 Bucket
Go to AWS Console → S3
Click Create Bucket
Provide a unique bucket name
Keep default settings and create
🧱 Step 2: Create IAM Role for Lambda
Go to IAM → Roles → Create Role
Select AWS Service → Lambda
Attach policies:
AmazonS3FullAccess (for learning/demo)
AWSLambdaBasicExecutionRole
Create role
🧱 Step 3: Create Lambda Function
Go to Lambda → Create Function
Choose Author from scratch
Select runtime: Python 3.x
Attach the IAM role created earlier
🧱 Step 4: Prepare Deployment Package
Open AWS CloudShell (recommended)
Create a working directory
Install required image processing library (Pillow)
Add your Lambda function file
Compress everything into a ZIP file
🧱 Step 5: Upload Code to Lambda
Go to Lambda → Code section
Upload the ZIP file
Set correct handler name
Click Deploy
🧱 Step 6: Configure S3 Trigger
Go to S3 bucket → Properties
Scroll to Event Notifications
Create new event:
Event type: PUT (Object Created)
Destination: Lambda function
Save configuration
🧱 Step 7: Configure Permissions (If Needed)
Ensure Lambda role has permission to:
Read objects from S3
Write objects to S3
🧪 Step 8: Test the System
Upload an image file to S3 bucket
Wait for Lambda to trigger automatically
Check the same bucket for resized image
📊 Expected Result
Original image remains unchanged
New resized image is created with modified filename
⚠️ Common Issues
Lambda not triggering → Check S3 event configuration
Import errors → Dependency not packaged correctly
Access denied → IAM role missing permissions
Infinite loop → Output file triggering Lambda again
🧠 Key Concepts Learned
Serverless architecture
Event-driven processing
AWS Lambda execution flow
S3 event notifications
Cloud-based image processing
