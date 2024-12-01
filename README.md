
# FastAPI + MySQL Docker Compose Setup

This repository provides a Docker Compose configuration to set up a FastAPI application with a MySQL database. The database and required tables are initialized using SQL scripts on container startup.

---

## Features

- **FastAPI**: The backend framework running in a Docker container.
- **MySQL**: Database container with persistence and auto-initialization.
- **Docker Compose**: Streamlined container orchestration.
- **Network Isolation**: Services are isolated on a custom bridge network.

---

## Requirements

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

---

## Getting Started

### 1. Clone the Repository

```bash
git clone <repository-url>
cd <repository-folder>
```

### 2. Project Structure

```plaintext
project/
│
├── docker-compose.yml         # Docker Compose configuration
├── init-scripts/              # Directory for SQL initialization scripts
│   └── init.sql               # SQL script to create the database schema
├── app/
│   └── main.py                # Your FastAPI application (to be created)
```

### 3. Initialization Script

Place the following SQL script in `init-scripts/init.sql` to create the `users` table in the `dbname` database:

```sql
USE dbname;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);
```

### 4. Run the Application

Build and start the containers using Docker Compose:

```bash
docker-compose up --build
```

---

## Services

### 1. **FastAPI** (`fastapi-app`)
- **Build Context**: `./`
- **Ports**: Exposes the application on `http://localhost:8000`
- **Environment Variables**:
  - `DB_USER`: MySQL username (default: `root`)
  - `DB_PASSWORD`: MySQL password (default: `password`)
  - `DB_HOST`: MySQL service hostname (default: `mysql`)
  - `DB_PORT`: MySQL service port (default: `3306`)
  - `DB_NAME`: Database name (default: `dbname`)

### 2. **MySQL** (`mysql-db`)
- **Image**: `mysql:8.0`
- **Ports**: Exposes the database on `localhost:3306`
- **Environment Variables**:
  - `MYSQL_ROOT_PASSWORD`: Root user password (default: `password`)
  - `MYSQL_DATABASE`: Initial database (default: `dbname`)
- **Volumes**:
  - `db_data`: Persistent storage for database data.
  - `init-scripts`: Directory containing SQL initialization scripts.

---

## Verify Setup

1. **Access the Database**:
   Log into the MySQL container and verify the `users` table:
   ```bash
   docker exec -it mysql-db mysql -uroot -ppassword
   USE dbname;
   SHOW TABLES;
   ```

2. **Test the FastAPI App**:
   Visit `http://localhost:8000` in your browser or use tools like `curl` or Postman to interact with the API.

---

## Network Configuration

- **Network Name**: `mynetwork`
- **Driver**: `bridge`
- **Purpose**: Enables communication between `fastapi-app` and `mysql-db`.

---

## Clean Up

To stop and remove all containers, networks, and volumes:

```bash
docker-compose down -v
```

---

## Notes

- Ensure your FastAPI app (`main.py`) is set up to use the environment variables for database connection.
- The database schema and tables are created automatically using the SQL script in the `init-scripts` directory.

--- 

## License

This project is licensed under the [MIT License](LICENSE).
