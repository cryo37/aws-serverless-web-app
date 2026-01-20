# aws-serverless-web-app

📌 **AWS Power Math Web Application**

This is an end-to-end serverless web application built on AWS that calculates `base^exponent`, displays the result, and stores the result in a highly available DynamoDB table.

It demonstrates how multiple AWS services interact together to build a functional cloud application.

---

## 🚀 Features

✔ Frontend hosted on AWS Amplify  
✔ Backend served via API Gateway + Lambda  
✔ DynamoDB for persistent storage  
✔ IAM for secure access control  
✔ Fully serverless  
✔ Pay-per-use, no servers to manage  

---

## 🧰 Tech Stack

| Component | Service |
|---|---|
| Frontend hosting | AWS Amplify |
| API | AWS API Gateway |
| Compute (Math logic) | AWS Lambda (Python 3.9) |
| Database | DynamoDB |
| IAM | Lambda execution role |
| Language | Python / JS / HTML |

---

## 🏗 Architecture

User → Amplify → API Gateway → Lambda → DynamoDB

<img width="927" height="475" alt="Image" src="https://github.com/user-attachments/assets/8b8c9482-147d-4018-9404-426773a289e6" />

---

## 🔁 Workflow

1. User enters base & exponent in web UI  
2. Amplify hosts static HTML  
3. API Gateway exposes a POST endpoint  
4. Lambda calculates `base^exponent`  
5. Result stored in DynamoDB  
6. Response sent back to UI  

---

## 📁 Repository Structure
```
frontend/
    index.html
lambda/
    power-math.py
architecture/
    power-math.png
IAM Permission/
    IAM policy for Lambda's Execution Role.txt
README.md


---

## 🎥 Demo Video

*Click to view:*  
https://drive.google.com/file/d/1rLJ9TDEI4K54KawP33tYP0q2Pwm_P2Cc/view?usp=sharing
---

## 🛠 AWS Deployment Steps (Short)

- Host HTML on Amplify
- Create a REST API in API Gateway
- Create Lambda function (Python 3.9)
- Create DynamoDB table
- Add IAM permissions for DynamoDB 
- Connect components

---

## 💰 Costs

- DynamoDB: On-demand tiny usage
- API Gateway/Lambda: Free tier friendly
- Amplify Hosting: Free tier OK for static hosting

---

## 🧠 Lessons Learned

- How services integrate in serverless architectures
- IAM roles & permissions matter for security
- Serverless apps scale automatically

---

## 🚀 Future Enhancements

- Add login via Cognito
- Display history of results
- Containerize Lambda via Docker
- Monitor usage via CloudWatch metrics

