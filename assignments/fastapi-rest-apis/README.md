# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a RESTful API using the FastAPI framework to practice defining routes, handling JSON requests and responses, validating data models, and implementing CRUD operations.

## 📝 Tasks

### 🛠️ Create the FastAPI application and CRUD endpoints

#### Description
Implement a FastAPI application that manages a collection of books. Create endpoints for listing books, retrieving a book by ID, creating new books, updating existing books, and deleting books.

#### Requirements
Completed program should:

- Use FastAPI to define the application and route handlers
- Implement `GET /books` to return all books
- Implement `GET /books/{book_id}` to return a single book by its ID
- Implement `POST /books` to add a new book
- Implement `PUT /books/{book_id}` to update an existing book
- Implement `DELETE /books/{book_id}` to remove a book
- Use JSON for request and response bodies
- Return a 404 error when a book is not found

### 🛠️ Add Pydantic models for validation

#### Description
Use Pydantic models to validate incoming request data and define the response structure. Ensure the API accepts only valid book data.

#### Requirements
Completed program should:

- Define a Pydantic model for creating books with fields such as `title`, `author`, `pages`, and `available`
- Define a Pydantic response model that includes a book `id`
- Use the appropriate request and response models on each endpoint
- Validate that `title` and `author` are non-empty strings and `pages` is a positive integer

### 🛠️ Test and document the API

#### Description
Run the FastAPI app and verify the endpoints using example requests. Document example request payloads and expected responses.

#### Requirements
Completed program should:

- Include example request bodies for creating and updating books
- Show how to run the app with `uvicorn`
- Confirm that the API returns JSON responses for each endpoint
- Demonstrate both successful and error responses in the documentation