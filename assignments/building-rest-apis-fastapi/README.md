# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a simple REST API using FastAPI by creating endpoints for health checks, listing resources, and creating new items with request validation.

## 📝 Tasks

### 🛠️ Create a FastAPI Application

#### Description
Create a new FastAPI app that serves a basic API for managing books or tasks.

#### Requirements
Completed program should:

- Create an instance of `FastAPI` with a descriptive title.
- Expose a `GET /health` endpoint that returns a JSON response with the API status.
- Run the app locally using Uvicorn or another compatible ASGI server.

### 🛠️ Build CRUD-style Endpoints

#### Description
Implement endpoints to list and create items in your API.

#### Requirements
Completed program should:

- Add a `GET /items` endpoint that returns a list of items in JSON format.
- Add a `POST /items` endpoint that accepts request data and returns the created item.
- Use appropriate status codes such as `200` for successful reads and `201` for successful creation.

### 🛠️ Validate Incoming Data

#### Description
Use Pydantic models to validate the shape of incoming requests.

#### Requirements
Completed program should:

- Define a request model with at least two fields, such as `name` and `description`.
- Ensure invalid requests are rejected with a helpful validation error.
- Return a clear JSON response for both successful and unsuccessful requests.

### 🛠️ Document the API

#### Description
Make the API easier to explore by using FastAPI’s built-in documentation features.

#### Requirements
Completed program should:

- Verify that the `/docs` page is available in the browser.
- Confirm that the API documentation shows the implemented routes.
- Include a short note in the project README explaining how to start the server.
