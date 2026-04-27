# 🚀 Serverless Image Resizer (Amazon S3 + AWS Lambda)

## 📌 Project Overview

This project implements a **serverless image processing pipeline** using **Amazon S3** and **AWS Lambda**.  

Whenever a user uploads an image into an S3 bucket, an event automatically triggers a Lambda function that resizes the image and stores the processed version back into the same bucket (or another output folder).

This solution is scalable, cost-effective, and requires **no server management**.

---

## 🎯 Objective

- Automatically resize images after upload
- Use event-driven cloud architecture
- Eliminate infrastructure management
- Build a scalable media processing workflow
- Reduce manual image optimization tasks

---

## 🧰 AWS Services Used

- **Amazon S3** – Stores original and resized images
- **AWS Lambda** – Processes and resizes uploaded images
- **IAM** – Manages permissions for Lambda
- **CloudWatch Logs** – Monitors execution logs
- **AWS CloudShell** – Used to package dependencies

---

## 🏗️ Architecture

```text
User Uploads Image
        ↓
Amazon S3 Bucket
        ↓
S3 PUT Event Trigger
        ↓
AWS Lambda Function
        ↓
Resize Image using Pillow
        ↓
Save Resized Image to S3

## ⚙️ Implementation Steps

### Step 1: Create S3 Bucket
- Open AWS Console → S3  
- Create a new bucket with a unique name  
- Keep default settings  

### Step 2: Create IAM Role
- Go to IAM → Roles  
- Create role for Lambda  
- Attach permissions:
  - AmazonS3FullAccess  
  - AWSLambdaBasicExecutionRole  

### Step 3: Create Lambda Function
- Open AWS Lambda  
- Create new function  
- Choose Python runtime  
- Attach IAM role  

### Step 4: Add Lambda Code
- Upload deployment package with Pillow library  
- Add Python code for image resizing  
- Deploy function  

### Step 5: Configure S3 Trigger
- Open S3 bucket → Properties  
- Create Event Notification  
- Select **Object Created (PUT)**  
- Set destination as Lambda function  

### Step 6: Test the Project
- Upload an image to S3 bucket  
- Lambda automatically resizes image  
- Resized image stored in output folder  

---

## 📂 Workflow

```text
Upload Image → S3 Bucket → Trigger Lambda → Resize Image → Save Resized Image

