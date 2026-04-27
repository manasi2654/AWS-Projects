# 🌐 Use SDK to Automate Static Web Hosting (Amazon S3 + boto3)

## 📌 Project Overview

This project demonstrates two methods of hosting a static website on AWS:

1. **Manual Method** – Creating an S3 bucket and uploading website files through AWS Console.  
2. **Automated Method** – Using **Python boto3 SDK** to create the bucket, upload files, and enable hosting automatically.

The project highlights how automation reduces manual effort and speeds up deployments.

---

## 🎯 Objectives

* Host a static website on Amazon S3  
* Understand manual deployment using AWS Console  
* Automate deployment using Python SDK (boto3)  
* Compare manual vs automated workflow  
* Build scalable and low-cost hosting solution  

---

## 🧰 AWS Services Used

* Amazon S3 (Static Website Hosting)  
* boto3 (AWS SDK for Python)  
* IAM (Access Management)  
* AWS CLI (Credential Setup)  

---

## 🏗️ Architecture

### 🔹 Architecture Diagram (Simplified)

```text
Website Files
   │
   ├── Manual Upload (AWS Console)
   │
   └── Python Script (boto3)
            │
            ▼
      Amazon S3 Bucket
            │
            ▼
   Static Website Hosting
            │
            ▼
      Public Website URL


🔄 Architecture Flow
Website Files → S3 Bucket → Static Hosting Enabled → Public Access

⚙️ Implementation Steps
🔹 Method 1: Manual Deployment (AWS Console)
Step 1: Create S3 Bucket
Open AWS Console → S3

Click Create Bucket

Enter unique bucket name

Create bucket

Step 2: Disable Public Access Block
Open bucket permissions

Disable block public access

Step 3: Upload Website Files
Upload:

index.html

style.css

Step 4: Enable Static Website Hosting
Go to bucket Properties

Enable Static Website Hosting

Set index document:


index.html
Step 5: Add Bucket Policy
Allow public read access.

Step 6: Access Website
Use generated S3 website endpoint URL.
