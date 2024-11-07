# Bathroom Designer API

A FastAPI-based REST API for designing and managing bathroom layouts. This API allows users to create, modify, and manage bathroom designs including fixtures, walls, windows, doors, and ventilation systems.

## Features

- Create and manage bathroom designs
- Add/Update/Delete bathroom components:
  - Fixtures (toilets, sinks, etc.)
  - Walls
  - Windows
  - Doors
  - Ventilation systems
- Design theme management
- Interactive API documentation

## Project Structure 

```
app/
├── init.py
├── main.py
├── models/
│ ├── init.py
│ ├── base.py
│ ├── fixtures.py
│ ├── room.py
│ └── styles.py
```

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd bathroom-designer-api
```

2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate the virtual environment:

```bash
# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

4. Install required dependencies:

```bash
pip install fastapi uvicorn pydantic
```

## Running the API

1. Start the development server:

```bash
python -m uvicorn app.main:app --reload
```

2. The API will be available at:
- API endpoints: `http://localhost:8000`
- Interactive API documentation: `http://localhost:8000/docs`
- Alternative API documentation: `http://localhost:8000/redoc`

## API Documentation

### Available Endpoints

- `POST /bathroom/` - Create a new bathroom design
- `GET /bathroom/{bathroom_id}` - Retrieve a specific bathroom design
- `POST /bathroom/{bathroom_id}/fixtures` - Add a new fixture
- `GET /design-themes/` - Get all available design themes
- `PUT /bathroom/{bathroom_id}/fixture/{fixture_id}` - Update a specific fixture
- `PUT /bathroom/{bathroom_id}/wall/{wall_id}` - Update a specific wall
- `PUT /bathroom/{bathroom_id}/window/{window_id}` - Update a specific window
- `PUT /bathroom/{bathroom_id}/door/{door_id}` - Update a specific door
- `PUT /bathroom/{bathroom_id}/ventilation/{vent_id}` - Update ventilation
- `DELETE /bathroom/{bathroom_id}/{component_type}/{component_id}` - Delete a component

For detailed API documentation, visit the `/docs` endpoint after starting the server.

## Development

### Project Configuration

The project uses FastAPI's built-in configuration system. Key configurations include:

- CORS middleware enabled for all origins (customize for production)
- In-memory storage for demonstration purposes
- Automatic API documentation generation

### Adding New Features

1. Add new models in the `app/models` directory
2. Create new endpoints in `app/main.py`
3. Update API documentation by adding appropriate docstrings

## Production Deployment

For production deployment:

1. Update CORS settings with specific origins
2. Implement proper database storage
3. Add authentication and authorization
4. Use proper environment variables for configuration
5. Deploy behind a proper web server (nginx, etc.)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

[Add your license information here]

## Contact

[Add your contact information here]

## Docker Deployment

### Prerequisites
- Docker
- Docker Compose

### Running with Docker

1. Build the Docker image:

```bash
docker-compose build
```

2. Start the container:

```bash
docker-compose up
```

The API will be available at:
- API endpoints: `http://localhost:8000`
- Interactive API documentation: `http://localhost:8000/docs`
- Alternative API documentation: `http://localhost:8000/redoc`

### Docker Commands

- Start containers in detached mode:
  ```bash
  docker-compose up -d
  ```

- Stop containers:
  ```bash
  docker-compose down
  ```

- View logs:
  ```bash
  docker-compose logs -f
  ```

- Rebuild containers after making changes:
  ```bash
  docker-compose up -d --build
  ```

### Docker Configuration

The Docker setup includes:
- Python 3.9 slim base image
- Automatic code reloading in development
- Volume mounting for live code updates
- Exposed port 8000
- Environment variable configuration
```

Key features of this Docker setup:

1. Uses Python 3.9 slim image for smaller container size
2. Includes necessary build tools
3. Proper handling of Python dependencies
4. Volume mounting for development
5. Environment variable support
6. Automatic restart policy
7. Port mapping for API access
8. Code reloading for development

The docker-compose.yml file makes it easy to:
- Start/stop the application
- Manage environment variables
- Handle volume mounting
- Configure networking

Remember to add the Docker files to your .gitignore if you don't want to track certain Docker-related files:

```text:.gitignore
# Docker
.docker/
docker-compose.override.yml
```