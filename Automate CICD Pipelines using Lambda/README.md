# 🚀 Automate CI/CD Pipelines using AWS Lambda

## 📌 Project Title
**Automate CI/CD Pipelines using Lambda**

---

## 🎯 Purpose

The purpose of this project is to automate software deployment workflows by integrating **AWS Lambda** with **AWS CodePipeline**.  

Whenever a trigger event occurs (such as code commit, file upload, or scheduled event), AWS Lambda automatically starts or manages the CI/CD pipeline, reducing manual effort and enabling faster deployments.

This project demonstrates how serverless automation can improve DevOps efficiency.

---

## 🧰 AWS Services Used

- **AWS Lambda** – Executes serverless automation logic
- **AWS CodePipeline** – Manages CI/CD workflow
- **IAM** – Provides secure access permissions
- **CloudWatch Logs** – Monitors Lambda execution
- **Amazon S3 / CodeCommit / GitHub** *(optional source)* – Source code repository

---

## 🏗️ Architecture

```text
Developer Pushes Code
        ↓
Source Repository (GitHub / CodeCommit / S3)
        ↓
AWS Lambda Triggered
        ↓
Lambda Starts CodePipeline
        ↓
Build Stage (CodeBuild)
        ↓
Deploy Stage (EC2 / S3 / Elastic Beanstalk)
📂 Project Workflow
Step 1️⃣ Create AWS CodePipeline
Open AWS Console

Search CodePipeline

Click Create Pipeline

Enter Pipeline Name:


My-CICD-Pipeline
Select source provider:

GitHub

CodeCommit

S3

Add Build Stage (optional CodeBuild)

Add Deploy Stage:

EC2

S3

Elastic Beanstalk

Create Pipeline

Step 2️⃣ Create IAM Role for Lambda
Go to IAM → Roles → Create Role

Choose:


AWS Service → Lambda
Attach Policy:

JSON

AWSCodePipelineFullAccess
CloudWatchLogsFullAccess
Role Name:


LambdaCodePipelineRole
Step 3️⃣ Create Lambda Function
Open AWS Lambda

Click Create Function

Choose:


Author from Scratch
Function Name:


TriggerPipelineFunction
Runtime:


Python 3.x
Execution Role:


Use Existing Role → LambdaCodePipelineRole
Step 4️⃣ Add Lambda Code
Python


Run
import boto3

def lambda_handler(event, context):
    
    client = boto3.client('codepipeline')
    
    response = client.start_pipeline_execution(
        name='My-CICD-Pipeline'
    )
    
    return {
        'statusCode': 200,
        'body': 'Pipeline Triggered Successfully'
    }
Step 5️⃣ Deploy Lambda
Click:


Deploy
Step 6️⃣ Test Lambda Function
Create Test Event:

JSON

{}
Click:


Test
✅ Expected Output

Pipeline Triggered Successfully
And in AWS CodePipeline:


Execution Started
📊 Monitoring
Use:

CloudWatch Logs
Check:

Lambda execution logs

Errors

Trigger history

🔐 Security Best Practices
Use least privilege IAM roles

Restrict Lambda permissions

Enable CloudTrail logging

Encrypt pipeline artifacts in S3

💡 Real-World Use Cases
🔹 Auto Deployment after Code Push
When developer pushes code to GitHub, Lambda starts pipeline automatically.

🔹 Nightly Build Trigger
Use EventBridge schedule + Lambda to run pipeline every night.

🔹 Multi-Environment Deployment
Lambda can trigger different pipelines:

Dev

QA

Production

📁 Project Structure

Automate-CICD-Lambda/
│── lambda_function.py
│── README.md
🧪 Sample Output

START RequestId: xxxx
Pipeline Triggered Successfully
END RequestId: xxxx
🚀 Advantages
Fully automated deployments

No server management

Faster release cycle

Reduced manual intervention

Scalable and cost-effective

📚 Future Enhancements
Add SNS notifications

Slack alerts after deployment

Rollback on failure

Multi-region deployments

Approval stage before production

👩‍💻 Author
Manasi Patil
AWS DevOps / Cloud Project

