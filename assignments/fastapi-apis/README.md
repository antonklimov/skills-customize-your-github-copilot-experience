# 📘 Assignment: Building REST APIs with FastAPI framework

## 🎯 Objective

Learn how to build RESTful APIs using the FastAPI framework. Students will create a simple API with routes for creating, reading, updating, and deleting resources, and learn how to run the server and test endpoints.

## 📝 Tasks

### 🛠️ Create a CRUD API with FastAPI

#### Description
Build a small REST API for managing a collection of items (for example, books or todos). The API should expose endpoints to create, list, retrieve, update, and delete items. Use in-memory storage (a Python list or dict) for simplicity.

#### Requirements
Completed project should:

- Use FastAPI to define the API and routes
- Provide endpoints: `GET /items`, `GET /items/{id}`, `POST /items`, `PUT /items/{id}`, `DELETE /items/{id}`
- Validate request and response data using Pydantic models
- Return appropriate HTTP status codes (201 for create, 404 for not found, etc.)
- Include clear README instructions on how to run the server and test endpoints

### 🛠️ Testing the API (Optional)

#### Description
Add simple tests or instructions for using `curl` or a tool like HTTPie/Postman to exercise the API.

#### Requirements

- Provide example requests for each endpoint in the README
- (Optional) Add a small test script using `requests` to exercise the endpoints
