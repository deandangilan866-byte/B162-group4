# Google Ad Exchange Buyer API Integration with FastAPI

## ITP 322 – Systems Integration and Architecture 2

### B162 – Group 4

---

# Project Title

FastAPI Integration with Google Ad Exchange Buyer API

---

# Project Description

This project demonstrates the integration of a cloud-based advertising service into a FastAPI backend application. The system connects to the Google Ad Exchange Buyer API to retrieve and manage information related to advertising buyers and bidding data.

The API allows authorized users to request advertising account data through secure FastAPI endpoints. The system also implements API authentication and rate limiting to protect the service from unauthorized access and excessive usage.

This project shows how cloud APIs can be integrated into modern backend systems while maintaining security, performance, and proper request management.

---

# Features

• Integration with Google Ad Exchange Buyer API
• Secure API access using API Key Authentication
• Rate limiting to prevent abuse of the API
• Structured REST API endpoints
• Error handling and validation
• Interactive testing through FastAPI Swagger UI

---

# Technologies Used

Python
FastAPI
Google Authorized Buyers API
Uvicorn
SlowAPI (Rate Limiting)
Python-dotenv

---

# Prerequisites

Before running the application, ensure the following are installed:

Python 3.9 or higher
pip package manager
Google Cloud account
Authorized Buyers API enabled in Google Cloud

You also need a **Google Cloud Service Account JSON credential file**.

---

# Project Folder Structure

google-adexchange-fastapi

app
    main.py
    auth.py
    limiter.py
    buyer_service.py

credentials
    service-account.json

.env
requirements.txt
README.md
.gitignore

---

# Installation Instructions

## 1 Clone the Repository

git clone https://github.com/deandangilan866-byte/B162-group4

cd group 4 B162

---

## 2 Install Dependencies

Install required Python libraries.

pip install -r requirements.txt

Or install manually:

pip install fastapi uvicorn google-api-python-client python-dotenv slowapi

---

# Google Cloud Setup

## Step 1 Create a Google Cloud Project

Go to:

https://console.cloud.google.com

Create a new project.

Example:

Project Name: Group4 AdExchange API

---

## Step 2 Enable Authorized Buyers API

Navigate to:

APIs & Services → Library

Search for:

Authorized Buyers API

Enable the API.

---

## Step 3 Create a Service Account

Navigate to:

IAM & Admin → Service Accounts

Click **Create Service Account**

Example:

Service Account Name: adexchange-api

Assign a role appropriate for accessing the API.

Click **Done**.

---

## Step 4 Generate Credentials

Open the Service Account

Keys → Add Key → Create New Key

Select **JSON**

Download the file.

Place the file inside the project:

credentials/service-account.json

---

# Environment Configuration

Create `.env` file.

Example configuration:

API_KEY=group4securekey
GOOGLE_APPLICATION_CREDENTIALS=credentials/service-account.json

---

# Running the Application

Start the FastAPI server:

uvicorn app.main:app --reload

Then open:

http://127.0.0.1:8000/docs

This opens FastAPI Swagger documentation where endpoints can be tested.

---

# API Endpoints

## 1 System Status

GET /

Description
Checks if the API server is running.

Response Example

{
"message": "Google Ad Exchange Buyer API Service Running"
}

---

## 2 Get Buyer Accounts

GET /buyers

Description
Retrieves information about advertising buyer accounts from Google Ad Exchange.

Headers

x-api-key: group4securekey

Response Example

{
"buyer_account": "example_buyer",
"status": "active"
}

---

# Authentication Implementation

The API uses **API Key Authentication**.

Each request must include an API key in the header.

Example header:

x-api-key: group4securekey

If authentication fails, the system returns:

401 Unauthorized

This ensures that only authorized users can access the API.

---

# Rate Limiting

The system uses the SlowAPI library to implement request limits.

Limit configuration:

5 requests per minute per IP address.

If the user exceeds the limit, the API returns:

429 Too Many Requests

This prevents excessive use of the API.

---

# Testing Instructions

Start the server:

uvicorn app.main:app --reload

Open Swagger documentation:

http://127.0.0.1:8000/docs

Use the interface to test the endpoints.

Add the API key header before sending requests.

---

# Troubleshooting Guide

## Error: ModuleNotFoundError

Cause
Missing Python dependencies.

Solution

Run:

pip install -r requirements.txt

---

## Error: DefaultCredentialsError

Cause
Google credentials file not found.

Solution

Ensure the file exists in:

credentials/service-account.json

Check `.env` configuration.

---

## Error: 401 Unauthorized

Cause
Invalid API key.

Solution

Verify header:

x-api-key: group4securekey

---

## Error: 429 Too Many Requests

Cause
Rate limit exceeded.

Solution

Wait one minute before sending another request.

---

## Error: API Not Enabled

Cause
Authorized Buyers API not enabled.

Solution

Go to:

Google Cloud Console → APIs & Services → Library

Enable **Authorized Buyers API**.

---

## Error: Billing Required

Cause
Google Cloud APIs require billing to be enabled.

Solution

Activate Google Cloud free trial to receive $300 credits.

---

# Demonstration Flow

During the presentation:

1 Start the FastAPI server
2 Open Swagger documentation
3 Call the /buyers endpoint
4 Show authentication using API key
5 Send multiple requests to demonstrate rate limiting
6 Explain how FastAPI communicates with the Google Ad Exchange API

---

# Team Members

Group 4 – B162

Dean Dangilan
Judith Patnaan
Jojo Taguitag
Gracelyn Tino
Bernadette Huag

---

# Contributions

Dean Dangilan – Backend development and API integration
Judith Patnaan – Documentation
Jojo Taguitag – Testing and debugging
Gracelyn Tino – Rate limiting implementation
Bernadette Huag – Presentation preparation

---

# License

This project is developed for academic purposes for the course ITP 322 – Systems Integration and Architecture 2.
