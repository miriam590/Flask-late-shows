## Lateshow API — Flask Application

## Overview
This is a Flask-based RESTful API for tracking Late Show episodes, guests, and their appearances. The API allows clients to retrieve episode and guest data, and create new guest appearances with ratings

### Relationships Between Entities:
- An **Episode** has many **Guests** through **Appearances**.
- A **Guest** appears in many **Episodes** through **Appearances**.
- An **Appearance** belongs to both an **Episode** and a **Guest**.

The project uses:
- **Flask-SQLAlchemy** for database management.
- **SQLAlchemy SerializerMixin** for serialization.
- **Flask-Migrate** for database migrations.

### Imports Necessary Libraries:
- `flask_sqlalchemy.SQLAlchemy` for ORM and database operations.
- `sqlalchemy.orm.validates` for validation logic.
- `sqlalchemy_serializer.SerializerMixin` for automatic serialization.
- `flask_migrate.Migrate` for database migrations.

### Imports Necessary Modules:
- `Flask` for creating the application.
- `jsonify` and `request` for handling HTTP requests and responses.
- `Migrate` for database migrations.
- Models (`db`, `Episode`, `Guest`, `Appearance`) from `models.py`.

---

## Endpoints:

### 1. **GET /episodes** - List all episodes:
- Retrieves all episodes from the database.
- Serializes each episode using `to_dict()` and returns them as JSON.

### 2. **GET /episodes/<int:id>** - Get episode details:
- Retrieves a specific episode by its ID.
- If the episode does not exist, returns a `404 Not Found` error.
- Serializes the episode and includes its appearances in the response.

### 3. **GET /guests** - List all guests:
- Retrieves all guests from the database.
- Serializes each guest using `to_dict()` and returns them as JSON.

### 4. **GET /guests/<int:guest_id>** - Get guest details:
- Retrieves a specific guest by their ID.
- If the guest does not exist, returns a `404 Not Found` error.
- Serializes the guest using `to_dict()` and returns it as JSON.

### 5. **POST /appearances** - Create a new appearance:
- Accepts a POST request to create a new appearance.
- Validates the input data:
  - Ensures the rating is between 1 and 5.
  - Ensures `episode_id` and `guest_id` are provided and valid.
- Creates a new **Appearance** record and commits it to the database.
- Returns the created appearance with details of the episode and guest in the response.

---

## HTTP Status Codes:

- **200 OK**: Request successful.
  - `GET /episodes`
  - `GET /guests`
  - `GET /guests/<int:guest_id>`

- **201 Created**: Resource successfully created.
  - `POST /appearances`

- **400 Bad Request**: Invalid data.
  - Missing fields or invalid rating in `POST /appearances`.

- **404 Not Found**: Resource not found.
  - Non-existent episode or guest in `GET /episodes/<int:id>`, `GET /guests/<int:guest_id>`, or `POST /appearances`.

---

## How to Run the Project:
1. Install dependencies using `pipenv install`.
2. Activate the virtual environment using `pipenv shell`.
3. Run the application:
   ```bash
   flask run