# User Management API

This project implements a set of APIs for user registration, login, linking an ID, and providing join and chain delete functionalities using Python and MongoDB. It uses the FastAPI framework for the web application and PyMongo for MongoDB interaction.

## Requirements

1. **Framework and Libraries:**
   - FastAPI for the web framework.
   - PyMongo for interacting with MongoDB.

2. **API Endpoints:**
   - **Registration API:** Endpoint to register a new user.
   - **Login API:** Endpoint to authenticate an existing user.
   - **Linking ID API:** Endpoint to link an ID to a user's account.
   - **Joins:** Functionality to join data from multiple collections.
   - **Chain Delete:** Functionality to delete a user and all associated data across collections.

3. **Database:**
   - MongoDB to store user information.

## Setup Instructions

### Prerequisites

- Python 3.7+
- MongoDB instance (local or cloud)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/user-management-api.git
   cd user-management-api
   ```

2. **Create a virtual environment and activate it:**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Setup environment variables:**
   - Create a `.env` file in the project root directory.
   - Add the following environment variables:
     ```
     MONGO_URI="your_mongodb_connection_string"
     SECRET_KEY="your_secret_key_for_jwt"
     ```

### Running the Application

1. **Start the FastAPI application:**
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the API documentation:**
   - Open your browser and go to `http://127.0.0.1:8000/docs` to see the interactive API documentation provided by FastAPI.

## API Endpoints

### Registration API

- **Endpoint:** `/register`
- **Method:** `POST`
- **Description:** Registers a new user.
- **Request Body:**
  ```json
  {
    "username": "string",
    "email": "string",
    "password": "string"
  }
  ```
- **Response:**
  - `201 Created`: User registered successfully.
  - `400 Bad Request`: Invalid input or user already exists.

### Login API

- **Endpoint:** `/login`
- **Method:** `POST`
- **Description:** Authenticates an existing user.
- **Request Body:**
  ```json
  {
    "email": "string",
    "password": "string"
  }
  ```
- **Response:**
  - `200 OK`: Returns a JWT token.
  - `401 Unauthorized`: Invalid credentials.

### Linking ID API

- **Endpoint:** `/link-id`
- **Method:** `POST`
- **Description:** Links an ID to a user's account.
- **Request Body:**
  ```json
  {
    "user_id": "string",
    "external_id": "string"
  }
  ```
- **Response:**
  - `200 OK`: ID linked successfully.
  - `400 Bad Request`: Invalid input.

### Joins

- **Endpoint:** `/join-data`
- **Method:** `GET`
- **Description:** Retrieves joined data from multiple collections.
- **Response:**
  - `200 OK`: Returns the joined data.
  - `400 Bad Request`: Invalid request.

### Chain Delete

- **Endpoint:** `/delete-user`
- **Method:** `DELETE`
- **Description:** Deletes a user and all associated data across collections.
- **Request Body:**
  ```json
  {
    "user_id": "string"
  }
  ```
- **Response:**
  - `200 OK`: User and associated data deleted successfully.
  - `400 Bad Request`: Invalid input.
